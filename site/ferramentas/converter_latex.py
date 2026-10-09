"""Converte capítulos de apostila em LaTeX (.tex) para o JSON usado pelo site.

Uso:
    python ferramentas/converter_latex.py <arquivo.tex> <saida.json>

Reconhece os comandos do modelo das apostilas:
  \\topico{1.1}{Título}            -> h2 (entra no sumário)
  \\subtopico{Título}              -> h3
  \\begin{destaque}{Título} ...    -> quadro destacado
  longtable                       -> tabela (linha com \\tbh = cabeçalho)
  itemize / enumerate             -> listas
  \\termo, \\textbf, \\textit, \\texttt -> negrito, itálico, código
Também aceita o modelo "por módulos" (Web Design II):
  \\modulotitulo{01}{Título}       -> número e título do capítulo
  \\subsection / \\subsubsection    -> h2 / h3
  codigo + Verbatim               -> bloco de código (texto literal)
  \\includegraphics               -> imagem (copiada com --imagens <pasta> <url>; PDF vira PNG)
  tabular                         -> tabela
E o modelo "livro" (Guia Node.js, Express e MySQL):
  \\section{Capítulo N -- Título} ou \\section{Apêndice A -- Título} -> número e título
Capa, sumário do capítulo, cabeçalho e rodapé são descartados, assim como as
seções de Resumo, Estudo de Caso e Exercícios de Fixação (mesma regra do
converter_capitulo.py).
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys

from converter_capitulo import remover_secoes, slug, verificar_termos

SIMBOLOS = {
    'square': '\u2610', 'approx': '\u2248', 'geq': '\u2265', 'leq': '\u2264', 'to': '\u2192',
    'rightarrow': '\u2192', 'times': '\u00d7', 'checkmark': '\u2713', 'ldots': '\u2026', 'dots': '\u2026',
    'quad': ' ', 'qquad': ' ', 'textbackslash': '\\', 'S': '\u00a7',
}
DESCARTAR = {'noindent', 'bigskip', 'medskip', 'smallskip', 'newpage', 'centering', 'small', 'large',
             'Large', 'huge', 'Huge', 'bfseries', 'itshape', 'par', 'hfill', 'clearpage', 'raggedright'}
DESCARTAR_COM_ARGS = {'vspace': 1, 'hspace': 1, 'addcontentsline': 3, 'thispagestyle': 1, 'setcounter': 2,
                      'label': 1, 'color': 1, 'rowcolor': 1, 'includegraphics': 1}
FORMATO = {'termo': 'strong', 'textbf': 'strong', 'textit': 'em', 'emph': 'em', 'texttt': 'code'}


def ler_grupo(s, i):
    """Lê {…} a partir de s[i] (que deve ser '{'). Retorna (conteúdo, posição após '}')."""
    assert s[i] == '{', s[i:i + 30]
    nivel, j = 0, i
    while j < len(s):
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            nivel += 1
        elif c == '}':
            nivel -= 1
            if nivel == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError('chave sem fechamento: ' + s[i:i + 60])


def pular_espacos(s, i):
    while i < len(s) and s[i] in ' \t\n':
        i += 1
    return i


def tipografia(t):
    t = t.replace('---', '\u2014').replace('--', '\u2013')
    t = t.replace('``', '\u201c').replace("''", '\u201d')
    return t


SIMBOLOS_MAT = {'le': '\u2264', 'ge': '\u2265', 'cdot': '\u00b7', 'Omega': '\u03a9', 'Theta': '\u0398',
                'log': 'log', 'ln': 'ln', 'infty': '\u221e', 'neq': '\u2260', 'pm': '\u00b1'}


def matematica(mat):
    """Fórmula LaTeX simples em HTML: símbolos viram caracteres e potências/índices viram <sup>/<sub>."""
    mat = re.sub(r'\\text\s*\{([^}]*)\}', r'\1', mat)
    for nome, simb in {**SIMBOLOS, **SIMBOLOS_MAT}.items():
        mat = re.sub(r'\\' + nome + r'(?![a-zA-Z])', lambda _, s=simb: s, mat)
    mat = re.sub(r'\\[,;:!]', ' ', mat).replace('\\', '')
    mat = html.escape(mat, quote=False)
    for marca, tag in (('^', 'sup'), ('_', 'sub')):
        mat = re.sub(re.escape(marca) + r'\{([^}]*)\}', rf'<{tag}>\1</{tag}>', mat)
        mat = re.sub(re.escape(marca) + r'([\w*])', rf'<{tag}>\1</{tag}>', mat)
    return re.sub(r'\s+', ' ', mat.replace('{', '').replace('}', '')).strip()


def inline(s, codigo=False):
    """Converte texto LaTeX de um parágrafo em HTML simples."""
    out = []
    i = 0
    texto = ''

    def descarregar():
        nonlocal texto
        if texto:
            t = html.escape(texto, quote=False)
            out.append(t if codigo else tipografia(t))
            texto = ''

    while i < len(s):
        c = s[i]
        if c == '%' and (i == 0 or s[i - 1] != '\\'):
            fim = s.find('\n', i)
            i = len(s) if fim < 0 else fim + 1
            continue
        if c == '~':
            texto += '\u00a0'
            i += 1
            continue
        if c == '$' or s.startswith('\\[', i):
            # $...$ no meio do texto ou \[...\] em destaque (no site vira o próprio parágrafo)
            fecha = '$' if c == '$' else '\\]'
            ini = i + (1 if c == '$' else 2)
            fim = s.find(fecha, ini)
            if codigo:
                texto += s[ini:fim]
            else:
                descarregar()
                out.append(matematica(s[ini:fim]))
            i = fim + len(fecha)
            continue
        if c in '{}':
            i += 1
            continue
        if c != '\\':
            texto += c
            i += 1
            continue
        # comando
        m = re.match(r'\\([a-zA-Z]+)\*?', s[i:])
        if not m:
            prox = s[i + 1:i + 2]
            if prox == '\\':
                descarregar()
                out.append('<br>')
                i += 2
                # \\[3pt]
                if s[i:i + 1] == '[':
                    i = s.index(']', i) + 1
            else:
                texto += {' ': ' ', ',': '\u202f'}.get(prox, prox)
                i += 2
            continue
        nome = m.group(1)
        i += len(m.group(0))
        if nome in FORMATO:
            j = pular_espacos(s, i)
            arg, i = ler_grupo(s, j)
            descarregar()
            tag = FORMATO[nome]
            out.append(f'<{tag}>{inline(arg, codigo=codigo or tag == "code")}</{tag}>')
        elif nome == 'textcolor':
            _, i = ler_grupo(s, pular_espacos(s, i))
            arg, i = ler_grupo(s, pular_espacos(s, i))
            descarregar()
            out.append(inline(arg, codigo))
        elif nome == 'tbh':
            arg, i = ler_grupo(s, pular_espacos(s, i))
            descarregar()
            out.append(inline(arg, codigo))
        elif nome == 'href':
            url, i = ler_grupo(s, pular_espacos(s, i))
            arg, i = ler_grupo(s, pular_espacos(s, i))
            descarregar()
            out.append(f'<a href="{html.escape(url)}" target="_blank" rel="noreferrer">{inline(arg)}</a>')
        elif nome == 'url':
            url, i = ler_grupo(s, pular_espacos(s, i))
            descarregar()
            out.append(f'<a href="{html.escape(url)}" target="_blank" rel="noreferrer">{html.escape(url)}</a>')
        elif nome in DESCARTAR_COM_ARGS:
            for _ in range(DESCARTAR_COM_ARGS[nome]):
                j = pular_espacos(s, i)
                if s[j:j + 1] == '[':
                    j = s.index(']', j) + 1
                    j = pular_espacos(s, j)
                if s[j:j + 1] == '{':
                    _, i = ler_grupo(s, j)
        elif nome in SIMBOLOS:
            texto += SIMBOLOS[nome]
            if s[i:i + 2] == '{}':
                i += 2
        elif nome in DESCARTAR:
            pass
        else:
            texto += nome  # comando desconhecido: mantém o nome para não perder texto
    descarregar()
    h = ''.join(out)
    h = re.sub(r'[ \t\n]+', ' ', h)
    return h.strip()


def achar_fim_ambiente(s, nome, inicio):
    """Posição do \\end{nome} que fecha o ambiente aberto antes de 'inicio'."""
    abre, fecha = '\\begin{' + nome + '}', '\\end{' + nome + '}'
    nivel, i = 1, inicio
    while True:
        a, f = s.find(abre, i), s.find(fecha, i)
        if f < 0:
            raise ValueError('ambiente sem fim: ' + nome)
        if 0 <= a < f:
            nivel += 1
            i = a + len(abre)
        else:
            nivel -= 1
            if nivel == 0:
                return f
            i = f + len(fecha)


def tipo_quadro(titulo):
    t = titulo.lower()
    if t.startswith('exemplo'):
        return 'exemplo'
    if t.startswith('resposta'):
        return 'resposta'
    if any(p in t for p in ('atenção', 'anti-padrão', 'corrói', 'não funcionar', 'cuidado', 'erro')):
        return 'atencao'
    if any(p in t for p in ('regra', 'referência', 'roi', 'prontos', 'não podem faltar', 'objetivo', 'boa prática',
                            'checklist')):
        return 'boa-pratica'
    return 'nota'


def dividir_itens(s):
    """Separa os \\item de uma lista (ignorando listas aninhadas)."""
    itens, nivel, atual, i = [], 0, None, 0
    while i < len(s):
        if s.startswith('\\begin{', i):
            nivel += 1
        elif s.startswith('\\end{', i):
            nivel -= 1
        elif nivel == 0 and re.match(r'\\item(?![a-zA-Z])', s[i:]):
            if atual is not None:
                itens.append(atual)
            atual = ''
            i += 5
            continue
        if atual is not None:
            atual += s[i]
        i += 1
    if atual is not None:
        itens.append(atual)
    return itens


def codigo_no_item(it):
    """Bloco de código dentro de um item de lista (passo a passo do livro Node.js) vira <pre> no próprio item."""
    trechos = []

    def guardar(m):
        trechos.append('<pre class="bloco-codigo"><code>' + html.escape(LITERAIS[int(m.group(1))]) + '</code></pre>')
        return f'\x03{len(trechos) - 1}\x03'
    it = re.sub(r'(?:\\begin\{codigo\})?\s*\x02(\d+)\x02\s*(?:\\end\{codigo\})?', guardar, it)
    return it, trechos


def lista(corpo, numerada):
    itens = []
    for n, it in enumerate(dividir_itens(corpo), 1):
        it, trechos = codigo_no_item(it.strip())
        marcador = ''
        if it.startswith('['):
            fim = it.index(']')
            marcador = inline(it[1:fim])
            it = it[fim + 1:]
        h = re.sub(r'\x03(\d+)\x03', lambda m: trechos[int(m.group(1))], inline(it))
        if marcador:
            h = f'{marcador} {h}'
        elif numerada:
            h = f'{n}. {h}'
        itens.append(h)
    # listas numeradas e de verificação levam o marcador no próprio texto
    return {'t': 'lista', 'numerada': numerada or any(i.startswith('\u2610') for i in itens), 'itens': itens}


def tabela(corpo):
    k = pular_espacos(corpo, 0)
    if corpo[k:k + 1] == '{':  # especificação de colunas, ex.: {L{3cm} L{4cm}}
        _, k = ler_grupo(corpo, k)
        corpo = corpo[k:]
    for cmd in ('toprule', 'midrule', 'bottomrule', 'hline', 'endhead', 'endfirsthead', 'endfoot', 'endlastfoot'):
        corpo = corpo.replace('\\' + cmd, '')
    linhas_tex = [l for l in re.split(r'\\\\\s*(?:\[[^]]*\])?', corpo) if l.strip()]
    cabecalho, linhas = [], []
    for l in linhas_tex:
        e_cabecalho = '\\tblheader' in l or '\\tbh' in l
        l = l.replace('\\tblheader', '')
        cels = [inline(c) for c in re.split(r'(?<!\\)&', l)]
        if e_cabecalho and not cabecalho:
            cabecalho = cels
        else:
            linhas.append(cels)
    return {'t': 'tabela', 'cabecalho': cabecalho, 'linhas': linhas}


def paragrafos(s):
    # Verbatim solto, fora do quadro "codigo" (aparece no livro Node.js): vira bloco de código à parte
    if '\x02' in s:
        blocos = []
        for k, parte in enumerate(re.split(r'\x02(\d+)\x02', s)):
            blocos += [{'t': 'codigo', 'texto': LITERAIS[int(parte)]}] if k % 2 else paragrafos(parte)
        return blocos
    blocos = []
    for p in re.split(r'\n\s*\n', s):
        if not re.sub(r'\\(noindent|bigskip|medskip|smallskip|newpage)\b|%[^\n]*', '', p).strip():
            continue
        h = inline(p)
        if not h:
            continue
        so_negrito = re.fullmatch(r'<strong>.*</strong>', h) and h.count('<strong>') == 1
        blocos.append({'t': 'p', 'estilo': 'destaque', 'html': h} if so_negrito else {'t': 'p', 'html': h})
    return blocos


PADRAO = re.compile(r'\\topico\s*\{|\\subtopico\s*\{|\\modulotitulo\s*\{|\\subsection\*?\s*\{|\\subsubsection\*?\s*\{|'
                    r'\\begin\{(destaque|longtable|tabular|itemize|enumerate|center|codigo)\}')

# conteúdo literal dos blocos Verbatim, guardado antes de tirar comentários (% no código é texto)
LITERAIS = {}
IMAGENS = []


def blocos_de(s):
    blocos, i = [], 0
    while True:
        m = PADRAO.search(s, i)
        if not m:
            blocos += paragrafos(s[i:])
            return blocos
        blocos += paragrafos(s[i:m.start()])
        tok = m.group(0)
        if tok.startswith('\\topico'):
            num, j = ler_grupo(s, m.end() - 1)
            tit, i = ler_grupo(s, pular_espacos(s, j))
            texto = (num.strip() + ' ' if num.strip() else '') + re.sub(r'<[^>]+>', '', inline(tit))
            blocos.append({'t': 'h2', 'id': '', 'texto': texto})
        elif tok.startswith('\\subtopico'):
            tit, i = ler_grupo(s, m.end() - 1)
            blocos.append({'t': 'h3', 'texto': re.sub(r'<[^>]+>', '', inline(tit))})
        elif tok.startswith('\\modulotitulo'):
            _, j = ler_grupo(s, m.end() - 1)
            _, i = ler_grupo(s, pular_espacos(s, j))  # número e título já lidos em converter()
        elif tok.startswith('\\subsection'):
            tit, i = ler_grupo(s, m.end() - 1)
            blocos.append({'t': 'h2', 'id': '', 'texto': re.sub(r'<[^>]+>', '', inline(tit))})
        elif tok.startswith('\\subsubsection'):
            tit, i = ler_grupo(s, m.end() - 1)
            blocos.append({'t': 'h3', 'texto': re.sub(r'<[^>]+>', '', inline(tit))})
        else:
            amb = m.group(1)
            ini = m.end()
            fim = achar_fim_ambiente(s, amb, ini)
            corpo = s[ini:fim]
            i = fim + len('\\end{' + amb + '}')
            if amb == 'destaque':
                tit, k = ler_grupo(corpo, pular_espacos(corpo, 0))
                tit_txt = re.sub(r'<[^>]+>', '', inline(tit))
                blocos.append({'t': 'quadro', 'tipo': tipo_quadro(tit_txt), 'titulo': tit_txt,
                               'blocos': blocos_de(corpo[k:])})
            elif amb in ('longtable', 'tabular'):
                blocos.append(tabela(corpo))
            elif amb == 'codigo':
                for chave in re.findall(r'\x02(\d+)\x02', corpo):
                    blocos.append({'t': 'codigo', 'texto': LITERAIS[int(chave)]})
            elif amb in ('itemize', 'enumerate'):
                corpo = re.sub(r'^\s*\[[^]]*\]', '', corpo)  # opções do enumitem
                blocos.append(lista(corpo, amb == 'enumerate'))
            else:  # center
                fig = re.search(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}', corpo)
                if fig:
                    arquivo = fig.group(1)
                    IMAGENS.append(arquivo)
                    nome = re.sub(r'[-_]+', ' ', os.path.splitext(os.path.basename(arquivo))[0])
                    blocos.append({'t': 'imagem', 'src': arquivo, 'alt': nome})
                    corpo = corpo.replace(fig.group(0), '')
                blocos += blocos_de(corpo)


def finalizar(blocos, numero, titulo):
    """Monta o capítulo do modelo "livro": ids das seções e sem Resumo/Estudo de Caso/Exercícios."""
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


def converter(caminho):
    s = open(caminho, encoding='utf-8').read()
    LITERAIS.clear()
    IMAGENS.clear()

    def guardar(m):
        LITERAIS[len(LITERAIS)] = m.group(1).strip('\n')
        return f'\x02{len(LITERAIS) - 1}\x02'
    s = re.sub(r'\\begin\{Verbatim\}(?:\[[^]]*\])?\n?(.*?)\\end\{Verbatim\}', guardar, s, flags=re.S)
    s = re.sub(r'(?<!\\)%[^\n]*', '', s)
    capa = s[s.index('\\begin{document}'):] if '\\begin{document}' in s else s
    # modelo "livro" (Guia Node.js): \section{Capítulo 1 -- Título} ou \section{Apêndice A -- Título}
    secao = re.search(r'\\section\*?\{(Cap[ií]tulo\s+(\d+)|Ap[eê]ndice\s+\w+)\s*(?:--|—|–)\s*([^}]*)\}', capa)
    if secao:
        capa = capa.replace(secao.group(0), '', 1)
        return finalizar(blocos_de(capa), int(secao.group(2)) if secao.group(2) else None, inline(secao.group(3)).strip())
    modulo = re.search(r'\\modulotitulo\s*\{([^}]*)\}\s*\{([^}]*)\}', capa)
    numero = re.search(r'CAP[IÍ]TULO\s+(\d+)', capa)
    titulo = re.search(r'\\(?:Huge|huge|LARGE)\\bfseries\s+(.*?)\}', capa, re.S)
    corpo = capa
    if '\\setcounter{page}{1}' in corpo:  # depois da capa e do sumário do capítulo
        corpo = corpo.split('\\setcounter{page}{1}', 1)[1]
    corpo = corpo.split('\\end{document}')[0]

    blocos = blocos_de(corpo)
    # texto de abertura antes da primeira seção vira "Introdução", como nas apostilas em Word
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
    if modulo:
        cap = {'numero': int(modulo.group(1)), 'titulo': inline(modulo.group(2)), 'blocos': remover_secoes(blocos)}
        return cap
    cap = {
        'numero': int(numero.group(1)) if numero else None,
        # quebra de linha da capa: "Humano-\\Computador" junta sem espaço; nas demais vira espaço
        'titulo': re.sub(r'\s+', ' ', re.sub(r'-\s*<br>\s*', '-', inline(titulo.group(1))).replace('<br>', ' ')).strip() if titulo else '',
        'blocos': remover_secoes(blocos),
    }
    return cap


def renumerar(cap, novo):
    """Muda o número do capítulo e das seções (8.1 -> 12.1), para reaproveitar um capítulo em outra posição."""
    antigo = cap['numero']
    cap['numero'] = novo
    for b in cap['blocos']:
        if b['t'] == 'h2' and antigo is not None:
            b['texto'] = re.sub(rf'^{antigo}\.(\d+)', lambda m: f'{novo}.{m.group(1)}', b['texto'])
            b['id'] = slug(b['texto'])
    return cap


if __name__ == '__main__':
    # uso opcional: converter_latex.py entrada.tex saida.json <novo número do capítulo>
    # opções: --imagens <pasta destino> <url base>   e   --trocar "texto antigo=>texto novo" (pode repetir)
    args = sys.argv[1:]
    imagens = None
    if '--imagens' in args:
        k = args.index('--imagens')
        imagens = (args[k + 1], args[k + 2])
        del args[k:k + 3]
    trocas = []
    while '--trocar' in args:
        k = args.index('--trocar')
        trocas.append(tuple(args[k + 1].split('=>')))
        del args[k:k + 2]
    # --sem-secao "Início do título" (pode repetir): tira seções inteiras que não vão para o site
    sem_secao = []
    while '--sem-secao' in args:
        k = args.index('--sem-secao')
        sem_secao.append(slug(args[k + 1]))
        del args[k:k + 2]
    entrada, saida = args[0], args[1]
    cap = converter(entrada)
    if len(args) > 2:
        cap = renumerar(cap, int(args[2]))
    if sem_secao:
        saida_blocos, pulando = [], False
        for b in cap['blocos']:
            if b['t'] == 'h2':
                pulando = any(slug(b['texto']).startswith(p) for p in sem_secao)
            if not pulando:
                saida_blocos.append(b)
        cap['blocos'] = saida_blocos
        IMAGENS[:] = [b['src'] for b in saida_blocos if b['t'] == 'imagem']
    if IMAGENS:
        if not imagens:
            sys.exit('ERRO: o capítulo tem imagens; informe --imagens <pasta destino> <url base>')
        os.makedirs(imagens[0], exist_ok=True)
        base = os.path.dirname(os.path.abspath(entrada))
        def ajustar(bs):
            for b in bs:
                if b['t'] == 'imagem':
                    origem = os.path.join(base, b['src'])
                    if not os.path.exists(origem):
                        origem = os.path.join(base, '..', b['src'])
                    destino = os.path.basename(b['src'])
                    if destino.lower().endswith('.pdf'):
                        # diagramas em PDF (TikZ/Inkscape) viram PNG para o navegador
                        destino = destino[:-4] + '.png'
                        subprocess.run(['pdftoppm', '-png', '-r', '150', '-singlefile', origem,
                                        os.path.join(imagens[0], destino[:-4])], check=True)
                    else:
                        shutil.copy(origem, os.path.join(imagens[0], destino))
                    b['src'] = imagens[1].rstrip('/') + '/' + destino
                elif b['t'] == 'quadro':
                    ajustar(b['blocos'])
        ajustar(cap['blocos'])
    texto = json.dumps(cap, ensure_ascii=False, indent=1)
    for antigo, novo in trocas:
        if antigo not in texto:
            sys.exit(f'ERRO: texto para trocar não encontrado: {antigo!r}')
        texto = texto.replace(antigo, novo)
    cap = json.loads(texto)
    verificar_termos(texto)
    # imagens não passam pela verificação de texto: confira cada uma a olho antes de publicar
    with open(saida, 'w', encoding='utf-8', newline='\n') as f:
        f.write(texto)
    contagem = {}
    for b in cap['blocos']:
        contagem[b['t']] = contagem.get(b['t'], 0) + 1
    print(f"Capítulo {cap['numero']}: {cap['titulo']} -> {contagem}")
