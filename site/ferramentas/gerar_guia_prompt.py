"""Monta src/data/capitulos/web2-prompt.json (Técnicas de Engenharia de Prompt).

Uso: python ferramentas/gerar_guia_prompt.py <pasta do site> [imagem1.png do Word "técnicas da engenharia de prompt"]
O texto fica aqui no script (os frameworks do Word eram capturas de tela de vídeo e foram reescritos).
Os diagramas de cada framework saem de ferramentas/gerar_diagramas_prompt.py; sem a imagem do Word, o
infográfico já publicado é mantido.
"""
import json
import re
import shutil
import sys
from pathlib import Path

site = Path(sys.argv[1])
imagem_origem = Path(sys.argv[2]) if len(sys.argv) > 2 else None


def ancora(t):
    import unicodedata
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')


def h2(t):
    return {'t': 'h2', 'id': ancora(t), 'texto': t}


def p(html, estilo=None):
    b = {'t': 'p', 'html': html}
    if estilo:
        b['estilo'] = estilo
    return b


def lista(itens, numerada=False):
    # nas listas numeradas do site o número faz parte do texto do item
    if numerada:
        itens = [f'{i}. {t}' for i, t in enumerate(itens, 1)]
    return {'t': 'lista', 'numerada': numerada, 'itens': itens}


def rotular(trecho, rotulo):
    # o rótulo entra antes da pontuação final do trecho: "remoto (META), crie"
    if not rotulo:
        return trecho
    corpo, pont = re.match(r'^(.*?)([,.:;]?)$', trecho, re.S).groups()
    return f'{corpo} <strong>({rotulo})</strong>{pont}'


def quadro(tipo, titulo, blocos):
    return {'t': 'quadro', 'tipo': tipo, 'titulo': titulo, 'blocos': blocos}


def framework(sigla, ingles, partes, prompt, quando):
    """partes: [(nome em português, sigla em inglês, explicação)]; prompt: [(trecho, rótulo)]"""
    montado = ' '.join(rotular(t, r) for t, r in prompt)
    return [
        {'t': 'h3', 'texto': f'{sigla} — {ingles}'},
        {'t': 'imagem', 'src': f'apostilas/web2/prompt-{sigla.lower()}.png',
         'alt': f'Diagrama {sigla}: ' + ' + '.join(n for n, _, _ in partes)},
        p(' + '.join(f'<strong>{n}</strong>' for n, _, _ in partes)),
        lista([f'<strong>{n}</strong> ({en}): {expl}' for n, en, expl in partes]),
        p(f'<strong>Quando usar:</strong> {quando}'),
        quadro('exemplo', f'Exemplo de prompt {sigla}', [p(montado)]),
    ]


blocos = [
    p('Engenharia de prompt é a habilidade de escrever pedidos claros para ferramentas de inteligência artificial, '
      'como ChatGPT, Gemini e Claude. Quanto mais bem estruturado o pedido, mais útil e precisa é a resposta. '
      'Neste guia você vai conhecer os passos de um bom prompt e alguns frameworks (modelos prontos) para montar '
      'os seus.'),

    h2('Os 5 passos de um bom prompt'),
    lista([
        '<strong>Definir o objetivo claramente:</strong> identifique o que você precisa saber ou o problema que '
        'precisa resolver. Isso ajuda a formular uma tarefa específica para o modelo.',
        '<strong>Especificar o contexto:</strong> forneça informações de fundo para enquadrar a pergunta. Isso pode '
        'incluir detalhes sobre o cenário, condições específicas ou premissas relevantes.',
        '<strong>Identificar o papel ou perspectiva desejada:</strong> decida se a resposta deve ser dada de um ponto '
        'de vista específico ou por um especialista em determinada área (use a técnica "atue como").',
        '<strong>Formular a tarefa de maneira precisa:</strong> seja específico sobre o que o modelo deve fazer: '
        'explicar, listar, comparar, analisar etc.',
        '<strong>Incluir instruções de formato, se necessário:</strong> especifique como você quer que a informação '
        'seja apresentada (lista, parágrafos, tabela etc.).',
    ], numerada=True),
    {'t': 'imagem', 'src': 'apostilas/web2/engenharia-de-prompt-rtf.png',
     'alt': 'Infográfico RTF: objetivo, contexto, papel, tarefa e formato', 'grande': True},

    h2('Exemplo: montando um prompt passo a passo'),
    {'t': 'tabela', 'cabecalho': ['Passo', 'O que você define', 'Exemplo'], 'linhas': [
        ['1', 'Objetivo', '"Quero entender HTML básico"'],
        ['2', 'Contexto', '"Sou aluno iniciante de Web Design"'],
        ['3', 'Papel', '"Atue como professor de Web Design"'],
        ['4', 'Tarefa', '"Explique as principais tags HTML"'],
        ['5', 'Formato', '"Explique com exemplos simples e código"'],
    ]},
    quadro('resposta', 'Prompt final', [
        p('Atue como um professor de Web Design. Explique as principais tags HTML para um aluno iniciante, usando '
          'exemplos simples e código.'),
    ]),

    h2('Frameworks de prompt'),
    p('Os frameworks são "receitas" que lembram você de incluir as partes certas no pedido. Cada sigla vem das '
      'iniciais em inglês. Não existe um melhor que o outro: escolha o que combina com a sua situação.'),
]

blocos += framework('RTF', 'Role + Task + Format', [
    ('Papel', 'Role', 'define quem ou o que está realizando a ação no prompt: uma pessoa, um profissional, uma entidade ou uma função.'),
    ('Tarefa', 'Task', 'especifica o que precisa ser feito, de forma clara e direta.'),
    ('Formato', 'Format', 'como a resposta deve ser estruturada: lista, parágrafo, tabela, artigo, código etc.'),
], [('Atue como um desenvolvedor front-end sênior', 'PAPEL'),
    ('e revise este componente React apontando problemas de acessibilidade', 'TAREFA'),
    ('em formato de lista numerada.', 'FORMATO')],
    'pedidos rápidos do dia a dia, quando basta dizer quem responde, o quê e como.')

blocos += framework('CTF', 'Context + Task + Format', [
    ('Contexto', 'Context', 'a situação que envolve o pedido.'),
    ('Tarefa', 'Task', 'o que precisa ser feito.'),
    ('Formato', 'Format', 'como a resposta deve ser entregue.'),
], [('Meu site em Next.js ficou lento no celular e a nota de desempenho do Lighthouse caiu para 45,', 'CONTEXTO'),
    ('liste as causas mais prováveis e como investigar cada uma', 'TAREFA'),
    ('em uma tabela com as colunas causa, como verificar e como corrigir.', 'FORMATO')],
    'quando a situação é o que mais importa para a resposta fazer sentido.')

blocos += framework('GRADE', 'Goal + Request + Action + Detail + Examples', [
    ('Meta', 'Goal', 'o objetivo maior por trás do pedido.'),
    ('Pedido', 'Request', 'o que você quer receber.'),
    ('Ação', 'Action', 'o que a IA deve fazer para atender o pedido.'),
    ('Detalhe', 'Detail', 'o nível de detalhe ou os requisitos de cada parte.'),
    ('Exemplos', 'Examples', 'exemplos que mostram o que você espera.'),
], [('Visando melhorar a acessibilidade do site da minha turma,', 'META'),
    ('crie um checklist para revisar páginas web.', 'PEDIDO'),
    ('Desenvolva uma lista com 10 verificações.', 'AÇÃO'),
    ('Cada verificação deve ter uma breve explicação e como testar.', 'DETALHE'),
    ('Inclua itens como texto alternativo em imagens, contraste de cores e navegação pelo teclado.', 'EXEMPLOS')],
    'quando você quer um material completo e já sabe que tipo de conteúdo espera.')

blocos += framework('PECRA', 'Purpose + Expectation + Context + Request + Action', [
    ('Propósito', 'Purpose', 'para que serve o resultado.'),
    ('Expectativa', 'Expectation', 'como você espera que seja a resposta.'),
    ('Contexto', 'Context', 'a situação ou o motivo do pedido.'),
    ('Pedido', 'Request', 'o que deve ser produzido.'),
    ('Ação', 'Action', 'o que cada parte da resposta deve conter.'),
], [('Para aprender a consumir APIs em React,', 'PROPÓSITO'),
    ('espero exercícios práticos e progressivos.', 'EXPECTATIVA'),
    ('Já sei usar useState, mas ainda não usei useEffect,', 'CONTEXTO'),
    ('elabore uma lista de 5 exercícios', 'PEDIDO'),
    ('em que cada exercício tenha o enunciado, a API pública usada e o que eu devo conseguir fazer no final.', 'AÇÃO')],
    'quando você precisa deixar claro o motivo e a expectativa, como em planos de estudo e materiais de apoio.')

blocos += framework('ROSES', 'Role + Objective + Scenario + Expected Solution + Steps', [
    ('Papel', 'Role', 'quem responde.'),
    ('Objetivo', 'Objective', 'o que se quer alcançar.'),
    ('Cenário', 'Scenario', 'a situação atual, com o problema.'),
    ('Solução esperada', 'Expected Solution', 'o resultado que você espera receber.'),
    ('Etapas', 'Steps', 'os passos que a resposta deve seguir.'),
], [('Como um líder técnico de uma equipe web,', 'PAPEL'),
    ('seu objetivo é organizar o fluxo de trabalho com Git.', 'OBJETIVO'),
    ('A equipe tem 4 pessoas e vive tendo conflitos de merge na branch principal.', 'CENÁRIO'),
    ('A solução esperada é um fluxo de branches simples, que todos consigam seguir.', 'SOLUÇÃO ESPERADA'),
    ('Descreva as etapas para: 1. criar as branches; 2. revisar o código com pull requests; 3. integrar na branch principal.', 'ETAPAS')],
    'para resolver problemas com passo a passo, como planos de ação e processos.')

blocos += framework('SPARK', 'Situation + Problem + Aspiration + Results + Kismet', [
    ('Situação', 'Situation', 'o cenário atual.'),
    ('Problema', 'Problem', 'o que está dando errado.'),
    ('Aspiração', 'Aspiration', 'aonde você quer chegar.'),
    ('Resultados', 'Results', 'como medir o sucesso.'),
    ('Sorte ou destino', 'Kismet', 'um fator imprevisto que a resposta deve considerar.'),
], [('Uma loja virtual pequena vende acessórios pelo próprio site.', 'SITUAÇÃO'),
    ('O problema é que muitos visitantes abandonam o carrinho antes de pagar.', 'PROBLEMA'),
    ('A aspiração é deixar a compra mais simples e confiável.', 'ASPIRAÇÃO'),
    ('Os resultados esperados são menos carrinhos abandonados e mais vendas concluídas.', 'RESULTADOS'),
    ('Considerando que um pico de acessos inesperado pode acontecer em uma data promocional,', 'SORTE OU DESTINO'),
    ('proponha melhorias na página de checkout.', None)],
    'em situações criativas ou de estratégia, em que imprevistos podem mudar o resultado.')

blocos += framework('CREATE', 'Character + Request + Examples + Adjustment + Type of output + Extras', [
    ('Personagem (papel)', 'Character', 'quem responde.'),
    ('Pedido', 'Request', 'o que deve ser produzido.'),
    ('Exemplos', 'Examples', 'exemplos do que você espera.'),
    ('Ajustes', 'Adjustment', 'para quem é a resposta ou que adaptações ela deve ter.'),
    ('Tipo de saída (formato)', 'Type of output', 'o formato final.'),
    ('Extras', 'Extras', 'qualquer complemento desejado.'),
], [('Como um especialista em desenvolvimento web,', 'PAPEL'),
    ('elabore um guia sobre como publicar um site Next.js gratuitamente.', 'PEDIDO'),
    ('Exemplos incluem publicar pela Vercel e pelo GitHub Pages.', 'EXEMPLOS'),
    ('Ajuste o guia para ser útil tanto para iniciantes quanto para quem já publicou algum site.', 'AJUSTES'),
    ('O tipo de saída deve ser um artigo de blog.', 'FORMATO'),
    ('Inclua uma tabela comparando as opções.', 'EXTRAS')],
    'para conteúdos mais elaborados, como artigos, tutoriais e materiais didáticos.')

blocos += [
    h2('Comparando os frameworks'),
    {'t': 'tabela', 'cabecalho': ['Framework', 'Partes', 'Bom para'], 'linhas': [
        ['RTF', 'Papel, Tarefa, Formato', 'pedidos rápidos e diretos'],
        ['CTF', 'Contexto, Tarefa, Formato', 'quando a situação define a resposta'],
        ['GRADE', 'Meta, Pedido, Ação, Detalhe, Exemplos', 'materiais completos com exemplos'],
        ['PECRA', 'Propósito, Expectativa, Contexto, Pedido, Ação', 'planos de estudo e materiais de apoio'],
        ['ROSES', 'Papel, Objetivo, Cenário, Solução esperada, Etapas', 'resolver problemas com passo a passo'],
        ['SPARK', 'Situação, Problema, Aspiração, Resultados, Sorte ou destino', 'estratégia e criatividade'],
        ['CREATE', 'Personagem, Pedido, Exemplos, Ajustes, Tipo de saída, Extras', 'artigos, tutoriais e conteúdos longos'],
    ]},
    quadro('boa-pratica', 'Dica', [
        p('Depois da primeira resposta, continue a conversa: peça para detalhar uma parte, mudar o formato ou '
          'corrigir algo. Um bom prompt é o começo, não o fim. E sempre confira o que a IA responder, principalmente '
          'código: teste antes de usar.'),
    ]),

    h2('Para saber mais'),
    p('Vídeos sobre engenharia de prompt e os frameworks apresentados neste guia:'),
    lista([f'<a href="{u}" target="_blank" rel="noreferrer">{u}</a>' for u in [
        'https://www.youtube.com/watch?v=SQOlDCWSSeE',
        'https://www.youtube.com/watch?v=lza2UY7lyws',
        'https://www.youtube.com/watch?v=Hkg3v4fLjj0',
        'https://www.youtube.com/@fvivascom',
    ]]),
]

capitulo = {'numero': None, 'titulo': 'Técnicas de Engenharia de Prompt', 'blocos': blocos}
(site / 'src/data/capitulos/web2-prompt.json').write_text(
    json.dumps(capitulo, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

if imagem_origem is None:
    sys.exit(0)

from PIL import Image
im = Image.open(imagem_origem)
destino = site / 'public/apostilas/web2/engenharia-de-prompt-rtf.png'
im.save(destino, optimize=True)
print('ok', destino.stat().st_size)
