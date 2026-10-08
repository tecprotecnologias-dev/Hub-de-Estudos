"""Converte um Word de questões objetivas "simples" (pasta "perguntas prova") para o banco do site.

Formato esperado do Word:
    Capítulo N — ...  /  Aqui estão 10 questões ...      (ignorado; o que vem antes é descartado)
    1. enunciado                                         (começa com número e ponto)
    a) ... b) ... c) ... d) ...                          (no mesmo parágrafo ou um por parágrafo)
A alternativa correta é a que está marcada no Word: em negrito ou em vermelho.
Os Words não trazem explicação do gabarito: ela vem de ferramentas/explicacoes_questoes_simples.json
(chave = id da questão). As questões entram com nivel "facil".

Uso:
    python ferramentas/converter_questoes_simples.py <Capitulo.docx> <disciplinaId> <capituloId> <saida.json>
As questões são acrescentadas às do capítulo já existentes no arquivo, com ids "<capituloId>-f<N>";
rodar de novo substitui apenas as questões "-f" daquele capítulo.
As questões listadas em REPETIDAS ficam de fora (o id das demais mantém o número do Word).
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

# questões do Word que repetem o caso e a resposta de outra questão do banco (número no Word -> a que fica)
REPETIDAS = {
    'legislacao-cap1': {2: 'cap1-q3', 8: 'cap1-q6'},
    'legislacao-cap2': {4: 'cap2-f10'},
    'legislacao-cap3': {7: 'cap3-q8'},
    'legislacao-cap4': {1: 'cap4-q6', 2: 'cap4-q2', 8: 'cap4-q3'},
    'legislacao-cap5': {1: 'cap5-q1', 3: 'cap5-q2'},
    'legislacao-cap6': {2: 'cap2-f1', 8: 'cap2-f2', 9: 'cap6-q4'},
    'legislacao-cap7': {1: 'cap7-q2', 6: 'cap7-q8'},
}

# correções em relação ao Word: (capítulo, número no Word, letra da alternativa ou 'enunciado') ->
# texto novo, ou (trecho antigo, trecho novo) para trocar só uma parte
CORRECOES = {
    # o Word dizia "prazo razoável a ser definido pela ANPD"; a ANPD fixou 3 dias úteis (Resolução CD/ANPD nº 15/2024)
    ('legislacao-cap1', 4, 'c'): 'O GDPR exige notificação à autoridade competente em até 72 horas; a LGPD, conforme o '
    'Regulamento de Comunicação de Incidentes da ANPD (Resolução CD/ANPD nº 15/2024), exige comunicação à ANPD em até '
    '3 dias úteis — em ambos os casos, os titulares também devem ser comunicados quando o incidente puder lhes causar '
    'risco ou dano relevante.',
    # o Word citava o "Tema 938" do STJ, que trata de comissão de corretagem, não de marketplaces
    ('legislacao-cap3', 2, 'enunciado'): ('Com base no STJ (Tema 938)', 'Com base no CDC e no entendimento do STJ'),
    # a Convenção de Budapeste já foi promulgada pelo Decreto nº 11.491/2023
    ('legislacao-cap4', 9, 'c'): ('e futuramente a Convenção de Budapeste — cujo processo de adesão pelo Brasil em 2023 '
                                  'fortalecerá esses mecanismos',
                                  'e a Convenção de Budapeste sobre crimes cibernéticos, já incorporada pelo Brasil pelo '
                                  'Decreto nº 11.491/2023, que facilita a cooperação entre os países signatários'),
    # o Word citava uma "RDC 163/2017 da ANVISA"; a norma sobre publicidade infantil é a Resolução nº 163/2014 do Conanda
    ('legislacao-cap5', 7, 'c'): ('infração à RDC 163/2017 da ANVISA para alimentos ultraprocessados dirigidos a crianças',
                                  'infração à Resolução nº 163/2014 do Conanda, que considera abusivo o direcionamento '
                                  'de publicidade à criança,'),
    # o Pillar Two foi implementado pela Lei nº 15.079/2024 (a Lei nº 14.754/2023 trata de outro assunto)
    ('legislacao-cap7', 4, 'enunciado'): ('Lei nº 14.754/2023', 'Lei nº 15.079/2024'),
    ('legislacao-cap7', 4, 'd'): ('Lei nº 14.754/2023', 'Lei nº 15.079/2024'),
    # Remessa Conforme: desde 1º/8/2024 (Lei nº 14.902/2024), até US$ 50 paga 20% de II e acima disso 60%,
    # com desconto de US$ 20 no imposto; a antiga regra de isenção virou alternativa errada
    ('legislacao-cap7', 7, 'c'): 'Imposto de Importação de 60% sobre o valor total, com desconto de US$ 20 no imposto '
    '(60% de US$ 120 = US$ 72; menos US$ 20 = US$ 52), além do ICMS estadual cobrado à parte, conforme as regras em '
    'vigor desde agosto de 2024 (Lei nº 14.902/2024).',
    ('legislacao-cap7', 7, 'd'): 'Isenção de Imposto de Importação sobre os primeiros US$ 50 e 20% de II apenas sobre os '
    'US$ 70 que excedem essa faixa, sem incidência de ICMS em compras feitas pelo Programa Remessa Conforme.',
}


def marcado(rpr):
    """negrito ou cor vermelha no run"""
    if rpr is None:
        return False
    b = rpr.find(W + 'b')
    if b is not None and b.get(W + 'val') not in ('0', 'false'):
        return True
    cor = rpr.find(W + 'color')
    if cor is not None:
        v = (cor.get(W + 'val') or '').upper()
        if len(v) == 6 and v != 'AUTO':
            r, g, bl = int(v[:2], 16), int(v[2:4], 16), int(v[4:], 16)
            return r > 150 and g < 90 and bl < 90
    return False


def paragrafos(caminho):
    """cada parágrafo como lista de (caractere, marcado)"""
    with zipfile.ZipFile(caminho) as z:
        raiz = ET.fromstring(z.read('word/document.xml'))
    for p in raiz.iter(W + 'p'):
        chars = []
        for r in p.iter(W + 'r'):
            m = marcado(r.find(W + 'rPr'))
            for t in r.iter(W + 't'):
                chars += [(c, m) for c in (t.text or '')]
        if ''.join(c for c, _ in chars).strip():
            yield chars


def limpar(t):
    return re.sub(r'\s+', ' ', t).strip()


def converter(caminho):
    questoes = []
    atual = None
    for chars in paragrafos(caminho):
        texto = ''.join(c for c, _ in chars)
        num = re.match(r'\s*(\d+)\.\s', texto)
        if num:
            atual = {'enunciado': limpar(texto[num.end():]), 'alts': []}
            questoes.append(atual)
            continue
        if re.match(r'\s*(Aqui estão|Capítulo)', texto):
            # alguns Words trazem uma cópia parcial das questões antes de "Aqui estão 10 questões ...";
            # vale só a lista que vem depois
            questoes, atual = [], None
            continue
        if atual is None:
            continue
        # pontos onde começa cada alternativa, na ordem a), b), c)...
        inicios = []
        for letra in 'abcde'[len(atual['alts']):]:
            m = re.compile(r'(?:^|(?<=\s))' + letra + r'\)\s').search(texto, inicios[-1][1] if inicios else 0)
            if not m:
                break
            inicios.append((m.start(), m.end()))
        if not inicios:
            if atual['alts']:
                raise SystemExit(f'parágrafo solto depois das alternativas: {texto[:80]}')
            atual['enunciado'] += ' ' + limpar(texto)
            continue
        for i, (ini, fim) in enumerate(inicios):
            ate = inicios[i + 1][0] if i + 1 < len(inicios) else len(chars)
            trecho = chars[fim:ate]
            letras = [m for c, m in trecho if not c.isspace()]
            atual['alts'].append((limpar(''.join(c for c, _ in trecho)), sum(letras) / max(len(letras), 1)))
    saida = []
    for n, q in enumerate(questoes, 1):
        notas = [f for _, f in q['alts']]
        corretas = [i for i, f in enumerate(notas) if f > 0.5]
        if len(q['alts']) < 4 or len(corretas) != 1:
            raise SystemExit(f'questão {n}: {len(q["alts"])} alternativas, marcação {notas}')
        saida.append((q['enunciado'], [t for t, _ in q['alts']], corretas[0]))
    return saida


if __name__ == '__main__':
    docx, disciplina, capitulo, arq = sys.argv[1:5]
    arq = Path(arq)
    banco = json.loads(arq.read_text(encoding='utf-8')) if arq.exists() else []
    explicacoes = json.loads((Path(__file__).parent / 'explicacoes_questoes_simples.json').read_text(encoding='utf-8'))
    prefixo = f'{capitulo}-f'
    banco = [q for q in banco if not q['id'].startswith(prefixo)]
    questoes = converter(docx)
    for (cap, n, campo), texto in CORRECOES.items():
        if cap != capitulo:
            continue
        enunciado, alternativas, correta = questoes[n - 1]
        atual = enunciado if campo == 'enunciado' else alternativas['abcde'.index(campo)]
        if isinstance(texto, tuple):
            if texto[0] not in atual:
                raise SystemExit(f'correção de {cap} questão {n} ({campo}): trecho não encontrado: {texto[0]}')
            texto = atual.replace(*texto)
        if campo == 'enunciado':
            questoes[n - 1] = (texto, alternativas, correta)
        else:
            alternativas['abcde'.index(campo)] = texto
    novas = [{
        'id': f'{prefixo}{n}',
        'disciplinaId': disciplina,
        'capituloId': capitulo,
        'tipo': 'objetiva',
        'nivel': 'facil',
        'enunciado': enunciado,
        'alternativas': alternativas,
        'correta': correta,
        **({'resolucao': explicacoes[f'{prefixo}{n}']} if f'{prefixo}{n}' in explicacoes else {}),
    } for n, (enunciado, alternativas, correta) in enumerate(questoes, 1)
        if n not in REPETIDAS.get(capitulo, {})]
    verificar_termos(json.dumps(novas, ensure_ascii=False))
    # as novas entram logo depois das demais questões do mesmo capítulo
    pos = max((i + 1 for i, q in enumerate(banco) if q['capituloId'] == capitulo), default=len(banco))
    banco[pos:pos] = novas
    arq.write_text(json.dumps(banco, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{capitulo}: {len(novas)} questões fáceis, gabarito', ''.join('ABCDE'[q['correta']] for q in novas),
          '| sem explicação:', [q['id'] for q in novas if 'resolucao' not in q])
    # reaplica as alternativas reescritas (correta não pode ser sempre a mais longa)
    from aplicar_ajustes_alternativas import main as aplicar_ajustes
    aplicar_ajustes()
