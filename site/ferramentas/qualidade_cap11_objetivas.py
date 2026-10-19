"""
Questões médias e difíceis do capítulo 11 (Melhores Práticas de Teste e Garantia de Qualidade) de
Qualidade e Testes de Software: 10 objetivas no estilo de concursos públicos e exames nacionais e
2 discursivas com um único comando. As funções comuns ficam em engsoft_questoes.py.
Uso (dentro de site/):

    python ferramentas/qualidade_cap11_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap11-o* e
qualidade-cap11-d*; as que já existiam (m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import QUALIDADE, Banco, p

banco = Banco('qualidade-cap11', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As atividades 1, 2 e 3 são, respectivamente, de',
    'Garantia de Qualidade (QA), Controle de Qualidade (QC) e Teste.',
    [
        'Controle de Qualidade (QC), Garantia de Qualidade (QA) e Teste.',
        'Garantia de Qualidade (QA), Teste e Controle de Qualidade (QC).',
        'Teste, Controle de Qualidade (QC) e Garantia de Qualidade (QA).',
        'Garantia de Qualidade (QA) nas três, pois todas melhoram a qualidade.',
    ],
    'A QA é orientada ao processo e preventiva: auditar e revisar a forma de trabalhar é QA (1). O QC é orientado ao '
    'produto e detectivo: inspecionar o produto e revisar o código é QC (2). O Teste também é detectivo e voltado ao '
    'produto, e o seu exemplo típico é a execução de casos de teste (3). Os três exemplos estão na tabela da apostila.',
    contexto=[p('Em uma empresa: (1) uma auditoria revisa se o processo de desenvolvimento está sendo seguido e onde ele '
                'pode melhorar; (2) a equipe inspeciona o produto e revisa o código antes da entrega; (3) os testadores '
                'executam os casos de teste da nova versão.')],
)

banco.multipla(
    'medio',
    'Nas situações 1, 2, 3 e 4, o QA atua, respectivamente, como',
    'consultor, automatizador, explorador e coach.',
    [
        'automatizador, consultor, explorador e coach.',
        'consultor, automatizador, analista de qualidade e coach.',
        'consultor, explorador, automatizador e analista de qualidade.',
        'coach, automatizador, explorador e consultor.',
    ],
    'Ajudar a definir critérios de aceitação e revisar a testabilidade é o papel de consultor (1). Liderar a estratégia '
    'de automação e definir frameworks e padrões é o de automatizador (2). Conduzir sessões exploratórias para achar o '
    'que os scripts não cobrem é o de explorador (3). Treinar e capacitar o time em práticas de qualidade é o de coach '
    '(4). O analista de qualidade coleta e interpreta métricas e comunica riscos.',
    contexto=[p('Em um time ágil, a profissional de QA: (1) ajuda o PO a escrever critérios de aceitação e revisa o '
                'design pensando em como testá-lo; (2) escolhe o framework de automação e define os padrões dos testes; '
                '(3) faz sessões livres de teste, simulando o comportamento de usuários reais; (4) dá oficinas para os '
                'desenvolvedores sobre como escrever bons testes.')],
)

banco.afirmativas(
    'medio',
    [
        ('Cada push no repositório dispara um build automatizado.', True),
        ('O retorno ao desenvolvedor pode levar até um dia, desde que seja completo.', False),
        ('O merge na branch principal pode ser feito com o build vermelho quando o prazo estiver apertado.', False),
        ('Os testes automatizados são executados a cada build.', True),
    ],
    'Entre os elementos essenciais de um pipeline de CI, a apostila lista o build automatizado a cada push (I, '
    'verdadeira) e os testes automatizados a cada build (IV, verdadeira). II é falsa: o retorno deve ser rápido, em menos '
    'de 10 minutos. III é falsa: o build verde é pré-requisito para o merge na branch principal.',
    contexto=[p('Uma equipe vai montar o seu primeiro pipeline de Integração Contínua e listou o que ele deve ter.')],
)

banco.assercao(
    'medio',
    'Organizar cada teste no padrão AAA (Arrange, Act, Assert) torna os testes mais fáceis de entender e de manter.',
    'O padrão AAA separa, em cada teste, a preparação do cenário, a ação testada e a verificação do resultado.',
    0,
    'As duas são verdadeiras, e a II explica a I. A apostila recomenda manter os testes simples e legíveis, seguindo o '
    'padrão AAA ou o Given-When-Then. Com as três partes separadas, quem lê o teste vê logo o que foi preparado, o que foi '
    'feito e o que se espera, e um teste fácil de entender é fácil de manter.',
    contexto=[p('Na revisão da suíte de testes, a equipe encontrou testes longos, em que a preparação dos dados, as '
                'chamadas e as verificações aparecem misturadas. Uma desenvolvedora propôs reorganizá-los no padrão AAA.')],
)

banco.multipla(
    'medio',
    'As ferramentas de CI/CD descritas em 1, 2, 3 e 4 são, respectivamente,',
    'GitHub Actions, GitLab CI/CD, Jenkins e CircleCI.',
    [
        'GitLab CI/CD, GitHub Actions, Jenkins e CircleCI.',
        'GitHub Actions, GitLab CI/CD, CircleCI e Jenkins.',
        'GitHub Actions, Jenkins, GitLab CI/CD e Azure Pipelines.',
        'Azure Pipelines, GitLab CI/CD, Jenkins e CircleCI.',
    ],
    'O GitHub Actions é integrado ao GitHub, com workflows em YAML e um marketplace de actions (1). O GitLab CI/CD é '
    'configurado no arquivo .gitlab-ci.yml (2). O Jenkins é o servidor de automação de código aberto mais antigo e '
    'flexível, com mais de 1.800 plugins, mas exige mais configuração e manutenção (3). O CircleCI é uma plataforma '
    'cloud-native com orbs reutilizáveis (4). O Azure Pipelines integra-se ao ecossistema Microsoft.',
    contexto=[p('Uma equipe comparou ferramentas de CI/CD: (1) integrada ao repositório do GitHub, com workflows em YAML; '
                '(2) configurada pelo arquivo .gitlab-ci.yml, dentro da própria plataforma do repositório; (3) servidor de '
                'código aberto com mais de 1.800 plugins, muito customizável, mas trabalhoso de manter; (4) plataforma na '
                'nuvem com "orbs" reutilizáveis e foco em velocidade.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Comparando com o perfil de elite das pesquisas DORA, qual métrica da equipe está fora do padrão?',
    'O lead time for changes, pois a elite leva menos de uma hora do commit até a produção, e a equipe leva três dias.',
    [
        'A frequência de deploy, pois a elite faz um deploy por semana, e cinco por dia é um excesso que gera risco.',
        'A taxa de falha de mudança, pois a elite tem zero falhas, e 4% dos deploys causando incidentes é muito alto.',
        'O MTTR, pois a elite restaura o serviço em menos de cinco minutos, e a equipe leva trinta minutos.',
        'Nenhuma, pois as quatro métricas da equipe já estão dentro do padrão de elite das pesquisas DORA.',
    ],
    'Pelas pesquisas DORA, as equipes de elite fazem deploy várias vezes por dia, têm lead time de menos de uma hora, '
    'taxa de falha de mudança abaixo de 5% e MTTR abaixo de uma hora. A frequência (5 por dia), a taxa de falha (4%) e o '
    'MTTR (30 minutos) estão no padrão; só o lead time, de três dias, fica muito acima da meta.',
    contexto=[p('Uma equipe mediu as quatro métricas DORA no último trimestre: cinco deploys por dia; lead time for changes '
                'de três dias; taxa de falha de mudança de 4%; e MTTR de 30 minutos.')],
)

banco.afirmativas(
    'dificil',
    [
        ('Dados de teste triviais, como usuário "teste" e valor 1, podem esconder problemas que os dados reais revelariam.',
         True),
        ('O recomendado é copiar os dados reais de produção para os testes, sem nenhum tratamento, para ganhar realismo.',
         False),
        ('Uma cobertura de 80% com testes superficiais vale menos que 60% com testes robustos e bem pensados.', True),
        ('A cobertura deve ser usada para encontrar lacunas nos testes, e não como uma meta a ser batida.', True),
    ],
    'I é verdadeira: dados simples demais não exercitam situações reais. II é falsa: a apostila recomenda dados '
    'parecidos com os de produção, mas com técnicas de ofuscação, para usá-los com segurança; copiar dados reais sem '
    'tratamento expõe informações pessoais. III e IV são verdadeiras: a cobertura é um indicador, e não um objetivo, e '
    'não deve ser "gamificada".',
    contexto=[p('Na revisão das práticas de teste de uma fintech, a equipe discutiu os dados usados nos testes e o papel da '
                'cobertura de código.')],
)

banco.assercao(
    'dificil',
    'A programação em pares dobra o custo do desenvolvimento sem nenhum ganho de qualidade, pois duas pessoas fazem o '
    'trabalho de uma.',
    'Na programação em pares, um desenvolvedor escreve e o outro revisa em tempo real, o que funciona como uma revisão de '
    'código contínua.',
    3,
    'A II é verdadeira, e é por ela que a I é falsa. No XP, a programação em pares funciona como revisão de código '
    'contínua e previne defeitos antes mesmo de eles chegarem ao repositório. Como corrigir um defeito fica mais caro a '
    'cada fase, encontrá-lo enquanto o código é escrito é um ganho real de qualidade, e não um desperdício.',
    contexto=[p('Um gerente quer proibir a programação em pares na equipe, alegando que "é pagar dois salários para '
                'escrever o mesmo código".')],
)

banco.multipla(
    'dificil',
    'Pela técnica dos "5 Porquês", a causa raiz do incidente e a ação mais adequada são:',
    'A falta de um processo para registrar as mudanças de requisito no backlog; a ação é criar esse processo de controle '
    'de mudanças.',
    [
        'O erro do desenvolvedor no cálculo; a ação é registrar a falha dele e exigir mais atenção nas próximas entregas.',
        'O cálculo de desconto errado; a ação é corrigir o código e encerrar a análise, já que o defeito foi resolvido.',
        'A falta de testes automatizados; a ação é aumentar a cobertura de testes, pois isso resolve a origem do problema.',
        'O e-mail do diretor; a ação é proibir que os diretores mandem e-mails com pedidos de mudança para a equipe.',
    ],
    'Os "5 Porquês" seguem a cadeia de causas até chegar à causa fundamental, e não param no sintoma. Aqui, o cálculo '
    'errado é o sintoma, e a regra desatualizada no código é uma causa intermediária; a causa raiz é a ausência de um '
    'processo que leve as mudanças de requisito para o backlog. Culpar o desenvolvedor contraria a ideia de '
    'post-mortems sem culpa, e mais testes não resolveriam um requisito que nunca chegou à equipe.',
    contexto=[p('Na análise de um incidente, a equipe perguntou "por quê?" várias vezes: o desconto foi calculado errado '
                'em produção, porque a regra de desconto mudou e o código não foi atualizado; o código não foi atualizado '
                'porque a nova regra foi enviada por e-mail a uma única pessoa, que estava de férias; e a regra foi enviada '
                'por e-mail porque não existe nenhum processo para registrar mudanças de requisito no backlog.')],
)

banco.multipla(
    'dificil',
    'Sobre uma cultura de qualidade autêntica, assinale a alternativa INCORRETA.',
    'Cortar testes por pressão de prazo deve ser decidido em silêncio pela equipe técnica, para não preocupar a liderança.',
    [
        'Os defeitos são vistos como oportunidades de aprendizado, e não como falhas pessoais de quem os introduziu.',
        'A qualidade é responsabilidade de todos: desenvolvedores, testadores, Product Owner e equipe de DevOps.',
        'O feedback é rápido, concreto e baseado em dados, e não em opiniões sobre o trabalho das pessoas.',
        'A liderança dá o exemplo, praticando os comportamentos de qualidade que espera ver na equipe.',
    ],
    'A afirmação incorreta é a do corte de testes: pela apostila, em uma cultura de qualidade, cortar atalhos de '
    'qualidade por pressão de prazo é uma decisão explícita e consciente, nunca tácita ou ignorada. As demais '
    'alternativas estão na lista de características de uma cultura de qualidade autêntica.',
    contexto=[p('Uma empresa quer descrever, no seu guia de cultura, como deve ser uma equipe com qualidade de verdade.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Em uma empresa de software, os testes rodam apenas no notebook de cada desenvolvedor, quando ele se lembra. As '
        'versões são publicadas manualmente, às sextas-feiras à noite, copiando os arquivos para o servidor. Nos últimos '
        'meses, três publicações levaram para produção um código que nem compilava, e uma delas expôs no repositório a '
        'senha do banco de dados.',
    ],
    'Proponha um pipeline de CI/CD com quality gates para essa empresa, explicando como cada etapa ajudaria a evitar os '
    'problemas relatados.',
    'O pipeline começaria a cada commit, com análise de código (linting), secret scanning, que teria barrado a senha '
    'enviada ao repositório, e um SAST rápido. Depois, o build automatizado, com verificação das dependências (SCA) e '
    'geração de artefatos versionados: código que não compila para ali, e nunca chega à produção. Em seguida, os testes '
    'unitários, com medição de cobertura, e os de integração, com testes de contrato de API e de banco em contêiner '
    'isolado, que deixam de depender da memória de cada desenvolvedor. Na análise estática completa, o SonarQube '
    'verifica segurança, qualidade e duplicações. O deploy em staging seria automático, com smoke tests e testes de '
    'aceitação, e depois viriam o DAST, a performance básica e a acessibilidade. Os quality gates bloqueiam o avanço se '
    'algo falhar: cobertura abaixo do mínimo, vulnerabilidade crítica, segredo no código ou teste de regressão quebrado, '
    'com aprovação manual para releases críticos. Por fim, o deploy em produção seria gradual (canary ou blue-green), com '
    'smoke tests e monitoramento, e não uma cópia manual de arquivos na sexta à noite.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma equipe de desenvolvimento tem taxa de falha de mudança de 25% e leva, em média, 8 horas para restaurar o '
        'serviço depois de um incidente. A cada problema, a liderança anuncia uma grande mudança no processo, mas nada é '
        'medido depois, e as mudanças são abandonadas em poucas semanas.',
    ],
    'Explique como a equipe poderia usar o ciclo PDCA e as técnicas de melhoria contínua do capítulo para melhorar esses '
    'resultados de forma sustentável.',
    'O problema é mudar sem planejar nem medir. No Plan, a equipe partiria dos dados (25% de falha de mudança e 8 horas de '
    'MTTR, comparados ao padrão de elite das pesquisas DORA: menos de 5% e menos de uma hora), usaria a análise de causa '
    'raiz, com os "5 Porquês" ou o diagrama de Ishikawa, para entender por que os deploys falham e por que a recuperação '
    'é lenta, e definiria objetivos mensuráveis, como reduzir a falha de mudança para 15% no próximo trimestre. No Do, '
    'aplicaria as mudanças em escala controlada, em uma equipe ou sprint piloto, por exemplo testes automatizados no '
    'pipeline e um procedimento de rollback. No Check, mediria se as métricas melhoraram e se houve efeitos colaterais. No '
    'Act, padronizaria e expandiria o que funcionou, ou ajustaria a abordagem e repetiria o ciclo, registrando o '
    'aprendizado. No lugar das grandes reformas, a ideia de Kaizen: pequenas melhorias frequentes, atacando primeiro a '
    'maior fonte de problemas. Retrospectivas com dados e post-mortems sem culpa depois de cada incidente alimentam o '
    'ciclo seguinte.',
)


if __name__ == '__main__':
    banco.gravar()
