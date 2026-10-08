"""Converte um Word simples de "comandos" (como COMANDOS GITHUB.docx) para o JSON do site.

Uso:
    python ferramentas/converter_word_comandos.py <arquivo.docx> <saida.json> [--numero N]

Modelo reconhecido (Word sem estilos de título):
  - primeiro parágrafo grande em negrito          -> título do material
  - demais parágrafos grandes em negrito (16pt)   -> seções (h2)
  - item numerado começando em negrito            -> subtítulo do comando (h3) + explicação
  - linha curta toda em negrito                   -> subtítulo menor (parágrafo em destaque)
  - "COMANDO ABAIXO" (marcado em verde)           -> o parágrafo seguinte vira bloco de código
  - linhas de comando soltas (git ..., # saída)   -> bloco de código
Parágrafos repetidos em sequência aparecem uma vez só.
"""
import html
import json
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

from converter_capitulo import remover_secoes, slug, verificar_termos

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
COMANDO = re.compile(r'^(git|touch|mv|cd|mkdir|ls|npm|npx|man)\b|^#')


def eh_linha_de_comando(linha):
    linha = linha.strip()
    if linha.startswith('nothing added'):
        return True
    # texto corrido que começa com "git ..." não é comando: é longo ou tem frase com ponto final
    return bool(COMANDO.match(linha)) and len(linha) < 90 and not re.search(r'[a-zà-ú]\.\s+[A-ZÀ-Ú]', linha)


def ler_paragrafo(p):
    """Devolve (pedaços [(texto, negrito)], tamanho, marcado_em_verde, numerado)."""
    pedacos, tamanho, verde = [], None, False
    for r in p.iter(W + 'r'):
        rpr = r.find(W + 'rPr')
        neg = rpr is not None and rpr.find(W + 'b') is not None and rpr.find(W + 'b').get(W + 'val', 'true') not in ('0', 'false')
        if rpr is not None and rpr.find(W + 'sz') is not None:
            tamanho = max(tamanho or 0, int(rpr.find(W + 'sz').get(W + 'val')))
        if rpr is not None and rpr.find(W + 'highlight') is not None:
            verde = True
        for ch in r:
            if ch.tag == W + 't':
                pedacos.append((ch.text or '', neg))
            elif ch.tag == W + 'br':
                pedacos.append(('\n', neg))
            elif ch.tag == W + 'tab':
                pedacos.append(('\t', neg))
    ppr = p.find(W + 'pPr')
    numerado = ppr is not None and ppr.find(W + 'numPr') is not None
    return pedacos, tamanho, verde, numerado


def texto(pedacos):
    return ''.join(t for t, _ in pedacos)


def html_de(pedacos):
    out = ''
    for t, n in pedacos:
        t = html.escape(t, quote=False).replace('\n', '<br>')
        out += f'<strong>{t}</strong>' if n and t.strip() else t
    return re.sub(r'</strong>(\s*)<strong>', r'\1', out).strip()


def corrigir_comando(t):
    # o Word troca "--" por travessão e usa espaço especial; em comando isso não funciona
    t = t.replace('\xa0', ' ')
    return re.sub(r'(^|\s)[–—](?=[a-z])', r'\1--', t)


def converter(caminho):
    root = ET.fromstring(zipfile.ZipFile(caminho).read('word/document.xml'))
    paras = [ler_paragrafo(p) for p in root.find(W + 'body').iter(W + 'p')]
    paras = [p for p in paras if texto(p[0]).strip()]

    titulo, blocos = None, []
    anterior = None
    i = 0
    while i < len(paras):
        pedacos, tam, verde, num = paras[i]
        t = texto(pedacos).replace('\xa0', ' ').strip()
        i += 1
        if re.sub(r'\s+', ' ', t) == re.sub(r'\s+', ' ', anterior or ''):
            continue  # parágrafo repetido em sequência
        anterior = t
        todo_negrito = all(n for x, n in pedacos if x.strip())

        if tam and tam >= 30 and todo_negrito:
            if titulo is None:
                titulo = t
            else:
                blocos.append({'t': 'h2', 'id': '', 'texto': t})
        elif verde and t.upper().startswith('COMANDO'):
            if i < len(paras):
                cod = texto(paras[i][0]).strip()
                blocos.append({'t': 'codigo', 'texto': corrigir_comando(cod)})
                anterior = cod
                i += 1
        elif num and pedacos and pedacos[0][1]:
            # "GIT CLONE – clonando... Explicação" -> subtítulo (parte em negrito) + explicação
            cab = ''
            k = 0
            while k < len(pedacos) and (pedacos[k][1] or not pedacos[k][0].strip()):
                cab += pedacos[k][0]
                k += 1
            cab = cab.strip()
            m = re.match(r'(.+?[–-]\s*[^.]+?)(?:\.\s+|\s+-\s+)(.+)', cab) if not pedacos[k:] else None
            resto = pedacos[k:]
            if m and not resto:
                cab, resto = m.group(1), [(m.group(2), False)]
            blocos.append({'t': 'h3', 'texto': re.sub(r'\s+', ' ', cab).strip(' -–.')})
            corpo = html_de(resto).lstrip(' -–.')
            if corpo:
                blocos.append({'t': 'p', 'html': corpo})
        elif todo_negrito and len(t) < 70:
            blocos.append({'t': 'p', 'estilo': 'destaque', 'html': html.escape(t.title() if t.isupper() else t)})
        elif all(eh_linha_de_comando(l) for l in t.split('\n') if l.strip()):
            # linhas de comando ou saída do terminal: junta com as seguintes do mesmo tipo
            linhas = [t]
            while i < len(paras):
                prox = texto(paras[i][0]).strip()
                if prox and all(eh_linha_de_comando(l) for l in prox.split('\n')) \
                        and not all(n for x, n in paras[i][0] if x.strip()):
                    linhas.append(prox)
                    i += 1
                else:
                    break
            blocos.append({'t': 'codigo', 'texto': corrigir_comando('\n'.join(linhas))})
        else:
            blocos.append({'t': 'p', 'html': html_de(pedacos)})

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
    return {'numero': None, 'titulo': titulo or '', 'blocos': remover_secoes(blocos)}


if __name__ == '__main__':
    args = sys.argv[1:]
    numero = None
    if '--numero' in args:
        k = args.index('--numero')
        numero = int(args[k + 1])
        del args[k:k + 2]
    trocas, remover = [], []
    while '--trocar' in args:
        k = args.index('--trocar')
        trocas.append(tuple(args[k + 1].split('=>')))
        del args[k:k + 2]
    while '--remover-primeiro' in args:
        k = args.index('--remover-primeiro')
        remover.append(args[k + 1])
        del args[k:k + 2]
    cap = converter(args[0])
    cap['numero'] = numero
    for inicio in remover:  # tira a primeira ocorrência de um parágrafo (ex.: colado no lugar errado)
        k = next((j for j, b in enumerate(cap['blocos']) if b['t'] == 'p' and b['html'].startswith(inicio)), None)
        if k is None:
            sys.exit(f'ERRO: parágrafo não encontrado: {inicio!r}')
        del cap['blocos'][k]
    conteudo = json.dumps(cap, ensure_ascii=False, indent=1)
    for antigo, novo in trocas:
        if antigo not in conteudo:
            sys.exit(f'ERRO: texto para trocar não encontrado: {antigo!r}')
        conteudo = conteudo.replace(antigo, novo)
    cap = json.loads(conteudo)
    verificar_termos(conteudo)
    with open(args[1], 'w', encoding='utf-8', newline='\n') as f:
        f.write(conteudo)
    contagem = {}
    for b in cap['blocos']:
        contagem[b['t']] = contagem.get(b['t'], 0) + 1
    print(f"{cap['titulo']} -> {contagem}")
