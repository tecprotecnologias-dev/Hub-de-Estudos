"""Converte capítulos de apostila em Word (.docx) para o JSON usado pelo site.

Uso:
    python ferramentas/converter_capitulo.py <arquivo.docx> <saida.json>

O conversor reconhece a formatação do modelo das apostilas:
  - "CAPÍTULO N" + título grande               -> cabeçalho do capítulo
  - títulos de seção (fonte 17pt)               -> h2 (entram no sumário)
  - subtítulos dourados (13pt)                  -> h3
  - rótulos dourados (10,5pt) como "Exemplo prático", "Atenção: ...",
    "Boa Prática: ...", "Resposta comentada"    -> quadros destacados
  - parágrafos com marcadores / numerados       -> listas
  - tabelas                                     -> tabelas (1ª linha = cabeçalho)
Imagens de cabeçalho e marca-d'água são ignoradas.
As seções de Resumo, Estudo de Caso e Exercícios de Fixação não entram no site.
"""
import html
import json
import re
import sys
import unicodedata
import zipfile
from xml.etree import ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
MC = '{http://schemas.openxmlformats.org/markup-compatibility/2006}'


def slug(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def ligado(rpr, tag):
    """Negrito/itálico ativo? (<w:b w:val="0"/> significa desligado)"""
    el = rpr.find(W + tag) if rpr is not None else None
    return el is not None and el.get(W + 'val', 'true') not in ('0', 'false')


def html_runs(p):
    """Texto do parágrafo em HTML, preservando negrito e itálico."""
    partes = []
    for r in p.iter(W + 'r'):
        t = ''.join(x.text or '' for x in r.iter(W + 't'))
        if not t:
            continue
        rpr = r.find(W + 'rPr')
        neg = ligado(rpr, 'b')
        ita = ligado(rpr, 'i')
        partes.append((html.escape(t, quote=False), neg, ita))
    # junta trechos vizinhos com a mesma formatação
    out = []
    for t, b, i in partes:
        if out and out[-1][1] == b and out[-1][2] == i:
            out[-1] = (out[-1][0] + t, b, i)
        else:
            out.append((t, b, i))
    s = ''
    for t, b, i in out:
        if i:
            t = f'<em>{t}</em>'
        if b:
            t = f'<strong>{t}</strong>'
        s += t
    return s.strip()


def texto(p):
    return ''.join(x.text or '' for x in p.iter(W + 't')).strip()


def assinatura(p):
    runs = [r for r in p.iter(W + 'r') if ''.join(x.text or '' for x in r.iter(W + 't')).strip()]
    rpr = runs[0].find(W + 'rPr') if runs else None

    def val(el, tag):
        x = el.find(W + tag) if el is not None else None
        return None if x is None else x.get(W + 'val')

    ppr = p.find(W + 'pPr')
    ind = ppr.find(W + 'ind') if ppr is not None else None
    return {
        'sz': int(val(rpr, 'sz') or 22),
        'b': ligado(rpr, 'b'),
        'i': ligado(rpr, 'i'),
        'cor': (val(rpr, 'color') or '').upper(),
        'num': ppr is not None and ppr.find(W + 'numPr') is not None,
        'pendente': ind is not None and ind.get(W + 'hanging') is not None,
        'recuo': ind is not None and ind.get(W + 'left') not in (None, '0'),
    }


def classificar(p):
    s = assinatura(p)
    t = texto(p)
    if s['sz'] >= 44:
        return 'titulo'
    if re.match(r'CAP[IÍ]TULO\s+\d+', t) and s['cor'] == '9C7A1E':
        return 'rotulo-capitulo'
    if s['sz'] >= 30 and s['b']:
        return 'h2'
    if s['sz'] >= 25 and s['b']:
        return 'h3'
    if s['b'] and s['cor'] == '9C7A1E':
        return 'quadro'
    if s['b'] and s['i'] and s['recuo']:
        return 'debate'
    if s['num']:
        return 'item'
    if s['pendente']:
        return 'item-numerado'
    if s['i'] and not s['b']:
        return 'nota'
    if s['b'] and not s['num']:
        return 'destaque'
    return 'p'


def tipo_quadro(rotulo):
    r = rotulo.lower()
    if r.startswith('exemplo'):
        return 'exemplo'
    if r.startswith('atenção') or r.startswith('atencao'):
        return 'atencao'
    if r.startswith('boa prática') or r.startswith('boa pratica'):
        return 'boa-pratica'
    if r.startswith('resposta'):
        return 'resposta'
    return 'nota'


def tabela(tbl):
    linhas = []
    for tr in tbl.iter(W + 'tr'):
        cels = []
        for tc in tr.findall(W + 'tc'):
            cels.append('<br>'.join(h for h in (html_runs(p) for p in tc.iter(W + 'p')) if h))
        linhas.append(cels)
    return {'t': 'tabela', 'cabecalho': linhas[0] if linhas else [], 'linhas': linhas[1:]}


def converter(caminho):
    root = ET.fromstring(zipfile.ZipFile(caminho).read('word/document.xml'))
    for pai in list(root.iter()):
        for filho in list(pai):
            if filho.tag == MC + 'Fallback':
                pai.remove(filho)

    elementos = []
    for el in root.find(W + 'body'):
        if el.tag == W + 'tbl':
            elementos.append(('tabela', el))
        elif el.tag == W + 'p' and texto(el):
            elementos.append((classificar(el), el))

    cap = {'numero': None, 'titulo': '', 'blocos': []}
    blocos = cap['blocos']
    usados = set()
    i = 0
    while i < len(elementos):
        tipo, el = elementos[i]
        i += 1
        if tipo == 'rotulo-capitulo':
            cap['numero'] = int(re.search(r'\d+', texto(el)).group())
        elif tipo == 'titulo':
            cap['titulo'] = texto(el)
        elif tipo == 'h2':
            t = re.sub(r'\s+', ' ', texto(el))
            ident = slug(t) or f'secao-{len(blocos)}'
            while ident in usados:
                ident += '-2'
            usados.add(ident)
            blocos.append({'t': 'h2', 'id': ident, 'texto': t})
        elif tipo == 'h3':
            blocos.append({'t': 'h3', 'texto': texto(el)})
        elif tipo == 'tabela':
            blocos.append(tabela(el))
        elif tipo in ('item', 'item-numerado'):
            itens = [html_runs(el)]
            while i < len(elementos) and elementos[i][0] == tipo:
                itens.append(html_runs(elementos[i][1]))
                i += 1
            blocos.append({'t': 'lista', 'numerada': tipo == 'item-numerado', 'itens': itens})
        elif tipo == 'quadro':
            rotulo = texto(el)
            q = {'t': 'quadro', 'tipo': tipo_quadro(rotulo), 'titulo': rotulo, 'blocos': []}
            # conteúdo do quadro: o próximo parágrafo, ou a lista/tabela que vem logo depois
            if i < len(elementos):
                prox, pel = elementos[i]
                if prox == 'tabela':
                    q['blocos'].append(tabela(pel))
                    i += 1
                elif prox in ('item', 'item-numerado'):
                    itens = []
                    while i < len(elementos) and elementos[i][0] == prox:
                        itens.append(html_runs(elementos[i][1]))
                        i += 1
                    q['blocos'].append({'t': 'lista', 'numerada': prox == 'item-numerado', 'itens': itens})
                elif prox in ('p', 'nota', 'destaque'):
                    q['blocos'].append({'t': 'p', 'html': html_runs(pel)})
                    i += 1
            while i < len(elementos) and elementos[i][0] == 'debate':
                q['blocos'].append({'t': 'p', 'estilo': 'debate', 'html': html_runs(elementos[i][1])})
                i += 1
            blocos.append(q)
        elif tipo == 'debate':
            blocos.append({'t': 'p', 'estilo': 'debate', 'html': html_runs(el)})
        elif tipo == 'nota':
            blocos.append({'t': 'p', 'estilo': 'nota', 'html': html_runs(el)})
        elif tipo == 'destaque':
            blocos.append({'t': 'p', 'estilo': 'destaque', 'html': html_runs(el)})
        else:
            blocos.append({'t': 'p', 'html': html_runs(el)})
    cap['blocos'] = remover_secoes(blocos)
    return cap


# Seções que não vão para o site (a professora usa em sala, fora do material do aluno).
SECOES_REMOVIDAS = ('resumo', 'estudo de caso', 'guia de discussao', 'exercicio',
                    'resolucao passo a passo', 'resolucao dos exercicios')


def remover_secoes(blocos):
    def removida(titulo):
        t = slug(titulo).replace('-', ' ')
        return t.startswith(SECOES_REMOVIDAS)

    saida, pulando = [], False
    for b in blocos:
        if b['t'] == 'h2':
            pulando = removida(b['texto'])
        if b['t'] == 'quadro' and removida(b['titulo']):
            continue  # quadro "Exercícios", "Resumo"...
        if not pulando:
            saida.append(b)
    return saida


# O material é da professora: nada que identifique instituição ou órgão de governo pode ir
# para o site. Se algum destes termos aparecer, a conversão para e o texto deve ser ajustado.
TERMOS_PROIBIDOS = re.compile(
    r'FAETERJ|FAETEC|ENADE|Barra Mansa|Faculdade de Educa[cç][aã]o Tecnol[oó]gica|'
    r'Funda[cç][aã]o de Apoio [àa] Escola T[eé]cnica|Secretaria de Estado de Ci[eê]ncia',
    re.I,
)


def verificar_termos(conteudo):
    """Para a conversão (com o trecho encontrado) se houver referência institucional."""
    m = TERMOS_PROIBIDOS.search(conteudo)
    if m:
        trecho = conteudo[max(0, m.start() - 80):m.end() + 40].replace('\n', ' ')
        sys.exit(f'ERRO: referência institucional encontrada ("{m.group(0)}"): ...{trecho}...\n'
                 'Ajuste o texto antes de publicar.')


if __name__ == '__main__':
    entrada, saida = sys.argv[1], sys.argv[2]
    cap = converter(entrada)
    verificar_termos(json.dumps(cap, ensure_ascii=False))
    with open(saida, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(cap, f, ensure_ascii=False, indent=1)
    contagem = {}
    for b in cap['blocos']:
        contagem[b['t']] = contagem.get(b['t'], 0) + 1
    print(f"Capítulo {cap['numero']}: {cap['titulo']} -> {contagem}")
