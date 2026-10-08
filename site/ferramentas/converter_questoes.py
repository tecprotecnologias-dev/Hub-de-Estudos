"""Converte um Word de questões de prova (modelo "FORMATO DA PROVA") para o banco do site.

Formato esperado do Word, por questão:
    Questão N — Questão Discursiva | Questão de Múltipla Escolha   (título)
    Capítulo X — ... — Texto N                                      (ignorado)
    "citação"                                                       (texto motivador)
    (Tradução livre: "...")                                         (opcional)
    AUTOR. Título. ...                                              (fonte)
    parágrafos do caso                                              (caso aplicado)
    enunciado em negrito                                            (opcional na discursiva)
    objetiva:   A) ... E)  /  Gabarito: X [explicação]  /  [Explicação: ...]
    discursiva: a) ... d)  /  [Padrão de resposta esperado  a) ... d)]

O cabeçalho do arquivo (instituição, disciplina, "nota para a professora") é descartado.

Formato "livre" (detectado sozinho quando os títulos não têm número: "Questão Discursiva",
"Questão de Múltipla Escolha"):
    <Disciplina> — Texto N | — mesmo texto ... (continuação)        (rótulo; "continuação" herda
                                                                    o contexto da questão anterior)
    [imagem] + "Figura N — legenda"                                 (figura)
    “citação” + referência (AUTOR, Nome. ...)                       (texto motivador; pode haver vários)
    parágrafos do caso; o último antes das alternativas é o enunciado
    (Gabarito: X — explicação)
Nesse formato a questão sai com "contexto" (lista de partes) em vez de "texto"/"caso".

Uso:
    python ferramentas/converter_questoes.py <Capitulo1.docx> <disciplinaId> <capituloId> <saida.json> [<pasta imagens> <url imagens>]
<capituloId> pode dividir o Word entre capítulos da apostila: "qualidade-cap2:2-5,qualidade-cap1"
(questões 2 a 5 no capítulo 2, as demais no capítulo 1; várias faixas com "+", ex.: 1-3+7-9).
A saída é uma lista JSON; vários capítulos podem ir para o mesmo arquivo (o capítulo é substituído).
"""
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).parent))
from converter_capitulo import verificar_termos  # noqa: E402

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
IMG = '\x00IMG:'


def paragrafos(caminho):
    """(texto, todo_negrito) de cada parágrafo não vazio; imagens saem como (IMG + caminho no zip, False)."""
    with zipfile.ZipFile(caminho) as z:
        raiz = ET.fromstring(z.read('word/document.xml'))
        rels = ET.fromstring(z.read('word/_rels/document.xml.rels'))
    alvos = {r.get('Id'): r.get('Target') for r in rels}
    for p in raiz.iter(W + 'p'):
        for blip in p.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}blip'):
            yield IMG + 'word/' + alvos[blip.get(R + 'embed')], False
        partes = []
        negrito = True
        for r in p.iter(W + 'r'):
            texto = ''
            for el in r:
                if el.tag == W + 't':
                    texto += el.text or ''
                elif el.tag in (W + 'br', W + 'cr'):
                    texto += '\n'
                elif el.tag == W + 'tab':
                    texto += ' '
            if not texto:
                continue
            if texto.strip():
                b = r.find(W + 'rPr/' + W + 'b')
                if b is None or b.get(W + 'val') in ('0', 'false'):
                    negrito = False
            partes.append(texto)
        texto = re.sub(r'[ \t]+', ' ', ''.join(partes)).strip()
        if texto:
            yield texto, negrito


RE_QUESTAO = re.compile(r'^Questão\s+(\d+)\s+[—–-]\s+(.*)$')
RE_ALT = re.compile(r'^([A-E])\)\s*(.*)$', re.S)
RE_ITEM = re.compile(r'^([a-e])\)\s*(.*)$', re.S)
RE_GABARITO = re.compile(r'^Gabarito:\s*([A-E])\b\s*(.*)$', re.S)


def limpar(t):
    return re.sub(r'\s*\n\s*', ' ', t).strip()


def montar(numero, titulo, corpo, disciplina_id, capitulo_id):
    discursiva = 'Discursiva' in titulo
    i = 0
    if i < len(corpo) and re.search(r'—\s*Texto\s+\d+\s*$', corpo[i][0]):
        i += 1
    citacao = limpar(corpo[i][0]); i += 1
    traducao = None
    if corpo[i][0].startswith('(Tradução'):
        traducao = limpar(corpo[i][0]); i += 1
    fonte = limpar(corpo[i][0]); i += 1

    caso, enunciado = [], None
    while i < len(corpo):
        t, negrito = corpo[i]
        if RE_ALT.match(t) if not discursiva else RE_ITEM.match(t):
            break
        if negrito:
            enunciado = limpar(t)
        else:
            caso.append(limpar(t))
        i += 1

    q = {
        'id': f'{capitulo_id}-q{numero}',
        'disciplinaId': disciplina_id,
        'capituloId': capitulo_id,
        'tipo': 'discursiva' if discursiva else 'objetiva',
        'texto': {'citacao': citacao, **({'traducao': traducao} if traducao else {}), 'fonte': fonte},
        'caso': caso,
    }

    if discursiva:
        itens, respostas, no_padrao = [], [], False
        for t, _ in corpo[i:]:
            if t.lower().startswith('padrão de resposta'):
                no_padrao = True
                continue
            m = RE_ITEM.match(t)
            if m:
                (respostas if no_padrao else itens).append(f'{m.group(1)}) {limpar(m.group(2))}')
            elif no_padrao and respostas:
                respostas[-1] += ' ' + limpar(t)
            elif itens:
                itens[-1] += ' ' + limpar(t)
        q['enunciado'] = enunciado or 'Com base no texto e no caso apresentado, responda:'
        q['itens'] = itens
        if respostas:
            q['respostaEsperada'] = '\n'.join(respostas)
        q['linhas'] = 12
        assert len(itens) >= 2, f'questão {numero}: itens não encontrados'
    else:
        alternativas, correta, resolucao = [], None, []
        for t, _ in corpo[i:]:
            m = RE_GABARITO.match(t)
            if m:
                correta = 'ABCDE'.index(m.group(1))
                if m.group(2).strip():
                    resolucao.append(limpar(m.group(2)))
                continue
            m = RE_ALT.match(t)
            if m and correta is None:
                alternativas.append(limpar(m.group(2)))
                continue
            if correta is not None:
                resolucao.append(limpar(re.sub(r'^Explicação:\s*', '', t)))
        assert enunciado, f'questão {numero}: enunciado não encontrado'
        assert len(alternativas) == 5 and correta is not None, f'questão {numero}: alternativas/gabarito'
        q['enunciado'] = enunciado
        q['alternativas'] = alternativas
        q['correta'] = correta
        if resolucao:
            q['resolucao'] = ' '.join(resolucao)
    return q


RE_QUESTAO_LIVRE = re.compile(r'^Questão (Discursiva|de Múltipla Escolha)\s*$')
# "Texto N — título": no modelo de Qualidade o texto de apoio vem ANTES do título "Questão N"
RE_TEXTO = re.compile(r'^Texto\s+\d+\s*[—–-]')
RE_FIGURA = re.compile(r'^Figura\s+\d+\s*[—–-]\s*(.*)$', re.S)
# referência bibliográfica: SOBRENOME, Nome. / ENTIDADE EM MAIÚSCULAS. Título / RFC 1234 — / ISO/IEC
RE_REFERENCIA = re.compile(r"^(?:[A-ZÀ-Ý][A-ZÀ-Ý0-9'.\-]+(?:\s[A-ZÀ-Ý0-9'.\-]+)*[,.]\s|RFC\s\d+\s[—–-]|ISO[/ ])")
RE_GABARITO_LIVRE = re.compile(r'^\(?Gabarito:\s*([A-E])\b\s*[—–:-]?\s*(.*?)\)?\s*$', re.S)


def montar_livre(numero, titulo, corpo, disciplina_id, capitulo_id, anterior, imagens):
    discursiva = titulo == 'Discursiva'
    contexto, herda, i, img = [], False, 0, None
    marca = re.compile(r'^[a-e]\)' if discursiva else r'^[A-E]\)')
    while i < len(corpo):
        t, _ = corpo[i]
        if marca.match(t):
            break
        i += 1
        if t.startswith(IMG):
            img = t[len(IMG):]
            continue
        m = RE_FIGURA.match(t)
        if m and img:
            contexto.append({'t': 'imagem', 'src': imagens(img), 'legenda': limpar(t)})
            img = None
            continue
        if not contexto and t[:1] not in '“"' and len(t) < 120 and (
                re.match(r'^[^“"]{0,60}\s[—–-]\s(Texto\s+\d+|.*continuação.*)$', t)
                or RE_TEXTO.match(t) or '(valor:' in t
                or (len(t) < 60 and not t.endswith(('.', ':', '?')))):
            herda = 'continuação' in t or 'mesmo texto' in t
            continue
        if t[:1] in '“"':
            contexto.append({'t': 'citacao', 'texto': limpar(t)})
            continue
        if t.startswith('(Tradução') and contexto and contexto[-1]['t'] == 'citacao':
            contexto[-1]['traducao'] = limpar(t)
            continue
        logo_apos_citacao = contexto and contexto[-1]['t'] == 'citacao' and 'fonte' not in contexto[-1]
        # referência fora do padrão SOBRENOME (ex.: "RTI International. ...", "Elaborado com base em: ...")
        parece_referencia = logo_apos_citacao and len(t) < 260 and re.search(r'\b(19|20)\d\d\b', t)
        if RE_REFERENCIA.match(t) or parece_referencia:
            if logo_apos_citacao:
                contexto[-1]['fonte'] = limpar(t)
            else:
                contexto.append({'t': 'fonte', 'texto': limpar(t)})
            continue
        contexto.append({'t': 'p', 'texto': limpar(t)})
    assert img is None, f'questão {numero}: imagem sem legenda "Figura N —"'
    if herda:
        assert anterior, f'questão {numero}: continuação sem questão anterior'
        contexto = anterior + contexto

    q = {
        'id': f'{capitulo_id}-q{numero}',
        'disciplinaId': disciplina_id,
        'capituloId': capitulo_id,
        'tipo': 'discursiva' if discursiva else 'objetiva',
    }
    if discursiva:
        itens, respostas, no_padrao = [], [], False
        for t, _ in corpo[i:]:
            if t.lower().startswith('padrão de resposta'):
                no_padrao = True
                continue
            m = RE_ITEM.match(t)
            if m:
                (respostas if no_padrao else itens).append(f'{m.group(1)}) {limpar(m.group(2))}')
            elif no_padrao and respostas:
                respostas[-1] += ' ' + limpar(t)
            elif itens:
                itens[-1] += ' ' + limpar(t)
        assert len(itens) >= 2, f'questão {numero}: itens não encontrados'
        q.update(contexto=contexto, enunciado='Com base no texto e no caso apresentado, responda:', itens=itens)
        if respostas:
            q['respostaEsperada'] = '\n'.join(respostas)
        q['linhas'] = 12
    else:
        assert contexto and contexto[-1]['t'] == 'p', f'questão {numero}: enunciado não encontrado'
        enunciado = contexto.pop()['texto']
        alternativas, correta, resolucao = [], None, []
        for t, _ in corpo[i:]:
            if re.match(r'^Fim da prova', t):
                continue
            m = RE_GABARITO_LIVRE.match(t)
            if m:
                correta = 'ABCDE'.index(m.group(1))
                if m.group(2).strip():
                    resolucao.append(limpar(m.group(2)))
                continue
            m = RE_ALT.match(t)
            if m and correta is None:
                alternativas.append(limpar(m.group(2)))
            elif correta is not None:
                resolucao.append(limpar(t))
        assert len(alternativas) == 5 and correta is not None, f'questão {numero}: alternativas/gabarito'
        q.update(contexto=contexto, enunciado=enunciado, alternativas=alternativas, correta=correta)
        if resolucao:
            q['resolucao'] = ' '.join(resolucao)
    return q, contexto


def capitulo_da_questao(spec, numero):
    padrao = None
    for parte in spec.split(','):
        cap, _, faixas = parte.partition(':')
        if not faixas:
            padrao = cap
            continue
        for faixa in faixas.split('+'):
            a, _, b = faixa.partition('-')
            if int(a) <= numero <= int(b or a):
                return cap
    return padrao


def converter(caminho, disciplina_id, capitulo_id, imagens=None):
    questoes, atual, livre, pendente = [], None, False, None
    for t, negrito in paragrafos(caminho):
        m = RE_QUESTAO.match(t)
        ml = RE_QUESTAO_LIVRE.match(t)
        if m and m.group(2).strip() in ('Discursiva', 'Múltipla Escolha'):
            ml, m = re.match(r'(.*)', m.group(2).strip()), None
        if m:
            atual = (int(m.group(1)), m.group(2), [])
            questoes.append(atual)
        elif ml:
            livre = True
            atual = (len(questoes) + 1, ml.group(1).replace('de ', '').strip(), pendente or [])
            questoes.append(atual)
            pendente = None
        elif pendente is not None:
            pendente.append((t, negrito))
        elif atual and atual[2] and RE_TEXTO.match(t) and 'continuação' not in t:
            pendente = [(t, negrito)]
        elif atual:
            atual[2].append((t, negrito))
    if not livre:
        return [montar(n, tit, corpo, disciplina_id, capitulo_da_questao(capitulo_id, n)) for n, tit, corpo in questoes]
    saida, anterior = [], None
    for n, tit, corpo in questoes:
        q, ctx = montar_livre(n, tit, corpo, disciplina_id, capitulo_da_questao(capitulo_id, n), anterior, imagens)
        anterior = ctx
        saida.append(q)
    return saida


def main():
    origem, disciplina_id, capitulo_id, saida = sys.argv[1:5]
    pasta_img, url_img = (sys.argv[5:7] + [None, None])[:2]
    contador = [0]

    def imagens(nome_zip):
        """copia a imagem do Word para a pasta pública e devolve o endereço usado no site"""
        assert pasta_img, 'o Word tem imagens: informe <pasta imagens> <url imagens>'
        contador[0] += 1
        nome = f'{capitulo_id.split(",")[-1].split(":")[0]}-figura{contador[0]}{Path(nome_zip).suffix}'
        Path(pasta_img).mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(origem) as z:
            (Path(pasta_img) / nome).write_bytes(z.read(nome_zip))
        return f'{url_img.rstrip("/")}/{nome}'

    novas = converter(origem, disciplina_id, capitulo_id, imagens)
    verificar_termos(json.dumps(novas, ensure_ascii=False))
    destino = Path(saida)
    existentes = json.loads(destino.read_text(encoding='utf-8')) if destino.exists() else []
    alvos = {q['capituloId'] for q in novas}
    existentes = [q for q in existentes if q['capituloId'] not in alvos] + novas
    destino.write_text(json.dumps(existentes, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    obj = sum(q['tipo'] == 'objetiva' for q in novas)
    print(f'{capitulo_id}: {len(novas)} questões ({obj} objetivas, {len(novas) - obj} discursivas) -> {saida}')
    if len(alvos) > 1:
        for c in sorted(alvos):
            print(f'  {c}: {sum(q["capituloId"] == c for q in novas)}')
    # reaplica as alternativas reescritas (correta não pode ser sempre a mais longa)
    from aplicar_ajustes_alternativas import main as aplicar_ajustes
    aplicar_ajustes()


if __name__ == '__main__':
    main()
