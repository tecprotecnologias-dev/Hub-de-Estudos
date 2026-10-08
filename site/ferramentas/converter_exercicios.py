"""Converte o "Caderno de Exercícios" (Web Design II) em questões discursivas com resolução.

Formato esperado do Word:
    MÓDULO 0N
    <título do módulo>                       (Título 1)
    Exercícios
    1. Título: enunciado ...                 (um parágrafo por exercício)
    Resolução Passo a Passo dos Exercícios   (Título 1)
    Exercício N – título                     (Título 2)
    parágrafos de texto e linhas de código   (código = parágrafos em fonte menor, sem espaço depois)

O cabeçalho (instituição, logo, sumário) é descartado. Cada exercício vira uma questão
discursiva do capítulo <prefixo>-cap<N>, com a resolução em blocos de texto e código.

Uso:
    python ferramentas/converter_exercicios.py <caderno.docx> <disciplinaId> <prefixo> <saida.json> [--trocar "a=>b" ...]
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


def texto_run(r):
    t = ''
    for el in r:
        if el.tag == W + 't':
            t += el.text or ''
        elif el.tag in (W + 'br', W + 'cr'):
            t += '\n'
        elif el.tag == W + 'tab':
            t += '    '
    return t


def paragrafos(caminho):
    """(estilo, texto, eh_codigo) de cada parágrafo."""
    with zipfile.ZipFile(caminho) as z:
        raiz = ET.fromstring(z.read('word/document.xml'))
    for p in raiz.iter(W + 'p'):
        estilo = p.find(f'{W}pPr/{W}pStyle')
        estilo = estilo.get(W + 'val') if estilo is not None else ''
        runs = [r for r in p.iter(W + 'r')]
        texto = ''.join(texto_run(r) for r in runs)
        if not texto.strip():
            continue
        tamanhos = set()
        for r in runs:
            if not texto_run(r).strip():
                continue
            sz = r.find(f'{W}rPr/{W}sz')
            tamanhos.add(sz.get(W + 'val') if sz is not None else None)
        eh_codigo = tamanhos == {'19'}
        yield estilo, texto.rstrip(), eh_codigo


def limpar(t):
    return re.sub(r'\s+', ' ', t).strip()


def converter(caminho, disciplina_id, prefixo):
    modulo = None
    enunciados = {}  # (modulo, n) -> texto
    resolucoes = {}  # (modulo, n) -> blocos
    secao = None
    atual = None
    esperando_titulo = False
    for estilo, t, codigo in paragrafos(caminho):
        m = re.match(r'^MÓDULO\s+0*(\d+)\s*$', t.strip())
        if m:
            modulo, secao, atual, esperando_titulo = int(m.group(1)), None, None, True
            continue
        if modulo is None:
            continue
        if esperando_titulo:
            esperando_titulo = False
            continue
        if t.strip() == 'Exercícios':
            secao = 'enunciados'
            continue
        if t.strip().startswith('Resolução Passo a Passo'):
            secao = 'resolucoes'
            continue
        if secao == 'enunciados':
            m = re.match(r'^(\d+)\.\s+(.*)$', t.strip(), re.S)
            if m:
                atual = (modulo, int(m.group(1)))
                enunciados[atual] = limpar(m.group(2))
            elif atual:
                enunciados[atual] += ' ' + limpar(t)
            continue
        if secao == 'resolucoes':
            m = re.match(r'^Exercício\s+(\d+)\s*[–—-]', t.strip())
            if m and not codigo:
                atual = (modulo, int(m.group(1)))
                resolucoes[atual] = []
                continue
            if atual is None:
                continue
            blocos = resolucoes[atual]
            if codigo:
                if blocos and blocos[-1]['t'] == 'codigo':
                    blocos[-1]['texto'] += '\n' + t
                else:
                    blocos.append({'t': 'codigo', 'texto': t})
            else:
                # "Passo 1. ...Passo 2. ..." colados no mesmo parágrafo viram parágrafos separados
                for parte in re.split(r'(?<=[.:)])\s*(?=Passo \d+\.)', t.strip()):
                    if parte.strip():
                        blocos.append({'t': 'p', 'texto': limpar(parte)})

    questoes = []
    for (mod, n), enunciado in sorted(enunciados.items()):
        q = {
            'id': f'{prefixo}-cap{mod}-e{n}',
            'disciplinaId': disciplina_id,
            'capituloId': f'{prefixo}-cap{mod}',
            'tipo': 'discursiva',
            'pratica': True,
            'enunciado': enunciado,
        }
        if (mod, n) in resolucoes:
            q['resolucao'] = resolucoes[(mod, n)]
        questoes.append(q)
    sem = [q['id'] for q in questoes if 'resolucao' not in q]
    if sem:
        print('aviso: exercícios sem resolução:', ', '.join(sem))
    return questoes


def main():
    args = sys.argv[1:]
    trocas = []
    while '--trocar' in args:
        i = args.index('--trocar')
        a, b = args[i + 1].split('=>')
        trocas.append((a, b))
        del args[i:i + 2]
    origem, disciplina_id, prefixo, saida = args[:4]
    questoes = converter(origem, disciplina_id, prefixo)
    texto = json.dumps(questoes, ensure_ascii=False)
    for a, b in trocas:
        texto = texto.replace(a, b)
    questoes = json.loads(texto)
    verificar_termos(texto)
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
