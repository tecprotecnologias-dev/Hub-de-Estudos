"""
Questões médias e difíceis do capítulo 5 (Estratégias de Teste) de Qualidade e Testes de Software:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/qualidade_cap5_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap5-o* e
qualidade-cap5-d*; as que já existiam (q* e m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import QUALIDADE, Banco, p

banco = Banco('qualidade-cap5', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As condições 1, 2 e 3 do plano são, respectivamente, critérios de',
    'entrada, saída e suspensão.',
    [
        'saída, entrada e suspensão.',
        'entrada, suspensão e saída.',
        'suspensão, saída e entrada.',
        'entrada, saída e aprovação.',
    ],
    'Os critérios de entrada são as pré-condições para começar os testes, como um build estável e o ambiente configurado '
    '(1). Os de saída são as condições para encerrá-los, como a cobertura atingida e nenhum defeito crítico aberto (2). Os '
    'de suspensão dizem quando pausar, como uma taxa de defeitos muito alta ou um ambiente instável (3).',
    contexto=[p('O plano de teste de um sistema de matrículas traz três condições: '
                '(1) os testes só começam com um build estável e o ambiente de homologação configurado; '
                '(2) os testes terminam quando a cobertura combinada for atingida e não houver nenhum defeito crítico '
                'aberto; '
                '(3) os testes param se a taxa de defeitos ficar muito alta ou se o ambiente ficar instável.')],
)

banco.multipla(
    'medio',
    'Em qual componente do plano de teste a equipe deve registrar essa decisão?',
    'Em "Funcionalidades excluídas", deixando explícito o que não será testado e a justificativa.',
    [
        'Em "Riscos e contingências", pois todo módulo sem teste é um risco que precisa de um plano B.',
        'Em "Critérios de suspensão", pois o módulo será desligado e os testes dele ficam suspensos.',
        'Em lugar nenhum, pois o plano só registra o que será testado, e não o que fica de fora dele.',
        'Em "Itens a serem testados", com a observação de que o módulo será testado só se sobrar tempo.',
    ],
    'Pela IEEE 829, o plano de teste tem um componente para as funcionalidades excluídas: a explicitação do que não será '
    'testado e por quê. O exemplo da própria apostila é um módulo legado de exportação CSV que será descontinuado na '
    'próxima versão. Deixar a exclusão por escrito evita mal-entendidos sobre o escopo, e o critério de suspensão trata de '
    'pausar os testes em andamento, e não de excluir um módulo.',
    contexto=[p('Ao planejar os testes da nova versão de um sistema de vendas, a equipe decidiu não testar o antigo módulo '
                'de exportação em CSV, porque ele será retirado do sistema na versão seguinte.')],
)

banco.afirmativas(
    'medio',
    [
        ('O Relatório de Log de Teste (Test Log) registra, em ordem, o que aconteceu durante a execução dos testes.', True),
        ('O Relatório de Incidente de Teste (Test Incident Report) registra os eventos que exigem investigação.', True),
        ('O Relatório de Resumo de Teste (Test Summary Report) é escrito antes da execução, para planejar os testes.',
         False),
        ('O Plano de Teste (Test Plan) também é um dos documentos definidos pela norma.', True),
    ],
    'A IEEE 829 (atualizada pela IEEE 29119) define o plano de teste, as especificações de design, de caso e de '
    'procedimento de teste, e três relatórios: o log, que registra a execução (I, verdadeira); o relatório de incidente, '
    'que registra o que precisa ser investigado (II, verdadeira); e o relatório de resumo, que consolida os resultados ao '
    'final, e não antes da execução (III, falsa). O plano de teste é um desses documentos (IV, verdadeira).',
    contexto=[p('Uma equipe vai organizar a documentação dos testes de acordo com a IEEE 829.')],
)

banco.multipla(
    'medio',
    'As técnicas de caixa preta mais adequadas aos contextos 1, 2, 3 e 4 são, respectivamente,',
    'teste exploratório, teste de contrato de interface, teste de caso de uso e testes de compatibilidade e usabilidade.',
    [
        'teste de contrato de interface, teste exploratório, teste de caso de uso e testes de compatibilidade e '
        'usabilidade.',
        'teste exploratório, teste de caso de uso, teste de contrato de interface e testes de compatibilidade e '
        'usabilidade.',
        'tabela de decisão, teste de contrato de interface, teste de caso de uso e testes de compatibilidade e '
        'usabilidade.',
        'teste exploratório, teste de contrato de interface, tabela de decisão e particionamento de equivalência.',
    ],
    'Pela tabela de escolha guiada por contexto da apostila: em sistemas novos sem documentação completa, o teste '
    'exploratório usa intuição e experiência (1); em APIs, o teste de contrato de interface valida respostas, códigos de '
    'status e payloads (2); em fluxos de trabalho do usuário, o teste de caso de uso valida o sistema do ponto de vista '
    'de quem o usa (3); e em interfaces web e mobile, os testes de compatibilidade e usabilidade verificam navegadores e '
    'dispositivos (4).',
    contexto=[p('Uma equipe tem quatro alvos de teste: (1) um sistema novo, quase sem documentação; (2) uma API REST usada '
                'por outros sistemas; (3) o fluxo completo de um cliente, da busca ao pagamento; (4) um site que precisa '
                'funcionar bem em vários navegadores e celulares.')],
)

banco.assercao(
    'medio',
    'Uma suíte com 90% de cobertura de desvios pode, mesmo assim, ter pouca capacidade de detectar defeitos.',
    'A análise de mutação avalia a qualidade dos testes introduzindo pequenas mudanças no código e verificando se os '
    'testes percebem essas mudanças.',
    1,
    'As duas são verdadeiras, mas a II não explica a I. A I é verdadeira porque a cobertura mostra quais trechos foram '
    'executados, e não se os testes verificam o resultado: testes sem boas asserções passam por tudo sem detectar nada. '
    'A II também é verdadeira e descreve uma ferramenta para medir esse problema (o mutation score), mas não é a causa '
    'dele.',
    contexto=[p('Uma equipe atingiu 90% de cobertura de desvios, mas os defeitos continuam chegando à produção. Um '
                'consultor sugeriu usar a análise de mutação, com ferramentas como Pitest ou mutmut.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Pela Matriz de Priorização da apostila, as funcionalidades 1, 2, 3 e 4 devem receber, respectivamente,',
    'teste prioritário e exaustivo, teste normal, teste normal e teste superficial ou omitido.',
    [
        'teste prioritário e exaustivo, teste normal, teste superficial ou omitido e teste superficial ou omitido.',
        'teste prioritário e exaustivo, teste prioritário e exaustivo, teste normal e teste superficial ou omitido.',
        'teste normal, teste normal, teste superficial ou omitido e teste superficial ou omitido.',
        'teste prioritário e exaustivo, teste normal, teste prioritário e exaustivo e teste superficial ou omitido.',
    ],
    'A prioridade é a probabilidade vezes o impacto: 3 × 3 = 9 (1); 2 × 2 = 4 (2); 1 × 3 = 3 (3); e 1 × 2 = 2 (4). '
    'Pontuação de 6 a 9 pede teste prioritário e exaustivo; de 3 a 4, teste normal; e de 1 a 2, teste superficial ou '
    'omitido. A funcionalidade 3 tem impacto alto, mas a probabilidade baixa leva a pontuação para 3, o que a mantém na '
    'faixa do teste normal.',
    contexto=[p('Na análise de risco de um sistema, a equipe atribuiu probabilidade de falha e impacto no negócio (de 1 a 3) '
                'a quatro funcionalidades: '
                '(1) pagamento: probabilidade 3 e impacto 3; '
                '(2) busca de produtos: probabilidade 2 e impacto 2; '
                '(3) emissão de nota fiscal: probabilidade 1 e impacto 3; '
                '(4) troca do tema de cores: probabilidade 1 e impacto 2.')],
)

banco.afirmativas(
    'dificil',
    [
        ('Na caixa cinza, o testador tem conhecimento parcial da estrutura interna, o que é comum nos testes de integração '
         'e de API.', True),
        ('Na estratégia, a caixa branca é aplicada principalmente nos testes de aceitação, por quem conhece o negócio.',
         False),
        ('A caixa preta não pode ser usada em testes de desempenho, pois esses testes exigem acesso ao código-fonte.',
         False),
        ('No nível de integração, a cobertura de caminhos nos pontos de integração é o critério recomendado para a caixa '
         'branca.', True),
    ],
    'I é verdadeira: é a definição de caixa cinza da apostila. II é falsa: a caixa branca é aplicada prioritariamente nos '
    'níveis mais baixos da pirâmide, como o unitário, em que há acesso direto ao código; a aceitação usa caixa preta. III '
    'é falsa: os testes de desempenho (carga, estresse e volume) aparecem como aplicação da caixa preta, feitos sem acesso '
    'ao código. IV é verdadeira: é o critério da tabela de caixa branca por nível.',
    contexto=[p('Ao montar a estratégia de testes de um sistema de logística, a equipe discutiu onde usar caixa branca, '
                'caixa preta e caixa cinza.')],
)

banco.assercao(
    'dificil',
    'No ATDD, os testes de aceitação são definidos antes do desenvolvimento e guiam tanto a implementação quanto os '
    'testes unitários.',
    'No ATDD, os testes de aceitação são escritos apenas pelo testador, depois que o código já está pronto.',
    2,
    'A I é verdadeira: é a definição de ATDD da apostila, que combina BDD e TDD. A II é falsa por dois motivos: os testes '
    'de aceitação vêm antes do código, e não depois; e eles são definidos em conjunto, aproximando o negócio, quem '
    'desenvolve e quem testa. Escrever os testes depois do código é o que essas práticas procuram evitar.',
    contexto=[p('Uma equipe ágil quer que o entendimento sobre o que o cliente espera de cada história esteja claro antes '
                'de qualquer linha de código, e decidiu adotar o ATDD.')],
)

banco.multipla(
    'dificil',
    'A ordem correta das etapas do planejamento estratégico de testes é:',
    'análise de requisitos e escopo; análise de riscos; níveis e tipos de teste; técnicas; critérios de qualidade; '
    'recursos e ferramentas; cronograma.',
    [
        'cronograma; recursos e ferramentas; análise de requisitos e escopo; análise de riscos; níveis e tipos de teste; '
        'técnicas; critérios.',
        'análise de riscos; análise de requisitos e escopo; técnicas; níveis e tipos de teste; cronograma; critérios; '
        'recursos e ferramentas.',
        'análise de requisitos e escopo; níveis e tipos de teste; técnicas; cronograma; análise de riscos; critérios; '
        'recursos e ferramentas.',
        'recursos e ferramentas; técnicas; análise de requisitos e escopo; análise de riscos; critérios; níveis e tipos; '
        'cronograma.',
    ],
    'A apostila organiza o planejamento em sete passos: primeiro entender o que deve ser testado (requisitos e escopo); '
    'depois, onde estão os maiores riscos; com isso, definir os níveis e tipos de teste e escolher as técnicas; '
    'estabelecer os critérios de entrada, saída e suspensão; planejar os recursos e as ferramentas; e, por fim, montar o '
    'cronograma, alinhado ao do desenvolvimento. Começar pelo cronograma ou pelos recursos, sem conhecer o escopo e os '
    'riscos, inverte a lógica.',
    contexto=[p('Uma test lead vai planejar a estratégia de testes de um novo sistema e precisa organizar as etapas do '
                'trabalho na ordem proposta pela apostila.')],
)

banco.multipla(
    'dificil',
    'Sobre as estratégias de teste em contextos ágeis, assinale a alternativa INCORRETA.',
    'No teste em sprints, a história é considerada pronta quando o código termina, e os testes dela ficam para a sprint '
    'seguinte.',
    [
        'No Shift-Left, os testadores participam do refinamento das histórias e escrevem os critérios de aceitação antes do '
        'código.',
        'O TDD, com o teste unitário escrito antes do código, garante cobertura de caixa branca e um design fácil de '
        'testar.',
        'No BDD, os critérios de aceitação escritos com Dado/Quando/Então servem de base para os testes de caixa preta.',
        'Um quality gate no pipeline bloqueia o merge quando o código novo não atinge a cobertura mínima definida.',
    ],
    'A afirmação incorreta é a do teste em sprints: pela apostila, cada história só é considerada pronta (Definition of '
    'Done) quando todos os testes planejados, unitários, de integração e de aceitação, estão passando. Deixar os testes '
    'para depois é o que o modelo ágil procura evitar. As demais alternativas descrevem corretamente o Shift-Left, o '
    'TDD, o BDD e o quality gate.',
    contexto=[p('Uma empresa que testava tudo no fim do projeto vai adotar Scrum, e a equipe reuniu algumas afirmações '
                'sobre como os testes passam a funcionar.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Um banco digital vai lançar, em três meses, um aplicativo com abertura de conta, transferências por Pix, '
        'pagamento de boletos e um painel com o histórico de gastos. A equipe de qualidade tem só dois testadores, e o '
        'desenvolvimento é feito em sprints de duas semanas. Nos projetos anteriores, os testes eram feitos todos no fim, '
        'sem um planejamento formal, e muitos defeitos chegaram aos clientes.',
    ],
    'Proponha, em linhas gerais, uma estratégia de teste para esse projeto, justificando as principais escolhas com base '
    'no capítulo.',
    'A estratégia deveria começar pela análise de requisitos e escopo, deixando claro o que está dentro e fora dos testes '
    'e as exigências regulatórias, como a LGPD. Depois, a análise de riscos, com a Matriz de Priorização: transferências '
    'por Pix, pagamentos e abertura de conta têm probabilidade e impacto altos e recebem teste prioritário e exaustivo; o '
    'painel de gastos, teste normal. Com poucos testadores, a priorização por risco é essencial. Os níveis seriam '
    'unitário, integração, sistema e aceitação, com testes de segurança e de desempenho. Nas técnicas, caixa branca nos '
    'unitários, com cobertura de desvios alta nos módulos críticos (cobertura progressiva); caixa cinza na integração e '
    'nas APIs; e caixa preta no sistema e na aceitação, com particionamento de equivalência e valor limite nos valores das '
    'transferências e tabela de decisão nas regras de tarifa. Em contexto ágil, o teste deixa de ficar para o fim: '
    'Shift-Left, com critérios de aceitação em BDD antes do código, TDD nos desenvolvedores, testes de cada história '
    'dentro da Definition of Done e automação no pipeline, com quality gates. Por fim, critérios de entrada, saída e '
    'suspensão definidos no plano, e um cronograma alinhado às sprints, com tempo para a regressão antes do lançamento.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'O plano de teste de um sistema de folha de pagamento tem apenas duas frases: "Testar todas as funcionalidades do '
        'sistema" e "Os testes serão feitos pela equipe de QA". Durante o projeto, a equipe não sabia se o módulo antigo de '
        'relatórios devia ser testado, discutiu por dias se o sistema estava pronto para o lançamento e, quando o ambiente '
        'de testes caiu por uma semana, ninguém tinha previsto o que fazer.',
    ],
    'Com base nos componentes do plano de teste definidos pela IEEE 829, explique quais elementos faltam nesse plano e '
    'como eles teriam evitado os problemas relatados.',
    'Faltam vários componentes da IEEE 829. "Testar todas as funcionalidades" não define os itens a serem testados nem '
    'as funcionalidades excluídas; com essas duas seções, o módulo antigo de relatórios estaria explicitamente dentro ou '
    'fora do escopo, com a justificativa. A discussão sobre o lançamento vem da falta de critérios de aprovação, como '
    '"nenhum defeito crítico aberto e cobertura de desvios de pelo menos 80%", que dariam uma resposta objetiva para a '
    'pergunta "está pronto?". A queda do ambiente mostra a falta de riscos e contingências (por exemplo, testar em um '
    'ambiente local com integrações simuladas) e de critérios de suspensão e retomada. "A equipe de QA" não define as '
    'responsabilidades de cada pessoa. Também faltam o identificador do plano, a introdução e os objetivos, a abordagem '
    'de teste (técnicas, níveis e tipos), os entregáveis, a descrição do ambiente de teste e a estimativa e o cronograma. '
    'Com esses elementos, as decisões teriam sido tomadas antes, e não no meio dos problemas.',
)


if __name__ == '__main__':
    banco.gravar()
