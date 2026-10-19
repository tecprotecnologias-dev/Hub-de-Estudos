"""
Questões médias e difíceis do capítulo 6 (Qualidade de Software) de Engenharia de Software e
da Usabilidade: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas
com um único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/engsoft_cap6_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap6-o* e
engsoft-cap6-d*; as fáceis (engsoft-cap6-f*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import Banco, codigo, p

banco = Banco('engsoft-cap6')


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Considerando as categorias do Custo da Qualidade (CoQ), os gastos 1, 2, 3 e 4 classificam-se, respectivamente, como custos de',
    'prevenção, avaliação, falha interna e falha externa.',
    [
        'avaliação, prevenção, falha externa e falha interna.',
        'prevenção, falha interna, avaliação e falha externa.',
        'avaliação, avaliação, falha interna e falha externa.',
        'prevenção, avaliação, falha externa e falha externa.',
    ],
    'O curso de testes automatizados é investimento para evitar defeitos: prevenção. '
    'Executar a suíte de regressão e fazer auditoria é verificar a qualidade: avaliação. '
    'O retrabalho feito na homologação interna corrige o defeito antes da entrega: falha interna. '
    'A multa por indisponibilidade vem de um defeito que chegou ao cliente: falha externa, a categoria mais cara.',
    contexto=[p('Ao fechar o balanço anual, uma empresa de software listou os seguintes gastos ligados à qualidade: '
                '(1) um curso de escrita de testes automatizados para os desenvolvedores; '
                '(2) as horas gastas na execução da suíte de testes de regressão e em uma auditoria de processos; '
                '(3) o retrabalho para corrigir um defeito encontrado na homologação interna, antes do lançamento; '
                '(4) a multa contratual paga a um cliente por causa de uma indisponibilidade do sistema em produção.')],
)

banco.afirmativas(
    'medio',
    [
        ('A revisão dos pull requests e a análise com o SonarQube são atividades de Controle de Qualidade (QC), '
         'pois atuam sobre um artefato que já foi produzido.', True),
        ('A análise estática de código executa o programa com dados de teste para encontrar falhas que só aparecem '
         'em tempo de execução.', False),
        ('A criação de um processo padrão com checklist e treinamento é uma atividade de QC, pois o seu objetivo '
         'também é reduzir a quantidade de defeitos.', False),
    ],
    'I é verdadeira: revisão de código e análise estática examinam o produto já criado, por isso são QC. '
    'II é falsa: a análise estática examina o código-fonte sem executá-lo; quem executa o programa são os testes. '
    'III é falsa: definir processos e treinar pessoas é Garantia da Qualidade (QA), que é orientada ao processo e previne defeitos. '
    'O objetivo de reduzir defeitos é comum a QA e QC; o que os distingue é atuar no processo ou no produto.',
    contexto=[p('Uma equipe adotou três práticas novas: todo pull request passa pela revisão de outro desenvolvedor; '
                'o pipeline roda o SonarQube a cada envio de código; e a gerência criou um processo padrão de desenvolvimento, '
                'com checklist, que vale para todos os projetos da empresa e é ensinado em um treinamento obrigatório.')],
)

banco.multipla(
    'medio',
    'A meta definida pela equipe está diretamente ligada à melhoria de qual métrica?',
    'MTTR, o tempo médio para restaurar o serviço após uma falha.',
    [
        'MTBF, o tempo médio entre falhas.',
        'Lead Time, o tempo desde a solicitação até a entrega em produção.',
        'Taxa de Defeitos Escapados, o percentual de defeitos encontrados em produção.',
        'Cycle Time, o tempo que uma tarefa leva do início até a entrega.',
    ],
    'Os 30 dias entre uma falha e outra são o MTBF, que a meta não pretende mudar: a reversão automática não evita a falha. '
    'O que ela encurta é o tempo para voltar a funcionar depois que a falha acontece, de 4 horas para 30 minutos: isso é o MTTR. '
    'Lead Time e Cycle Time medem o tempo de entrega de trabalho, e a taxa de defeitos escapados mede quantos defeitos chegam à produção.',
    contexto=[p('O painel de monitoramento de um sistema de agendamento mostra que, em média, o sistema fica 30 dias funcionando '
                'sem falhas. Quando uma falha acontece, porém, a equipe leva em média 4 horas para colocá-lo de volta no ar. '
                'A equipe decidiu implantar uma reversão automática (rollback) para a versão anterior, com a meta de '
                'deixar o sistema fora do ar por no máximo 30 minutos a cada falha.')],
)

banco.multipla(
    'medio',
    'A complexidade ciclomática da função e o número mínimo de casos de teste para percorrer todos os seus caminhos '
    'independentes são, respectivamente,',
    '5 e 5.',
    [
        '4 e 4.',
        '4 e 5.',
        '5 e 3.',
        '6 e 6.',
    ],
    'A complexidade ciclomática é o número de pontos de decisão mais 1. A função tem quatro decisões: o for, '
    'o if p.cancelado, o if p.valor > 1000 e o elif p.valor > 500 (o else não conta, pois não testa condição). '
    'Assim, 4 + 1 = 5. Esse número é também a quantidade de caminhos independentes, que é o mínimo de casos de teste '
    'para percorrer todos eles.',
    contexto=[
        p('Durante a revisão de código, uma desenvolvedora analisou a função abaixo, escrita em Python.'),
        codigo('''
def total_pedidos(pedidos):
    total = 0
    for p in pedidos:
        if p.cancelado:
            continue
        if p.valor > 1000:
            total += p.valor * 0.90
        elif p.valor > 500:
            total += p.valor * 0.95
        else:
            total += p.valor
    return total
'''),
    ],
)

banco.assercao(
    'medio',
    'A taxa de defeitos escapados dessa equipe é de aproximadamente 11%.',
    'A taxa de defeitos escapados é o percentual de defeitos encontrados em produção sobre o total de defeitos encontrados.',
    3,
    'A II é a definição correta da métrica. Pela própria definição, a I é falsa: o total de defeitos é 90 + 10 = 100, '
    'e os 10 encontrados em produção correspondem a 10%. O valor de 11% aparece quando se divide 10 por 90, '
    'ou seja, pelos defeitos internos em vez do total.',
    contexto=[p('Em um semestre, a equipe de um aplicativo de delivery encontrou 90 defeitos durante os testes internos. '
                'No mesmo período, os usuários relataram mais 10 defeitos no aplicativo já publicado.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.afirmativas(
    'dificil',
    [
        ('Os gastos com o atendimento emergencial, a devolução de valores e o desgaste com o Procon são custos de '
         'falha externa, a categoria mais cara do Custo da Qualidade.', True),
        ('A medida 1 é uma ação de Garantia da Qualidade (QA), de caráter preventivo, e ataca a origem do problema: '
         'um defeito de requisito custa bem menos para corrigir quando é detectado na própria fase de requisitos.', True),
        ('A medida 2 tende a elevar a qualidade de forma confiável, pois 100% de cobertura de testes assegura que '
         'defeitos como o do cálculo de juros sejam encontrados antes da entrega.', False),
        ('A medida 3 está alinhada à cultura DevOps, pois um post-mortem com responsabilização individual incentiva '
         'a equipe a relatar falhas com transparência.', False),
    ],
    'I é verdadeira: o defeito chegou ao cliente, por isso os custos são de falha externa. '
    'II é verdadeira: treinamento e revisão de requisitos melhoram o processo (QA), e pela Regra dos 10x o defeito '
    'corrigido nos requisitos custa 1x, contra 100x ou mais em produção. '
    'III é falsa: alta cobertura não garante ausência de defeitos, e transformar a cobertura em meta premiada leva a '
    'testes sem valor, só para bater o número (Lei de Goodhart). '
    'IV é falsa: a cultura DevOps adota o post-mortem blameless, sem culpados; punir pessoas faz a equipe esconder falhas.',
    contexto=[
        p('Uma fintech lançou uma atualização do seu aplicativo de empréstimos. Duas semanas depois, descobriu que o '
          'cálculo de juros estava errado, e centenas de clientes foram cobrados a mais. A equipe de suporte trabalhou '
          'em regime emergencial, a empresa precisou devolver valores e foi notificada pelo Procon. A investigação '
          'mostrou que o erro vinha de um requisito ambíguo, escrito ainda no início do projeto.'),
        p('Para evitar novos casos, a diretoria propôs três medidas: (1) treinar a equipe em engenharia de requisitos e '
          'revisar os critérios de aceitação com o cliente antes do desenvolvimento; (2) dar um bônus à equipe que '
          'atingir 100% de cobertura de testes no próximo trimestre; (3) fazer um post-mortem do incidente para '
          'identificar o culpado e aplicar uma advertência formal.'),
    ],
)

banco.assercao(
    'dificil',
    'Depois que a velocity passou a ser usada para comparar e premiar as equipes, ela tende a perder o valor '
    'como indicador da capacidade de entrega de cada equipe.',
    'A velocity mede o tempo desde a solicitação do cliente até a entrega em produção, o que a torna sensível '
    'a atrasos causados fora da equipe.',
    2,
    'A I é verdadeira: é a Lei de Goodhart ("quando uma medida se torna uma meta, ela deixa de ser uma boa medida"). '
    'Com prêmio em jogo, as equipes passam a inflar as estimativas ou a quebrar as histórias em pedaços artificialmente pequenos, '
    'e os pontos deixam de refletir o que é entregue. A II é falsa: velocity é a quantidade de pontos entregues por sprint; '
    'o tempo da solicitação até a entrega em produção é o Lead Time.',
    contexto=[p('Uma empresa com cinco equipes ágeis criou um ranking mensal pela velocity de cada equipe, com bônus '
                'para as duas primeiras colocadas. Três meses depois, a velocity de todas as equipes havia dobrado, '
                'mas a quantidade de funcionalidades entregues aos clientes continuava a mesma.')],
)

banco.multipla(
    'dificil',
    'Sobre os modelos de maturidade e a situação dessa empresa, assinale a alternativa INCORRETA.',
    'Por ser de pequeno porte, a empresa pode adotar o MPS.BR, cuja escala de sete níveis começa no nível A, '
    'o de menor maturidade, e termina no nível G, o de maior maturidade.',
    [
        'A dependência de dois desenvolvedores experientes para que os projetos deem certo é típica do nível 1 '
        '(Inicial) do CMMI.',
        'O MPS.BR, desenvolvido pela SOFTEX, é um modelo nacional equivalente ao CMMI, adaptado a empresas de pequeno '
        'e médio porte e reconhecido em licitações públicas de TI no Brasil.',
        'Para chegar ao nível 3 (Definido) do CMMI, a empresa precisa ter processos padronizados para toda a '
        'organização, e não apenas regras que cada projeto define por conta própria.',
        'No nível 4 (Gerenciado Quantitativamente) do CMMI, o processo passa a ser medido e controlado estatisticamente.',
    ],
    'A afirmação incorreta é a da escala do MPS.BR: os sete níveis vão de G, o menos maduro, até A, o mais maduro, '
    'e não o contrário. As demais estão corretas: depender de "heróis" caracteriza o nível 1 do CMMI; o MPS.BR é o '
    'modelo nacional da SOFTEX, voltado a pequenas e médias empresas; o nível 3 exige processos padronizados para toda '
    'a organização; e o nível 4 mede e controla o processo estatisticamente.',
    contexto=[p('Uma empresa brasileira de software com 15 funcionários quer participar de licitações públicas de TI. '
                'Hoje, cada projeto é conduzido do jeito que o gerente da vez prefere, e as entregas só saem no prazo '
                'quando dois desenvolvedores mais experientes assumem o trabalho nos momentos críticos.')],
)

banco.multipla(
    'dificil',
    'A análise correta dessa situação é:',
    'Trata-se de débito técnico: as decisões tomadas para ganhar velocidade geraram um custo futuro que cresce como '
    'juros e deve ser pago aos poucos, com refatoração e testes.',
    [
        'Trata-se de um custo de falha externa, pois os problemas apareceram depois do lançamento; por isso, '
        'a solução é reforçar a equipe de suporte ao cliente.',
        'A lentidão é natural em todo software que cresce e não tem relação com as decisões anteriores; '
        'por isso, a equipe deve apenas aumentar o prazo das próximas entregas.',
        'Débito técnico só existe quando há defeitos em produção; como os problemas estão no desenvolvimento, '
        'o conceito não se aplica a essa situação.',
        'A melhor saída é aumentar a meta de velocity das sprints, para compensar o tempo perdido com as correções.',
    ],
    'Débito técnico é o custo futuro do trabalho extra causado por decisões técnicas inadequadas tomadas para ganhar '
    'velocidade. Como uma dívida financeira, ele acumula juros: cada funcionalidade nova fica mais lenta e cada '
    'correção quebra outra parte. A lentidão não é natural, é consequência das escolhas feitas no lançamento. '
    'O débito não depende de defeitos em produção, e aumentar a meta de velocity só pioraria o quadro (Lei de Goodhart).',
    contexto=[p('Para lançar um aplicativo antes da concorrência, uma startup suspendeu as revisões de código e deixou '
                'de escrever testes automatizados, com a promessa de "arrumar depois". Seis meses após o lançamento, '
                'cada nova funcionalidade leva o dobro do tempo para ficar pronta, e quase toda correção de defeito '
                'quebra alguma outra parte do sistema.')],
)

banco.afirmativas(
    'dificil',
    [
        ('Com a Integração Contínua, um defeito pode ser detectado poucos minutos depois de ser introduzido, '
         'quando a correção ainda é barata.', True),
        ('Como os testes passaram a ser automatizados, a responsabilidade pela qualidade fica concentrada na equipe '
         'de QA, o que libera os desenvolvedores para cuidar apenas de novas funcionalidades.', False),
        ('Na Entrega Contínua, o pipeline é mantido sempre pronto para implantação, mas a decisão de publicar em '
         'produção pode continuar sendo tomada por uma pessoa.', True),
    ],
    'I é verdadeira: os testes rodam a cada commit, e o defeito é encontrado logo depois de criado, ainda na '
    'implementação, quando corrigir é muito mais barato do que em produção (Regra dos 10x). '
    'II é falsa: em uma cultura DevOps madura, a qualidade não é responsabilidade de um departamento isolado, '
    'e sim de toda a cadeia de entrega. '
    'III é verdadeira: a Entrega Contínua garante que o código esteja sempre em condições de ser implantado; '
    'publicar sem nenhuma aprovação humana já é a Implantação Contínua.',
    contexto=[p('Uma empresa de comércio eletrônico reorganizou o seu processo de entrega. Agora, a cada commit, '
                'um pipeline compila o sistema e executa os testes automatizados; o código da branch principal fica '
                'sempre pronto para ser implantado; e a liberação para os clientes é feita quando o gerente de produto '
                'aprova a publicação.')],
)


# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"Cease dependence on inspection to achieve quality. Eliminate the need for inspection on a mass basis '
                   'by building quality into the product in the first place."',
        'traducao': '(Tradução livre: "Deixe de depender da inspeção para alcançar a qualidade. Elimine a necessidade de '
                    'inspeção em massa construindo a qualidade no produto desde o início.")',
        'fonte': 'DEMING, W. E. Out of the Crisis. Cambridge: MIT Press, 1986.',
    },
    [
        'Uma empresa desenvolve um sistema de agendamento para hospitais. Ao fim de cada versão, uma equipe de oito '
        'testadores passa três semanas testando o sistema antes da entrega. Mesmo assim, os hospitais continuam '
        'encontrando muitos defeitos depois da implantação. Um levantamento mostrou que a maior parte desses defeitos '
        'nasceu de requisitos mal compreendidos, ainda no início de cada versão.',
        'Para resolver o problema, o diretor de tecnologia propôs dobrar a equipe de testes e estender a fase de testes '
        'de três para seis semanas.',
    ],
    'Com base no texto de Deming e no caso apresentado, avalie se a proposta do diretor é a melhor estratégia para '
    'melhorar a qualidade do sistema, justificando a sua resposta com os conceitos do capítulo.',
    'A proposta não é a melhor estratégia. Dobrar os testadores e alongar a fase de testes reforça apenas o Controle de '
    'Qualidade (QC): uma ação reativa, orientada ao produto, que encontra defeitos depois que eles já foram criados. '
    'É exatamente a "dependência da inspeção" que Deming critica, e no Custo da Qualidade isso aumenta os gastos com '
    'avaliação e falha interna sem atacar a causa. Como os defeitos nascem nos requisitos, cada um deles atravessa design '
    'e implementação antes de ser encontrado; pela Regra dos 10x, o defeito que custaria 1x para corrigir nos requisitos '
    'custa 20x nos testes e 100x ou mais em produção, onde se torna falha externa. O caminho indicado é investir em '
    'Garantia da Qualidade (QA), que é proativa e orientada ao processo: revisar os requisitos e os critérios de aceitação '
    'com o hospital antes do desenvolvimento, treinar a equipe, adotar revisão de código e testes automatizados desde o '
    'início, com integração contínua. Os testes continuam necessários, pois QA sem QC nunca verifica o resultado, mas '
    'não podem ser a única forma de buscar qualidade.',
)

banco.discursiva(
    'dificil',
    {
        'citacao': '"When a measure becomes a target, it ceases to be a good measure."',
        'traducao': '(Tradução livre: "Quando uma medida se torna uma meta, ela deixa de ser uma boa medida.")',
        'fonte': 'STRATHERN, M. "Improving ratings": audit in the British University system. European Review, '
                 'v. 5, n. 3, p. 305-321, 1997. Formulação conhecida como Lei de Goodhart.',
    },
    [
        'Para melhorar a qualidade dos seus sistemas, a gerência de uma empresa de software determinou que nenhum pull '
        'request seria aprovado com cobertura de testes abaixo de 90% e criou um bônus trimestral para as equipes que '
        'mantivessem a maior cobertura.',
        'Três meses depois, a cobertura média subiu de 55% para 93%, mas a taxa de defeitos escapados continuou a mesma. '
        'Uma revisão por amostragem mostrou que muitos dos testes novos executavam o código, mas não verificavam se o '
        'resultado estava correto.',
    ],
    'Com base no texto e no caso apresentado, explique por que a meta de cobertura não trouxe a melhoria de qualidade '
    'esperada pela gerência.',
    'A cobertura de testes mede apenas quanto do código foi executado pelos testes, e não se os testes verificam o '
    'comportamento correto; por isso, alta cobertura não garante ausência de defeitos. Ao transformar a cobertura em '
    'meta obrigatória e premiada, a gerência criou o efeito descrito pela Lei de Goodhart: as equipes passaram a '
    'otimizar o número, e não a qualidade, escrevendo testes sem valor, sem verificações, só para "passar pelo" código. '
    'A métrica subiu, mas deixou de representar o que deveria medir, e a prova disso é a taxa de defeitos escapados, '
    'que mostra o que de fato chega ao cliente e não mudou. As métricas devem ser usadas para entender e melhorar o '
    'processo, não para pressionar ou premiar; a cobertura funciona melhor como indicador acompanhado junto com outras '
    'métricas, como a taxa de defeitos escapados e a densidade de defeitos, e apoiado por revisão de código que avalie '
    'a qualidade dos próprios testes.',
)


if __name__ == '__main__':
    banco.gravar()
