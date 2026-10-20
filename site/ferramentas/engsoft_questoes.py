"""
Funções comuns aos scripts de questões de Engenharia de Software e da Usabilidade
(engsoft_capN_objetivas.py): objetivas no estilo de concursos públicos e exames nacionais
(situação-problema, afirmativas, asserção-razão, "assinale a incorreta" e leitura de código,
sempre com 5 alternativas) e discursivas com um único comando.

A primeira alternativa de cada objetiva é a certa; o site embaralha a ordem, por isso a
resolução nunca cita letras. Cada script grava só as suas questões (ids <capítulo>-o* e
<capítulo>-d*) no JSON da disciplina; as demais ficam como estão.

Também serve a outras disciplinas, ex.: Banco('qualidade-cap2', QUALIDADE) grava em qualidade.json.
"""

import json
import sys
from itertools import combinations
from pathlib import Path

PASTA_QUESTOES = Path(__file__).resolve().parent.parent / 'src' / 'data' / 'questoes'
# (id da disciplina, arquivo de questões)
ENGSOFT = ('engenharia-de-software-e-da-usabilidade', PASTA_QUESTOES / 'engsoft.json')
QUALIDADE = ('qualidade-e-testes-de-software', PASTA_QUESTOES / 'qualidade.json')
LEGISLACAO = ('legislacao-em-negocios-digitais', PASTA_QUESTOES / 'legislacao.json')
PROIBIDAS = ['faeterj', 'faetec', 'enade', 'barra mansa']
ROMANOS = ['I', 'II', 'III', 'IV']

ASSERCAO = [
    'As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.',
    'As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.',
    'A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.',
    'A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.',
    'As asserções I e II são proposições falsas.',
]


def p(texto):
    return {'t': 'p', 'texto': texto}


def codigo(texto):
    return {'t': 'codigo', 'texto': texto.strip('\n')}


def _rotulo(chave, total):
    if len(chave) == total:
        return ', '.join(chave[:-1]) + ' e ' + chave[-1] + '.'
    if len(chave) == 1:
        return f'{chave[0]}, apenas.'
    return ', '.join(chave[:-1]) + ' e ' + chave[-1] + ', apenas.'


class Banco:
    """Questões de um capítulo, ex.: Banco('engsoft-cap6') ou Banco('qualidade-cap2', QUALIDADE)."""

    def __init__(self, capitulo, disciplina=ENGSOFT):
        self.capitulo = capitulo
        self.disciplina, self.arquivo = disciplina
        self.objetivas = []
        self.discursivas = []

    def _base(self, nivel, enunciado, contexto=None, caso=None):
        q = {
            'id': f'{self.capitulo}-o{len(self.objetivas) + 1}',
            'disciplinaId': self.disciplina,
            'capituloId': self.capitulo,
            'tipo': 'objetiva',
            'nivel': nivel,
        }
        if contexto:
            q['contexto'] = contexto
        if caso:
            q['caso'] = caso
        q['enunciado'] = enunciado
        return q

    def multipla(self, nivel, enunciado, certa, erradas, resolucao, contexto=None):
        q = self._base(nivel, enunciado, contexto)
        q['alternativas'] = [certa, *erradas]
        q['correta'] = 0
        q['resolucao'] = resolucao
        self.objetivas.append(q)

    def afirmativas(self, nivel, itens, resolucao, contexto=None, intro='Avalie as afirmativas a seguir.'):
        """itens: lista de (texto, verdadeira), de 3 ou 4. A resposta é o conjunto das verdadeiras."""
        romanos = ROMANOS[:len(itens)]
        caso = [intro] + [f'{romanos[i]}. {t}' for i, (t, _) in enumerate(itens)]
        certa = tuple(romanos[i] for i, (_, v) in enumerate(itens) if v)
        todas = [c for n in range(1, len(romanos) + 1) for c in combinations(romanos, n)]
        outras = [c for c in todas if c != certa]
        # distratoras parecidas com a certa primeiro (diferem em um item), depois as demais
        outras.sort(key=lambda c: len(set(c) ^ set(certa)))
        q = self._base(nivel, 'É correto o que se afirma em', contexto, caso)
        q['alternativas'] = [_rotulo(c, len(romanos)) for c in [certa, *outras[:4]]]
        q['correta'] = 0
        q['resolucao'] = resolucao
        self.objetivas.append(q)

    def assercao(self, nivel, i, ii, resposta, resolucao, contexto=None):
        """resposta: índice em ASSERCAO (0 = I e II verdadeiras e II justifica I ...)."""
        caso = ['Avalie as asserções a seguir e a relação proposta entre elas.', f'I. {i}', 'PORQUE', f'II. {ii}']
        q = self._base(nivel, 'A respeito dessas asserções, assinale a opção correta.', contexto, caso)
        q['alternativas'] = [ASSERCAO[resposta]] + [a for k, a in enumerate(ASSERCAO) if k != resposta]
        q['correta'] = 0
        q['resolucao'] = resolucao
        self.objetivas.append(q)

    def discursiva(self, nivel, texto, caso, enunciado, resposta):
        """Discursiva com um único comando (sem itens a, b, c...) e a resposta esperada.
        texto=None quando não há citação real que sirva (nunca inventar uma)."""
        q = {
            'id': f'{self.capitulo}-d{len(self.discursivas) + 1}',
            'disciplinaId': self.disciplina,
            'capituloId': self.capitulo,
            'tipo': 'discursiva',
            'nivel': nivel,
        }
        if texto:
            q['texto'] = texto
        q.update({'caso': caso, 'enunciado': enunciado, 'linhas': 10, 'respostaEsperada': resposta})
        self.discursivas.append(q)

    def validar(self, objetivas=10, discursivas=2):
        erros = []
        for q in self.objetivas:
            if len(q['alternativas']) != 5:
                erros.append(f'{q["id"]}: {len(q["alternativas"])} alternativas')
            if len(set(q['alternativas'])) != len(q['alternativas']):
                erros.append(f'{q["id"]}: alternativas repetidas')
            # a certa não pode se destacar por ser bem mais comprida que as outras
            tamanhos = [len(a) for a in q['alternativas']]
            certa, maior_errada = tamanhos[q['correta']], max(tamanhos[:q['correta']] + tamanhos[q['correta'] + 1:])
            if certa > maior_errada * 1.15 and certa - maior_errada > 15:
                erros.append(f'{q["id"]}: a certa ({certa}) é bem mais longa que as erradas ({maior_errada})')
            if q['nivel'] not in ('medio', 'dificil'):
                erros.append(f'{q["id"]}: nível {q["nivel"]}')
            for parte in q.get('contexto', []):
                if parte['t'] == 'codigo':
                    for linha in parte['texto'].splitlines():
                        if len(linha) > 66:
                            erros.append(f'{q["id"]}: linha de código com mais de 66 colunas')
        for q in self.discursivas:
            if 'itens' in q:
                erros.append(f'{q["id"]}: discursiva com itens (deve ter um único comando)')
        for q in self.objetivas + self.discursivas:
            texto = json.dumps(q, ensure_ascii=False).lower()
            for palavra in PROIBIDAS:
                if palavra in texto:
                    erros.append(f'{q["id"]}: contém "{palavra}"')
        if len(self.objetivas) != objetivas:
            erros.append(f'{len(self.objetivas)} objetivas (esperado {objetivas})')
        if len(self.discursivas) != discursivas:
            erros.append(f'{len(self.discursivas)} discursivas (esperado {discursivas})')
        return erros

    def gravar(self):
        erros = self.validar()
        if erros:
            print('\n'.join(erros))
            sys.exit(1)
        existentes = json.loads(self.arquivo.read_text(encoding='utf-8'))
        manter = [q for q in existentes
                  if not q['id'].startswith((f'{self.capitulo}-o', f'{self.capitulo}-d'))]
        # as novas entram logo depois das demais questões do capítulo
        ultimo = max(i for i, q in enumerate(manter) if q['capituloId'] == self.capitulo)
        final = manter[:ultimo + 1] + self.discursivas + self.objetivas + manter[ultimo + 1:]
        self.arquivo.write_text(json.dumps(final, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        niveis = [q['nivel'] for q in self.objetivas]
        print(self.capitulo, {n: niveis.count(n) for n in ('medio', 'dificil')})
        print(f'{len(self.objetivas)} objetivas e {len(self.discursivas)} discursivas gravadas; '
              f'{len(final)} questões no total em {self.arquivo.name}')
