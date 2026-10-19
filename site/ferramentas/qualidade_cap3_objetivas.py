"""
Questões médias e difíceis do capítulo 3 (Modelos de Maturidade do Software) de Qualidade e Testes de
Software: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um
único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/qualidade_cap3_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap3-o* e
qualidade-cap3-d*; as que já existiam (q* e m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import QUALIDADE, Banco, p

banco = Banco('qualidade-cap3', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Qual alternativa relaciona corretamente os nomes dos níveis 2 e 5 no CMM e no CMMI (representação por estágios)?',
    'Nível 2: Repetível (CMM) e Gerenciado (CMMI); nível 5: Otimizado (CMM) e Em Otimização (CMMI).',
    [
        'Nível 2: Gerenciado (CMM) e Repetível (CMMI); nível 5: Em Otimização (CMM) e Otimizado (CMMI).',
        'Nível 2: Definido (CMM) e Gerenciado (CMMI); nível 5: Otimizado (CMM) e Em Otimização (CMMI).',
        'Nível 2: Repetível nos dois; nível 5: Gerenciado Quantitativamente (CMM) e Em Otimização (CMMI).',
        'Nível 2: Repetível (CMM) e Gerenciado (CMMI); nível 5: Inicial (CMM) e Em Otimização (CMMI).',
    ],
    'Pelas tabelas da apostila, os níveis do CMM são Inicial, Repetível, Definido, Gerenciado e Otimizado; os do CMMI, '
    'Inicial, Gerenciado, Definido, Gerenciado Quantitativamente e Em Otimização. O nível 2 se chama Repetível no CMM e '
    'Gerenciado no CMMI, e o nível 5, Otimizado no CMM e Em Otimização no CMMI. Atenção: "Gerenciado" é o nível 4 do CMM, '
    'mas o nível 2 do CMMI.',
    contexto=[p('Ao comparar os dois modelos do SEI, uma aluna percebeu que alguns níveis mudaram de nome do CMM para o '
                'CMMI.')],
)

banco.afirmativas(
    'medio',
    [
        ('O CMM foi descontinuado e substituído pelo CMMI.', True),
        ('O MPS.BR tem sete níveis, do G, o mais alto, ao A, o mais baixo.', False),
        ('O CMMI tem como escopo apenas os processos de software.', False),
        ('O custo de avaliação do MPS.BR é classificado como médio ou baixo, enquanto o do CMMI é alto.', True),
    ],
    'I é verdadeira: pela tabela comparativa, a situação atual do CMM é "descontinuado (substituído pelo CMMI)". II é '
    'falsa: os níveis vão do G, o mais baixo, ao A, o mais alto. III é falsa: o escopo do CMMI inclui software, sistemas, '
    'serviços e aquisição; apenas software era o escopo do CMM. IV é verdadeira: é um dos motivos pelos quais o MPS.BR é '
    'voltado às micro, pequenas e médias empresas.',
    contexto=[p('Para um seminário, um grupo preparou uma tabela comparando o CMM, o CMMI e o MPS.BR.')],
)

banco.multipla(
    'medio',
    'Os focos 1, 2, 3 e 4 correspondem, respectivamente, aos níveis do MPS.BR',
    'G, F, C e A.',
    [
        'G, F, B e A.',
        'F, G, C e A.',
        'G, E, C e A.',
        'G, F, C e B.',
    ],
    'Pela tabela da apostila: o nível G (Parcialmente Gerenciado) trata da gerência de projetos e de requisitos (1); o F '
    '(Gerenciado), da gerência de configuração, da aquisição e da medição (2); o C (Definido), da gerência de riscos e '
    'das decisões (3); e o A (Em Otimização), da inovação e da análise de causas de problemas (4). O B trata do desempenho '
    'quantitativo dos processos.',
    contexto=[p('Uma consultora explicou o foco de quatro níveis do MPS.BR: '
                '(1) gerência básica de projetos e de requisitos; '
                '(2) gerência de configuração, aquisição e medição; '
                '(3) gerência de riscos e de decisões; '
                '(4) inovação e análise das causas de problemas.')],
)

banco.assercao(
    'medio',
    'Na representação contínua do CMMI, a organização recebe um nível de capacidade para cada área de processo, '
    'em uma escala de 0 a 3.',
    'A representação contínua avalia a capacidade de cada área de processo individualmente.',
    0,
    'As duas são verdadeiras, e a II explica a I. Como cada área de processo é avaliada separadamente, o resultado não é '
    'um único número para a organização, mas um nível de capacidade (CL 0 a 3) para cada área. Na representação por '
    'estágios, a organização recebe um nível de maturidade geral (ML 1 a 5).',
    contexto=[p('Depois de uma avaliação pela representação contínua do CMMI, uma empresa recebeu o seu resultado e '
                'estranhou não ter um "nível do CMMI" único para mostrar aos clientes.')],
)

banco.multipla(
    'medio',
    'Qual alternativa descreve corretamente mudanças trazidas pelo CMMI v2.0, de 2018?',
    'Linguagem mais simples, ênfase no desempenho de negócio, integração com o ágil e foco em segurança cibernética.',
    [
        'Retirada da representação por estágios, que deixou de existir, e volta ao foco exclusivo em processos de software.',
        'Aumento do número de níveis de maturidade de cinco para sete, para ficar compatível com o modelo brasileiro '
        'MPS.BR.',
        'Passagem da administração do modelo do ISACA para o SEI, que voltou a ser o responsável pelo CMMI.',
        'Proibição de práticas ágeis, como Scrum e Kanban, nas organizações que buscam os níveis 4 e 5 do modelo.',
    ],
    'Pela apostila, o CMMI v2.0 simplificou a linguagem e a estrutura, deu mais ênfase ao desempenho de negócio, e não só '
    'à maturidade do processo, integrou de forma explícita práticas ágeis como Scrum, Kanban e SAFe, trouxe um novo foco '
    'em segurança cibernética e gestão de fornecedores e passou a administração do SEI para o ISACA, e não o contrário. '
    'Os cinco níveis foram mantidos.',
    contexto=[p('Uma empresa avaliada no CMMI 1.3 quer entender o que mudou na versão 2.0 antes de renovar a avaliação.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Pelas orientações da apostila, qual é a estratégia mais adequada para essa empresa?',
    'Combinar os dois: o MPS.BR para as licitações brasileiras e o CMMI para os clientes internacionais.',
    [
        'Adotar só o MPS.BR, pois ele é aceito também nos contratos internacionais como substituto direto do CMMI.',
        'Adotar só o CMMI, pois ele é o único modelo aceito nas licitações do governo federal brasileiro.',
        'Adotar só o CMM, pois ele é o modelo original e o mais reconhecido nos dois mercados.',
        'Não adotar nenhum modelo, pois os de maturidade só fazem sentido para empresas com mais de mil pessoas.',
    ],
    'A apostila indica o CMMI para quem atua em mercados internacionais ou busca prestígio global, o MPS.BR para quem '
    'participa de licitações do governo brasileiro ou busca um caminho gradual e mais barato, e a combinação dos dois para '
    'quem atua no mercado nacional e no internacional ao mesmo tempo, como essa empresa. A equivalência entre os níveis '
    'facilita usar os dois, e o CMM foi descontinuado.',
    contexto=[p('Uma empresa brasileira de software com 120 funcionários participa de licitações do governo federal e '
                'acabou de fechar os primeiros contratos com clientes dos Estados Unidos e da Europa, que pedem uma '
                'certificação de maturidade de prestígio global.')],
)

banco.afirmativas(
    'dificil',
    [
        ('A avaliação e a implementação do MPS.BR custam cerca de 5 a 10 vezes menos que as do CMMI.', True),
        ('O MPS.BR é compatível com as normas ISO/IEC 12207 e ISO/IEC 15504 (SPICE).', True),
        ('Uma empresa certificada no MPS.BR precisa recomeçar do zero se quiser obter o CMMI.', False),
        ('O MPS.BR é reconhecido pelo governo federal nos processos de licitação de TI.', True),
    ],
    'I, II e IV estão entre as vantagens do MPS.BR listadas na apostila, junto com o material em português e a progressão '
    'mais gradual em sete níveis. III é falsa: a apostila afirma o contrário, que as empresas certificadas no MPS.BR podem '
    'migrar para o CMMI com menor esforço adicional, e a equivalência entre os níveis facilita essa migração.',
    contexto=[p('Uma pequena empresa de Belo Horizonte avalia as vantagens de começar pelo MPS.BR.')],
)

banco.assercao(
    'dificil',
    'Organizações com processos maduros tendem a ter prazos e custos mais previsíveis.',
    'Em processos maduros, os resultados dependem do esforço heroico de algumas pessoas-chave.',
    2,
    'A I é verdadeira: a previsibilidade, com estimativas de prazo e custo mais precisas, é o primeiro benefício da '
    'maturidade citado na apostila, ao lado da consistência entre projetos. A II é falsa: depender de pessoas-chave é a '
    'marca do nível 1 (Inicial); nos processos maduros, a capacidade está na organização, e não em indivíduos.',
    contexto=[p('Uma empresa que acabou de chegar ao nível 3 do CMMI percebeu que as suas estimativas ficaram muito mais '
                'precisas e que os projetos passaram a ter resultados parecidos, qualquer que seja a equipe.')],
)

banco.multipla(
    'dificil',
    'Em que nível de maturidade do CMMI (representação por estágios) essa organização se encontra?',
    'Nível 3, Definido: os processos são padronizados para toda a organização, mas ainda não são controlados '
    'estatisticamente.',
    [
        'Nível 2, Gerenciado: cada projeto define os seus processos, planejados e controlados de forma básica.',
        'Nível 4, Gerenciado Quantitativamente: ter um conjunto padrão de processos já basta para chegar a esse nível.',
        'Nível 5, Em Otimização: os projetos adaptam o processo padrão, o que demonstra uma melhoria contínua.',
        'Nível 1, Inicial: a ausência de controle estatístico mostra que os processos ainda são caóticos.',
    ],
    'No nível 3 (Definido), os processos são caracterizados para toda a organização e padronizados, e os projetos os '
    'adaptam de um conjunto padrão, exatamente o caso. Para o nível 4, seria preciso usar dados quantitativos e '
    'estatísticos para gerenciar os processos, o que ainda não acontece. No nível 2, os processos são definidos por '
    'projeto, e não pela organização.',
    contexto=[p('Em uma empresa, todos os projetos seguem um processo padrão da organização, documentado e ensinado em '
                'treinamentos, e cada projeto o adapta às suas necessidades. A empresa coleta algumas métricas, mas ainda '
                'não usa dados estatísticos para controlar o desempenho dos processos.')],
)

banco.multipla(
    'dificil',
    'Sobre o MPS.BR e a sua equivalência com o CMMI, assinale a alternativa INCORRETA.',
    'O nível B do MPS.BR equivale ao nível 5 do CMMI, e o nível A equivale ao nível 4.',
    [
        'Os níveis G e F do MPS.BR equivalem, juntos, ao nível 2 do CMMI.',
        'Os níveis E, D e C do MPS.BR equivalem ao nível 3 do CMMI.',
        'O MPS.BR foi criado em 2003 pela SOFTEX, com apoio do Ministério da Ciência e Tecnologia e do BNDES.',
        'O nível D do MPS.BR inclui os processos de verificação e de validação do software.',
    ],
    'A afirmação incorreta inverte a equivalência dos níveis mais altos: o nível B do MPS.BR (Gerenciado '
    'Quantitativamente) corresponde ao nível 4 do CMMI, e o nível A (Em Otimização), ao nível 5. As demais alternativas '
    'estão corretas, de acordo com as tabelas de equivalência e de processos da apostila.',
    contexto=[p('Uma empresa certificada no MPS.BR quer entender como os seus níveis se relacionam com os do CMMI.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Uma software house brasileira, com 40 funcionários, quer participar de licitações de TI do governo federal e, '
        'em dois anos, começar a atender clientes nos Estados Unidos. Hoje, cada projeto é conduzido de um jeito, os '
        'requisitos mudam sem controle e o sucesso depende de três desenvolvedores muito experientes.',
    ],
    'Com base no capítulo, proponha uma estratégia de evolução da maturidade de processos para essa empresa, '
    'indicando o modelo ou os modelos mais adequados e por onde começar.',
    'A empresa está hoje no nível 1 (Inicial): processos imprevisíveis e sucesso dependente de pessoas-chave. Como é uma '
    'empresa brasileira de pequeno a médio porte que quer participar de licitações federais, o caminho mais adequado é '
    'começar pelo MPS.BR, que é mais barato (cerca de 5 a 10 vezes menos que o CMMI), está em português, é reconhecido '
    'nas licitações de TI do governo federal e permite evoluir em degraus menores. O primeiro passo seria o nível G, com '
    'gerência de requisitos, que resolve as mudanças sem controle, e gerência de projetos; depois, o nível F, com '
    'gerência de configuração, medição e garantia da qualidade. Com isso, a empresa passa a ter processos que não '
    'dependem só dos três desenvolvedores. Como os níveis G e F equivalem ao nível 2 do CMMI e o MPS.BR é compatível com '
    'ele, a empresa poderá migrar com menor esforço quando for atender os clientes dos Estados Unidos, combinando os dois '
    'modelos. A evolução deve ser gradual, sem pular níveis, consolidando cada etapa antes da seguinte.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Em uma reunião, o líder de uma equipe que usa Scrum afirmou: "Modelos de maturidade como o CMMI são burocracia de '
        'empresa grande. Somos ágeis, e agilidade não combina com níveis de maturidade."',
    ],
    'Com base no capítulo, avalie a afirmação do líder da equipe.',
    'A afirmação parte de uma visão antiga dos modelos de maturidade. O CMMI v2.0, de 2018, passou a integrar de forma '
    'explícita práticas ágeis como Scrum, Kanban e SAFe, simplificou a linguagem e a estrutura do modelo e deu mais ênfase '
    'ao desempenho de negócio, e não à documentação pela documentação. Maturidade e agilidade não se opõem: as práticas '
    'ágeis podem ser a forma de implementar o que o modelo pede, como planejar, monitorar, gerenciar requisitos e medir. '
    'Os benefícios da maturidade também valem para equipes ágeis: previsibilidade de prazos e custos, consistência entre '
    'equipes, melhoria contínua com base em dados, redução de riscos e competitividade em licitações e contratos. O MPS.BR, '
    'por sua vez, foi pensado justamente para empresas pequenas e médias, com um caminho gradual e de custo menor. O que '
    'a equipe deve evitar é aplicar o modelo de forma burocrática; o modelo em si não exige isso.',
)


if __name__ == '__main__':
    banco.gravar()
