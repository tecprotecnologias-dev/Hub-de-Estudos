"""
Questões médias e difíceis do capítulo 6 (Automação de Testes) de Qualidade e Testes de Software:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/qualidade_cap6_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap6-o* e
qualidade-cap6-d*; as que já existiam (q* e m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import QUALIDADE, Banco, codigo, p

banco = Banco('qualidade-cap6', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Os elementos 1, 2, 3 e 4 correspondem, respectivamente, aos componentes de um sistema de automação chamados',
    'dados de teste, ambiente de execução, relatórios e integração CI/CD.',
    [
        'scripts de teste, ambiente de execução, relatórios e integração CI/CD.',
        'dados de teste, framework de teste, relatórios e ambiente de execução.',
        'dados de teste, ambiente de execução, integração CI/CD e relatórios.',
        'framework de teste, integração CI/CD, scripts de teste e relatórios.',
    ],
    'Pela tabela de componentes da apostila: arquivos com entradas e saídas esperadas são os dados de teste (1); a '
    'infraestrutura onde os testes rodam, como contêineres Docker e o Selenium Grid, é o ambiente de execução (2); a '
    'saída com resultados e métricas, como o relatório HTML do Allure, são os relatórios (3); e o pipeline que dispara os '
    'testes a cada build, como o GitHub Actions, é a integração CI/CD (4).',
    contexto=[p('Na automação dos testes de uma loja virtual, a equipe usa: '
                '(1) arquivos CSV com os valores de entrada e os resultados esperados de cada caso; '
                '(2) contêineres Docker com o Selenium Grid, onde os testes rodam; '
                '(3) um relatório HTML do Allure com os resultados e as métricas de cada execução; '
                '(4) um fluxo do GitHub Actions que dispara a suíte a cada build.')],
)

banco.multipla(
    'medio',
    'Pelos critérios de priorização da apostila, qual teste deve ser automatizado primeiro?',
    'O teste 2, pois é frequente, determinístico, cobre uma função crítica do negócio e tem dados estáveis.',
    [
        'O teste 1, pois a avaliação da beleza do novo layout é a parte que mais demora no teste manual.',
        'O teste 3, pois uma funcionalidade nova e instável precisa de mais testes do que uma já estável.',
        'O teste 4, pois um teste que roda uma vez só ganha muito com a rapidez dos scripts automatizados.',
        'Nenhum deles, pois a automação só compensa depois que todos os testes manuais foram executados.',
    ],
    'Os critérios da apostila priorizam testes executados com frequência, com resultado determinístico, que cobrem '
    'funções críticas, como o pagamento, que estão no caminho crítico do usuário e que têm dados estáveis: é o teste 2. '
    'Avaliar se um layout é bonito exige julgamento humano; uma funcionalidade que muda toda semana faria a manutenção '
    'superar o benefício; e um teste executado uma única vez tem retorno negativo.',
    contexto=[p('Uma equipe de QA tem quatro candidatos à automação: '
                '(1) avaliar se o novo layout da página inicial ficou bonito; '
                '(2) finalizar a compra com cartão de crédito, executado a cada sprint, com dados de teste fixos e '
                'resultado esperado bem definido; '
                '(3) testar um recurso experimental cujas telas mudam toda semana; '
                '(4) conferir a migração de dados que será feita uma única vez.')],
)

banco.assercao(
    'medio',
    'Testes que usam dados fixos escritos diretamente no código (hardcoded) tendem a ficar frágeis.',
    'O pytest tem plugins para medir a cobertura (pytest-cov) e para executar os testes em paralelo (pytest-xdist).',
    1,
    'As duas são verdadeiras. A I é uma das boas práticas da apostila: dados hardcoded tornam os testes frágeis, e a '
    'recomendação é usar factories, fixtures ou bancos de teste dedicados. A II descreve corretamente plugins do pytest, '
    'mas cobertura e execução paralela não explicam por que os dados fixos deixam os testes frágeis.',
    contexto=[p('Os testes de uma equipe quebram sempre que alguém altera um cliente cadastrado no banco de dados de '
                'homologação, pois o código dos testes usa o CPF e o nome desse cliente escritos diretamente nos scripts.')],
)

banco.multipla(
    'medio',
    'Sobre o teste manual e o teste automatizado, assinale a alternativa INCORRETA.',
    'O teste automatizado detecta problemas visuais subjetivos e de usabilidade melhor que uma pessoa.',
    [
        'O teste manual é excelente para testes exploratórios, de usabilidade e para análises subjetivas.',
        'O teste automatizado é rápido, consistente e repetível, mas exige investimento em scripts.',
        'O teste manual é lento e caro para a regressão de um sistema com muitos casos de teste.',
        'Um ambiente instável pode fazer a suíte automatizada falhar sem que haja defeito no código.',
    ],
    'A afirmação incorreta é a dos problemas visuais: entre as limitações da automação, a apostila lista justamente que '
    'ela não detecta problemas visuais subjetivos ou de usabilidade e não avalia a experiência do usuário de forma '
    'holística. A automação complementa o teste manual, não o substitui. As demais alternativas estão de acordo com a '
    'comparação e com a tabela de vantagens e limitações do capítulo.',
    contexto=[p('Em uma reunião de planejamento, a equipe discutia se ainda valia a pena manter testadores fazendo testes '
                'manuais depois da automação da suíte de regressão.')],
)

banco.multipla(
    'medio',
    'As ferramentas mais adequadas às necessidades 1, 2, 3 e 4 são, respectivamente,',
    'Cypress, Puppeteer, Playwright e Appium.',
    [
        'Puppeteer, Cypress, Playwright e Appium.',
        'Cypress, Puppeteer, Appium e Playwright.',
        'Playwright, Puppeteer, Cypress e JMeter.',
        'Cypress, Playwright, Puppeteer e Appium.',
    ],
    'O Cypress executa os testes dentro do navegador, com acesso ao DOM, e é excelente para frontends em React com '
    'JavaScript (1). O Puppeteer, do Google, controla o Chrome e o Chromium pelo protocolo DevTools e é ideal para Node.js '
    '(2). O Playwright, da Microsoft, testa Chrome, Firefox e Safari com uma única API, inclusive em Python, e intercepta '
    'requisições (3). O Appium automatiza aplicativos iOS e Android (4).',
    contexto=[p('Uma consultoria atende quatro clientes: '
                '(1) uma equipe de frontend em React, com JavaScript, que quer rodar os testes dentro do navegador, com '
                'depuração visual; '
                '(2) uma equipe de Node.js que precisa controlar o Chrome pelo protocolo DevTools; '
                '(3) uma equipe de Python que quer testar no Chrome, no Firefox e no Safari com uma única API e '
                'interceptar as requisições; '
                '(4) uma equipe que precisa automatizar um aplicativo nativo de Android e de iOS.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Pela fórmula de ROI da apostila, qual é o retorno da automação ao fim do primeiro ano?',
    '100%.',
    ['140%.', '50%.', '200%.', '240%.'],
    'Cada ciclo manual custa 300 x 6 min = 1.800 min = 30 h; 30 h x R$ 40 = R$ 1.200. Com 24 releases, são R$ 28.800 '
    'economizados no ano. O custo da automação no primeiro ano é R$ 12.000 + R$ 2.400 = R$ 14.400. ROI = (28.800 - 14.400) '
    '/ 14.400 x 100% = 100%. Esquecer a manutenção levaria a 140%; dividir só a economia pelo custo, a 200%; e dividir a '
    'economia pelo desenvolvimento, a 240%.',
    contexto=[p('Uma equipe executa manualmente 300 casos de teste, de 6 minutos cada, a um custo de R$ 40 por hora, em 24 '
                'releases por ano. Automatizar a suíte custará R$ 12.000 de desenvolvimento e R$ 2.400 por ano de '
                'manutenção. Considere que a automação elimina todo o esforço manual dessa suíte.')],
)

banco.multipla(
    'dificil',
    'Comparando com a distribuição ideal da pirâmide de automação, é correto afirmar que a suíte',
    'forma um cone de sorvete, com 50% de testes de UI, bem acima dos 5% a 15% ideais, e por isso é lenta e frágil.',
    [
        'segue a pirâmide, pois tem mais testes de UI, que são os que validam os fluxos críticos de ponta a ponta.',
        'forma um cone de sorvete só porque tem poucos testes de integração, já que os unitários estão na faixa ideal.',
        'está equilibrada, pois a pirâmide define apenas a quantidade total de testes, e não a distribuição.',
        'forma um cone de sorvete, que deve ser corrigido trocando os testes unitários por mais testes de integração.',
    ],
    'A pirâmide recomenda de 60% a 70% de unitários, de 20% a 25% de integração e de 5% a 15% de UI. A suíte tem 30% de '
    'unitários, 20% de integração e 50% de UI: o excesso de UI e a falta de unitários formam o cone de sorvete, que gera '
    'suítes lentas, frágeis e caras de manter. A correção é escrever mais testes unitários e reduzir os de UI aos fluxos '
    'críticos, e não trocar unitários por integração.',
    contexto=[p('A suíte automatizada de um sistema tem 1.000 testes: 300 unitários, 200 de integração e 500 de interface '
                '(UI), feitos com Selenium. A execução completa leva duas horas, e vários testes falham de forma '
                'intermitente.')],
)

banco.multipla(
    'dificil',
    'Se o teste login falhar, o que acontece com os demais e como avaliar esse uso de dependências?',
    'criarPedido e pagarPedido são pulados, sem executar; isso facilita o diagnóstico, mas contraria a independência '
    'do FIRST.',
    [
        'criarPedido e pagarPedido são executados mesmo assim, pois o TestNG ignora o atributo quando um teste falha.',
        'Toda a suíte é interrompida com erro, pois um dependsOnMethods que falha impede a classe de compilar.',
        'criarPedido e pagarPedido são pulados, e esse recurso existe também no JUnit 5 com a anotação @Nested.',
        'criarPedido e pagarPedido falham com a mesma mensagem de erro, o que segue o princípio FIRST.',
    ],
    'No TestNG, dependsOnMethods faz o teste depender de outro: se login falha, os dependentes não são executados e '
    'aparecem como pulados (skipped), e não como falhos, o que evita uma cascata de falhas enganosas. Pela tabela da '
    'apostila, o JUnit 5 não suporta dependência entre testes nativamente; @Nested só agrupa testes. Mas as boas práticas '
    'pedem que cada teste rode de forma isolada, como diz o I (Independent) do FIRST.',
    contexto=[
        p('Observe a classe de teste abaixo, escrita em Java com TestNG.'),
        codigo('''
public class PedidoTest {
    @Test
    public void login() { /* ... */ }

    @Test(dependsOnMethods = "login")
    public void criarPedido() { /* ... */ }

    @Test(dependsOnMethods = "criarPedido")
    public void pagarPedido() { /* ... */ }
}
'''),
    ],
)

banco.multipla(
    'dificil',
    'Sobre a execução desses testes com o pytest, é correto afirmar que',
    'cada teste recebe um carrinho novo, criado pela fixture, e por isso a ordem de execução não muda os resultados.',
    [
        'os dois testes recebem o mesmo carrinho, e test_carrinho_vazio falha se rodar depois de test_adiciona_item.',
        'os testes falham, pois a fixture precisaria ser chamada como carrinho() dentro de cada um dos testes.',
        'os testes não são encontrados, pois o pytest só executa testes escritos em classes que herdam de TestCase.',
        'test_adiciona_item falha, pois o pytest passa o nome da fixture como texto, e não o objeto que ela retorna.',
    ],
    'O pytest encontra as funções que começam com test_ e injeta a fixture pelo nome do parâmetro, passando o objeto que '
    'ela retorna. Por padrão, a fixture é executada de novo para cada teste que a usa, então cada um recebe um carrinho '
    'novo. Assim, os testes são independentes e repetíveis, como pede o FIRST, e os dados de teste ficam gerenciados pela '
    'fixture, e não espalhados pelos testes.',
    contexto=[
        p('Observe os testes abaixo, escritos em Python com pytest.'),
        codigo('''
import pytest

@pytest.fixture
def carrinho():
    return Carrinho()

def test_carrinho_vazio(carrinho):
    assert carrinho.total() == 0

def test_adiciona_item(carrinho):
    carrinho.adicionar("livro", 50)
    assert carrinho.total() == 50
'''),
    ],
)

banco.afirmativas(
    'dificil',
    [
        ('O JUnit Vintage permite executar, no JUnit 5, testes escritos em JUnit 3 e 4.', True),
        ('O JUnit Platform é a API para escrever os testes, e o JUnit Jupiter é o módulo que os executa.', False),
        ('O TestNG gera relatório HTML nativo, enquanto o JUnit 5 depende de terceiros, como Allure e Surefire.', True),
        ('No TestNG, a execução paralela exige um plugin do Maven ou do Gradle, pois não é suportada nativamente.', False),
    ],
    'I é verdadeira: o JUnit Vintage é o módulo de compatibilidade com o JUnit 3 e 4. II é falsa: os papéis estão '
    'trocados; o JUnit Platform cuida da execução, e o JUnit Jupiter é a API de testes. III é verdadeira, pela tabela '
    'comparativa da apostila. IV é falsa: no TestNG a execução paralela é nativa, configurada no testng.xml; quem depende '
    'de plugin do Maven ou do Gradle é o JUnit 5.',
    contexto=[p('Uma equipe Java vai escolher entre o JUnit 5 e o TestNG para a nova suíte de testes e precisa migrar '
                'testes antigos, escritos em JUnit 4.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Uma rede de farmácias tem 1.200 casos de teste manuais no seu sistema de vendas, executados a cada release '
        'quinzenal. Entre eles estão: login e finalização de compra, cálculo de descontos de convênios, consultas à API de '
        'estoque, avaliação da facilidade de uso da nova tela do caixa, uma conferência da migração de dados que será feita '
        'uma única vez e testes de um módulo de promoções cujas telas mudam quase toda semana. A diretoria quer '
        '"automatizar tudo" para acabar com os testes manuais.',
    ],
    'Avalie a proposta da diretoria e proponha quais testes devem ser automatizados e quais devem continuar manuais, '
    'justificando com base nos critérios estudados no capítulo.',
    'Automatizar tudo não é adequado: a automação complementa o teste manual, e automatizar o que não deveria gera '
    'desperdício. Devem ser automatizados os testes repetitivos, determinísticos e de alto valor: login e finalização de '
    'compra (caminho crítico, funções críticas, executados a cada release), o cálculo de descontos de convênios (lógica '
    'de negócio, em testes unitários na base da pirâmide) e as consultas à API de estoque (testes de API rápidos e '
    'reutilizáveis), integrados ao pipeline de CI/CD, além dos smoke tests e da regressão. Devem continuar manuais a '
    'avaliação da facilidade de uso da tela do caixa (usabilidade exige julgamento humano), os testes exploratórios, a '
    'conferência da migração única (ROI negativo, pois o esforço não se paga) e o módulo de promoções enquanto as telas '
    'mudarem toda semana (a manutenção dos scripts superaria o benefício). Com releases quinzenais e muitos casos, o '
    'retorno do investimento tende a ser positivo, mas a equipe deve prever o custo inicial e a manutenção dos scripts.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'A suíte de testes de interface de um portal de notícias, feita com Selenium, demora três horas e falha de forma '
        'intermitente. Uma análise mostrou que: os testes usam Thread.sleep(3000) para esperar o carregamento das '
        'páginas; os localizadores dos elementos estão repetidos em dezenas de testes; o teste de publicar uma notícia '
        'depende do teste de login ter rodado antes; os usuários e senhas estão escritos diretamente no código; e 70% dos '
        'testes da suíte são de interface.',
    ],
    'Analise os problemas encontrados nessa suíte e proponha as melhorias, com base nas boas práticas de automação '
    'estudadas no capítulo.',
    'O Thread.sleep fixo deixa os testes lentos quando a página é rápida e faz falharem quando ela demora mais que o '
    'previsto; a melhoria é usar esperas explícitas, como o WebDriverWait, que aguardam o elemento ficar disponível. Os '
    'localizadores repetidos fazem cada mudança na interface exigir alterações em muitos testes; a melhoria é adotar o '
    'Page Object Model, centralizando os localizadores em uma classe por página. A dependência entre os testes de login e '
    'de publicação contraria o princípio FIRST (Independent); cada teste deve preparar o próprio estado e rodar isolado. '
    'Os dados escritos no código tornam os testes frágeis; devem ser usados dados gerenciados, com factories, fixtures ou '
    'um banco de teste dedicado. Por fim, 70% de testes de interface formam um cone de sorvete; a suíte deve seguir a '
    'pirâmide, com 60% a 70% de unitários, 20% a 25% de integração e 5% a 15% de UI, deixando a interface só para os '
    'fluxos críticos. Também vale executar os testes em paralelo, com o Selenium Grid, e refatorar a suíte regularmente.',
)


if __name__ == '__main__':
    banco.gravar()
