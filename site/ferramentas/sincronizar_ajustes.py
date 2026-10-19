"""Faz ajustes_alternativas.json concordar com as questões atuais de src/data/questoes/*.json.

O aplicar_ajustes_alternativas.py grava, por letra, as alternativas, resoluções, enunciados e
respostas guardados em ajustes_alternativas.json. Quando uma questão é revisada direto no JSON
(ou gerada de novo por um script engsoft_capN_objetivas.py), o ajuste antigo passaria a escrever
por cima da versão nova. Este script atualiza cada ajuste para o texto atual da questão e remove
os ajustes de questões que deixaram de existir, para que rodar o aplicar_ajustes não mude nada.
Uso (dentro de site/):

    python ferramentas/sincronizar_ajustes.py
"""

import glob
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AJUSTES = os.path.join(RAIZ, 'ferramentas', 'ajustes_alternativas.json')
QUESTOES = os.path.join(RAIZ, 'src', 'data', 'questoes')
LETRAS = 'ABCDE'


def main():
    with open(AJUSTES, encoding='utf-8') as f:
        ajustes = json.load(f)
    questoes = {}
    for caminho in glob.glob(os.path.join(QUESTOES, '*.json')):
        with open(caminho, encoding='utf-8') as f:
            questoes.update({q['id']: q for q in json.load(f)})

    atualizados, removidos = [], []
    for id_, ajuste in list(ajustes.items()):
        if id_.startswith('_'):
            continue
        q = questoes.get(id_)
        if q is None:
            del ajustes[id_]
            removidos.append(id_)
            continue
        for chave in list(ajuste):
            if chave in LETRAS:
                i = LETRAS.index(chave)
                atual = q['alternativas'][i] if i < len(q.get('alternativas', [])) else None
            else:
                atual = q.get(chave)
            if atual is None:
                del ajuste[chave]
            elif ajuste[chave] != atual:
                ajuste[chave] = atual
            else:
                continue
            atualizados.append(f'{id_}:{chave}')
        if not ajuste:
            del ajustes[id_]

    # mantém o recuo e as quebras de linha do arquivo, para o git mostrar só os ajustes que mudaram
    with open(AJUSTES, encoding='utf-8', newline='') as f:
        inicio = f.read(200)
    quebra = '\r\n' if '\r\n' in inicio else '\n'
    segunda = inicio.split('\n')[1]
    recuo = len(segunda) - len(segunda.lstrip(' '))
    with open(AJUSTES, 'w', encoding='utf-8', newline=quebra) as f:
        json.dump(ajustes, f, ensure_ascii=False, indent=recuo)
        f.write('\n')
    print(f'{len(atualizados)} ajustes atualizados, {len(removidos)} removidos')
    for item in atualizados + removidos:
        print('  ', item)


if __name__ == '__main__':
    main()
