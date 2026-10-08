"""Converte um capítulo em PDF gerado pelo modelo LaTeX das apostilas
(\\topico, \\subtopico, destaque, longtable) para o JSON usado pelo site.

Use só quando NÃO houver o arquivo-fonte (.tex/.docx) da versão mais nova.

Uso:
    python ferramentas/converter_pdf_latex.py <capitulo.pdf> <saida.json>

Como o PDF é lido:
  - capa e "Sumário do capítulo" (páginas sem cabeçalho) são ignorados,
    assim como cabeçalho e rodapé de cada página;
  - "SEÇÃO x.y" + título grande               -> h2
  - título grande sem número                  -> h2 (Resumo, Estudo de Caso... são removidos depois)
  - linha toda em negrito, sem traço acima     -> h3 (\\subtopico)
  - traço colorido + linha em negrito          -> quadro (destaque) com o texto logo abaixo
  - cabeçalho de texto branco                  -> tabela (colunas pela posição do cabeçalho)
  - letras com códigos de controle da fonte T1 do LaTeX são traduzidas
    (0x1C = "fi", 0x1D = "fl", 0x15 = "–", 0x16 = "—" ...)
"""
import html
import json
import re
import sys

import pymupdf

from converter_capitulo import remover_secoes, slug, verificar_termos

# Codificação T1 do LaTeX: posições que o PDF não traduz para Unicode
T1 = {
    '\x15': '–', '\x16': '—', '\x1b': 'ff', '\x1c': 'fi', '\x1d': 'fl', '\x1e': 'ffi', '\x1f': 'ffl',
    '\x10': '“', '\x11': '”', '\x12': '„', '\x13': '«', '\x14': '»', '\x0d': '‚', '\x0e': '‹', '\x0f': '›',
}

# distâncias verticais (em pontos) entre o fim de uma linha e o começo da seguinte
NOVO_PARAGRAFO = 5    # parskip: separa parágrafos
FIM_DO_QUADRO = 15    # \bigskip depois de um destaque
MARGEM_DIREITA = 524  # linhas justificadas terminam aqui; antes disso = quebra forçada
QUEBRA = '\x01'       # marca interna de quebra de linha


def cor_rgb(c):
    return tuple(int(v * 255) for v in c) if c else None


def eh_cor_destaque(rgb):
    # traço dos quadros/seções: cor de destaque (vinho), não preto
    return rgb is not None and rgb != (0, 0, 0) and max(rgb) - min(rgb) > 30


class Linha:
    def __init__(self, pagina, line):
        self.pagina = pagina
        self.y0, self.y1 = line['bbox'][1], line['bbox'][3]
        self.x0, self.x1 = line['bbox'][0], line['bbox'][2]
        self.spans = [s for s in line['spans'] if ''.join(c['c'] for c in s['chars']).strip()]
        self.size = max(s['size'] for s in self.spans)
        self.cor = self.spans[0]['color']
        self.fontes = {s['font'] for s in self.spans}
        self.bruto = ''.join(c['c'] for s in self.spans for c in s['chars'])

    def eh_secao(self):
        return self.size < 10.5 and self.cor not in (0, 0xFFFFFF) and 'SEÇÃO' in self.bruto

    def html(self, negrito, faixa=None):
        # Linhas justificadas não trazem o espaço como caractere: ele é deduzido
        # pela distância entre o fim de uma letra e o começo da próxima.
        # faixa=(xa, xb): só as letras dessa faixa horizontal (uma coluna de tabela).
        pedacos = []
        fim_anterior, ultimo = None, ''
        for s in self.spans:
            t = ''
            for c in s['chars']:
                x0, x1 = c['bbox'][0], c['bbox'][2]
                if faixa and not (faixa[0] <= (x0 + x1) / 2 < faixa[1]):
                    continue
                if (fim_anterior is not None and x0 - fim_anterior > 0.15 * s['size']
                        and c['c'] != ' ' and ultimo != ' '):
                    t += ' '
                t += T1.get(c['c'], c['c'])
                fim_anterior, ultimo = x1, c['c']
            pedacos.append((t, s['font'] in negrito))
        h = ''
        for t, n in pedacos:
            t = html.escape(t, quote=False)
            if n and t.strip():
                esq, meio, dir_ = re.match(r'^(\s*)(.*?)(\s*)$', t, re.S).groups()
                h += f'{esq}<strong>{meio}</strong>{dir_}'
            else:
                h += t
        return re.sub(r'</strong>(\s*)<strong>', r'\1', h)

    def texto(self, negrito=()):
        return re.sub(r'<[^>]+>', '', self.html(negrito)).strip()


def ler(caminho):
    doc = pymupdf.open(caminho)
    numero, titulo = None, []
    for b in doc[0].get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ''.join(s['text'] for s in l['spans']).strip()
            m = re.match(r'CAP[IÍ]TULO\s*(\d+)', t)
            if m:
                numero = int(m.group(1))
            elif max(s['size'] for s in l['spans']) > 18:
                titulo.append(''.join(T1.get(ch, ch) for ch in t))
    titulo = re.sub(r'-\s+', '-', ' '.join(titulo))

    itens = []  # ('traco'|'linha', pagina, y, objeto)
    preenchidos = []  # (pagina, y0, y1, x0, x1): fundos das células de tabela
    for pno, page in enumerate(doc):
        d = page.get_text('rawdict')
        linhas = [l for b in d['blocks'] for l in b.get('lines', [])
                  if ''.join(c['c'] for s in l['spans'] for c in s['chars']).strip()]
        if not any(l['bbox'][1] < 45 for l in linhas):
            continue  # capa e sumário do capítulo não têm cabeçalho
        for dr in page.get_drawings():
            r = dr['rect']
            if dr.get('fill') and 50 < r.y0 < 780:
                preenchidos.append((pno, r.y0, r.y1, r.x0, r.x1))
            if not dr.get('fill') and r.width > 400 and 50 < r.y0 < 780 and eh_cor_destaque(cor_rgb(dr.get('color'))):
                itens.append(('traco', pno, r.y0, None))
        for l in linhas:
            if 45 < l['bbox'][1] < 780:
                itens.append(('linha', pno, l['bbox'][1], Linha(pno, l)))
    itens.sort(key=lambda i: (i[1], i[2], 0 if i[0] == 'traco' else 1))

    # fonte em negrito = a do título que vem logo abaixo de um traço de quadro
    negrito = set()
    for k, (tipo, p, y, obj) in enumerate(itens):
        if tipo == 'traco' and k + 1 < len(itens) and itens[k + 1][0] == 'linha':
            prox = itens[k + 1][3]
            if prox.pagina == p and prox.y0 - y < 12 and not prox.eh_secao() and prox.size < 12:
                negrito |= prox.fontes
    return numero, titulo, itens, negrito, preenchidos


def juntar(partes):
    """Une linhas de um parágrafo desfazendo a hifenização de fim de linha.
    Uma parte terminada em QUEBRA indica quebra de linha forçada no original."""
    texto = ''
    for h in partes:
        h = h.strip()
        if texto.endswith(QUEBRA):
            texto = texto[:-len(QUEBRA)] + '<br>' + h
        elif texto.endswith('-') and re.match(r'(<[^>]+>)*[a-zà-ú]', h):
            texto = texto[:-1] + h
        elif texto:
            texto += ' ' + h
        else:
            texto = h
    texto = texto.replace(QUEBRA, '')
    return re.sub(r'</strong> <strong>', ' ', texto)


def converter(caminho):
    numero, titulo, itens, negrito, preenchidos = ler(caminho)
    n = len(itens)
    blocos = []

    def lin(k):
        return itens[k][3] if 0 <= k < n and itens[k][0] == 'linha' else None

    def distancia(a, b):
        """espaço vertical entre a linha a e a linha b; na troca de página, conta a partir do topo"""
        la, lb = lin(a), lin(b)
        if la.pagina != lb.pagina:
            return lb.y0 - 85  # o texto da página seguinte começa por volta de y=72..89
        return lb.y0 - la.y1

    def toda_negrito(l):
        return all(s['font'] in negrito for s in l.spans)

    def eh_titulo(l):
        return l.size > 12 or l.eh_secao() or toda_negrito(l) or l.cor == 0xFFFFFF

    def paragrafo(k):
        partes = [lin(k).html(negrito)]
        k += 1
        while lin(k) and not eh_titulo(lin(k)) and lin(k).x0 < 100 and distancia(k - 1, k) <= NOVO_PARAGRAFO:
            if lin(k - 1).x1 < MARGEM_DIREITA - 40:
                partes[-1] += QUEBRA
            partes.append(lin(k).html(negrito))
            k += 1
        return juntar(partes), k

    i = 0
    while i < n:
        tipo, p, y, l = itens[i]
        if tipo == 'traco':
            prox = lin(i + 1)
            if prox and toda_negrito(prox) and not prox.eh_secao() and prox.y0 - y < 12:
                tit = prox.texto(negrito)
                k = i + 2
                corpo = []
                while lin(k) and not eh_titulo(lin(k)) and lin(k).x0 < 100 and distancia(k - 1, k) < FIM_DO_QUADRO:
                    h, k = paragrafo(k)
                    corpo.append({'t': 'p', 'html': h})
                blocos.append({'t': 'quadro', 'tipo': tipo_quadro(tit), 'titulo': tit, 'blocos': corpo})
                i = k
            else:
                i += 1
            continue

        if l.eh_secao():
            num = re.search(r'\d+\.\d+', l.bruto).group(0)
            tit = ''
            if lin(i + 1) and lin(i + 1).size > 12:
                tit = lin(i + 1).texto(negrito)
                i += 1
            blocos.append({'t': 'h2', 'id': '', 'texto': f'{num} {tit}'})
            i += 1
        elif l.size > 12:
            blocos.append({'t': 'h2', 'id': '', 'texto': l.texto(negrito)})
            i += 1
        elif l.cor == 0xFFFFFF:
            i = tabela(i, itens, lin, negrito, blocos, preenchidos)
        elif toda_negrito(l):
            blocos.append({'t': 'h3', 'texto': l.texto(negrito)})
            i += 1
        else:
            h, i = paragrafo(i)
            blocos.append({'t': 'p', 'html': h})

    if blocos and blocos[0]['t'] != 'h2':
        blocos.insert(0, {'t': 'h2', 'id': '', 'texto': 'Introdução'})
    usados = set()
    for b in blocos:
        if b['t'] == 'h2':
            ident = slug(b['texto']) or 'secao'
            while ident in usados:
                ident += '-2'
            usados.add(ident)
            b['id'] = ident
    return {'numero': numero, 'titulo': titulo, 'blocos': remover_secoes(blocos)}


def tabela(i, itens, lin, negrito, blocos, preenchidos):
    """Lê uma tabela a partir da linha de cabeçalho (texto branco) em i; devolve o próximo índice.

    Colunas: início de cada retângulo de fundo do cabeçalho. Linhas da tabela: faixas
    delimitadas pelas bordas dos fundos coloridos (as linhas alternadas têm fundo), o que
    mantém juntas as células que ocupam várias linhas de texto.
    """
    l0 = lin(i)
    colunas = sorted({round(f[3], 1) for f in preenchidos
                      if f[0] == l0.pagina and f[1] - 2 <= l0.y0 <= f[2]}) or [l0.x0 - 6]
    limites = colunas[1:] + [10_000]

    def faixa_col(j):
        return (colunas[j] if j else 0, limites[j])

    bordas = {}
    for (pg, y0, y1, x0, x1) in preenchidos:
        if x0 >= colunas[0] - 8:
            bordas.setdefault(pg, set()).update({round(y0, 1), round(y1, 1)})

    def faixa_linha(l):
        meio = (l.y0 + l.y1) / 2
        return (l.pagina, sum(1 for v in bordas.get(l.pagina, ()) if v <= meio))

    k = i
    membros = []
    while k < len(itens):
        if itens[k][0] == 'traco':
            break
        lk = lin(k)
        if lk.x0 < colunas[0] - 8 or lk.size > 12:
            break
        membros.append(lk)
        k += 1

    grupos, ordem = {}, []
    for lk in membros:
        chave = faixa_linha(lk)
        if chave not in grupos:
            grupos[chave] = [[] for _ in colunas]
            ordem.append(chave)
        for j in range(len(colunas)):
            h = lk.html(negrito, faixa_col(j))
            if h.strip():
                grupos[chave][j].append(h)

    linhas = [[juntar(c) for c in grupos[ch]] for ch in ordem]
    cabecalho = [re.sub(r'</?strong>', '', c) for c in linhas[0]] if linhas else []
    blocos.append({'t': 'tabela', 'cabecalho': cabecalho, 'linhas': linhas[1:]})
    return k


def tipo_quadro(titulo):
    t = titulo.lower()
    if t.startswith('exemplo'):
        return 'exemplo'
    if any(p in t for p in ('atenção', 'cuidado', 'anti-padrão')):
        return 'atencao'
    if any(p in t for p in ('regra', 'boa prática', 'dica')):
        return 'boa-pratica'
    return 'nota'


if __name__ == '__main__':
    # uso opcional: --trocar "texto antigo=>texto novo" (pode repetir), aplicado antes da verificação
    args = sys.argv[1:]
    trocas = []
    while '--trocar' in args:
        k = args.index('--trocar')
        antigo, novo = args[k + 1].split('=>')
        trocas.append((antigo, novo))
        del args[k:k + 2]
    entrada, saida = args[0], args[1]
    cap = converter(entrada)
    texto = json.dumps(cap, ensure_ascii=False, indent=1)
    for antigo, novo in trocas:
        if antigo not in texto:
            sys.exit(f'ERRO: texto para trocar não encontrado: {antigo!r}')
        texto = texto.replace(antigo, novo)
    cap = json.loads(texto)
    verificar_termos(texto)
    with open(saida, 'w', encoding='utf-8', newline='\n') as f:
        f.write(texto)
    contagem = {}
    for b in cap['blocos']:
        contagem[b['t']] = contagem.get(b['t'], 0) + 1
    print(f"Capítulo {cap['numero']}: {cap['titulo']} -> {contagem}")
