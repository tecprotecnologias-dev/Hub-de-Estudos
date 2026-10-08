"""Aplica ferramentas/ajustes_alternativas.json (alternativas e resoluções) às questões em src/data/questoes/*.json.

As alternativas reescritas evitam que a correta seja sempre a mais longa, e as letras
citadas nas resoluções viram marcas {{A}} que acompanham o embaralhamento.
Rode de novo sempre que reconverter as questões a partir dos Words:

    python ferramentas/aplicar_ajustes_alternativas.py
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AJUSTES = os.path.join(RAIZ, 'ferramentas', 'ajustes_alternativas.json')
QUESTOES = os.path.join(RAIZ, 'src', 'data', 'questoes')
LETRAS = 'ABCDE'

sys.path.insert(0, os.path.join(RAIZ, 'ferramentas'))
try:
    from converter_capitulo import verificar_termos
except ImportError:
    verificar_termos = None


# Letras de alternativas citadas nas resoluções ("B e E são...", "A ignora...") viram {{B}}, {{E}}, {{A}}:
# o site troca a marca pela letra que a alternativa recebe depois de embaralhada (src/lib/util.ts).
LETRA_SOLTA = re.compile(r'(?<![\w.#\-/§º{])([A-E])(?![\w#+\-/{}])')
VERBOS = {'aceita', 'afirma', 'apenas', 'assume', 'atribui', 'atribuem', 'cai', 'caem', 'comete', 'cometem',
          'confunde', 'contradizem', 'contraria', 'descarta', 'descreve', 'descrevem', 'dilui', 'distorce',
          'distorcem', 'é', 'erra', 'erram', 'está', 'exagera', 'exige', 'explora', 'fabrica', 'fazem',
          'funciona', 'generaliza', 'ignora', 'ignoram', 'ilustra', 'introduz', 'inventa', 'inventam', 'inverte',
          'invertem', 'isola', 'minimiza', 'não', 'nega', 'presume', 'prioriza', 'propõe', 'repete', 'repetem',
          'restringe', 'são', 'simplifica', 'subestima', 'sugere', 'tenta', 'transforma', 'transformam', 'trata',
          'tratam', 'usa', 'vão'}


def _cita_alternativa(texto, m):
    antes, depois = texto[:m.start()], texto[m.end():]
    if re.search(r'(nível|Nível|Fornecedor|CC|Resolução)\s*$', antes):
        return False
    if re.match(r'[\s,)]', depois) and re.search(r'(\(|distrator|\bde)\s*$', antes):
        return True  # "(C está errada)", "distrator A,", "o erro de A,"
    if re.match(r'\s*(,|e)\s+([A-E]|\{\{)', depois) or re.search(r'(\b[A-E]|\}\})\s*(,|e)\s*$', antes):
        return True  # listas: "B, C, D e E"
    prox = depois.split()
    return bool(prox) and prox[0].strip(',.;:') in VERBOS


def marcar_letras(texto):
    return LETRA_SOLTA.sub(lambda m: '{{%s}}' % m.group(1) if _cita_alternativa(texto, m) else m.group(1), texto)


def main():
    with open(AJUSTES, encoding='utf-8') as f:
        ajustes = {k: v for k, v in json.load(f).items() if not k.startswith('_')}
    usados = set()
    for caminho in sorted(glob.glob(os.path.join(QUESTOES, '*.json'))):
        with open(caminho, encoding='utf-8') as f:
            questoes = json.load(f)
        mudou = False
        for q in questoes:
            if q.get('tipo') != 'objetiva':
                continue
            novo = ajustes.get(q['id'], {})
            if novo:
                usados.add(q['id'])
            for letra, texto in novo.items():
                if letra in ('resolucao', 'enunciado'):
                    # resolução ou enunciado reescrito (correção de conteúdo ou citação pelo conteúdo)
                    if q.get(letra) != texto:
                        q[letra] = texto
                        mudou = True
                    continue
                i = LETRAS.index(letra)
                if q['alternativas'][i] != texto:
                    q['alternativas'][i] = texto
                    mudou = True
            if isinstance(q.get('resolucao'), str):
                marcada = marcar_letras(q['resolucao'])
                if marcada != q['resolucao']:
                    q['resolucao'] = marcada
                    mudou = True
        if verificar_termos:
            verificar_termos(json.dumps(questoes, ensure_ascii=False))
        if mudou:
            with open(caminho, 'w', encoding='utf-8') as f:
                json.dump(questoes, f, ensure_ascii=False, indent=2)
                f.write('\n')
        obj = [q for q in questoes if q.get('tipo') == 'objetiva']
        longa = sum(1 for q in obj
                    if max(range(len(q['alternativas'])), key=lambda i: len(q['alternativas'][i])) == q['correta'])
        print(f'{os.path.basename(caminho)}: {len(obj)} objetivas, correta mais longa em {longa}')
    faltando = set(ajustes) - usados
    if faltando:
        print('Ids sem questão correspondente:', ', '.join(sorted(faltando)))


if __name__ == '__main__':
    main()
