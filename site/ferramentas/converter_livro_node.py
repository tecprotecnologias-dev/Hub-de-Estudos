"""Converte o livro "Node.js, Express e MySQL" (LaTeX, pasta Guia NODES.js/LIVRO A5) para o site.

Uso:
    python ferramentas/converter_livro_node.py "<pasta livro-completo-A5>"

Cada capítulo vira src/data/capitulos/web2-node-capN.json (apêndices: web2-node-apa / -apb), com os
diagramas em public/apostilas/web2/node/. O capítulo 10 está dividido em quatro arquivos (10a a 10d),
que são juntados numa página só. Usa ferramentas/converter_latex.py (modelo "livro"), que tira as
seções de Resumo e Estudo de Caso, como nas demais apostilas.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(AQUI)

ARQUIVOS = [(f'capitulo-{n:02d}', f'web2-node-cap{n}') for n in range(1, 10)] + [
    ('capitulo-10', 'web2-node-cap10'),
    ('capitulo-11', 'web2-node-cap11'),
    ('capitulo-12', 'web2-node-cap12'),
    ('capitulo-13', 'web2-node-cap13'),
    ('apendice-a', 'web2-node-apa'),
    ('apendice-b', 'web2-node-apb'),
]


def main():
    livro = sys.argv[1]
    with tempfile.TemporaryDirectory() as tmp:
        # trabalha numa cópia, para não mexer na pasta do livro
        copia = os.path.join(tmp, 'livro')
        shutil.copytree(livro, copia)
        caps = os.path.join(copia, 'capitulos')
        with open(os.path.join(caps, 'capitulo-10.tex'), 'w', encoding='utf-8') as f:
            for parte in 'abcd':
                with open(os.path.join(caps, f'capitulo-10{parte}.tex'), encoding='utf-8') as p:
                    f.write(p.read() + '\n')
        for nome, ident in ARQUIVOS:
            subprocess.run([sys.executable, '-X', 'utf8', os.path.join(AQUI, 'converter_latex.py'),
                            os.path.join(caps, nome + '.tex'),
                            os.path.join(SITE, 'src', 'data', 'capitulos', ident + '.json'),
                            '--imagens', os.path.join(SITE, 'public', 'apostilas', 'web2', 'node'),
                            'apostilas/web2/node'], check=True)
            # abertura antes de "3.1 Introdução" (quadro de pré-requisitos): evita duas seções "Introdução"
            saida = os.path.join(SITE, 'src', 'data', 'capitulos', ident + '.json')
            with open(saida, encoding='utf-8') as f:
                cap = json.load(f)
            secoes = [b for b in cap['blocos'] if b['t'] == 'h2']
            if len(secoes) > 1 and secoes[0]['texto'] == 'Introdução' and secoes[1]['texto'].endswith('Introdução'):
                secoes[0].update(texto='Antes de começar', id='antes-de-comecar')
                with open(saida, 'w', encoding='utf-8', newline='\n') as f:
                    json.dump(cap, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
