"""
Questões médias e difíceis do capítulo 10 (Engenharia de Requisitos) de Engenharia de Software e
da Usabilidade: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas
com um único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/engsoft_cap10_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap10-o* e
engsoft-cap10-d*; as que já existiam (engsoft-cap10-m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import Banco, p

banco = Banco('engsoft-cap10')


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Os desafios das situações 1, 2, 3 e 4 e as formas mais adequadas de endereçá-los são, respectivamente:',
    'conflitos de interesse (workshop JAD com facilitador neutro), expectativas implícitas (prototipagem rápida), '
    'volatilidade (gestão de mudanças e arquitetura flexível) e escopo inflado (MoSCoW e valor vs. esforço).',
    [
        'volatilidade (gestão de mudanças), conhecimento tácito (observação etnográfica), conflitos de interesse '
        '(workshop JAD) e escopo inflado (MoSCoW).',
        'conflitos de interesse (MoSCoW), expectativas implícitas (observação etnográfica), escopo inflado (prototipagem '
        'rápida) e volatilidade (workshop JAD).',
        'escopo inflado (workshop JAD), conhecimento tácito (prototipagem rápida), volatilidade (gestão de mudanças) e '
        'conflitos de interesse (MoSCoW).',
        'conflitos de interesse (workshop JAD), volatilidade (prototipagem rápida), expectativas implícitas (gestão de '
        'mudanças) e escopo inflado (MoSCoW).',
    ],
    'Diretores com prioridades opostas são um conflito de interesse, tratado em um workshop JAD com facilitador neutro '
    '(1). Deixar de citar algo por achar óbvio é uma expectativa implícita, que aparece quando o usuário vê um protótipo '
    '(2). Uma lei nova que muda uma regra é volatilidade, tratada com gestão de mudanças e arquitetura flexível (3). '
    'Uma lista enorme em que tudo parece essencial é escopo inflado, tratado com MoSCoW e valor vs. esforço (4).',
    contexto=[p('No levantamento de requisitos de um sistema para uma rede de lojas: '
                '(1) o diretor de vendas quer liberar descontos pelo celular dos vendedores, e o diretor financeiro quer '
                'que todo desconto passe por sua aprovação; '
                '(2) ninguém mencionou que o sistema precisa imprimir a nota fiscal, porque "isso é óbvio"; '
                '(3) no meio do projeto, uma nova lei mudou a forma de calcular um imposto; '
                '(4) os gerentes entregaram uma lista com 120 funcionalidades, todas marcadas como indispensáveis.')],
)

banco.afirmativas(
    'medio',
    [
        ('O saldo insuficiente e o cartão bloqueado devem ser documentados como fluxos alternativos ou de exceção do '
         'caso de uso.', True),
        ('Como o caso de uso descreve o caminho em que tudo dá certo, ele não é adequado para documentar situações de '
         'erro, que ficam para os testes.', False),
        ('O caso de uso descreve a interação entre um ator, o cliente, e o sistema, e pode ser documentado com um '
         'diagrama UML e uma descrição textual.', True),
    ],
    'I é verdadeira: além do fluxo principal, o caso de uso registra os fluxos alternativos e de exceção. II é falsa: '
    'documentar as exceções é justamente uma das vantagens dos casos de uso, pois elas costumam ser esquecidas em outras '
    'técnicas. III é verdadeira: casos de uso descrevem interações entre atores e o sistema, com diagramas UML e '
    'descrição textual.',
    contexto=[p('Um analista está documentando o caso de uso "Sacar dinheiro" de um caixa eletrônico. No fluxo principal, '
                'o cliente insere o cartão, digita a senha, escolhe o valor e retira as notas. Durante a conversa com o '
                'banco, surgiram duas situações: o cliente sem saldo suficiente e o cartão bloqueado.')],
)

banco.multipla(
    'medio',
    'Os requisitos 1, 2, 3 e 4 falham, respectivamente, nos atributos de qualidade',
    'completo, viável, não ambíguo e rastreável.',
    [
        'correto, verificável, completo e rastreável.',
        'completo, correto, não ambíguo e viável.',
        'não ambíguo, viável, completo e verificável.',
        'completo, viável, rastreável e não ambíguo.',
    ],
    'O requisito 1 não diz o que acontece quando o e-mail é inválido: não cobre todas as situações relevantes, logo não '
    'é completo. O 2 não pode ser implementado com aquele orçamento: não é viável. No 3, "recentes" pode ser 24 horas ou '
    'um mês: tem mais de uma interpretação, logo é ambíguo. O 4 não pode ser ligado a quem o pediu nem ao objetivo que '
    'atende: não é rastreável.',
    contexto=[p('Ao revisar o documento de requisitos de uma loja virtual, uma analista separou quatro requisitos: '
                '(1) "O sistema deve enviar o boleto por e-mail ao cliente", sem dizer o que fazer quando o e-mail '
                'informado for inválido; '
                '(2) "O sistema deve funcionar 100% do tempo, sem nenhuma interrupção", em um projeto com orçamento de '
                'R$ 5 mil; '
                '(3) "A tela inicial deve exibir os pedidos recentes do cliente"; '
                '(4) "O sistema deve gerar um relatório de devoluções por região", que ninguém sabe dizer quem pediu nem '
                'para que serve.')],
)

banco.assercao(
    'medio',
    'A história 2 não atende ao critério Independente do INVEST.',
    'Uma história Independente pode entrar em uma sprint sem depender de outra história.',
    0,
    'As duas são verdadeiras, e a II explica a I. A história 2 só pode ser feita se a 1 já existir, pois não há como '
    'pagar com um cartão salvo antes de existir o cadastro de cartões. Ela depende de outra história e, por isso, não '
    'pode entrar sozinha em uma sprint.',
    contexto=[p('No Product Backlog de um aplicativo de delivery, estão as histórias: (1) "Como cliente, quero cadastrar '
                'um cartão de crédito, para não digitá-lo a cada compra"; (2) "Como cliente, quero pagar com um cartão '
                'salvo, para concluir o pedido mais rápido". A Product Owner quer colocar só a história 2 na próxima '
                'sprint, e a história 1 ainda não foi feita.')],
)

banco.multipla(
    'medio',
    'Seguindo a estrutura do SRS (IEEE 830), os itens 1, 2, 3 e 4 devem ficar, respectivamente, nas seções',
    'Requisitos de Interface, Requisitos Não Funcionais, Introdução e Apêndices.',
    [
        'Requisitos Funcionais, Requisitos Não Funcionais, Descrição Geral e Apêndices.',
        'Requisitos de Interface, Requisitos Funcionais, Introdução e Descrição Geral.',
        'Descrição Geral, Requisitos Não Funcionais, Apêndices e Introdução.',
        'Requisitos Não Funcionais, Requisitos de Interface, Introdução e Apêndices.',
    ],
    'A comunicação com um sistema externo, como a API dos Correios, é um requisito de interface (1). O tempo de '
    'resposta é desempenho, um requisito não funcional (2). Propósito e escopo do documento ficam na Introdução (3). '
    'Diagramas UML, modelos de dados e glossário vão para os Apêndices (4).',
    contexto=[p('Uma analista está organizando o SRS de uma loja virtual e precisa encaixar quatro itens: '
                '(1) a troca de dados com a API dos Correios para calcular o frete; '
                '(2) a exigência de que a página de busca responda em até 2 segundos; '
                '(3) o propósito do documento e o escopo do sistema; '
                '(4) o diagrama de classes UML do módulo de pedidos.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'As abordagens de requisitos mais adequadas aos projetos 1, 2 e 3 são, respectivamente:',
    'ágil, tradicional e híbrida.',
    [
        'tradicional, ágil e híbrida.',
        'híbrida, tradicional e ágil.',
        'ágil, híbrida e tradicional.',
        'ágil, ágil e ágil, pois a abordagem ágil é adequada a qualquer projeto.',
    ],
    'Na startup, os requisitos ainda estão sendo descobertos e mudam a cada semana: o backlog priorizado e evolutivo, '
    'com detalhamento just-in-time, é o mais adequado (1). No contrato de escopo fechado, com requisitos estáveis e '
    'aprovação formal antes do desenvolvimento, cabe a abordagem tradicional, com SRS completo (2). No banco, as regras '
    'do BACEN e da LGPD exigem documentação formal e auditável, mas as novidades saem a cada sprint: a híbrida combina '
    'documento de visão e roadmap formais com um backlog ágil (3).',
    contexto=[p('Uma empresa tem três projetos: '
                '(1) o aplicativo de uma startup que ainda está testando ideias com os primeiros clientes e muda de '
                'direção quase toda semana; '
                '(2) um sistema contratado por licitação, com escopo fechado, requisitos estáveis e que precisam ser '
                'aprovados formalmente antes do início do desenvolvimento; '
                '(3) o aplicativo de um banco, que precisa cumprir normas do BACEN e da LGPD, sujeitas a auditoria, e '
                'lançar novidades a cada sprint.')],
)

banco.afirmativas(
    'dificil',
    [
        ('A distribuição indica escopo inflado, pois os requisitos Must Have somam 75% do esforço, acima dos 60% '
         'recomendados.', True),
        ('Para seguir a regra prática, os requisitos Must Have deveriam somar no máximo 160 horas.', False),
        ('Com tantos requisitos obrigatórios, sobra pouco espaço de negociação caso o projeto atrase.', True),
        ('Para cada requisito Must Have, a pergunta a fazer é se o produto pode ser lançado sem ele; se puder, ele '
         'não é Must Have.', True),
    ],
    'I é verdadeira: 300 de 400 horas são 75% do esforço, acima do limite de 60%. II é falsa: 60% de 400 horas são '
    '240 horas; 160 horas seriam 40%. III é verdadeira: quando quase tudo é obrigatório, não há o que tirar do escopo '
    'para acomodar um atraso, que é o sintoma do escopo inflado. IV é verdadeira: Must Have é o que, se faltar, impede '
    'o lançamento; o que é importante, mas não impede, é Should Have.',
    contexto=[p('Na priorização do MVP de um aplicativo de agendamento, com esforço total estimado em 400 horas, a equipe '
                'chegou a: Must Have, 300 horas; Should Have, 60 horas; Could Have, 40 horas. Alguns itens ficaram como '
                'Won\'t Have.')],
)

banco.assercao(
    'dificil',
    'Como corrigir um erro de requisito durante os testes pode custar vinte vezes mais, a equipe deve congelar todos os '
    'requisitos no início do projeto e recusar qualquer mudança posterior.',
    'O custo de corrigir um erro de requisito cresce conforme o projeto avança.',
    3,
    'A II é verdadeira, mas a conclusão da I é falsa. O custo crescente é um motivo para cuidar bem da elicitação, da '
    'análise e da validação, e não para proibir mudanças. Os requisitos mudam porque os negócios evoluem e as leis se '
    'atualizam (volatilidade). A resposta adequada é a gestão de mudanças, com análise de impacto pela matriz de '
    'rastreabilidade, e uma arquitetura flexível.',
    contexto=[p('Depois de um projeto em que um requisito mal entendido só foi descoberto nos testes, o diretor de uma '
                'empresa propôs uma nova regra para todos os projetos.')],
)

banco.multipla(
    'dificil',
    'A análise correta da situação é:',
    'É uma expectativa implícita: o cliente considerou o requisito óbvio e não o mencionou; protótipos rápidos, '
    'mostrados no início, teriam feito a falta aparecer antes do desenvolvimento.',
    [
        'É conhecimento tácito: o cliente sabe imprimir as etiquetas, mas não consegue explicar como; a observação '
        'etnográfica resolveria o problema sem precisar de protótipos.',
        'É volatilidade: o requisito surgiu depois, por uma mudança no negócio do cliente, e deve entrar pela gestão de '
        'mudanças.',
        'É um conflito de interesses entre o cliente e a equipe, que deveria ter sido resolvido em um workshop JAD.',
        'Não há falha na elicitação: como o SRS foi aprovado, o cliente é o único responsável pela ausência do requisito.',
    ],
    'O cliente sempre precisou imprimir etiquetas e não falou disso porque achou óbvio: é uma expectativa implícita, '
    'que a prototipagem rápida revela, pois ao ver a tela o usuário percebe o que falta. Não é conhecimento tácito, '
    'em que a pessoa sabe fazer, mas não consegue explicar; aqui ela explicaria sem dificuldade, só não mencionou. '
    'Também não é volatilidade, pois a necessidade não mudou. E a aprovação do SRS não elimina a falha: descobrir isso '
    'só agora sai muito mais caro.',
    contexto=[p('Uma transportadora aprovou o SRS do seu novo sistema de pedidos. Ao ver a primeira versão funcionando, '
                'o gerente de expedição perguntou: "Cadê o botão para imprimir a etiqueta de envio? Sem isso não dá para '
                'despachar nada". A impressão de etiquetas não aparece em nenhuma parte do documento, e ninguém da '
                'transportadora tinha falado dela nas entrevistas.')],
)

banco.multipla(
    'dificil',
    'Sobre requisitos em contextos ágeis, assinale a alternativa INCORRETA.',
    'Em projetos ágeis, o objetivo é eliminar a documentação de requisitos, substituindo-a apenas por conversas entre a '
    'equipe e o cliente.',
    [
        'Na abordagem ágil, o Product Backlog é priorizado e evolutivo, e o detalhamento de cada item é feito '
        'just-in-time, perto do momento de desenvolvê-lo.',
        'Uma boa história de usuário deve ser pequena o suficiente para ser concluída em um a três dias.',
        'Critérios de aceitação escritos em Gherkin conectam os requisitos diretamente a testes automatizáveis.',
        'Em sistemas com requisitos regulatórios, a abordagem híbrida documenta formalmente os requisitos não funcionais '
        'e arquiteturais e mantém um backlog ágil detalhado.',
    ],
    'A afirmação incorreta é a primeira: em projetos ágeis, a especificação é mais leve e evolutiva, mas o objetivo não '
    'é eliminar a documentação, e sim ter a quantidade certa, no momento certo. As demais estão corretas: backlog '
    'evolutivo com detalhamento just-in-time, histórias pequenas (o "S" do INVEST), critérios de aceitação em Gherkin '
    'e abordagem híbrida para requisitos regulatórios.',
    contexto=[p('Uma equipe que sempre trabalhou com SRS completo, aprovado antes do desenvolvimento, vai passar a usar '
                'Scrum. Na reunião de transição, os membros discutem como os requisitos passarão a ser tratados.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"The hardest single part of building a software system is deciding precisely what to build."',
        'traducao': '(Tradução livre: "A parte mais difícil de construir um sistema de software é decidir com precisão '
                    'o que construir.")',
        'fonte': 'BROOKS, F. P. No Silver Bullet: Essence and Accidents of Software Engineering. Computer, v. 20, '
                 'n. 4, p. 10-19, 1987.',
    },
    [
        'Para levantar os requisitos de um sistema de agendamento de cirurgias, o analista fez uma única entrevista, '
        'com o diretor do hospital. Com base nela, escreveu o documento de requisitos, que o diretor aprovou.',
        'Três meses depois da implantação, as equipes do centro cirúrgico voltaram a usar planilhas em papel: o sistema '
        'não considera o tempo de esterilização das salas nem a disponibilidade dos anestesistas, e a ordem de '
        'prioridade das cirurgias definida pela diretoria é diferente da que os cirurgiões usam no dia a dia.',
    ],
    'Com base no texto de Brooks e no caso apresentado, explique como a elicitação de requisitos deveria ter sido '
    'conduzida nesse projeto.',
    'O analista decidiu "o que construir" ouvindo uma única pessoa, que não executa o trabalho. A elicitação deveria ter '
    'começado pela identificação de todos os envolvidos: cirurgiões, anestesistas, enfermeiros e equipe de '
    'esterilização, além da diretoria. Como quem faz o trabalho tem conhecimento tácito, difícil de explicar em '
    'entrevista, a observação etnográfica do centro cirúrgico revelaria regras como o tempo de esterilização. '
    'Protótipos rápidos mostrados a essas equipes fariam aparecer as expectativas implícitas, como a disponibilidade '
    'dos anestesistas. O conflito entre as prioridades da diretoria e as dos cirurgiões deveria ser tratado em um '
    'workshop JAD, com facilitador neutro. Os casos de uso ajudariam a documentar as exceções, como cancelamentos e '
    'emergências. Por fim, os requisitos deveriam ser analisados quanto aos atributos de qualidade, como completo e '
    'correto, e validados com os usuários antes do desenvolvimento, já que corrigir um erro de requisito depois custa '
    'muito mais.',
)

banco.discursiva(
    'dificil',
    {
        'citacao': '"Working software over comprehensive documentation."',
        'traducao': '(Tradução livre: "Software em funcionamento mais do que documentação abrangente.")',
        'fonte': 'BECK, K. et al. Manifesto for Agile Software Development. 2001. Disponível em: agilemanifesto.org.',
    },
    [
        'Inspirada no Manifesto Ágil, uma equipe decidiu não escrever nada além do título das histórias de usuário, como '
        '"Como gerente, quero gerenciar os pedidos". Não há critérios de aceitação. Ao fim de cada sprint, a Product '
        'Owner e os desenvolvedores discordam sobre o que estava combinado, e boa parte das histórias volta para ser '
        'refeita.',
    ],
    'Com base no texto e no caso apresentado, explique como a equipe deveria especificar os seus requisitos para seguir '
    'o Manifesto Ágil sem cair no retrabalho.',
    'O Manifesto valoriza mais o software funcionando, mas não manda eliminar a documentação: em contextos ágeis, o '
    'objetivo é ter a quantidade certa de documentação, no momento certo. A equipe confundiu especificação leve com '
    'ausência de especificação. Primeiro, as histórias deveriam atender ao INVEST: "gerenciar os pedidos" é grande demais '
    'e difícil de estimar, e deveria ser dividida em histórias pequenas, como "cancelar um pedido" e "alterar o endereço '
    'de entrega". Depois, cada história precisa de critérios de aceitação objetivos, que a tornem testável; escritos em '
    'Gherkin (Dado/Quando/Então), eles deixam claro o que a PO espera e podem virar testes automatizados. Esse '
    'detalhamento é feito just-in-time, no refinamento, pouco antes de a história entrar na sprint. Assim, a discussão '
    'sobre o que estava combinado acontece antes do desenvolvimento, e não depois, quando refazer custa mais.',
)


if __name__ == '__main__':
    banco.gravar()
