"""Converte um Word de quiz (pasta 04- PROVAS, ex.: "QUIZ CAP. 5,6.docx") para o banco do site.

Formato esperado do Word:
    CONTEÚDO DO CAPÍTULO N                         (abre a seção de um capítulo; vale a do capítulo pedido)
    6.1  ... 6.5 ...                               (sumário, ignorado)
    1. enunciado                                   (começa com número e ponto)
    A) ... B) ... C) ... D) ...                    (no mesmo parágrafo, sem espaço entre elas)
    ✅ Resposta correta: X

Uso:
    python ferramentas/converter_quiz.py <quiz.docx> <número do capítulo no Word> <disciplinaId> <capituloId> <saida.json>
As questões entram com nivel "facil" e ids "<capituloId>-f<N>"; rodar de novo substitui apenas essas.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from converter_capitulo import verificar_termos  # noqa: E402
from converter_questoes_simples import limpar, paragrafos  # noqa: E402


def converter(caminho, capitulo_word):
    questoes, na_secao, atual = [], False, None
    for chars in paragrafos(caminho):
        texto = ''.join(c for c, _ in chars)
        secao = re.match(r'\s*CONTEÚDO DO CAPÍTULO\s+(\d+)', texto)
        if secao:
            na_secao = int(secao.group(1)) == capitulo_word
            continue
        if not na_secao:
            continue
        num = re.match(r'\s*\d+\.\s', texto)
        if num:
            atual = {'enunciado': limpar(texto[num.end():]), 'alts': [], 'correta': None}
            questoes.append(atual)
        elif atual and re.match(r'\s*A\)', texto):
            partes = re.split(r'(?:^|(?<=\S))\s*([A-E])\)\s*', texto.strip())
            atual['alts'] = [limpar(partes[i + 1]) for i in range(1, len(partes) - 1, 2)]
        elif atual and 'Resposta correta' in texto:
            atual['correta'] = 'ABCDE'.index(re.search(r'Resposta correta:\s*([A-E])', texto).group(1))
    for n, q in enumerate(questoes, 1):
        if len(q['alts']) < 4 or q['correta'] is None:
            raise SystemExit(f'questão {n}: {len(q["alts"])} alternativas, gabarito {q["correta"]}')
    return questoes


if __name__ == '__main__':
    docx, cap_word, disciplina, capitulo, arq = sys.argv[1:6]
    arq = Path(arq)
    banco = json.loads(arq.read_text(encoding='utf-8')) if arq.exists() else []
    prefixo = f'{capitulo}-f'
    banco = [q for q in banco if not q['id'].startswith(prefixo)]
    novas = [{
        'id': f'{prefixo}{n}',
        'disciplinaId': disciplina,
        'capituloId': capitulo,
        'tipo': 'objetiva',
        'nivel': 'facil',
        'enunciado': q['enunciado'],
        'alternativas': q['alts'],
        'correta': q['correta'],
    } for n, q in enumerate(converter(docx, int(cap_word)), 1)]
    verificar_termos(json.dumps(novas, ensure_ascii=False))
    # entram depois das demais questões do capítulo anterior, mantendo a ordem dos capítulos
    num_cap = int(re.search(r'(\d+)$', capitulo).group(1)) if re.search(r'(\d+)$', capitulo) else 0
    pos = max((i + 1 for i, q in enumerate(banco)
               if re.search(r'cap(\d+)$', q['capituloId']) and int(re.search(r'cap(\d+)$', q['capituloId']).group(1)) <= num_cap),
              default=len(banco))
    banco[pos:pos] = novas
    arq.write_text(json.dumps(banco, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{capitulo}: {len(novas)} questões (facil), gabarito', ''.join('ABCDE'[q['correta']] for q in novas))
    # reaplica as alternativas reescritas (correta não pode ser sempre a mais longa)
    from aplicar_ajustes_alternativas import main as aplicar_ajustes
    aplicar_ajustes()
