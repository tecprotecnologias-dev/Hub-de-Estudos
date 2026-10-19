"""
Questões médias e difíceis do capítulo 3 (Arquitetura de Software) de Engenharia de Software e da
Usabilidade: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com
um único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/engsoft_cap3_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap3-o* e
engsoft-cap3-d*; as que já existiam (engsoft-cap3-q*) e as dos outros capítulos ficam como estão.
Os princípios SOLID já têm uma questão cada no cap. 4: aqui entram só em leitura de código.
"""

from engsoft_questoes import Banco, codigo, p

banco = Banco('engsoft-cap3')


# =====================================================================================
# Médias
# =====================================================================================

banco.assercao(
    'medio',
    'A arquitetura em camadas e o MVC são padrões arquiteturais, diferentes dos padrões de projeto apresentados no livro '
    'Gang of Four.',
    'Os padrões arquiteturais operam em um nível mais alto, o da estrutura geral do sistema, e não no da estrutura '
    'interna de uma classe.',
    0,
    'As duas são verdadeiras, e a II explica a I. Padrões arquiteturais, como camadas, microsserviços, eventos e MVC, '
    'são soluções consolidadas para organizar sistemas em larga escala. Os padrões de projeto do Gang of Four tratam de '
    'problemas menores, dentro da estrutura das classes. A diferença está justamente no nível em que cada um atua.',
    contexto=[p('Em uma entrevista de emprego, um candidato afirmou que "camadas, MVC e os padrões do livro Gang of Four '
                'são a mesma coisa, só com nomes diferentes". O entrevistador pediu que ele revisse a afirmação.')],
)

banco.multipla(
    'medio',
    'A decisão do desenvolvedor:',
    'fere a arquitetura em camadas, em que cada camada só se comunica com a camada imediatamente adjacente.',
    [
        'está correta, pois na arquitetura em camadas qualquer camada pode chamar qualquer outra quando for mais rápido.',
        'fere o padrão MVC, pois a tela deveria acessar o banco de dados por meio do Model e da View ao mesmo tempo.',
        'está correta, pois a camada de lógica de negócio é opcional quando a consulta é simples e não tem regras.',
        'fere a arquitetura de microsserviços, pois cada tela deveria ter o seu próprio banco de dados separado.',
    ],
    'Na arquitetura em camadas, cada camada tem uma responsabilidade e só conversa com a vizinha: a apresentação fala com '
    'a lógica de negócio, que fala com o acesso a dados. Pular a camada de negócio espalha regras e consultas pela '
    'interface e destrói a separação de responsabilidades, que é a principal vantagem do padrão. Se a camada só '
    'repassasse chamadas, o problema seria outro, o das camadas que não agregam valor.',
    contexto=[p('Em um sistema de biblioteca organizado em três camadas (apresentação, lógica de negócio e acesso a '
                'dados), um desenvolvedor fez a tela de empréstimos executar comandos SQL diretamente no banco de dados, '
                '"para ganhar tempo".')],
)

banco.afirmativas(
    'medio',
    [
        ('O serviço de recomendações pode ganhar mais servidores sem que os demais serviços precisem ser escalados.',
         True),
        ('Cada equipe pode desenvolver e implantar o seu serviço com autonomia, sem depender das outras.', True),
        ('Como cada serviço é pequeno, o monitoramento do sistema como um todo fica mais simples do que em um monólito.',
         False),
        ('A consistência dos dados entre os serviços, cada um com o seu banco, passa a exigir atenção especial.', True),
    ],
    'I é verdadeira: cada microsserviço pode ser escalado de forma independente. II é verdadeira: times autônomos '
    'desenvolvem e implantam o seu serviço separadamente. III é falsa: os microsserviços trazem complexidade '
    'operacional, e o monitoramento passa a ser distribuído, o que é mais difícil. IV é verdadeira: manter os dados '
    'consistentes entre serviços é uma das limitações citadas na apostila.',
    contexto=[p('Uma plataforma de streaming com 15 equipes de desenvolvimento dividiu o seu sistema em microsserviços, '
                'como catálogo, pagamentos, recomendações e reprodução, cada um com o seu próprio banco de dados.')],
)

banco.multipla(
    'medio',
    'A estratégia adotada pela equipe é:',
    'a migração incremental (Strangler Fig), que substitui o legado aos poucos até que ele possa ser desligado.',
    [
        'o encapsulamento (wrapping), que cria uma API moderna em torno do legado, que continua fazendo todo o trabalho.',
        'a refatoração, que reestrutura o código interno do legado sem alterar o seu comportamento externo.',
        'a substituição completa, que troca todo o sistema de uma só vez, em uma única data de virada.',
        'a manutenção corretiva, que corrige os defeitos encontrados no legado depois da sua implantação.',
    ],
    'A equipe construiu um módulo novo à parte, desviou para ele as requisições daquela funcionalidade e vai repetir isso '
    'módulo a módulo até desligar o sistema antigo: é a migração incremental (Strangler Fig), que reduz o risco em '
    'comparação com uma reescrita total. No wrapping, o legado continua fazendo o trabalho por trás de uma API; na '
    'refatoração, o próprio código antigo é melhorado; e na substituição completa, a troca é de uma só vez.',
    contexto=[p('Uma loja virtual tem um sistema antigo e difícil de manter. A equipe construiu um novo módulo de busca de '
                'produtos, separado do sistema antigo, e configurou um roteador para enviar a ele as buscas, enquanto o '
                'carrinho, o pagamento e o resto continuam no sistema antigo. O plano é repetir isso com cada módulo até '
                'que o sistema antigo possa ser desligado.')],
)

banco.multipla(
    'medio',
    'Ao planejar a substituição, a equipe deve considerar principalmente:',
    'o risco de interromper as operações do negócio, o treinamento dos usuários e a migração dos dados históricos.',
    [
        'apenas o custo da nova tecnologia, pois os dados antigos podem ser descartados com o sistema que sai de uso.',
        'apenas a escolha da linguagem de programação, pois os usuários se adaptam sozinhos ao sistema novo depois.',
        'a refatoração completa do sistema antigo antes da troca, para que ele possa ser mantido em paralelo para sempre.',
        'o encapsulamento do sistema antigo em uma API, já que a substituição dispensa qualquer migração de dados.',
    ],
    'A substituição completa é necessária quando a modernização já não é viável, como no caso: tecnologia sem suporte e '
    'manutenção mais cara que uma reescrita. A apostila lista o que essa decisão deve considerar: o risco de interromper '
    'operações críticas, o custo de treinar os usuários no sistema novo e a migração dos dados históricos. Descartar os '
    'dados ou ignorar os usuários tornaria a troca muito arriscada.',
    contexto=[p('Uma rede de hospitais usa um sistema de prontuários escrito em uma tecnologia que não recebe mais '
                'atualizações, roda em servidores que já não são fabricados, e cuja manutenção passou a custar mais do '
                'que construir um sistema novo. A diretoria decidiu substituí-lo.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.afirmativas(
    'dificil',
    [
        ('A escolha das tecnologias afeta a produtividade da equipe e a capacidade de encontrar profissionais no '
         'mercado.', True),
        ('Um sistema bem arquitetado no nível de sistema continua fácil de manter, mesmo que os seus componentes sejam '
         'mal projetados.', False),
        ('Decidir que os módulos vão se comunicar por uma fila de mensagens é uma decisão de definição de interfaces.',
         True),
        ('As decisões arquiteturais são baratas de reverter, pois cada uma afeta apenas uma funcionalidade do sistema.',
         False),
    ],
    'I é verdadeira: é o que a apostila destaca sobre a escolha de tecnologias. II é falsa: um sistema bem arquitetado no '
    'nível macro, mas mal projetado no nível de componentes, ainda pode ficar difícil de manter; os dois níveis precisam '
    'andar juntos. III é verdadeira: definir como os componentes se comunicam (APIs REST, filas, eventos) é definição de '
    'interfaces. IV é falsa: as decisões arquiteturais afetam o sistema inteiro e são muito mais caras de reverter '
    'depois que o desenvolvimento avança.',
    contexto=[p('Na primeira reunião de arquitetura de um sistema de reservas de hotéis, a equipe discutiu o impacto das '
                'decisões de design.')],
)

banco.multipla(
    'dificil',
    'Ao executar o teste com um objeto Quadrado, o que acontece e qual princípio o código viola?',
    'A área calculada é 16, e não 20, e o teste falha; o código viola o Princípio da Substituição de Liskov.',
    [
        'A área calculada é 20, e o teste passa; o código está correto, pois Quadrado é um tipo de Retangulo.',
        'A área calculada é 16, e não 20, e o teste falha; o código viola o Princípio da Responsabilidade Única.',
        'O teste nem chega a ser executado, pois Python não permite sobrescrever métodos herdados de uma superclasse.',
        'A área calculada é 25, e não 20, e o teste falha; o código viola o Princípio da Segregação de Interfaces.',
    ],
    'Em Quadrado, definir_largura(5) faz largura e altura valerem 5; depois, definir_altura(4) faz as duas valerem 4. A '
    'área fica 4 × 4 = 16, e o teste, escrito para um Retangulo, falha. Um objeto da subclasse não pode substituir o da '
    'superclasse sem quebrar o comportamento esperado: é a violação do Princípio da Substituição de Liskov, o exemplo '
    'clássico da apostila. A solução é que os dois herdem de uma classe mais genérica, em vez de um herdar do outro.',
    contexto=[
        p('Observe o código abaixo, escrito em Python.'),
        codigo('''
class Retangulo:
    def definir_largura(self, largura):
        self.largura = largura

    def definir_altura(self, altura):
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Quadrado(Retangulo):
    def definir_largura(self, largura):
        self.largura = largura
        self.altura = largura

    def definir_altura(self, altura):
        self.largura = altura
        self.altura = altura

def testar(r):
    r.definir_largura(5)
    r.definir_altura(4)
    assert r.area() == 20
'''),
    ],
)

banco.assercao(
    'dificil',
    'Na arquitetura orientada a eventos, o serviço de Pedidos não precisa conhecer os serviços que consomem o evento '
    'que ele publica.',
    'Na arquitetura orientada a eventos, o fluxo de dados fica explícito no código, o que facilita rastrear e depurar '
    'o sistema.',
    2,
    'A I é verdadeira: o serviço de Pedidos só publica o evento no barramento, e os outros o consomem de forma '
    'independente; por isso o acoplamento é baixo, e um novo consumidor pode entrar sem mudar o serviço de Pedidos. '
    'A II é falsa: essa mesma independência faz o fluxo ficar espalhado, difícil de rastrear e depurar, o que exige '
    'ferramentas específicas de observabilidade.',
    contexto=[p('Em uma loja virtual, o serviço de Pedidos publica o evento "PedidoPago" em um barramento de mensagens. '
                'Os serviços de Estoque, Nota Fiscal e Entrega reagem a esse evento. A empresa quer incluir um serviço '
                'de pontos de fidelidade, que também vai reagir ao pagamento.')],
)

banco.multipla(
    'dificil',
    'A reorganização correta, segundo o padrão MVC, é:',
    'o Controller recebe as ações do usuário, aciona o Model e decide qual View exibir; o Model fica só com dados e '
    'regras.',
    [
        'manter o Model como está, pois no MVC é ele quem recebe os cliques e decide qual tela deve ser exibida.',
        'passar para a View o tratamento dos cliques e as regras de negócio, deixando o Model apenas com os dados.',
        'eliminar o Controller, pois o Model e a View já conseguem se comunicar sozinhos, sem um intermediário.',
        'criar um Controller para cada regra de negócio do sistema, com o cálculo das multas feito dentro dele.',
    ],
    'No MVC, o Controller recebe as ações do usuário, interpreta essas ações, aciona o Model e determina qual View deve '
    'ser exibida. O Model representa os dados e as regras de negócio, independentemente de como serão exibidos, e não '
    'deve conhecer as telas. Com essa separação, mudanças na interface não afetam as regras, e as equipes podem '
    'trabalhar em paralelo em cada parte. Levar as regras para a View ou para o Controller repete o erro com outro nome.',
    contexto=[p('Em um sistema de biblioteca, a classe Emprestimo (o Model) guarda os dados, calcula as multas, recebe '
                'diretamente os cliques nos botões da tela e decide qual página deve ser mostrada em seguida. Qualquer '
                'mudança no visual das telas obriga a equipe a mexer nessa classe.')],
)

banco.multipla(
    'dificil',
    'Sobre manutenção e modernização de software, assinale a alternativa INCORRETA.',
    'Para encapsular um sistema legado (wrapping), é preciso antes reescrever a sua lógica interna na nova linguagem.',
    [
        'A refatoração reestrutura o código interno sem alterar o comportamento externo, melhorando a qualidade aos '
        'poucos.',
        'A migração incremental (Strangler Fig) reduz o risco em comparação com a reescrita total do sistema.',
        'A manutenção preventiva busca reduzir a probabilidade de falhas futuras ou facilitar as manutenções futuras.',
        'A maior parte do ciclo de vida de um sistema é gasta na sua manutenção, e não no desenvolvimento inicial.',
    ],
    'A afirmação incorreta é a do encapsulamento: o wrapping cria uma API moderna em torno do legado justamente para '
    'que os sistemas novos o usem sem entender nem reescrever a sua implementação interna. As demais estão corretas: '
    'refatorar não muda o comportamento, o Strangler Fig reduz o risco da reescrita total, a manutenção preventiva '
    'previne falhas e facilita manutenções futuras, e a manutenção ocupa a maior parte do ciclo de vida.',
    contexto=[p('Uma cooperativa avalia como lidar com um sistema de vinte anos que ainda funciona bem, mas que não se '
                'integra aos aplicativos novos. A equipe reuniu algumas afirmações sobre as opções disponíveis.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"Organizations which design systems (in the broad sense used here) are constrained to produce designs '
                   'which are copies of the communication structures of these organizations."',
        'traducao': '(Tradução livre: "Organizações que projetam sistemas (no sentido amplo usado aqui) são levadas a '
                    'produzir projetos que são cópias das estruturas de comunicação dessas organizações.")',
        'fonte': 'CONWAY, M. E. How Do Committees Invent? Datamation, v. 14, n. 4, p. 28-31, 1968. (Conhecida como Lei '
                 'de Conway.)',
    },
    [
        'Uma empresa de logística decidiu migrar o seu sistema para microsserviços. Os 30 desenvolvedores, porém, '
        'continuam divididos em três grandes equipes por especialidade técnica: uma só de telas, uma só de regras de '
        'negócio e uma só de banco de dados. Seis meses depois, qualquer mudança em um "microsserviço" exige reuniões '
        'entre as três equipes, os serviços não podem ser implantados separadamente, e o sistema ficou mais difícil de '
        'monitorar do que o antigo.',
    ],
    'Com base no texto de Conway e no caso apresentado, analise por que a migração não trouxe as vantagens esperadas e '
    'proponha um caminho para a empresa.',
    'Pela Lei de Conway, o sistema acaba copiando a forma como as pessoas se comunicam. A empresa trocou o nome da '
    'arquitetura, mas manteve equipes por camada técnica, e por isso o sistema continuou organizado em camadas: cada '
    'mudança atravessa as três equipes, e os serviços não podem ser implantados separadamente. As vantagens dos '
    'microsserviços, escalabilidade independente e times autônomos, dependem de que cada serviço corresponda a uma '
    'capacidade de negócio e tenha uma equipe que o desenvolva e implante sozinha. Ao mesmo tempo, a empresa já paga o '
    'preço dos microsserviços: monitoramento distribuído, consistência de dados entre serviços e mais infraestrutura. '
    'Há dois caminhos coerentes. O primeiro é reorganizar as equipes por capacidade de negócio (por exemplo, '
    'rastreamento, faturamento e roteirização), cada uma multifuncional e responsável pelo seu serviço, com o seu '
    'banco. O segundo, se a empresa não puder mudar a organização, é voltar a um sistema bem organizado em camadas, '
    'mais simples de operar, e só separar em serviço o que realmente precisar escalar de forma independente.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma loja virtual roda em um único sistema, em que todas as funções se chamam diretamente. Na última Black '
        'Friday, o volume de acessos chegou a vinte vezes o normal. O servidor de envio de e-mails ficou lento e, como a '
        'finalização da compra esperava o envio do e-mail de confirmação, o checkout passou a travar. Para piorar, para '
        'aguentar o pico da vitrine de produtos, foi preciso aumentar a capacidade do sistema inteiro, inclusive de '
        'partes quase sem uso, como o painel administrativo.',
    ],
    'Analise o caso e explique quais decisões de design de sistemas e quais padrões arquiteturais poderiam evitar esses '
    'problemas na próxima Black Friday.',
    'Os dois problemas são de design de sistemas. O primeiro está na definição de interfaces: o checkout chama o envio '
    'de e-mail diretamente e espera a resposta, e por isso a lentidão de uma parte secundária derrubou a mais '
    'importante. Com uma comunicação por fila de mensagens ou por eventos, o checkout publicaria um evento como '
    '"PedidoConfirmado" e seguiria em frente, e o e-mail seria enviado quando possível; esse baixo acoplamento é a '
    'principal vantagem da arquitetura orientada a eventos, que exige, em troca, ferramentas de observabilidade para '
    'rastrear o fluxo. O segundo está na decomposição e na estratégia de escalabilidade: com tudo em um bloco só, não '
    'dá para escalar apenas a vitrine. Separar em serviços as partes com picos muito diferentes, como vitrine e '
    'checkout, permitiria escalá-las de forma independente, como nos microsserviços. Essa separação deve ser feita com '
    'cuidado, só onde compensa, porque os microsserviços trazem complexidade operacional: monitoramento distribuído, '
    'consistência de dados entre serviços e mais infraestrutura. Por fim, a estratégia de disponibilidade deve prever '
    'como o sistema se comporta quando um componente falha, para que a falha do e-mail não pare as vendas.',
)


if __name__ == '__main__':
    banco.gravar()
