"""Separa uma apostila LaTeX com vários capítulos (Apostila_Completa.tex) em um
arquivo .tex por capítulo, no formato que o converter_latex.py entende.

Uso:
    python ferramentas/separar_latex.py <Apostila_Completa.tex> <pasta_saida>

Cada capítulo começa no comentário "% ---------- Capa do capítulo". O texto do
capítulo começa depois do "SUMÁRIO DO CAPÍTULO" (no primeiro \\newpage seguinte).
"""
import os
import re
import sys

entrada, pasta = sys.argv[1], sys.argv[2]
s = open(entrada, encoding='utf-8').read()
preambulo = s[:s.index('\\begin{document}')]
marcador = '% ---------- Capa do capítulo'
partes = s.split(marcador)[1:]
os.makedirs(pasta, exist_ok=True)
for parte in partes:
    parte = parte.split('\\end{document}')[0]
    numero = int(re.search(r'CAP[IÍ]TULO\s+(\d+)', parte).group(1))
    i_sumario = parte.index('SUMÁRIO DO CAPÍTULO')
    i_corpo = parte.index('\\newpage', i_sumario) + len('\\newpage')
    capa, corpo = parte[:i_corpo], parte[i_corpo:]
    # tira cabeçalhos de página que o próximo capítulo define antes da sua capa
    corpo = re.sub(r'\\fancyhead\[[LRC]\]\{[^\n]*\}\s*$', '', corpo.rstrip())
    tex = (preambulo + '\\begin{document}\n' + capa + '\n\\setcounter{page}{1}\n' + corpo + '\n\\end{document}\n')
    destino = os.path.join(pasta, f'Capitulo{numero}.tex')
    open(destino, 'w', encoding='utf-8', newline='\n').write(tex)
    print(f'Capítulo {numero}: {len(corpo.splitlines())} linhas -> {destino}')
