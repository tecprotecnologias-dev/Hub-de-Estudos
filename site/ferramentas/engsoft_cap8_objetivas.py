"""
Questões médias e difíceis do capítulo 8 (Gestão de Projetos de Software) de Engenharia de
Software e da Usabilidade: 10 objetivas no estilo de concursos públicos e exames nacionais e
2 discursivas com um único comando. As funções comuns ficam em engsoft_questoes.py.
Uso (dentro de site/):

    python ferramentas/engsoft_cap8_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap8-o* e
engsoft-cap8-d*; as que já existiam (engsoft-cap8-m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import Banco, codigo, p

banco = Banco('engsoft-cap8')


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As técnicas de estimativa usadas nas situações 1, 2, 3 e 4 são, respectivamente,',
    'Analogia, COCOMO, Planning Poker e T-Shirt Sizing.',
    [
        'COCOMO, Analogia, T-Shirt Sizing e Planning Poker.',
        'Analogia, Planning Poker, COCOMO e T-Shirt Sizing.',
        'Planning Poker, COCOMO, Analogia e T-Shirt Sizing.',
        'Analogia, COCOMO, T-Shirt Sizing e Planning Poker.',
    ],
    'Comparar com um projeto parecido já concluído é estimar por Analogia (1). Usar uma fórmula com o tamanho do '
    'software e fatores de custo é o COCOMO, um modelo paramétrico matemático (2). Chegar a um consenso com cartas '
    'de story points é o Planning Poker (3). Classificar os itens em P, M, G e GG, para ter uma visão rápida, '
    'é o T-Shirt Sizing (4).',
    contexto=[p('Em uma empresa, quatro equipes estimaram seus trabalhos de formas diferentes: '
                '(1) a primeira usou os dados de um sistema muito parecido, entregue no ano anterior; '
                '(2) a segunda aplicou um modelo matemático que calcula o esforço a partir do tamanho estimado do '
                'software e de fatores de custo; '
                '(3) a terceira reuniu o time para votar, com cartas, quantos story points vale cada história, '
                'discutindo as divergências; '
                '(4) a quarta classificou todos os itens do backlog em P, M, G e GG, para ter uma visão rápida do tamanho '
                'do projeto.')],
)

banco.multipla(
    'medio',
    'Sobre o cronograma desse projeto, assinale a alternativa correta.',
    'O caminho crítico é A → B → D, com duração mínima de 12 dias; um atraso de 2 dias na tarefa C não altera a data '
    'de término do projeto.',
    [
        'O caminho crítico é A → C → D, com duração mínima de 9 dias, pois é a sequência mais curta do projeto.',
        'A duração mínima do projeto é de 14 dias, que é a soma das durações de todas as tarefas.',
        'O caminho crítico é A → B → D, com 12 dias; por isso, um atraso de 2 dias na tarefa C também atrasa o '
        'projeto em 2 dias.',
        'Todas as tarefas estão no caminho crítico, pois a tarefa D depende de B e de C.',
    ],
    'B e C começam depois de A e podem correr em paralelo; D só começa quando as duas terminam. O caminho A → B → D '
    'soma 3 + 5 + 4 = 12 dias, e o A → C → D soma 3 + 2 + 4 = 9 dias. O caminho crítico é a sequência mais longa, '
    'pois é ela que determina a duração mínima: 12 dias. A tarefa C tem 3 dias de folga (ela termina no dia 5, e D só '
    'pode começar no dia 8), por isso um atraso de 2 dias nela não muda o fim do projeto.',
    contexto=[
        p('O cronograma de um projeto tem quatro tarefas:'),
        codigo('''
Tarefa  Duração  Depende de
A       3 dias   -
B       5 dias   A
C       2 dias   A
D       4 dias   B e C
'''),
    ],
)

banco.afirmativas(
    'medio',
    [
        ('A situação caracteriza scope creep, o crescimento não controlado do escopo.', True),
        ('Uma EAP bem feita, que decompõe o projeto em pacotes de trabalho, ajuda a deixar claro o que faz parte do '
         'escopo e torna visíveis os pedidos novos.', True),
        ('Pelo Triângulo de Ferro, como o prazo e o custo não mudaram, o aumento do escopo não afeta a qualidade, '
         'pois essas variáveis são independentes.', False),
    ],
    'I é verdadeira: pedidos pequenos e sem registro, acumulados, são o scope creep, uma das principais causas de '
    'falha em projetos. II é verdadeira: com a EAP, cada pacote de trabalho do escopo fica explícito, e qualquer '
    'pedido fora dela pode ser reconhecido e negociado. III é falsa: escopo, prazo e custo são interdependentes; se o '
    'escopo cresce e os outros dois não mudam, o que cede é a qualidade, gerando débito técnico e problemas futuros.',
    contexto=[p('Durante o desenvolvimento de um sistema de reservas, o cliente pediu, em várias conversas informais, '
                '"só um ajustezinho": um relatório a mais, um campo novo, uma tela extra. Os pedidos não foram '
                'registrados, e o prazo e o orçamento continuaram os mesmos. No fim, o projeto atrasou dois meses, '
                'e a equipe passou a pular testes para tentar recuperar o tempo.')],
)

banco.assercao(
    'medio',
    'A forma como a equipe conduz a Daily Scrum se afasta do propósito desse evento.',
    'A Daily Scrum é uma reunião diária de até quinze minutos, focada em impedimentos, e não uma reunião de status '
    'para o gerente.',
    0,
    'As duas são verdadeiras, e a II explica a I. A Daily Scrum é do Time: serve para que os próprios desenvolvedores '
    'identifiquem o que está impedindo o trabalho. Uma reunião de quarenta minutos, em que cada um presta contas ao '
    'gerente, foge do timebox de quinze minutos e transforma o evento em controle de status.',
    contexto=[p('Em uma empresa que diz usar Scrum, a Daily dura cerca de quarenta minutos. Nela, cada desenvolvedor '
                'relata ao gerente tudo o que fez no dia anterior, e o gerente anota quem está "produzindo pouco".')],
)

banco.multipla(
    'medio',
    'As situações 1, 2 e 3 correspondem, respectivamente, aos eventos',
    'Sprint Retrospective, Sprint Review e Sprint Planning.',
    [
        'Sprint Review, Sprint Retrospective e Sprint Planning.',
        'Daily Scrum, Sprint Review e Sprint Planning.',
        'Sprint Retrospective, Sprint Planning e Sprint Review.',
        'Sprint Planning, Sprint Review e Sprint Retrospective.',
    ],
    'Na Retrospective, a equipe reflete sobre o próprio processo, como a demora das revisões de código (1). '
    'Na Review, o incremento é demonstrado aos stakeholders, que dão feedback (2). A Planning abre a sprint e define '
    'o que será entregue e como (3). A Daily é a reunião diária, focada em impedimentos.',
    contexto=[p('Em três reuniões de uma equipe Scrum: '
                '(1) o Time percebeu que as revisões de código estavam demorando dias e decidiu experimentar a '
                'programação em pares na sprint seguinte; '
                '(2) a nova tela de pagamento foi apresentada aos representantes do cliente, que sugeriram mudanças; '
                '(3) o Time e a Product Owner escolheram os itens do Product Backlog que entrariam no ciclo e '
                'planejaram como construí-los.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'A análise correta da situação do projeto, segundo o EVM, é:',
    'SV = +R$ 20.000 e SPI = 1,10, ou seja, o projeto está adiantado; CV = -R$ 55.000 e CPI = 0,80, ou seja, '
    'está acima do orçamento.',
    [
        'SV = -R$ 20.000 e SPI = 0,91, ou seja, o projeto está atrasado; CV = +R$ 55.000 e CPI = 1,25, ou seja, '
        'está econômico.',
        'SV = +R$ 20.000 e SPI = 1,10, ou seja, o projeto está adiantado; CV = +R$ 55.000 e CPI = 1,25, ou seja, '
        'está econômico.',
        'SV = -R$ 75.000 e SPI = 0,73, ou seja, o projeto está atrasado e, por isso, também está acima do orçamento.',
        'O projeto está em boa situação, pois gastou mais do que o planejado e, portanto, entregou mais trabalho.',
    ],
    'SV = EV - PV = 220.000 - 200.000 = +20.000 e SPI = EV / PV = 1,10: foi feito mais trabalho do que o planejado '
    'até a data, então o projeto está adiantado. CV = EV - AC = 220.000 - 275.000 = -55.000 e CPI = EV / AC = 0,80: '
    'cada real gasto rendeu só 80 centavos de trabalho, então o projeto está acima do orçamento. Prazo e custo são '
    'medidos separadamente: estar adiantado não significa estar econômico, e gastar mais não prova que se entregou mais.',
    contexto=[p('Na metade de um projeto, o relatório de acompanhamento mostra: valor planejado até a data (PV) de '
                'R$ 200.000, valor agregado (EV) de R$ 220.000 e custo real (AC) de R$ 275.000.')],
)

banco.afirmativas(
    'dificil',
    [
        ('O diretor comercial não deveria incluir itens no Sprint Backlog, que pertence ao Time; os pedidos dele '
         'devem ir para o Product Backlog, priorizado pela Product Owner.', True),
        ('Ter três Product Owners, cada um com a sua lista de prioridades, está de acordo com o Scrum, pois cada '
         'departamento é um cliente diferente.', False),
        ('Sprints de seis semanas contrariam o Scrum, que define para a sprint um timebox fixo de uma a quatro semanas.',
         True),
        ('O incremento entregue sem testes pode ser considerado pronto se a Product Owner aprovar, pois a '
         'Definition of Done é apenas uma recomendação.', False),
    ],
    'I é verdadeira: durante a sprint, o Sprint Backlog é do Time, e pedidos novos vão para o Product Backlog. '
    'II é falsa: o PO é a única voz do cliente e mantém um único Product Backlog ordenado; três listas concorrentes '
    'impedem saber o que é mais importante. III é verdadeira: o timebox da sprint é fixo, de uma a quatro semanas. '
    'IV é falsa: o incremento precisa estar completamente desenvolvido, testado e alinhado à Definition of Done; '
    'o que não a cumpre não está pronto.',
    contexto=[p('Uma empresa diz ter adotado o Scrum, mas: o diretor comercial inclui itens direto no Sprint Backlog '
                'quando fecha uma venda; cada um dos três departamentos tem o seu próprio Product Owner, com a sua '
                'lista de prioridades; a duração das sprints muda conforme a necessidade e às vezes chega a seis '
                'semanas; e os incrementos costumam ser entregues sem testes, "para testar na próxima sprint".')],
)

banco.assercao(
    'dificil',
    'Para adotar o Kanban, a equipe precisa primeiro reorganizar todo o seu processo, criando os papéis de Product '
    'Owner e Scrum Master e sprints de duração fixa.',
    'O Kanban não prescreve timeboxes, papéis ou reuniões fixas e é aplicado sobre o processo que já existe.',
    3,
    'A II descreve corretamente o Kanban, e por isso a I é falsa. O Kanban começa pelo processo atual: a equipe '
    'visualiza o fluxo que já tem em um quadro, limita o WIP e melhora aos poucos, usando dados. Papéis de PO e Scrum '
    'Master e sprints de duração fixa são do Scrum, não do Kanban.',
    contexto=[p('A equipe de infraestrutura de uma empresa atende pedidos que chegam a qualquer hora e quer começar '
                'a usar o Kanban. Um consultor afirmou que, antes do primeiro quadro, seria preciso redesenhar todo o '
                'trabalho da equipe.')],
)

banco.multipla(
    'dificil',
    'A melhor recomendação para essa equipe é:',
    'Combinar os dois métodos (Scrumban): manter as sprints, com Sprint Goal, para as funcionalidades planejadas, e '
    'tratar os defeitos urgentes em um fluxo contínuo, com limite de WIP.',
    [
        'Manter o Scrum puro e incluir cada defeito urgente no Sprint Backlog assim que ele chegar, mesmo que isso '
        'comprometa o Sprint Goal.',
        'Abandonar as sprints e qualquer planejamento, passando a atender só os defeitos, que são mais urgentes do que '
        'as funcionalidades novas.',
        'Guardar todos os defeitos urgentes até o fim da sprint, para não interromper o trabalho planejado.',
        'Aumentar a duração das sprints para oito semanas, para que caibam as funcionalidades e os defeitos.',
    ],
    'O trabalho da equipe tem duas naturezas: funcionalidades em ciclos regulares, em que o Scrum traz '
    'comprometimento e previsibilidade, e defeitos urgentes e imprevisíveis, em que o Kanban responde melhor. Combinar '
    'os dois é o Scrumban. Pôr cada urgência no Sprint Backlog fere a regra de não ameaçar o Sprint Goal; segurar '
    'defeitos graves até o fim da sprint prejudica os clientes; sprints de oito semanas fogem do timebox de uma a '
    'quatro semanas; e largar o planejamento sacrifica as funcionalidades.',
    contexto=[p('Uma equipe desenvolve funcionalidades novas para um aplicativo em sprints de duas semanas, mas também é '
                'responsável pelos defeitos urgentes que aparecem em produção a qualquer momento. Eles ocupam cerca de '
                '40% do tempo da equipe e, em quase todas as sprints, acabam derrubando o Sprint Goal.')],
)

banco.multipla(
    'dificil',
    'Sobre a gestão desses riscos, assinale a alternativa INCORRETA.',
    'O risco 4 pode ser aceito sem nenhuma resposta, pois a Matriz de Riscos prioriza os riscos só pela probabilidade, '
    'e a probabilidade dele é baixa.',
    [
        'Contratar um provedor de hospedagem com acordo de nível de serviço e multa por indisponibilidade, no risco 1, '
        'é uma forma de transferir o risco.',
        'Trocar a biblioteca de videochamada em versão beta por uma versão estável, no risco 2, é uma forma de evitar o '
        'risco.',
        'Treinar a equipe e construir um protótipo antes de usar a nova tecnologia, no risco 3, é uma forma de mitigar '
        'o risco, reduzindo a sua probabilidade.',
        'Aceitar o risco 5, de baixa probabilidade e baixo impacto, é uma resposta válida, desde que ele fique '
        'registrado e acompanhado.',
    ],
    'A afirmação incorreta é a do risco 4: a Matriz de Riscos cruza probabilidade e impacto. Um vazamento de dados de '
    'pacientes tem impacto altíssimo e precisa de resposta, mesmo com probabilidade baixa. As demais estão corretas: '
    'passar a consequência a um terceiro é transferir; eliminar a causa é evitar; reduzir a probabilidade ou o '
    'impacto é mitigar; e aceitar é adequado para riscos pequenos, desde que acompanhados.',
    contexto=[p('A equipe de um aplicativo de telemedicina listou cinco riscos: '
                '(1) o servidor ficar fora do ar durante as consultas; '
                '(2) a biblioteca de videochamada, em versão beta, apresentar falhas; '
                '(3) a equipe atrasar por não conhecer a nova tecnologia de agendamento; '
                '(4) um vazamento dos dados dos pacientes, de baixa probabilidade, mas de impacto muito alto; '
                '(5) um atraso de um dia por causa de um feriado local, de baixa probabilidade e baixo impacto.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"Adding manpower to a late software project makes it later."',
        'traducao': '(Tradução livre: "Adicionar pessoas a um projeto de software atrasado o atrasa ainda mais.")',
        'fonte': 'BROOKS, F. P. The Mythical Man-Month: Essays on Software Engineering. Reading: Addison-Wesley, 1975.',
    },
    [
        'Um sistema de matrículas precisa estar pronto em três semanas, no início do semestre. O relatório de EVM '
        'mostra SPI = 0,75 e CPI = 0,90. A equipe tem cinco desenvolvedores que conhecem bem o sistema, e o caminho '
        'crítico passa pelo módulo de pagamento, que ainda está pela metade.',
        'Para recuperar o atraso, o diretor decidiu contratar mais cinco desenvolvedores, que nunca trabalharam no '
        'projeto, e manter todo o escopo previsto.',
    ],
    'Com base no texto de Brooks e no caso apresentado, avalie a decisão do diretor e proponha uma forma mais adequada '
    'de lidar com o atraso.',
    'Os indicadores mostram um projeto atrasado (SPI < 1) e acima do orçamento (CPI < 1). Contratar cinco pessoas '
    'novas a três semanas do prazo tende a piorar os dois: elas precisam aprender o sistema, ocupam o tempo dos cinco '
    'desenvolvedores experientes, que vão ensiná-las, e aumentam a comunicação e a coordenação, que é o que Brooks '
    'aponta. O custo também sobe, enquanto o CPI já está ruim. Pelo Triângulo de Ferro, se o prazo não pode mudar e o '
    'custo já passou do previsto, a variável a negociar é o escopo, nunca a qualidade. O mais adequado é rever o '
    'escopo com o cliente: priorizar o que é indispensável para o início das matrículas, a começar pelo módulo de '
    'pagamento, que está no caminho crítico, e deixar o resto para uma entrega posterior. Também vale tratar o atraso '
    'como risco, com respostas planejadas, e acompanhar o SPI e o CPI até o fim.',
)

banco.discursiva(
    'dificil',
    {
        'citacao': '"Responding to change over following a plan."',
        'traducao': '(Tradução livre: "Responder a mudanças mais do que seguir um plano.")',
        'fonte': 'BECK, K. et al. Manifesto for Agile Software Development. 2001. Disponível em: agilemanifesto.org.',
    },
    [
        'Uma empresa desenvolve um aplicativo para uma rede de academias. No início, montou um cronograma detalhado de '
        'doze meses, com toda a EAP e o caminho crítico definidos. Desde o segundo mês, porém, o cliente pede mudanças '
        'com frequência, porque está descobrindo o que os alunos realmente usam. A cada pedido, o gerente refaz o '
        'cronograma inteiro, e a equipe passa mais tempo replanejando do que desenvolvendo.',
        'O prazo final e o orçamento do contrato não podem mudar.',
    ],
    'Com base no texto e no caso apresentado, explique como a gestão desse projeto poderia ser organizada para lidar '
    'com as mudanças frequentes de requisitos.',
    'O planejamento tradicional, com cronograma de doze meses, EAP e caminho crítico fechados no início, funciona bem '
    'quando o escopo é estável. Neste caso, cada mudança obriga a refazer tudo, e o plano vira um peso. O Scrum lida '
    'melhor com isso, como propõe o Manifesto Ágil. O Product Backlog é uma lista viva, ordenada pela Product Owner, '
    'que é a voz do cliente: os pedidos novos entram nele e são priorizados, sem refazer o projeto inteiro. As sprints, '
    'de uma a quatro semanas, protegem o trabalho em andamento, e as mudanças entram na sprint seguinte, na Sprint '
    'Planning. A cada Sprint Review, o cliente vê um incremento funcionando e dá feedback, descobrindo cedo o que os '
    'alunos usam. Como prazo e custo são fixos, pelo Triângulo de Ferro o escopo é que se ajusta: o que for mais '
    'valioso é entregue primeiro, e o menos importante fica por último ou sai. As mudanças continuam controladas, pelo '
    'backlog, o que evita o scope creep.',
)


if __name__ == '__main__':
    banco.gravar()
