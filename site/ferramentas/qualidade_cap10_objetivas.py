"""
Questões médias e difíceis do capítulo 10 (Gerenciamento de Defeitos e Relatórios) de Qualidade e
Testes de Software: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas
com um único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/qualidade_cap10_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap10-o* e
qualidade-cap10-d*; as que já existiam (m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import QUALIDADE, Banco, p

banco = Banco('qualidade-cap10', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Pela escala da apostila, os defeitos 1, 2, 3 e 4 têm, respectivamente, severidade',
    'crítica (S1), alta (S2), média (S3) e trivial (S5).',
    [
        'alta (S2), crítica (S1), média (S3) e trivial (S5).',
        'crítica (S1), média (S3), alta (S2) e baixa (S4).',
        'crítica (S1), alta (S2), baixa (S4) e trivial (S5).',
        'alta (S2), alta (S2), média (S3) e baixa (S4).',
    ],
    'Sistema inoperante com perda de dados é crítico (S1), com correção imediata (1). Funcionalidade principal '
    'comprometida sem contorno viável é alta (S2), com correção na sprint atual (2). Funcionalidade afetada, mas com um '
    'contorno aceitável, é média (S3) (3). Erro de ortografia, imperceptível para o uso, é trivial (S5) (4). A severidade '
    'baixa (S4) fica para problemas menores de usabilidade ou cosméticos.',
    contexto=[p('Em um sistema de vendas, foram registrados quatro defeitos: '
                '(1) o sistema sai do ar ao fechar o caixa e perde as vendas do dia; '
                '(2) não é possível emitir nota fiscal, e não há outra forma de fazer isso; '
                '(3) o filtro por data dos relatórios não funciona, mas dá para ordenar a lista e encontrar o período; '
                '(4) a palavra "desconto" aparece escrita como "descomto" em uma tela de configuração.')],
)

banco.multipla(
    'medio',
    'Pela classificação por tipo da apostila, os defeitos 1, 2, 3 e 4 são, respectivamente, de',
    'compatibilidade, performance, segurança e dados.',
    [
        'interface, performance, segurança e dados.',
        'compatibilidade, usabilidade, segurança e funcional.',
        'compatibilidade, performance, dados e segurança.',
        'funcional, performance, segurança e regressão.',
    ],
    'Comportamento incorreto em um navegador, sistema ou dispositivo específico é defeito de compatibilidade (1). '
    'Lentidão ou consumo excessivo de recursos é de performance (2). Senha visível em log compromete a '
    'confidencialidade: é de segurança (3). Valor arredondado de forma incorreta é um problema de dados (4). Os quatro '
    'exemplos estão na própria apostila.',
    contexto=[p('A equipe de QA classificou quatro defeitos: '
                '(1) a busca funciona no Chrome, mas não no Safari; '
                '(2) o relatório mensal leva 45 segundos para carregar; '
                '(3) a senha do usuário aparece em texto puro no log da aplicação; '
                '(4) o valor total do pedido é arredondado para baixo de forma errada.')],
)

banco.afirmativas(
    'medio',
    [
        ('Um defeito marcado como Duplicado é fechado com uma referência ao registro original.', True),
        ('Um defeito marcado como Não Reproduzível é fechado automaticamente como inválido, sem mais nenhuma ação.', False),
        ('Um defeito marcado como Won\'t Fix foi reconhecido, mas se decidiu não corrigi-lo neste ciclo.', True),
        ('Um defeito Reaberto volta ao desenvolvedor porque a correção foi insuficiente ou causou uma regressão.', True),
    ],
    'I, III e IV descrevem corretamente os estados do ciclo de vida da apostila. II é falsa: quando o defeito não pode ser '
    'reproduzido com as informações fornecidas, solicitam-se mais detalhes a quem o registrou; ele não é simplesmente '
    'descartado.',
    contexto=[p('Uma equipe está configurando os estados do ciclo de vida dos defeitos na sua ferramenta de rastreamento.')],
)

banco.assercao(
    'medio',
    'A lentidão observada em certo horário deve ser registrada, a princípio, como incidente, e não necessariamente como '
    'defeito.',
    'Um incidente é qualquer evento que exige investigação e pode ou não ser causado por um defeito.',
    0,
    'As duas são verdadeiras, e a II explica a I. A lentidão pode vir de um defeito no código, mas também de um pico de '
    'carga, de um problema de rede ou de uma tarefa agendada no servidor. É o exemplo da própria apostila: um sistema '
    'lento em determinado horário é um incidente até que a investigação mostre a causa; só então se sabe se há um '
    'defeito a registrar.',
    contexto=[p('Todos os dias, por volta das 18 horas, os usuários de um sistema de pedidos relatam que ele fica lento. '
                'Ainda não se sabe a causa.')],
)

banco.multipla(
    'medio',
    'Como a equipe deve registrar esse pedido?',
    'Como melhoria (enhancement), pois é um comportamento que não estava especificado, e não um defeito.',
    [
        'Como defeito de severidade alta, pois o cliente considera que falta algo importante no sistema.',
        'Como defeito de compatibilidade, pois o sistema não funciona com o Excel, que o cliente usa no dia a dia.',
        'Como defeito de regressão, pois algo que o cliente esperava deixou de existir no sistema entregue.',
        'Em lugar nenhum, pois só defeitos entram na ferramenta de rastreamento, e pedidos novos ficam por e-mail.',
    ],
    'Entre as boas práticas da apostila está diferenciar defeito de melhoria: um comportamento que não estava '
    'especificado, mas que o usuário gostaria de ter, é uma melhoria. Registrá-lo como defeito distorce as métricas, '
    'como a densidade de defeitos, e reportar sugestões como defeitos é um dos antipadrões do bug report. A melhoria '
    'também deve ser registrada, na categoria certa.',
    contexto=[p('Depois da entrega de um sistema de estoque, que exporta relatórios em PDF, como diz a especificação, um '
                'cliente abriu um chamado: "O sistema deveria exportar os relatórios também em Excel."')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'A análise correta das métricas é:',
    'O backlog cresce 15 defeitos por sprint, e a reabertura de 20% mostra correções de baixa qualidade.',
    [
        'O backlog diminui 15 defeitos por sprint, e a reabertura de 20% está dentro da meta de prontidão.',
        'O backlog fica estável, pois cada correção cobre um defeito, e a reabertura é de 9%, abaixo de 10%.',
        'O backlog cresce 15 defeitos por sprint, mas a reabertura de 20% mostra correções de alta qualidade.',
        'As métricas não permitem avaliar o backlog, pois a detecção e a correção medem coisas diferentes.',
    ],
    'Comparar a taxa de detecção com a de correção mostra se o backlog de defeitos cresce ou diminui: com 60 novos e 45 '
    'corrigidos e verificados por sprint, ele cresce 15 a cada sprint. A taxa de reabertura é 9 de 45, ou 20%, o dobro '
    'do limite de 10% citado nos critérios de prontidão; uma taxa alta indica baixa qualidade nas correções.',
    contexto=[p('Em média, por sprint, a equipe encontra 60 defeitos novos e corrige e verifica 45. Dos 45 corrigidos, 9 '
                'são reabertos porque a correção não resolveu o problema.')],
)

banco.afirmativas(
    'dificil',
    [
        ('O critério sobre defeitos críticos (S1) está atendido.', True),
        ('O critério sobre defeitos de severidade alta (S2) não está atendido.', True),
        ('Os critérios de DDE e de taxa de reabertura estão atendidos.', True),
        ('O defeito de severidade alta aberto ontem não impede o release, pois os outros critérios foram cumpridos.', False),
    ],
    'I é verdadeira: não há defeitos S1 abertos, e o critério é zero. II é verdadeira: há 5 defeitos S2 abertos, acima do '
    'limite de 3. III é verdadeira: o DDE de 93% passa dos 90%, e a reabertura de 8% fica abaixo de 10%. IV é falsa: um '
    'dos indicadores de prontidão é não ter nenhum defeito novo de alta severidade nas últimas 48 horas de teste; somado '
    'ao critério de S2, o produto não está pronto.',
    contexto=[p('Às vésperas de um release, cujos critérios seguem os indicadores da apostila (com no máximo 3 defeitos S2 '
                'abertos), a equipe tem: nenhum defeito S1 aberto; 5 defeitos S2 abertos; DDE de 93%; taxa de reabertura '
                'de 8%; e um defeito novo de severidade alta encontrado ontem nos testes.')],
)

banco.assercao(
    'dificil',
    'Na triagem, o QA Lead ou o Tech Lead valida o defeito, define a severidade e a prioridade e o atribui ao '
    'desenvolvedor responsável.',
    'Na triagem, os defeitos duplicados devem seguir todo o fluxo, até a verificação, para que nenhuma informação se '
    'perca.',
    2,
    'A I é verdadeira: é o papel da triagem na tabela de responsabilidades por estado. A II é falsa: pela apostila, '
    'defeitos inválidos ou duplicados são fechados diretamente na triagem; o duplicado é fechado com uma referência ao '
    'registro original, onde as informações continuam disponíveis.',
    contexto=[p('Na reunião diária de triagem, a equipe encontrou um defeito novo, válido, e outro que repete um registro '
                'já existente.')],
)

banco.multipla(
    'dificil',
    'As ferramentas mais adequadas às equipes 1, 2, 3 e 4 são, respectivamente,',
    'Bugzilla, Azure DevOps, GitHub Issues e Jira.',
    [
        'Jira, Azure DevOps, GitHub Issues e Bugzilla.',
        'Bugzilla, GitHub Issues, Azure DevOps e Jira.',
        'GitHub Issues, Azure DevOps, Bugzilla e Jira.',
        'Bugzilla, Azure DevOps, Jira e GitHub Issues.',
    ],
    'O Bugzilla, da Mozilla, é gratuito, pode ser hospedado pela própria organização e tem dependências entre bugs (1). '
    'O Azure DevOps se integra ao ecossistema Microsoft e tem relatórios excelentes com Power BI (2). O GitHub Issues fica '
    'junto do código e pode fechar a issue automaticamente quando o pull request com a correção é integrado (3). O Jira '
    'tem fluxos muito customizáveis e plugins como Zephyr e Xray para integrar os casos de teste (4).',
    contexto=[p('Quatro equipes escolhem uma ferramenta de gerenciamento de defeitos: '
                '(1) um projeto de código aberto que precisa de uma solução gratuita, hospedada nos próprios servidores, '
                'com dependências entre bugs; '
                '(2) um time .NET que usa Azure e quer relatórios no Power BI; '
                '(3) desenvolvedores que querem que a issue seja fechada sozinha quando o pull request da correção for '
                'aceito; '
                '(4) um time ágil que precisa de fluxos de trabalho muito personalizados e de casos de teste integrados por '
                'plugins.')],
)

banco.multipla(
    'dificil',
    'Sobre as boas práticas de gerenciamento de defeitos, assinale a alternativa INCORRETA.',
    'As discussões sobre o defeito devem ficar no chat da equipe, que é mais rápido, e o registro deve ter só o título e a '
    'severidade.',
    [
        'O número do defeito deve ser citado nos commits e nos pull requests, criando rastreabilidade entre o código e o '
        'defeito.',
        'Um template obrigatório na ferramenta de rastreamento garante que as informações essenciais não sejam omitidas.',
        'A triagem deve ser regular, pois um backlog de defeitos não triados é uma dívida técnica escondida.',
        'As causas raiz devem ser analisadas periodicamente para encontrar padrões, como módulos com muitos defeitos.',
    ],
    'A afirmação incorreta é a do chat: pela apostila, toda discussão sobre o defeito, como esclarecimentos, descobertas '
    'da investigação e a razão da abordagem escolhida, deve ficar registrada no próprio ticket, e não em conversas que se '
    'perdem. Um registro só com título e severidade também fere o template padronizado. As demais alternativas são boas '
    'práticas do capítulo.',
    contexto=[p('Uma equipe vai escrever o seu guia interno de gerenciamento de defeitos e reuniu algumas recomendações.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Ao testar a versão 3.2.0 de um sistema de agendamento, no ambiente de homologação, com o Firefox 125 no Windows '
        '11, uma testadora percebeu que, ao tentar remarcar uma consulta para um horário no dia seguinte, aparece a '
        'mensagem "Erro inesperado" e a consulta continua no horário antigo. O log do servidor mostra o código HTTP 500. '
        'Pela regra de negócio, a remarcação para qualquer horário livre deveria ser aceita. Ela tentou cinco vezes, e o '
        'erro aconteceu em todas. O registro que ela abriu diz apenas: "Remarcação não funciona."',
    ],
    'Reescreva esse registro como um bug report completo, seguindo a anatomia apresentada no capítulo, e justifique a '
    'severidade e a prioridade escolhidas.',
    'Título: "Erro 500 ao remarcar consulta para um horário do dia seguinte na tela de agendamento". Severidade: Alta (S2), '
    'pois a remarcação é uma funcionalidade principal e não há contorno viável. Prioridade: Alta, pois afeta diretamente '
    'pacientes e clínicas no uso diário. Ambiente: Windows 11, Firefox 125, homologação, versão 3.2.0. Componente: '
    'Agendamento. Pré-condições: usuário autenticado com uma consulta já marcada e horários livres no dia seguinte. '
    'Passos para reproduzir: (1) abrir a consulta marcada; (2) clicar em "Remarcar"; (3) escolher um horário livre no dia '
    'seguinte; (4) clicar em "Confirmar". Resultado obtido: mensagem "Erro inesperado", a consulta permanece no horário '
    'antigo e o log registra HTTP 500. Resultado esperado: a consulta é remarcada para o novo horário, com mensagem de '
    'confirmação, conforme a regra de negócio. Frequência: sempre (5 em 5 tentativas). Evidências: print da tela e trecho '
    'do log com o erro 500. Reportado por: nome da testadora e data. Assim, o desenvolvedor consegue reproduzir o defeito '
    'sem precisar perguntar nada, e ele não vira "Não Reproduzível".',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Em uma empresa de software, os defeitos são comunicados por e-mail ou por mensagens no chat. Cada desenvolvedor '
        'decide sozinho o que corrigir primeiro e, quando termina, avisa que "está resolvido". Não há registro de quantos '
        'defeitos existem, e a diretoria não consegue saber se o produto está pronto para um lançamento. Vários defeitos '
        'reaparecem depois de "resolvidos", e outros são esquecidos.',
    ],
    'Com base no capítulo, proponha um processo de gerenciamento de defeitos para essa empresa, explicando como ele '
    'resolveria os problemas relatados.',
    'O primeiro passo é centralizar tudo em uma ferramenta de rastreamento, como Jira, GitHub Issues ou Azure DevOps, '
    'com um template obrigatório de bug report (título, ambiente, passos, resultado obtido e esperado, evidências, '
    'severidade e prioridade). Assim nenhum defeito se perde. Em seguida, um ciclo de vida com estados e responsáveis: o '
    'testador registra (Novo); o QA Lead ou o Tech Lead faz a triagem regular, valida, define severidade e prioridade e '
    'atribui ao desenvolvedor, o que tira dele a decisão solitária sobre o que fazer primeiro; o desenvolvedor corrige e '
    'marca como Resolvido, indicando o commit; e só o testador fecha, depois de verificar a correção e procurar '
    'regressões, ou reabre. Isso ataca os defeitos que voltam. As discussões ficam no ticket, e o número do defeito é '
    'citado nos commits. Com os dados registrados, a empresa passa a ter métricas: defeitos abertos por severidade, '
    'taxas de detecção, de correção e de reabertura, DDE e burn down, que respondem de forma objetiva se o produto está '
    'pronto. Por fim, a análise de causa raiz nas retrospectivas ajuda a evitar que defeitos semelhantes voltem.',
)


if __name__ == '__main__':
    banco.gravar()
