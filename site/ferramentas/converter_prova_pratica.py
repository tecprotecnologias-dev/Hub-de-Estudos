"""Converte uma prova prática (ex.: P1 de Web Design II) e o Word com as resoluções em questões discursivas.

Prova (enunciados):
    Questão N / <título> / "Exercício N.M: Título Texto..." seguido dos itens (lista) / "Valor: x"
    (Questão sem "Exercício" vira um único exercício "N", com os parágrafos como itens.)
    Cabeçalho (instituição, aluno, regras de entrega) é descartado: só conta o que vem depois de "Questão 1".
Resoluções:
    "Exercício N.M: ..." (negrito), as mesmas linhas do enunciado, e depois os passos:
    parágrafos que começam em negrito = texto ("Passo 1 — ...", "Atenção: ..."),
    os demais = código (rótulos "javascript", "jsx", "json"... só separam blocos), exceto frases em prosa.

Uso:
    python ferramentas/converter_prova_pratica.py <prova.docx> <resolucoes.docx> <disciplinaId> <prefixo> <saida.json>
        --capitulos "1=web2-cap1,2=web2-cap2,3=web2-cap3,4=web2-cap4,5=web2-cap4" [--trocar "a=>b" ...]
O número antes do ponto ("1" em "Exercício 1.2") escolhe o capítulo.
"""
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).parent))
from converter_capitulo import verificar_termos  # noqa: E402

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
ROTULOS = {'javascript', 'js', 'jsx', 'tsx', 'ts', 'typescript', 'json', 'bash', 'shell', 'css', 'html', 'text', 'plaintext'}
RE_EXERCICIO = re.compile(r'^Exercício\s+(\d+)(?:\.(\d+))?\s*:\s*(.*)$', re.S)


def paragrafos(caminho):
    """(texto, comeca_em_negrito, eh_item_de_lista)"""
    with zipfile.ZipFile(caminho) as z:
        raiz = ET.fromstring(z.read('word/document.xml'))
    for p in raiz.iter(W + 'p'):
        texto, negrito = '', None
        for r in p.iter(W + 'r'):
            t = ''
            for el in r:
                if el.tag == W + 't':
                    t += el.text or ''
                elif el.tag in (W + 'br', W + 'cr'):
                    t += '\n'
                elif el.tag == W + 'tab':
                    t += '    '
            if negrito is None and t.strip():
                b = r.find(f'{W}rPr/{W}b')
                negrito = b is not None and b.get(W + 'val') not in ('0', 'false')
            texto += t
        if texto.strip():
            lista = p.find(f'{W}pPr/{W}numPr') is not None
            yield texto.rstrip(), bool(negrito), lista


def limpar(t):
    # links copiados como markdown: [https://x](https://x) -> https://x
    t = re.sub(r'\[(https?://[^\]]+)\]\(\1\)', r'\1', t)
    return re.sub(r'\s+', ' ', t).strip()


def separar_titulo(t):
    """'Criando um script CLI com Node.js Crie uma pasta...' -> 'Criando um script CLI com Node.js: Crie uma pasta...'"""
    return re.sub(r'^(.{5,80}?)\s+(?=(Crie|Dentro|Use|Faça|Implemente|Construa)\b)', r'\1: ', t, count=1)


def chave(m):
    return f'{m.group(1)}.{m.group(2)}' if m.group(2) else m.group(1)


def enunciados(caminho):
    """{ '1.1': {'titulo', 'enunciado', 'itens'} } na ordem da prova."""
    saida, atual, questao, iniciou = {}, None, None, False
    for t, negrito, lista in paragrafos(caminho):
        s = t.strip()
        mq = re.match(r'^Questão\s+(\d+)$', s)
        if mq:
            iniciou, questao, atual = True, mq.group(1), None
            continue
        if not iniciou or re.match(r'^Valor:', s):
            continue
        m = RE_EXERCICIO.match(s)
        if m:
            atual = {'enunciado': separar_titulo(limpar(m.group(3))), 'itens': []}
            saida[chave(m)] = atual
            continue
        if atual is None:
            # título da questão; se a questão não tiver "Exercício N.M", ela inteira é um exercício
            atual = {'titulo': limpar(s), 'enunciado': '', 'itens': [], 'sem_exercicio': True}
            saida[questao] = atual
            continue
        if atual.get('sem_exercicio') and not atual['enunciado']:
            atual['enunciado'] = limpar(s)
        else:
            atual['itens'].append(limpar(s))
    # exercícios com sub-número dentro de uma questão que tem título: o título vira só referência
    for k in [k for k, v in saida.items() if v.get('sem_exercicio') and not v['enunciado']]:
        del saida[k]
    return saida


def parece_prosa(s):
    """frase explicativa sem cara de código (ex.: 'Repare também que ...')"""
    if re.search(r'[;{}<>=]|=>|\(\)|^\s|^(npm|npx|node|cd|mkdir|git)\b', s):
        return False
    return len(s.split()) >= 6 and s.rstrip()[-1:] in '.:!?'


def resolucoes(caminho, chaves_enunciado):
    saida, atual, ignorar = {}, None, set()
    depois_de_saida = False
    for t, negrito, lista in paragrafos(caminho):
        s = t.strip()
        m = RE_EXERCICIO.match(s) if negrito else None
        if m:
            atual = saida.setdefault(chave(m), [])
            ignorar = chaves_enunciado.get(chave(m), set())
            continue
        if negrito and re.match(r'^Módulo\s+\d+', s):
            continue
        if atual is None:
            continue
        if limpar(s) in ignorar:
            continue
        if s.lower() in ROTULOS:
            atual.append({'t': 'codigo', 'texto': ''})
            continue
        if negrito or (parece_prosa(s) and not depois_de_saida):
            atual.append({'t': 'p', 'texto': limpar(s)})
            depois_de_saida = bool(re.match(r'^Saída', s))
            continue
        depois_de_saida = False
        if atual and atual[-1]['t'] == 'codigo':
            atual[-1]['texto'] += ('\n' if atual[-1]['texto'] else '') + t
        else:
            atual.append({'t': 'codigo', 'texto': t})
    for blocos in saida.values():
        blocos[:] = [b for b in blocos if b['texto'].strip()]
    return saida


def main():
    args = sys.argv[1:]
    trocas, capitulos = [], {}
    while '--trocar' in args:
        i = args.index('--trocar')
        trocas.append(tuple(args[i + 1].split('=>')))
        del args[i:i + 2]
    if '--capitulos' in args:
        i = args.index('--capitulos')
        capitulos = dict(p.split('=') for p in args[i + 1].split(','))
        del args[i:i + 2]
    prova, resolvidas, disciplina_id, prefixo, saida = args[:5]

    enun = enunciados(prova)
    linhas = {k: {limpar(v['enunciado']), *v['itens'], limpar(f"{v.get('titulo', '')}")} for k, v in enun.items()}
    # o Word de resoluções repete o enunciado com o título do exercício colado no começo
    res = resolucoes(resolvidas, linhas)

    questoes = []
    for k, v in enun.items():
        cap = capitulos[k.split('.')[0]]
        q = {
            'id': f'{prefixo}-e{k.replace(".", "-")}',
            'disciplinaId': disciplina_id,
            'capituloId': cap,
            'tipo': 'discursiva',
            'pratica': True,
            'enunciado': (f"{v['titulo']}: " if v.get('titulo') else '') + v['enunciado'],
        }
        if v['itens']:
            q['itens'] = v['itens']
        if res.get(k):
            q['resolucao'] = res[k]
        else:
            print('aviso: sem resolução para o exercício', k)
        questoes.append(q)

    texto = json.dumps(questoes, ensure_ascii=False)
    for a, b in trocas:
        texto = texto.replace(a, b)
    verificar_termos(texto)
    questoes = json.loads(texto)
    destino = Path(saida)
    existentes = json.loads(destino.read_text(encoding='utf-8')) if destino.exists() else []
    ids = {q['id'] for q in questoes}
    existentes = [q for q in existentes if q['id'] not in ids] + questoes
    destino.write_text(json.dumps(existentes, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    por_cap = {}
    for q in questoes:
        por_cap[q['capituloId']] = por_cap.get(q['capituloId'], 0) + 1
    print(f'{len(questoes)} exercícios -> {saida}:', por_cap)


if __name__ == '__main__':
    main()
