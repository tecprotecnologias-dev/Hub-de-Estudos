"""Aplica ao Módulo 04 de Web Design II (convertido do LaTeX de 24/08) as mudanças
que só existem na versão em PDF de 12/09 (APOSTILAS NOVAS/apostila-web2-modulo-04.pdf).

Uso:
    python ferramentas/ajustar_web2_modulo4.py src/data/capitulos/web2-cap4.json

Os textos abaixo foram copiados do PDF de 12/09. Se o LaTeX for atualizado com
essas mudanças, este script deixa de ser necessário.
"""
import json
import re
import sys


def c(t):
    return f'<code>{t}</code>'


def quadro(titulo, html):
    tipo = 'atencao'
    return {'t': 'quadro', 'tipo': tipo, 'titulo': titulo, 'blocos': [{'t': 'p', 'html': html}]}


caminho = sys.argv[1]
cap = json.load(open(caminho, encoding='utf-8'))
b = cap['blocos']


def achar(pred, desc):
    for i, x in enumerate(b):
        if pred(x):
            return i
    sys.exit(f'ERRO: não achei {desc} no Módulo 4 (o LaTeX mudou?)')


# 1) 4.3 — perguntas do create-next-app em duas versões
i = achar(lambda x: x['t'] == 'p' and x['html'].startswith('O assistente faz várias perguntas'), 'parágrafo das perguntas')
b[i:i + 1] = [
    {'t': 'p', 'html': 'Dependendo da versão da ferramenta, o assistente pergunta de dois jeitos diferentes. '
                       'Versões mais recentes fazem uma pergunta só:'},
    {'t': 'codigo', 'texto': 'Would you like to use the recommended Next.js defaults?   -> Yes'},
    {'t': 'p', 'html': 'Versões um pouco mais antigas ainda perguntam item por item – nesse caso, responda assim, '
                       'para manter consistência com o que já aprendemos:'},
]

# 2) 4.3 — Tailwind instalado pelos defaults (logo depois do quadro "Atenção" sobre o Vite)
i = achar(lambda x: x['t'] == 'quadro' and 'Vite' in json.dumps(x, ensure_ascii=False), 'quadro sobre o Vite')
b.insert(i + 1, quadro('Erro Comum',
    '"Escolhi os defaults recomendados e agora tenho Tailwind CSS instalado, mesmo o guia dizendo para não usar." – '
    f'Sem problema: o Tailwind convive tranquilamente com o CSS "normal" que usamos no curso (o {c("globals.css")}). '
    f'Só ignore as classes e os arquivos extras dele (como o {c("postcss.config.mjs")}) – eles não atrapalham em nada.'))

# 3) 4.4 — pasta src/ não criada (logo depois da árvore de pastas)
i = achar(lambda x: x['t'] == 'codigo' and x['texto'].startswith('meu-portfolio-next/'), 'árvore de pastas')
b.insert(i + 1, quadro('Erro Comum',
    f'"Minha pasta {c("src/")} não foi criada, mesmo respondendo Yes." – Isso pode acontecer dependendo da versão da '
    f'ferramenta. Não é um erro seu, e não precisa recriar o projeto: se sua pasta {c("app/")} está direto dentro de '
    f'{c("meu-portfolio-next/")} (sem passar por {c("src/")}), é só usar os caminhos deste capítulo sem o {c("src/")} '
    f'no meio – ex: {c("app/page.tsx")} em vez de {c("src/app/page.tsx")}. O restante funciona exatamente igual.'))

# 4) 4.5 — pastas de rota lado a lado (antes do quadro sobre o nome page.tsx)
i = achar(lambda x: x['t'] == 'p' and x['html'].startswith('Cada pasta vira um segmento da URL'), 'parágrafo de 4.5')
b.insert(i + 1, quadro('Atenção',
    f'As pastas de rota ({c("sobre/")}, {c("projetos/")}, {c("blog/")}) devem ficar todas lado a lado, soltas direto '
    f'dentro de {c("app/")} – nunca uma dentro da outra. Criar {c("app/blog/projetos/")} por engano (em vez de '
    f'{c("app/projetos/")}) faz a URL virar {c("/blog/projetos")} em vez de {c("/projetos")}. Depois de criar as '
    'pastas, confira visualmente no Explorador de Arquivos que todas estão no mesmo nível de recuo.'))

# 5) O Projeto Portfólio não vai para o site (pedido da professora): tira as frases que dependem dele
i = achar(lambda x: x['t'] == 'p' and x['html'].startswith('Até agora, seu portfólio é um projeto React'),
          'parágrafo "seu portfólio"')
b[i]['html'] = b[i]['html'].replace('Até agora, seu portfólio é um projeto React', 'Até agora, trabalhamos com um projeto React', 1)
i = achar(lambda x: x['t'] == 'quadro' and 'Guia de Criação' in json.dumps(x, ensure_ascii=False), 'quadro com Etapa 4')
for p in b[i]['blocos']:
    if p['t'] == 'p':
        p['html'] = re.sub(r'\s*Vamos migrar seus componentes.*?passo a passo completo\.', '', p['html'])

json.dump(cap, open(caminho, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('Módulo 4 ajustado para a versão de 12/09 (4 mudanças) e sem referências ao Projeto Portfólio.')
