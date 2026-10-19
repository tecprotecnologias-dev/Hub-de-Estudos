"""
Questões médias e difíceis do capítulo 7 (Testes de Regressão) de Qualidade e Testes de Software:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/qualidade_cap7_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap7-o* e
qualidade-cap7-d*; as que já existiam (q* e m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import QUALIDADE, Banco, codigo, p

banco = Banco('qualidade-cap7', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Qual das situações descreve um defeito de regressão?',
    'Depois da atualização de uma biblioteca, o cálculo de juros, que estava correto, passou a arredondar errado.',
    [
        'Na primeira execução do teste de uma funcionalidade recém-criada, o botão de exportar não gerou o arquivo.',
        'O cliente pediu que o relatório mostrasse o saldo por mês, mas a equipe entendeu que era por semana.',
        'Um requisito novo, ainda não implementado, aparece como pendente na matriz de rastreabilidade do projeto.',
        'Um teste exploratório encontrou um defeito em uma tela que foi criada nesta sprint e nunca tinha sido testada.',
    ],
    'Um defeito de regressão ocorre quando uma funcionalidade que funcionava corretamente deixa de funcionar depois de uma '
    'modificação, e a atualização de uma biblioteca de terceiros é um dos exemplos da apostila. Defeitos em funcionalidades '
    'novas, ainda não aprovadas, são encontrados pelos testes de desenvolvimento, e não pela regressão; um requisito mal '
    'entendido e um requisito pendente também não são regressões.',
    contexto=[p('Durante uma sprint, a equipe registrou várias ocorrências no sistema de controle de defeitos e quer '
                'saber quais devem ser classificadas como regressões.')],
)

banco.afirmativas(
    'medio',
    [
        ('Uma mudança apenas em variáveis de ambiente dispensa a regressão, pois nenhuma linha de código foi alterada.',
         False),
        ('Quando uma API de terceiros é atualizada, os pontos de integração com ela devem ser verificados de novo.', True),
        ('Uma refatoração que não muda a lógica interna pode introduzir mudanças sutis de comportamento.', True),
        ('A regressão completa antes do deploy em produção só é necessária em projetos com releases pouco frequentes.',
         False),
    ],
    'I é falsa: mudanças de configuração ou de infraestrutura, como variáveis de ambiente, estão entre os gatilhos da '
    'regressão, pois podem afetar o comportamento da aplicação. II e III são verdadeiras: são os gatilhos de integração '
    'com sistemas externos e de refatoração. IV é falsa: independentemente da frequência de desenvolvimento, a regressão '
    'completa deve ser executada antes de qualquer deploy em produção.',
    contexto=[p('Uma equipe está escrevendo a política que define quando os testes de regressão devem ser executados.')],
)

banco.multipla(
    'medio',
    'Pela arquitetura em camadas da regressão automatizada, os gatilhos 1, 2, 3 e 4 disparam, respectivamente, a '
    'regressão',
    'unitária, de integração e API, de sistema e UI, e completa.',
    [
        'unitária, de sistema e UI, de integração e API, e completa.',
        'de integração e API, unitária, de sistema e UI, e completa.',
        'unitária, de integração e API, completa, e de sistema e UI.',
        'completa, de integração e API, de sistema e UI, e unitária.',
    ],
    'Na arquitetura da apostila, a regressão unitária roda a cada commit, em menos de 5 minutos (1); a de integração e API, '
    'a cada merge na branch de desenvolvimento, de 5 a 20 minutos (2); a de sistema e UI, a cada release candidate ou '
    'merge na branch principal, de 20 a 90 minutos (3); e a completa, com execução paralela, antes de cada release para '
    'produção, de 2 a 8 horas (4).',
    contexto=[p('No pipeline de uma empresa, a regressão é acionada por quatro eventos: '
                '(1) cada commit em uma branch; '
                '(2) cada merge na branch de desenvolvimento; '
                '(3) cada release candidate ou merge na branch principal; '
                '(4) a véspera de cada release para produção.')],
)

banco.multipla(
    'medio',
    'As ferramentas mais adequadas às necessidades 1, 2, 3 e 4 são, respectivamente,',
    'Allure, RestAssured, pytest-xdist e GitHub Actions.',
    [
        'RestAssured, Allure, pytest-xdist e GitHub Actions.',
        'Allure, RestAssured, GitHub Actions e pytest-xdist.',
        'Allure, pytest-xdist, RestAssured e GitHub Actions.',
        'GitHub Actions, RestAssured, pytest-xdist e Allure.',
    ],
    'Pela tabela de ferramentas para a regressão: o Allure gera relatórios visuais com histórico de execuções, tendências '
    'e falhas por categoria (1); o RestAssured valida contratos de APIs REST em Java, com sintaxe fluente (2); o pytest '
    'com o pytest-xdist executa os testes em paralelo (3); e o Jenkins ou o GitHub Actions orquestram o CI/CD, disparando '
    'a suíte a cada evento do repositório (4).',
    contexto=[p('Uma equipe quer melhorar a sua suíte de regressão e listou quatro necessidades: '
                '(1) relatórios com o histórico das execuções e as tendências de falhas; '
                '(2) validar em Java os contratos das APIs REST; '
                '(3) executar em paralelo os testes unitários escritos em Python; '
                '(4) disparar a suíte automaticamente a cada evento do repositório.')],
)

banco.assercao(
    'medio',
    'O teste de regressão verifica se funcionalidades já testadas e aprovadas continuam funcionando depois de uma mudança.',
    'Testar as funcionalidades novas, criadas na sprint, faz parte do escopo principal do teste de regressão.',
    2,
    'A I é verdadeira: é a definição do teste de regressão na apostila. A II é falsa: pela tabela de definição e escopo, '
    'testar novas funcionalidades não é regressão, e sim responsabilidade dos testes de desenvolvimento (unitário, '
    'integração e sistema). Depois de aprovados, esses novos testes podem passar a fazer parte da suíte de regressão.',
    contexto=[p('Em uma reunião, um gerente sugeriu juntar todos os testes da sprint, os das funcionalidades novas e os das '
                'antigas, em uma única atividade chamada "regressão".')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Qual é a ordem correta dessas etapas no fluxo de regressão do pipeline CI/CD?',
    '2, 4, 5, 1, 3 e 6.',
    ['2, 5, 4, 1, 3 e 6.', '2, 4, 5, 3, 1 e 6.', '4, 2, 5, 1, 3 e 6.', '2, 4, 1, 5, 6 e 3.'],
    'No fluxo da apostila, a profundidade cresce conforme o código avança: no commit, a análise estática e os unitários '
    '(2); no pull request, a integração e os contratos de API (4); no merge, os testes de sistema pela interface (5); no '
    'release candidate, a regressão completa em paralelo (1); em staging, a aceitação automatizada e os exploratórios, '
    'com aprovação humana (3); e, em produção, os smoke tests pós-deploy (6).',
    contexto=[p('Um estagiário anotou, fora de ordem, as etapas do pipeline de uma empresa: '
                '(1) regressão completa, em paralelo, em vários ambientes; '
                '(2) análise estática e testes unitários; '
                '(3) testes de aceitação automatizados e exploratórios manuais, com aprovação humana; '
                '(4) testes de integração e de contrato de API; '
                '(5) build completo e testes de sistema pela interface; '
                '(6) monitoramento e smoke tests depois do deploy.')],
)

banco.multipla(
    'dificil',
    'Pelos parâmetros de smoke test da apostila, como avaliar a proposta?',
    'Não é um smoke test: 1.200 casos são 30% da suíte e levam 50 minutos; o certo seriam de 200 a 400 casos críticos.',
    [
        'É um bom smoke test: quanto mais casos ele tiver, maior a chance de rejeitar um build com problemas.',
        'É um sanity test, pois a duração de 50 minutos fica entre 15 minutos e 1 hora, a faixa do sanity.',
        'Não é um smoke test: o certo seria rodar a suíte completa, com os 4.000 casos, a cada build gerado.',
        'Não é um smoke test: ele deveria ter de 400 a 800 casos, que são de 10% a 20% da suíte de regressão.',
    ],
    'O smoke test cobre de 5% a 10% dos casos, só os fluxos mais críticos, e dura de 5 a 15 minutos, pois roda a cada '
    'build. Com 4.000 casos, isso dá de 200 a 400 casos; 1.200 casos são 30%. Classificar como sanity também está errado, '
    'pois o sanity é definido pelo escopo, a área modificada por uma correção, e não só pela duração. Rodar a suíte '
    'completa a cada build seria inviável.',
    contexto=[p('Uma equipe tem 4.000 casos de regressão automatizados. Um analista propôs um "smoke test" com 1.200 desses '
                'casos, que leva 50 minutos para rodar, a ser executado a cada novo build.')],
)

banco.multipla(
    'dificil',
    'Sobre as estratégias de seleção de casos de regressão, assinale a alternativa INCORRETA.',
    'A regressão progressiva dispensa disciplina da equipe, pois os novos casos entram na suíte sozinhos a cada entrega.',
    [
        'A regressão total garante a cobertura máxima, mas é inviável em pipelines que rodam a cada commit.',
        'A seletiva por impacto exige boa rastreabilidade e pode perder defeitos em áreas indiretamente afetadas.',
        'A baseada em risco equilibra cobertura e tempo, mas defeitos em funções de baixo risco podem escapar.',
        'A regressão por camadas exige planejar com cuidado a organização e a categorização dos casos de teste.',
    ],
    'A afirmação incorreta é a da regressão progressiva: a limitação apontada pela apostila é justamente que ela exige '
    'disciplina para adicionar novos testes à suíte a cada entrega. As demais alternativas descrevem corretamente as '
    'vantagens e as limitações das regressões total, seletiva por impacto, baseada em risco e por camadas.',
    contexto=[p('Uma equipe vai escolher a estratégia de seleção de casos de regressão do seu projeto e reuniu as '
                'características de cada uma.')],
)

banco.multipla(
    'dificil',
    'Comparando com as metas saudáveis da apostila, quais métricas estão fora da meta?',
    'Apenas a taxa de flakiness, de 2,4%, e o custo de manutenção, de 25% do esforço de testes.',
    [
        'Apenas a taxa de aprovação, de 96%, pois a meta saudável é de 100% dos testes passando sempre.',
        'Apenas o tempo da suíte completa, de 1 hora e 40 minutos, pois a meta é de menos de 1 hora.',
        'A taxa de flakiness, de 2,4%, o custo de manutenção, de 25%, e a taxa de aprovação, de 96%.',
        'Nenhuma delas, pois todas as métricas da equipe estão dentro das metas saudáveis da apostila.',
    ],
    'A flakiness é 60 / 2.500 = 2,4%, acima da meta de menos de 2%. O custo de manutenção é 45 / 180 = 25% do esforço de '
    'testes, acima da meta de menos de 20%. A taxa de aprovação, de 96%, está acima da meta de 95%, e a suíte completa, '
    'de 1 hora e 40 minutos com paralelismo, está abaixo da meta de 2 horas.',
    contexto=[p('Uma suíte de regressão tem 2.500 testes, dos quais 60 passam e falham de forma intermitente. A taxa de '
                'aprovação nas execuções estáveis é de 96%, e a suíte completa, com paralelismo, roda em 1 hora e 40 '
                'minutos. No último mês, a equipe gastou 45 das suas 180 horas de testes mantendo a suíte.')],
)

banco.multipla(
    'dificil',
    'Ao executar o teste de regressão abaixo sobre a versão 2, o que acontece e como classificar o problema?',
    'O teste falha, pois a versão 2 pula a primeira nota e retorna 6; é um defeito de regressão da refatoração.',
    [
        'O teste passa, pois a versão 2 percorre as notas com um laço e chega ao mesmo resultado 8 da versão 1.',
        'O teste falha com divisão por zero, pois o laço da versão 2 zera o tamanho da lista antes da divisão.',
        'O teste falha, mas não é regressão, pois refatorações não estão entre os gatilhos dos testes de regressão.',
        'O teste falha, mas não é regressão, pois a função media foi alterada e passou a ser uma nova funcionalidade.',
    ],
    'Na versão 2, o laço começa em 1 e ignora notas[0]: soma 8 + 10 = 18 e divide por 3, retornando 6, e não 8. A função '
    'funcionava e deixou de funcionar depois de uma modificação: é um defeito de regressão. A apostila lista a refatoração '
    'entre os gatilhos, pois mesmo sem mudar a lógica pretendida ela pode introduzir mudanças sutis de comportamento.',
    contexto=[
        p('Observe as duas versões de uma função, escrita em Python, e o teste de regressão que a acompanha.'),
        codigo('''
# Versão 1
def media(notas):
    return sum(notas) / len(notas)

# Versão 2, depois de uma refatoração
def media(notas):
    total = 0
    for i in range(1, len(notas)):
        total += notas[i]
    return total / len(notas)

assert media([6, 8, 10]) == 8
'''),
    ],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Um banco digital entrega uma nova versão do aplicativo a cada duas semanas, com um time Scrum e um pipeline de '
        'CI/CD. A regressão ainda é manual: 3.000 casos de teste, que três testadores levam quatro dias para executar, '
        'sempre na última semana antes do release. Mesmo assim, no último trimestre, quatro defeitos de regressão chegaram '
        'à produção, e um deles obrigou a equipe a reverter o deploy.',
    ],
    'Proponha uma estratégia de testes de regressão para esse banco, considerando a automação, a seleção dos casos e a '
    'integração ao pipeline de CI/CD.',
    'A regressão manual de 3.000 casos não acompanha releases quinzenais e deixa escapar defeitos, com custo alto, '
    'rollback e perda de confiança. O primeiro passo é automatizar a regressão, começando pelos fluxos críticos, como '
    'login, transferências e pagamentos. A suíte deve seguir a arquitetura em camadas: unitários a cada commit, em menos '
    'de 5 minutos; integração e contratos de API a cada merge na branch de desenvolvimento; testes de sistema e UI a cada '
    'release candidate; e a regressão completa, em paralelo, com Selenium Grid ou serviços em nuvem, antes de cada '
    'release. A seleção pode combinar camadas (smoke a cada build, sanity após cada correção e regressão completa antes '
    'do release) com a regressão baseada em risco, priorizando as funções críticas, e a progressiva, adicionando os novos '
    'casos a cada sprint, como parte da Definition of Done. Depois do deploy, entram os smoke tests em produção e o '
    'monitoramento sintético. Os testadores, liberados da execução repetitiva, passam a fazer testes exploratórios.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'A suíte de regressão de um sistema de logística tem 4.500 testes automatizados. Nos últimos meses, a equipe '
        'percebeu que: cerca de 8% dos testes passam e falham sem que o código mude; muitos testes verificam telas que já '
        'foram removidas; vários cenários são verificados por mais de um teste; quando o teste de cadastro falha, dezenas '
        'de outros falham junto; e, quando um requisito muda, ninguém sabe quais testes precisam ser atualizados. Os '
        'desenvolvedores já ignoram as falhas da suíte, dizendo que "é sempre o teste que está errado".',
    ],
    'Analise os problemas dessa suíte e proponha um plano de gestão e manutenção para recuperar a confiança da equipe nos '
    'resultados.',
    'A suíte virou um passivo. Os 8% de testes instáveis (flaky), muito acima da meta de menos de 2%, devem ir para uma '
    'quarentena, para não bloquear o pipeline, e ser corrigidos e reintegrados depois de estabilizados. Os testes '
    'obsoletos, que verificam telas removidas, geram falhas falsas e devem ser removidos; os duplicados aumentam o tempo '
    'sem acrescentar cobertura e devem ser eliminados. As falhas em cascata mostram acoplamento excessivo: cada teste deve '
    'preparar o próprio estado e rodar de forma isolada. Falta rastreabilidade bidirecional: cada teste deve estar ligado '
    'ao requisito que verifica, para que os testes afetados sejam identificados quando ele mudar. O plano deve incluir a '
    'revisão periódica da suíte em cada sprint, tratada como código de produção, nomes descritivos e o monitoramento das '
    'métricas: taxa de aprovação acima de 95%, flakiness abaixo de 2%, tempo de execução, defeitos escapados e custo de '
    'manutenção abaixo de 20% do esforço de testes.',
)


if __name__ == '__main__':
    banco.gravar()
