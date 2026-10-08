"""Gera os diagramas dos frameworks de prompt (RTF, CTF, GRADE, PECRA, ROSES, SPARK, CREATE).

Uso: python ferramentas/gerar_diagramas_prompt.py <pasta do site>
Mesmo visual do infográfico RTF e das telas do vídeo do Word: fundo escuro, blocos azuis unidos por "+" amarelo.
Saída: public/apostilas/web2/prompt-<sigla>.png
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

site = Path(sys.argv[1])
destino = site / 'public/apostilas/web2'

FUNDO = (43, 46, 59)
AZUL = (47, 128, 237)
AZUL_TITULO = (59, 140, 240)
AMARELO = (245, 184, 46)
BRANCO = (255, 255, 255)
CINZA = (200, 205, 220)
CLARO = (214, 230, 255)

FONTES = Path('C:/Windows/Fonts')
negrito = lambda t: ImageFont.truetype(str(FONTES / 'segoeuib.ttf'), t)
normal = lambda t: ImageFont.truetype(str(FONTES / 'segoeui.ttf'), t)

# (sigla, [(nome em português, palavra em inglês)])
FRAMEWORKS = [
    ('RTF', [('Papel', 'Role'), ('Tarefa', 'Task'), ('Formato', 'Format')]),
    ('CTF', [('Contexto', 'Context'), ('Tarefa', 'Task'), ('Formato', 'Format')]),
    ('GRADE', [('Meta', 'Goal'), ('Pedido', 'Request'), ('Ação', 'Action'), ('Detalhe', 'Detail'),
               ('Exemplos', 'Examples')]),
    ('PECRA', [('Propósito', 'Purpose'), ('Expectativa', 'Expectation'), ('Contexto', 'Context'),
               ('Pedido', 'Request'), ('Ação', 'Action')]),
    ('ROSES', [('Papel', 'Role'), ('Objetivo', 'Objective'), ('Cenário', 'Scenario'),
               ('Solução esperada', 'Expected Solution'), ('Etapas', 'Steps')]),
    ('SPARK', [('Situação', 'Situation'), ('Problema', 'Problem'), ('Aspiração', 'Aspiration'),
               ('Resultados', 'Results'), ('Sorte ou destino', 'Kismet')]),
    ('CREATE', [('Personagem (papel)', 'Character'), ('Pedido', 'Request'), ('Exemplos', 'Examples'),
                ('Ajustes', 'Adjustment'), ('Tipo de saída', 'Type of output'), ('Extras', 'Extras')]),
]

LARG = 1400
BLOCO_L, BLOCO_A = 330, 120
MAIS_L = 70
LINHA_GAP = 50


def centro(d, texto, fonte, y, cor, larg=LARG, x0=0):
    w = d.textlength(texto, font=fonte)
    d.text((x0 + (larg - w) / 2, y), texto, font=fonte, fill=cor)


def desenhar(sigla, partes):
    # até 3 blocos por linha, como nas telas do vídeo
    linhas = [partes[i:i + 3] for i in range(0, len(partes), 3)]
    topo = 250
    alt = topo + len(linhas) * BLOCO_A + (len(linhas) - 1) * LINHA_GAP + 110
    im = Image.new('RGB', (LARG, alt), FUNDO)
    d = ImageDraw.Draw(im)

    centro(d, sigla, negrito(96), 40, AZUL_TITULO)
    centro(d, ' + '.join(en for _, en in partes), normal(34), 170, CINZA)

    f_pt, f_en, f_mais = negrito(36), normal(26), negrito(64)
    for n, linha in enumerate(linhas):
        # o "+" que liga uma linha à anterior fica no começo da linha, como nas telas do vídeo
        antes = n > 0
        larg_linha = len(linha) * BLOCO_L + (len(linha) - 1) * MAIS_L + (MAIS_L if antes else 0)
        x = (LARG - larg_linha) / 2
        y = topo + n * (BLOCO_A + LINHA_GAP)
        if antes:
            centro(d, '+', f_mais, y + BLOCO_A / 2 - 46, AMARELO, MAIS_L, x)
            x += MAIS_L
        for i, (pt, en) in enumerate(linha):
            d.rounded_rectangle((x, y, x + BLOCO_L, y + BLOCO_A), radius=28, fill=AZUL)
            fonte = f_pt if d.textlength(pt, font=f_pt) < BLOCO_L - 30 else negrito(30)
            centro(d, pt, fonte, y + 20, BRANCO, BLOCO_L, x)
            centro(d, en, f_en, y + 72, CLARO, BLOCO_L, x)
            x += BLOCO_L
            if i < len(linha) - 1:
                centro(d, '+', f_mais, y + BLOCO_A / 2 - 46, AMARELO, MAIS_L, x)
                x += MAIS_L
    return im


for sigla, partes in FRAMEWORKS:
    arq = destino / f'prompt-{sigla.lower()}.png'
    desenhar(sigla, partes).save(arq, optimize=True)
    print('ok', arq.name, arq.stat().st_size)
