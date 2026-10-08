"""Converte capítulos em Word que usam ESTILOS de título e caixas em tabela
(modelo das apostilas de Qualidade e Testes) para o JSON usado pelo site.

Uso:
    python ferramentas/converter_word_estilos.py <arquivo.docx> <saida.json>

Reconhece:
  - "Capítulo N  Título" (azul, 10pt)            -> número e título do capítulo
  - estilo Título 1 / Título 2                    -> h2 (entra no sumário)
  - estilo Título 3 ou subtítulo azul em negrito  -> h3
  - "Parágrafo da Lista" numerado ou com marcador -> listas
  - tabela de 1 coluna (faixa colorida)           -> quadro com título e linhas
  - tabela 1x2 colorida (cartão de ferramenta)    -> quadro com nome e descrição
  - demais tabelas                                -> tabela (1ª linha = cabeçalho)
Descarta: caixa "Conteúdo do capítulo", cabeçalho/rodapé/logo, e as seções e
caixas de Resumo, Estudo de Caso e Exercícios (regra de todas as apostilas).
"""
import json
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

from converter_capitulo import SECOES_REMOVIDAS, W, html_runs, ligado, remover_secoes, slug, texto, verificar_termos

MARCADORES = ('•', '→', '-', '–', '▪', '◦')


def numeracoes(z):
    """numId -> {nível: formato} a partir de word/numbering.xml."""
    try:
        root = ET.fromstring(z.read('word/numbering.xml'))
    except KeyError:
        return {}
    abstratos = {}
    for a in root.findall(W + 'abstractNum'):
        abstratos[a.get(W + 'abstractNumId')] = {
            lvl.get(W + 'ilvl'): (lvl.find(W + 'numFmt').get(W + 'val') if lvl.find(W + 'numFmt') is not None else 'bullet')
            for lvl in a.findall(W + 'lvl')
        }
    mapa = {}
    for n in root.findall(W + 'num'):
        mapa[n.get(W + 'numId')] = abstratos.get(n.find(W + 'abstractNumId').get(W + 'val'), {})
    return mapa


def estilo(p):
    st = p.find(f'{W}pPr/{W}pStyle')
    return st.get(W + 'val') if st is not None else ''


def primeiro_rpr(p):
    for r in p.iter(W + 'r'):
        if ''.join(t.text or '' for t in r.iter(W + 't')).strip():
            return r.find(W + 'rPr')
    return None


def tamanho(rpr):
    sz = rpr.find(W + 'sz') if rpr is not None else None
    return int(sz.get(W + 'val')) if sz is not None else None


def cor(rpr):
    c = rpr.find(W + 'color') if rpr is not None else None
    return (c.get(W + 'val') or '').upper() if c is not None else ''


def preenchimento(tc):
    shd = tc.find(f'{W}tcPr/{W}shd')
    return (shd.get(W + 'fill') or '').upper() if shd is not None else ''


def removida(titulo):
    return slug(titulo).replace('-', ' ').startswith(SECOES_REMOVIDAS)


def tipo_por_titulo_e_cor(titulo, fill):
    t = titulo.lower()
    if t.startswith('exemplo'):
        return 'exemplo'
    if any(p in t for p in ('atenção', 'cuidado', 'erro', 'armadilha', 'anti-padrão', 'evite')):
        return 'atencao'
    if any(p in t for p in ('dica', 'boa prática', 'boas práticas', 'checklist', 'regra')):
        return 'boa-pratica'
    # as caixas coloridas (verde, amarelo, rosa...) alternam cor só por decoração;
    # o tipo vem do título. A faixa azul padrão vira o quadro azul do site.
    if fill == '2E75B6':
        return 'exemplo'
    return 'nota'


def linhas_para_blocos(linhas):
    """Linhas (HTML) de uma caixa -> parágrafos e listas."""
    blocos, itens = [], []

    def fechar_lista():
        nonlocal itens
        if itens:
            blocos.append({'t': 'lista', 'numerada': False, 'itens': itens})
            itens = []

    for h in linhas:
        puro = re.sub(r'<[^>]+>', '', h).strip()
        if not puro:
            fechar_lista()
            continue
        if puro.startswith(MARCADORES):
            # tira o marcador (fica o da lista do site), preservando negrito/itálico
            itens.append(re.sub(r'^((?:<[^>]+>)*)\s*[•→\-–▪◦]\s*', r'\1', h, count=1))
            continue
        fechar_lista()
        maiusculo = puro.upper() == puro and any(c.isalpha() for c in puro)
        if maiusculo or (puro.endswith(':') and len(puro) < 80):
            blocos.append({'t': 'p', 'estilo': 'destaque', 'html': h})
        else:
            blocos.append({'t': 'p', 'html': h})
    fechar_lista()
    return blocos


def paragrafos_da_celula(tc):
    return [html_runs(p) for p in tc.iter(W + 'p')]


def converter_tabela(tbl):
    linhas = tbl.findall(W + 'tr')
    celulas = [r.findall(W + 'tc') for r in linhas]
    ncols = max(len(c) for c in celulas)
    tc0 = celulas[0][0]
    fill = preenchimento(tc0)
    primeiro = texto(tc0)

    if ncols == 1 and primeiro.upper().startswith('CONTEÚDO DO CAPÍTULO'):
        return []
    if ncols == 1:
        if len(linhas) == 1:
            paras = paragrafos_da_celula(tc0)
            titulo, resto = re.sub(r'<[^>]+>', '', paras[0]), paras[1:]
        else:
            titulo = primeiro
            resto = []
            for cels in celulas[1:]:
                resto += paragrafos_da_celula(cels[0])
        if removida(titulo):
            return []
        return [{'t': 'quadro', 'tipo': tipo_por_titulo_e_cor(titulo, fill), 'titulo': titulo,
                 'blocos': linhas_para_blocos(resto)}]
    if ncols == 2 and len(linhas) == 1:
        esquerda = [re.sub(r'<[^>]+>', '', h) for h in paragrafos_da_celula(celulas[0][0]) if h]
        direita = [h for h in paragrafos_da_celula(celulas[0][1]) if h]
        if esquerda and esquerda[0].strip().isdigit() and direita:
            # passo numerado: "1" | título + itens
            titulo = f'Passo {esquerda[0].strip()} — ' + re.sub(r'<[^>]+>', '', direita[0])
            return [{'t': 'quadro', 'tipo': 'nota', 'titulo': titulo, 'blocos': linhas_para_blocos(direita[1:])}]
        # cartão de ferramenta/tipo: nome (e categoria) à esquerda, descrição à direita.
        # As cores dos cartões se alternam só por decoração, então todos usam o mesmo estilo.
        titulo = esquerda[0] + (f' ({", ".join(esquerda[1:])})' if len(esquerda) > 1 else '')
        return [{'t': 'quadro', 'tipo': 'nota', 'titulo': titulo, 'blocos': linhas_para_blocos(direita)}]

    def celula(tc):
        return '<br>'.join(h for h in paragrafos_da_celula(tc) if h)

    cab = [re.sub(r'</?strong>', '', celula(tc)) for tc in celulas[0]]
    return [{'t': 'tabela', 'cabecalho': cab, 'linhas': [[celula(tc) for tc in cels] for cels in celulas[1:]]}]


def converter(caminho):
    z = zipfile.ZipFile(caminho)
    root = ET.fromstring(z.read('word/document.xml'))
    nums = numeracoes(z)
    cap = {'numero': None, 'titulo': '', 'blocos': []}
    blocos = []
    lista_atual = None

    def fechar_lista():
        nonlocal lista_atual
        if lista_atual:
            blocos.append(lista_atual)
        lista_atual = None

    for el in root.find(W + 'body'):
        if el.tag == W + 'tbl':
            fechar_lista()
            blocos += converter_tabela(el)
            continue
        if el.tag != W + 'p' or not texto(el):
            continue
        t = re.sub(r'\s+', ' ', texto(el))
        st = estilo(el)
        rpr = primeiro_rpr(el)
        sz = tamanho(rpr)
        m = re.match(r'Cap[ií]tulo\s+(\d+)\s+(.+)', t)
        if m and cap['numero'] is None and not st:
            cap['numero'], cap['titulo'] = int(m.group(1)), m.group(2).strip()
            continue
        if sz and sz >= 36:  # faixa "QUALIDADE E TESTE DE SOFTWARE"
            continue
        numpr = el.find(f'{W}pPr/{W}numPr')
        if numpr is not None:
            num_id = numpr.find(W + 'numId').get(W + 'val') if numpr.find(W + 'numId') is not None else ''
            nivel = numpr.find(W + 'ilvl').get(W + 'val') if numpr.find(W + 'ilvl') is not None else '0'
            numerada = nums.get(num_id, {}).get(nivel, 'bullet') not in ('bullet', 'none')
            if lista_atual is None or lista_atual['_id'] != num_id:
                fechar_lista()
                lista_atual = {'t': 'lista', 'numerada': numerada, 'itens': [], '_id': num_id}
            item = html_runs(el)
            if numerada:
                item = f'{len(lista_atual["itens"]) + 1}. {item}'
            lista_atual['itens'].append(item)
            continue
        fechar_lista()
        if removida(t) and len(t) < 60:
            # "Resumo do Capítulo N" / "Exercícios de Fixação" com qualquer formatação
            blocos.append({'t': 'h2', 'id': '', 'texto': t})
        elif re.match(r'(Ttulo|Heading|Titulo)[12]$', st):
            blocos.append({'t': 'h2', 'id': '', 'texto': t})
        elif re.match(r'(Ttulo|Heading|Titulo)3$', st):
            blocos.append({'t': 'h3', 'texto': t})
        elif ligado(rpr, 'b') and sz and sz >= 25:
            blocos.append({'t': 'h2', 'id': '', 'texto': t})
        elif sz and sz >= 21 and len(t) < 120 and cor(rpr) not in ('', '000000', 'AUTO'):
            # subtítulo azul (em alguns capítulos o negrito vem do estilo, não do texto)
            blocos.append({'t': 'h3', 'texto': t})
        else:
            blocos.append({'t': 'p', 'html': html_runs(el)})
    fechar_lista()
    for b in blocos:
        b.pop('_id', None)

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
    cap['blocos'] = remover_secoes(blocos)
    return cap


if __name__ == '__main__':
    entrada, saida = sys.argv[1], sys.argv[2]
    cap = converter(entrada)
    conteudo = json.dumps(cap, ensure_ascii=False, indent=1)
    verificar_termos(conteudo)
    with open(saida, 'w', encoding='utf-8', newline='\n') as f:
        f.write(conteudo)
    contagem = {}
    for b in cap['blocos']:
        contagem[b['t']] = contagem.get(b['t'], 0) + 1
    print(f"Capítulo {cap['numero']}: {cap['titulo']} -> {contagem}")
