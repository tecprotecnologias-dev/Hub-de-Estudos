"""
Questões médias e difíceis do capítulo 1 (Ciclo de Vida de Desenvolvimento de Software) de
Engenharia de Software e da Usabilidade: 10 objetivas no estilo de concursos públicos e exames
nacionais e 2 discursivas com um único comando. As funções comuns ficam em engsoft_questoes.py.
Uso (dentro de site/):

    python ferramentas/engsoft_cap1_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap1-o* e
engsoft-cap1-d*; as que já existiam (engsoft-cap1-q*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import Banco, p

banco = Banco('engsoft-cap1')


# =====================================================================================
# Médias
# =====================================================================================

banco.afirmativas(
    'medio',
    [
        ('No Modelo Cascata, a participação do cliente acontece no início e no fim do projeto.', True),
        ('Nos modelos ágeis, a documentação é extensa e formal, para compensar as mudanças frequentes.', False),
        ('No Modelo Espiral, a gestão de riscos é proativa, com análise de riscos a cada ciclo.', True),
    ],
    'I é verdadeira: no Cascata, o cliente participa no início (requisitos) e no fim (entrega). II é falsa: nos modelos '
    'ágeis, a documentação é a mínima necessária; a extensa e formal é a do Cascata. III é verdadeira: o Espiral tem '
    'gestão de riscos proativa, com análise explícita de riscos em cada volta, enquanto a do Cascata é reativa.',
    contexto=[p('Em uma aula sobre o comparativo entre os modelos de desenvolvimento, a professora pediu que a turma '
                'avaliasse algumas afirmações sobre participação do cliente, documentação e gestão de riscos.')],
)

banco.assercao(
    'medio',
    'Os modelos ágeis tendem a ser menos adequados para um contrato em que o cliente exige, antes da assinatura, o '
    'escopo completo e o custo total exato do projeto.',
    'Os modelos ágeis têm maior dificuldade para estimar o escopo e o custo total logo no início do projeto.',
    0,
    'As duas são verdadeiras, e a II explica a I. Os modelos ágeis oferecem alta adaptabilidade, mas, em troca, têm '
    'mais dificuldade para estimar escopo e custo total no início. Quando o contrato exige justamente essa estimativa '
    'fechada antes de começar, com requisitos estáveis, um modelo como o Cascata, que facilita estimar prazos e custos, '
    'tende a se encaixar melhor.',
    contexto=[p('Um órgão público vai contratar um sistema de protocolo de documentos. O edital exige que a empresa '
                'apresente, antes da assinatura do contrato, o escopo completo e o preço total, que não poderá mudar. '
                'Os requisitos já estão definidos em lei e quase não mudam.')],
)

banco.multipla(
    'medio',
    'A proposta do desenvolvedor é:',
    'pouco adequada: o Espiral é indicado para projetos grandes, complexos e de alto risco, e o seu custo não '
    'compensa em um projeto pequeno.',
    [
        'adequada: por ser o modelo mais completo, o Espiral é a melhor escolha para qualquer projeto, de qualquer porte.',
        'adequada: como o Espiral faz análise de riscos a cada ciclo, ele reduz o custo e o prazo de projetos pequenos.',
        'pouco adequada: o Espiral não usa prototipagem nem ciclos de desenvolvimento, e por isso não serve para '
        'aplicativos de celular.',
        'pouco adequada: o Espiral só pode ser usado em sistemas que envolvem hardware, como os softwares aeronáuticos '
        'e médicos.',
    ],
    'O Espiral combina o Cascata com prototipagem iterativa e faz uma análise de riscos a cada volta. Isso compensa em '
    'projetos grandes, complexos e de alto risco, como os softwares aeronáutico, médico e financeiro. Em um aplicativo '
    'pequeno e de baixo risco, o processo mais complexo e o custo mais elevado não se justificam; a apostila o '
    'considera pouco adequado para projetos pequenos. Nenhum modelo é o melhor para todos os casos.',
    contexto=[p('Dois desenvolvedores vão criar, em dois meses, um aplicativo simples de lista de compras para uso '
                'próprio e de alguns amigos. Um deles propõe usar o Modelo Espiral, "porque é o mais completo".')],
)

banco.multipla(
    'medio',
    'Considerando as fases do ciclo de vida, assinale a alternativa correta.',
    'O TDD e as revisões de código são práticas da Implementação; com CI/CD, a Implantação é automatizada e pode '
    'acontecer várias vezes ao dia.',
    [
        'O TDD é uma prática da fase de Requisitos, pois os testes são escritos antes de existir qualquer linha de '
        'código do sistema.',
        'A revisão de código pertence à fase de Manutenção, pois só é feita depois que o sistema já foi entregue e está '
        'em produção.',
        'Com CI/CD, a fase de Implantação deixa de existir, pois o código vai direto da máquina do desenvolvedor para o '
        'usuário final.',
        'A Implantação ocorre uma única vez em todo o ciclo de vida do sistema, mesmo nas equipes que usam CI/CD.',
    ],
    'Na Implementação, os desenvolvedores escrevem o código seguindo padrões e boas práticas, e é ali que o TDD e as '
    'revisões de código se tornam essenciais. A Implantação continua existindo, pois é a disponibilização do software '
    'em produção. Com CI/CD, ela é automatizada e acontece várias vezes ao dia, o que é diferente de deixar de existir '
    'ou de acontecer uma única vez.',
    contexto=[p('Uma equipe de um aplicativo de transporte escreve os testes antes do código, toda alteração passa pela '
                'revisão de um colega, e um pipeline publica a nova versão em produção várias vezes ao dia.')],
)

banco.multipla(
    'medio',
    'Sobre o ciclo de vida de desenvolvimento de software, assinale a alternativa INCORRETA.',
    'Nos modelos ágeis, as fases de Análise e Design deixam de existir, pois a equipe passa direto para a codificação.',
    [
        'Todo modelo de desenvolvimento tem as mesmas atividades essenciais; o que varia é a ordem no tempo, a intensidade '
        'de cada etapa e a flexibilidade para revisões.',
        'A Manutenção é a fase mais longa do ciclo de vida e pode durar décadas.',
        'O Design se divide em design de alto nível e design detalhado, e as suas decisões afetam a manutenibilidade e a '
        'escalabilidade futuras.',
        'A Implantação envolve instalação, migração de dados, treinamento dos usuários e um plano de rollback.',
    ],
    'A afirmação incorreta é a dos modelos ágeis: as sete fases estão presentes em qualquer projeto, em maior ou menor '
    'grau. Nos modelos ágeis, análise e design acontecem de forma mais leve e repetida a cada iteração, mas não '
    'desaparecem. As demais alternativas descrevem corretamente o que todos os modelos têm em comum, a duração da '
    'manutenção, os dois níveis de design e as atividades da implantação.',
    contexto=[p('Em um debate sobre modelos de desenvolvimento, alunos de um curso de tecnologia apresentaram várias '
                'afirmações sobre as fases do ciclo de vida.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Os modelos de desenvolvimento mais adequados aos projetos 1, 2, 3 e 4 são, respectivamente,',
    'Cascata, Espiral, Ágil e Incremental.',
    [
        'Espiral, Cascata, Ágil e Incremental.',
        'Cascata, Ágil, Espiral e Incremental.',
        'Incremental, Espiral, Ágil e Cascata.',
        'Cascata, Espiral, Incremental e Ágil.',
    ],
    'Requisitos estáveis, escopo fechado e contrato formal, como no software embarcado, apontam para o Cascata (1). Um '
    'sistema crítico, em que uma falha pode causar dano grave, pede a gestão explícita de riscos do Espiral (2). '
    'Requisitos incertos, que mudam com o retorno dos clientes, e equipe pequena são o cenário do Ágil (3). Um sistema '
    'grande, com partes que podem ser entregues de forma independente e uma delas prioritária, combina com o '
    'Incremental (4).',
    contexto=[p('Uma empresa tem quatro projetos: '
                '(1) o software embarcado de uma máquina industrial, com requisitos fixos, escopo fechado e contrato '
                'formal; '
                '(2) o sistema que controla a dose de radiação de um equipamento de radioterapia, em que uma falha pode '
                'causar danos graves aos pacientes; '
                '(3) o aplicativo de uma startup, feito por uma equipe de quatro pessoas, cujas funcionalidades mudam '
                'conforme a reação dos primeiros clientes; '
                '(4) o sistema de gestão de uma universidade, em que o módulo de matrículas precisa entrar em uso logo, '
                'e os de biblioteca e de finanças podem vir depois.')],
)

banco.afirmativas(
    'dificil',
    [
        ('O Incremental e o RAD dividem o trabalho em partes, mas o RAD depende de usuários muito engajados, '
         'participando de ciclos curtos.', True),
        ('O Espiral combina elementos do Cascata com prototipagem iterativa e é pouco adequado para projetos pequenos.',
         True),
        ('No Incremental, como cada parte é entregue de forma independente, não é preciso planejar a arquitetura geral '
         'no início.', False),
        ('No comparativo, a flexibilidade a mudanças do Espiral é maior que a do Incremental e menor que a do Ágil.',
         True),
    ],
    'I é verdadeira: os dois trabalham com partes, mas o RAD prototipa e revisa cada módulo em ciclos curtos, com o '
    'usuário presente, e exige usuários muito engajados. II é verdadeira: o Espiral junta o Cascata à prototipagem '
    'iterativa, e o seu custo não compensa em projetos pequenos. III é falsa: o Incremental exige bom planejamento '
    'inicial da arquitetura geral, porque a integração dos incrementos pode gerar inconsistências. IV é verdadeira: a '
    'flexibilidade é baixa no Cascata, média no Incremental, alta no Espiral e muito alta no Ágil.',
    contexto=[p('Ao preparar a escolha do modelo para um novo projeto, um gerente reuniu as características do '
                'Incremental, do Espiral e do RAD.')],
)

banco.assercao(
    'dificil',
    'O Modelo Cascata é adequado ao sistema embarcado descrito.',
    'No Modelo Cascata, a gestão de riscos é proativa, com análise explícita de riscos no início de cada fase.',
    2,
    'A I é verdadeira: requisitos muito bem definidos, escopo fechado e baixa chance de mudança são o cenário em que o '
    'Cascata se encaixa, com gerenciamento simples e prazos e custos fáceis de estimar. A II é falsa: no Cascata, a '
    'gestão de riscos é reativa; a gestão proativa, com análise explícita de riscos a cada ciclo, é a marca do Espiral.',
    contexto=[p('Uma fabricante vai desenvolver o software embarcado de um novo modelo de forno industrial. As funções '
                'estão totalmente definidas em contrato, o escopo é fechado, e a chance de mudanças durante o projeto é '
                'muito baixa.')],
)

banco.multipla(
    'dificil',
    'A análise correta da situação é:',
    'Houve falhas na Implantação: a migração de dados foi feita sem cuidado, os usuários não foram treinados e faltou '
    'um plano de rollback.',
    [
        'Foi um problema de Manutenção corretiva, que só pode ser resolvido depois, com a correção dos defeitos relatados '
        'pelos usuários.',
        'Foi uma falha exclusiva da fase de Testes; com mais testes unitários, a implantação teria ocorrido sem nenhum '
        'problema.',
        'Foi uma falha da fase de Requisitos, pois os usuários deveriam ter pedido o treinamento e o plano de volta ao '
        'sistema antigo.',
        'Não houve falha de processo, pois todo sistema novo passa por uma semana de instabilidade depois de entrar em '
        'produção.',
    ],
    'A Implantação é a fase em que o software chega à produção e envolve instalação e configuração, migração de dados, '
    'treinamento dos usuários e um plano de rollback caso algo dê errado. O caso falhou em três desses pontos: a '
    'migração perdeu dados, ninguém foi treinado e não havia como voltar à versão anterior. Mais testes ajudariam, mas '
    'não substituem essas atividades, e a instabilidade não é inevitável.',
    contexto=[p('Uma rede de farmácias trocou o seu sistema de vendas em um único fim de semana. Na segunda-feira, parte '
                'do histórico de clientes não aparecia, porque a migração dos dados tinha sido feita às pressas; os '
                'atendentes não sabiam usar as telas novas, pois não houve treinamento; e, como o sistema antigo já '
                'tinha sido desligado, não havia como voltar a ele.')],
)

banco.multipla(
    'dificil',
    'O modelo de desenvolvimento mais adequado para esse projeto é:',
    'o Espiral, pois o alto risco de um sistema crítico justifica a gestão explícita de riscos a cada ciclo, mesmo com '
    'custo maior.',
    [
        'o Cascata, pois o contrato formal e o escopo definido são suficientes para garantir a segurança do sistema.',
        'o RAD, pois a prototipagem rápida com os controladores permite entregar o sistema no menor prazo possível.',
        'o Ágil, pois o alto risco exige mudanças constantes de requisitos a cada sprint, com o cliente sempre presente.',
        'o Incremental, pois o sistema pode ser entregue em partes, começando pelas mais simples, sem planejar o todo.',
    ],
    'O caso mistura sinais: contrato formal e escopo definido lembram o Cascata, mas o ponto decisivo é o alto risco. '
    'Em um sistema crítico, em que uma falha pode causar acidentes, a gestão explícita de riscos a cada ciclo do '
    'Espiral compensa o processo mais complexo e o custo maior; a apostila cita justamente o software aeronáutico. O '
    'Cascata tem gestão de riscos reativa, o RAD prioriza a velocidade, e o Incremental exige planejamento da '
    'arquitetura geral.',
    contexto=[p('O órgão responsável pelo controle do espaço aéreo vai contratar um novo sistema de apoio aos '
                'controladores de voo. O contrato é formal e o escopo está definido, mas o sistema é grande, '
                'tecnicamente complexo e usa tecnologias que a equipe ainda não domina. Uma falha pode causar acidentes.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"Plan to throw one away; you will, anyhow."',
        'traducao': '(Tradução livre: "Planeje jogar uma versão fora; você vai fazer isso de qualquer jeito.")',
        'fonte': 'BROOKS, F. P. The Mythical Man-Month: Essays on Software Engineering. Reading: Addison-Wesley, 1975.',
    },
    [
        'Uma empresa desenvolveu, ao longo de um ano e meio, o sistema de gestão de uma rede de academias, seguindo o '
        'Modelo Cascata. Na entrega, os gerentes das academias perceberam que o sistema não correspondia ao modo como '
        'elas funcionam: a matrícula exigia passos desnecessários, e o controle de frequência não servia para as aulas '
        'em grupo. Boa parte do sistema precisou ser refeita.',
    ],
    'Com base no texto de Brooks e no caso apresentado, explique como outros modelos de desenvolvimento teriam '
    'lidado com o risco de construir uma primeira versão que não serve.',
    'Brooks lembra que a primeira versão de um sistema quase sempre revela que algo foi mal entendido, e que é melhor '
    'planejar isso do que ser pego de surpresa. No Cascata, a "versão para jogar fora" só aparece no fim, depois de '
    'todo o investimento, porque o cliente participa só no início e no fim e o produto só fica visível na entrega. '
    'Os outros modelos antecipam essa descoberta. O Espiral combina o Cascata com prototipagem iterativa e analisa os '
    'riscos a cada volta, então o protótipo descartável faz parte do plano. O RAD constrói protótipos rápidos de cada '
    'módulo, revisados com o usuário presente, e teria mostrado cedo os problemas da matrícula. O Incremental entrega '
    'partes funcionais, e o retorno sobre o primeiro incremento corrigiria o rumo dos seguintes. Nos modelos ágeis, o '
    'cliente participa continuamente e vê o produto a cada sprint, e o erro apareceria em semanas, quando corrigir '
    'ainda é barato. Em todos eles, o que se joga fora é pequeno, e não um ano e meio de trabalho.',
)

banco.discursiva(
    'dificil',
    {
        'citacao': '"Deliver working software frequently, from a couple of weeks to a couple of months, with a preference '
                   'to the shorter timescale."',
        'traducao': '(Tradução livre: "Entregue software funcionando com frequência, de poucas semanas a poucos meses, '
                    'com preferência pelo prazo mais curto.")',
        'fonte': 'BECK, K. et al. Princípios por trás do Manifesto Ágil. 2001. Disponível em: agilemanifesto.org.',
    },
    [
        'Uma cooperativa de pequenos produtores rurais quer um aplicativo para vender seus produtos direto aos '
        'consumidores da cidade. Os diretores ainda não sabem bem quais funcionalidades serão mais usadas e querem '
        'testar a ideia com alguns consumidores o quanto antes. O prazo total é de seis meses, a equipe tem cinco '
        'pessoas e um dos diretores pode acompanhar o projeto toda semana.',
    ],
    'Com base no texto e no comparativo entre os modelos apresentado no capítulo, compare como o Modelo Cascata e um '
    'modelo ágil conduziriam esse projeto e indique o mais adequado, justificando a sua escolha.',
    'No Cascata, todos os requisitos seriam levantados e aprovados no início, e só depois viriam design, código, testes '
    'e implantação. O produto só ficaria visível no fim dos seis meses, a participação do cliente seria só no início e '
    'no fim, e a flexibilidade a mudanças é baixa. Como os diretores ainda não sabem o que os consumidores vão usar, o '
    'risco é entregar, no fim, um aplicativo que ninguém quer. Em um modelo ágil, como o Scrum, a equipe entregaria '
    'software funcionando a cada sprint de poucas semanas, como propõe o princípio citado. O diretor que acompanha o '
    'projeto toda semana garantiria a participação contínua do cliente, e o retorno dos primeiros consumidores '
    'orientaria as próximas entregas. A flexibilidade a mudanças é muito alta e a documentação é a mínima necessária. '
    'O modelo ágil é o mais adequado, porque os requisitos são mal definidos no início, a equipe é pequena e há um '
    'representante do cliente disponível. A contrapartida é a dificuldade de estimar o escopo total no início, o que '
    'combina com o objetivo de testar a ideia e decidir o resto pelo caminho.',
)


if __name__ == '__main__':
    banco.gravar()
