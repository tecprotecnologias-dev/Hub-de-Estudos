"""
Questões médias e difíceis do capítulo 5 (Testes de Software) de Engenharia de Software e da
Usabilidade: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas
com um único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/engsoft_cap5_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap5-o* e
engsoft-cap5-d*; as que já existiam (engsoft-cap5-q*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import Banco, codigo, p

banco = Banco('engsoft-cap5')


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Os níveis de teste mais adequados para detectar os problemas 1, 2, 3 e 4 são, respectivamente,',
    'unitário, integração, sistema e aceitação.',
    [
        'integração, unitário, aceitação e sistema.',
        'unitário, sistema, integração e aceitação.',
        'sistema, integração, unitário e aceitação.',
        'unitário, integração, aceitação e sistema.',
    ],
    'O problema 1 está dentro de uma única função, o menor componente testável: teste unitário. '
    'O 2 só aparece quando dois serviços conversam, cada um correto isoladamente: teste de integração. '
    'O 3 exige o sistema inteiro, em ambiente parecido com o de produção, sob carga: teste de sistema (desempenho). '
    'O 4 depende do julgamento de quem conhece o processo real do negócio, o usuário final: teste de aceitação (UAT).',
    contexto=[p('Antes de lançar a nova versão de uma loja virtual, a equipe registrou quatro problemas: '
                '(1) a função que calcula o desconto de um cupom aceita cupons vencidos; '
                '(2) o serviço de pedidos envia a data no formato "dd/mm/aaaa", mas o serviço de estoque espera '
                '"aaaa-mm-dd", e as reservas de produtos falham; '
                '(3) o site fica lento com 5 mil usuários simultâneos, situação esperada para a Black Friday; '
                '(4) o gerente de uma loja física, ao usar o sistema, percebe que o fluxo de troca de produtos '
                'não segue o procedimento que as lojas realmente adotam.')],
)

banco.assercao(
    'medio',
    'As atividades realizadas pela equipe são atividades de verificação.',
    'Revisão de código, inspeção e análise estática avaliam se o produto atende às reais necessidades do usuário.',
    2,
    'A I é verdadeira: revisão de código, inspeção e análise estática respondem à pergunta "estamos construindo o '
    'produto corretamente?", conferindo a conformidade com especificações e padrões. A II é falsa: avaliar se o '
    'produto atende às reais necessidades do usuário é validação ("estamos construindo o produto correto?"), feita '
    'com testes de aceitação e usuários reais. Por isso, mesmo sem nenhuma não conformidade, a equipe ainda não sabe '
    'se construiu o produto certo.',
    contexto=[p('Antes de liberar a nova versão de um aplicativo bancário, uma equipe fez revisão de código por pares, '
                'uma inspeção formal do módulo de pagamentos e uma análise estática com o SonarQube. '
                'Nenhuma não conformidade foi encontrada.')],
)

banco.multipla(
    'medio',
    'Sobre as técnicas de teste caixa branca, caixa preta e caixa cinza, assinale a alternativa INCORRETA.',
    'Por ter acesso ao código-fonte, o teste caixa branca garante que o sistema atende às necessidades reais dos '
    'usuários, o que dispensa os testes caixa preta.',
    [
        'No teste caixa preta, o testador não tem acesso ao código e compara as respostas do sistema com o que os '
        'requisitos determinam.',
        'O teste caixa branca costuma ser feito pelos desenvolvedores e alcança alta cobertura técnica da lógica interna.',
        'O teste caixa cinza combina as duas perspectivas, com acesso parcial à estrutura interna, e costuma ser '
        'conduzido por testadores experientes ou pentesters.',
        'Uma limitação do teste caixa preta é não garantir que todos os caminhos internos do código tenham sido exercitados.',
    ],
    'A afirmação incorreta é a do teste caixa branca: ver o código dá alta cobertura técnica, mas não mostra se o '
    'sistema atende à necessidade real do usuário. Essa é justamente a sua limitação, e por isso ele não dispensa o '
    'caixa preta, que valida os requisitos. As demais alternativas descrevem corretamente a visibilidade, quem '
    'executa, as vantagens e as limitações de cada técnica.',
    contexto=[p('Uma empresa vai definir a estratégia de testes de um sistema de matrículas on-line. Na reunião, '
                'a equipe discute quem deve testar o quê e com qual nível de acesso ao código.')],
)

banco.multipla(
    'medio',
    'Qual reorganização do pipeline está de acordo com as boas práticas de automação de testes?',
    'Executar primeiro os testes unitários, depois os de integração e por último os E2E, interrompendo o pipeline '
    'na primeira falha, para que os defeitos mais simples sejam apontados em poucos minutos.',
    [
        'Manter os testes E2E no início, pois, por testarem o sistema inteiro, eles tornam desnecessária a execução '
        'dos testes unitários e de integração.',
        'Executar todas as etapas até o fim mesmo quando alguma falha, e liberar o deploy se a maioria dos testes passar.',
        'Fazer o deploy logo após o commit e rodar os testes depois, já em produção, para não atrasar as entregas.',
        'Remover os testes unitários e manter apenas os E2E, que são os mais próximos do uso real do sistema.',
    ],
    'Os testes unitários são os mais rápidos e baratos, por isso vêm primeiro: em poucos minutos, a equipe sabe se '
    'quebrou algo. Em seguida vêm os de integração e, por último, os E2E, os mais lentos e caros. Pela regra de ouro '
    'do pipeline, se um teste falha, o pipeline para e nenhum código com defeito avança; liberar o deploy com falhas '
    'ou testar só em produção contraria essa regra. Remover os unitários inverte a Pirâmide de Testes.',
    contexto=[p('O pipeline de uma equipe executa, nesta ordem: commit → testes E2E (50 minutos) → testes de integração '
                '(10 minutos) → testes unitários (3 minutos) → deploy. Quando um teste unitário falha, os '
                'desenvolvedores só ficam sabendo depois de mais de uma hora.')],
)

banco.multipla(
    'medio',
    'Considerando os conceitos de verificação e validação, o aplicativo está',
    'validado, mas não verificado: atende à necessidade real dos usuários, mas o código tem problemas técnicos que '
    'trarão dificuldades no futuro.',
    [
        'verificado, mas não validado: o código segue as especificações, mas não atende à necessidade dos usuários.',
        'verificado e validado, pois a aprovação dos usuários em testes reais comprova também a qualidade técnica do código.',
        'nem verificado nem validado, pois a validação só é possível depois que existem testes automatizados.',
        'apenas verificado, pois as sessões com os estudantes são uma forma de revisão de código.',
    ],
    'As sessões com usuários reais são validação, e os estudantes aprovaram: o aplicativo é o produto certo. '
    'Mas a verificação, que confere se o produto foi construído corretamente, falharia: não há testes nem revisão, '
    'e o código tem problemas técnicos (inclusive de segurança, ao montar consultas com o texto digitado). '
    'É o caso "válido, mas não verificado": o usuário aprova o resultado, mas o código trará dores de cabeça no futuro.',
    contexto=[p('Uma startup apresentou o protótipo de um aplicativo de caronas para universitários. Nas sessões de teste, '
                'os estudantes aprovaram o aplicativo e disseram que ele resolve exatamente o problema deles. Uma revisão '
                'técnica feita depois mostrou que não há nenhum teste automatizado, que as consultas ao banco de dados são '
                'montadas juntando o texto digitado pelo usuário, que há trechos de código copiados em vários lugares e '
                'que nenhum código passou por revisão.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.assercao(
    'dificil',
    'Mesmo com 100% de cobertura de linhas, a função ainda tem um defeito que o teste criado não é capaz de revelar.',
    'A cobertura de linhas indica apenas quais instruções foram executadas durante os testes; ela não garante que '
    'todos os desvios de decisão e os valores-limite da regra tenham sido verificados.',
    0,
    'As duas são verdadeiras, e a II explica a I. A regra diz "mais de 65 anos", mas o código usa >=: um cliente com '
    'exatamente 65 anos fica isento indevidamente. O único teste, com 70 anos, executa todas as linhas, mas só percorre '
    'o caminho em que a condição é verdadeira. Ficam sem teste o caminho falso (por exemplo, 30 anos) e o valor-limite '
    '(65 anos), que revelaria o defeito.',
    contexto=[
        p('Um banco definiu a regra: "clientes com mais de 65 anos são isentos da tarifa mensal de R$ 15,00". '
          'Um desenvolvedor escreveu a função abaixo e um único teste automatizado, que passou:'),
        codigo('''
def calcular_tarifa(idade):
    tarifa = 15
    if idade >= 65:
        tarifa = 0
    return tarifa

assert calcular_tarifa(70) == 0
'''),
        p('A ferramenta de análise mostrou 100% de cobertura de linhas, e o desenvolvedor concluiu que a função estava '
          'livre de defeitos.'),
    ],
)

banco.afirmativas(
    'dificil',
    [
        ('A falha só apareceu em 2024, mas o defeito existia no código desde a implantação do sistema.', True),
        ('Como o sistema funcionou durante três anos sem nenhuma falha, até fevereiro de 2024 era correto afirmar que '
         'ele estava livre de defeitos.', False),
        ('O erro foi o programador não considerar os anos bissextos; o defeito é a regra de fevereiro com 28 dias, '
         'escrita no código; a falha é o travamento observado no dia 29 de fevereiro de 2024.', True),
    ],
    'I é verdadeira: o defeito, a manifestação do erro no código, estava lá desde o início; ele só não tinha sido '
    'executado em uma situação que o revelasse. II é falsa: a ausência de falhas observadas não prova a ausência de '
    'defeitos, assim como os testes provam a presença de defeitos, mas não a sua ausência. III é verdadeira: erro é a '
    'ação humana, defeito é o que ficou no código e falha é o comportamento incorreto que o usuário observa.',
    contexto=[p('Um sistema de folha de pagamento foi implantado em 2021 e funcionou sem problemas por três anos. '
                'No dia 29 de fevereiro de 2024, ele gerou contracheques com data inválida e travou. A investigação '
                'mostrou que o programador, ao escrever a rotina de datas, não considerou os anos bissextos, e a função '
                'trata fevereiro sempre como um mês de 28 dias.')],
)

banco.multipla(
    'dificil',
    'Sobre a situação, assinale a alternativa correta.',
    'A desenvolvedora está na fase Green, em que se escreve o mínimo de código necessário para o teste passar; novos '
    'testes, com outros valores e com clientes não VIP, vão obrigar o código a se generalizar, e a fase Refactor '
    'melhora o código mantendo os testes passando.',
    [
        'O colega está certo: no TDD, o código deve ser escrito por completo antes do primeiro teste, e o teste só '
        'confirma o que já foi implementado.',
        'A desenvolvedora está na fase Red, pois a função ainda não calcula o desconto de forma geral.',
        'A desenvolvedora errou ao ver o teste falhar antes de escrever o código; no TDD, o teste deve passar já na '
        'primeira execução.',
        'A desenvolvedora está na fase Refactor, que consiste em escrever o código mínimo para o teste passar.',
    ],
    'O ciclo do TDD é Red (escrever um teste que falha), Green (escrever o mínimo de código para o teste passar) e '
    'Refactor (melhorar o código mantendo os testes passando). Ver o teste falhar primeiro é o passo Red, feito '
    'corretamente. Devolver 10 é o mínimo que faz o teste passar: é a fase Green. A função ainda não está completa, '
    'mas os próximos testes, que falharão com outros valores, vão exigir o cálculo de verdade.',
    contexto=[
        p('Uma desenvolvedora pratica TDD. Ela escreveu primeiro o teste abaixo, executou-o e viu que falhou. '
          'Em seguida, escreveu a função, e o teste passou.'),
        codigo('''
def test_desconto_cliente_vip():
    assert calcular_desconto(100, vip=True) == 10

def calcular_desconto(valor, vip):
    return 10
'''),
        p('Um colega criticou: "Isso não é TDD, é trapaça: a função devolve sempre 10".'),
    ],
)

banco.afirmativas(
    'dificil',
    [
        ('O teste feito pelo grupo de clientes é o último nível de validação antes da implantação em produção.', True),
        ('Por estar na linguagem do negócio, o cenário pode ser lido e conferido pela Product Owner, mesmo sem '
         'conhecimento de programação.', True),
        ('Como o cenário descreve o comportamento do sistema, ele substitui os testes unitários da função que '
         'calcula o saldo.', False),
        ('A linha iniciada por "Então" corresponde ao resultado esperado de um caso de teste.', True),
    ],
    'I é verdadeira: o teste de aceitação (UAT), feito pelos usuários finais, é o último nível antes da produção. '
    'II é verdadeira: o BDD usa Gherkin justamente para aproximar os testes da linguagem do negócio. '
    'III é falsa: o cenário fica no topo da Pirâmide de Testes e não substitui a base; a função do saldo continua '
    'precisando de testes unitários, rápidos e isolados. IV é verdadeira: o "Dado" traz as condições, o "Quando", '
    'a ação, e o "Então", o resultado esperado, as mesmas partes de um caso de teste.',
    contexto=[
        p('A equipe de um aplicativo bancário escreveu o cenário abaixo como critério de aceitação de uma nova '
          'funcionalidade. Antes da implantação, um grupo de clientes do banco vai usar o aplicativo para confirmar '
          'que ele atende ao que precisam.'),
        codigo('''
Cenário: Pagamento recusado por saldo insuficiente
  Dado que o cliente tem R$ 50,00 de saldo
  Quando ele tenta pagar uma compra de R$ 80,00
  Então o pagamento é recusado
  E o sistema mostra a mensagem "Saldo insuficiente"
'''),
    ],
)

banco.assercao(
    'dificil',
    'Por acessar o banco de dados real, esse teste é um teste unitário mais confiável do que um que use mock, '
    'pois trabalha com dados verdadeiros.',
    'O teste unitário verifica o menor componente testável de forma isolada, com as dependências externas '
    'substituídas por mocks ou stubs.',
    3,
    'A II é a definição correta de teste unitário. Por ela, a I é falsa: o teste depende do servidor e de um pedido '
    'que outras pessoas podem alterar, por isso falha sem que a função calcular_total tenha mudado. Ele não é isolado '
    'e, na prática, é um teste de integração. Para testar a função de forma unitária, o pedido deve ser montado no '
    'próprio teste ou fornecido por um mock ou stub, sempre com os mesmos dados.',
    contexto=[
        p('Uma equipe escreveu o teste abaixo, classificado como unitário, para a função que calcula o total de um pedido.'),
        codigo('''
def test_calcular_total_pedido():
    banco = conectar("servidor-producao.empresa.com")
    pedido = banco.buscar_pedido(1234)
    assert calcular_total(pedido) == 250.0
'''),
        p('O teste às vezes falha quando o servidor está lento ou quando alguém altera o pedido 1234, mesmo sem nenhuma '
          'mudança na função calcular_total.'),
    ],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"Testing is the process of executing a program with the intent of finding errors."',
        'traducao': '(Tradução livre: "Testar é o processo de executar um programa com a intenção de encontrar erros.")',
        'fonte': 'MYERS, G. J. The Art of Software Testing. New York: John Wiley & Sons, 1979.',
    },
    [
        'Em uma empresa que desenvolve um sistema de gestão escolar, cada desenvolvedor escreve os testes da própria '
        'funcionalidade quando termina de programá-la, usando apenas dados que sabe que funcionam: alunos com cadastro '
        'completo e notas válidas. Em todas as versões, o relatório mostra 100% dos testes passando, e o gerente '
        'apresenta esse número à diretoria como prova de que o sistema tem qualidade.',
        'Mesmo assim, as escolas relatam falhas frequentes: o sistema trava com notas em branco, calcula errado a média '
        'de alunos transferidos no meio do semestre e não aceita nomes com acento.',
    ],
    'Com base no texto de Myers e no caso apresentado, analise a forma como a equipe conduz os testes e o uso que o '
    'gerente faz do resultado "100% dos testes passando".',
    'Para Myers, testar é procurar defeitos; um bom teste é aquele que tem chance de revelar um defeito. A equipe faz o '
    'contrário: testa só o "caminho feliz", com dados que já sabe que funcionam, e por isso os testes apenas confirmam '
    'o que o desenvolvedor esperava, sem procurar problemas. O resultado de 100% dos testes passando mostra só que os '
    'casos pensados funcionam, e não que o sistema está livre de defeitos: testes provam a presença de defeitos, nunca '
    'a ausência. As falhas relatadas pelas escolas vêm de defeitos que já existiam e que nenhum caso de teste '
    'procurou. A equipe deveria criar casos de teste com entradas inválidas, vazias e incomuns (nota em branco, aluno '
    'transferido, nomes acentuados); incluir testes caixa preta feitos por testadores que comparem o sistema com os '
    'requisitos, sem o viés de quem escreveu o código; fazer testes exploratórios, que dependem da criatividade '
    'humana; e realizar testes de aceitação com as secretarias das escolas antes de cada versão.',
)

banco.discursiva(
    'dificil',
    {
        'citacao': '"Test-driven development is a way of managing fear during programming."',
        'traducao': '(Tradução livre: "O desenvolvimento guiado por testes é uma forma de administrar o medo durante a '
                    'programação.")',
        'fonte': 'BECK, K. Test-Driven Development: By Example. Boston: Addison-Wesley, 2003.',
    },
    [
        'Uma empresa mantém há dez anos o módulo de cálculo da folha de pagamento dos seus clientes. O módulo não tem '
        'testes automatizados, e os desenvolvedores evitam alterá-lo: quase toda mudança quebra alguma outra parte, '
        'e os problemas só aparecem no fim do mês, quando o setor de recursos humanos confere os contracheques.',
        'A empresa precisa incluir no módulo uma nova regra de adicional noturno e decidiu que, a partir de agora, '
        'toda regra nova será desenvolvida com TDD.',
    ],
    'Com base no texto de Beck e no caso apresentado, explique como o ciclo do TDD pode ajudar a equipe a lidar com o '
    '"medo" de alterar esse módulo.',
    'O medo vem da falta de retorno: hoje, a equipe só descobre que quebrou algo semanas depois, quando o erro já virou '
    'falha para o cliente. No TDD, o ciclo Red, Green e Refactor muda isso. Primeiro se escreve um teste que falha, '
    'descrevendo o comportamento esperado do adicional noturno (Red); depois, o mínimo de código para ele passar '
    '(Green); por fim, o código é melhorado com a segurança de que os testes continuam passando (Refactor). O teste '
    'documenta a regra antes da implementação, e o código já nasce testável. Cada teste criado fica na suíte e passa a '
    'funcionar como teste de regressão automatizado: rodando no pipeline a cada commit, ele aponta em minutos qualquer '
    'mudança que quebre uma regra já testada, e o pipeline para antes de o defeito chegar à produção, quando a correção '
    'ainda é barata. Com o tempo, a rede de testes cresce e a equipe passa a alterar o módulo com confiança. Para as '
    'partes antigas, vale escrever testes sobre o comportamento atual antes de mexer nelas.',
)


if __name__ == '__main__':
    banco.gravar()
