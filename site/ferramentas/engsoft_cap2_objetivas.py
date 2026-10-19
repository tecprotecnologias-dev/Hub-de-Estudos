"""
Questões médias e difíceis do capítulo 2 (Requisitos de Software) de Engenharia de Software e da
Usabilidade: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com
um único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/engsoft_cap2_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap2-o* e
engsoft-cap2-d*; as que já existiam (engsoft-cap2-q*) e as dos outros capítulos ficam como estão.
O cap. 10 também trata de requisitos: aqui ficam de fora os temas já cobrados lá.
"""

from engsoft_questoes import Banco, p

banco = Banco('engsoft-cap2')


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As técnicas de elicitação mais adequadas às situações 1, 2, 3 e 4 são, respectivamente,',
    'questionários, entrevistas, prototipagem e histórias de usuário.',
    [
        'entrevistas, questionários, prototipagem e histórias de usuário.',
        'questionários, entrevistas, histórias de usuário e prototipagem.',
        'prototipagem, entrevistas, questionários e histórias de usuário.',
        'questionários, prototipagem, entrevistas e histórias de usuário.',
    ],
    'Muitos usuários espalhados geograficamente, para validar prioridades, pedem questionários (1). Poucos '
    'stakeholders com conhecimento profundo, quando é preciso entender contexto e motivações, pedem entrevistas (2). '
    'Quando o usuário não consegue definir o que quer sem ver algo concreto, a prototipagem é a mais eficaz (3). Em um '
    'contexto ágil, que prioriza a comunicação, as histórias de usuário são a técnica natural (4).',
    contexto=[p('Uma empresa tem quatro projetos e precisa escolher como levantar os requisitos de cada um: '
                '(1) um aplicativo para os 3 mil agentes de saúde de cinco estados, que precisam indicar quais funções '
                'são mais urgentes; '
                '(2) um sistema de cálculo atuarial, que só três especialistas da seguradora entendem a fundo; '
                '(3) o novo painel de um aplicativo de investimentos, em que os clientes dizem que "só vão saber se '
                'gostam quando virem a tela"; '
                '(4) um aplicativo desenvolvido com Scrum, em que a equipe prefere conversar a produzir documentos '
                'formais.')],
)

banco.afirmativas(
    'medio',
    [
        ('A história 1 está incompleta, pois não informa o benefício que o gerente quer obter.', True),
        ('A história 2 é uma boa história de usuário, pois descreve uma necessidade do cliente.', False),
        ('A história 3 dispensa critérios de aceitação, pois o formato "Como, quero, para" já descreve o seu valor.',
         False),
        ('Para a história 3, "o usuário deve poder filtrar por período personalizado" pode ser um critério de aceitação.',
         True),
    ],
    'I é verdadeira: falta a parte "para [alcançar um objetivo]", que mostra o valor da história. II é falsa: escolher '
    'o banco de dados é uma decisão técnica, e não uma funcionalidade descrita do ponto de vista do usuário. III é '
    'falsa: toda história de usuário deve vir acompanhada de critérios de aceitação, que dizem quando ela está pronta. '
    'IV é verdadeira: é um dos critérios de aceitação que a própria apostila dá para a história do extrato.',
    contexto=[p('O backlog de um banco digital tem três itens: '
                '(1) "Como gerente, quero relatórios de vendas por período e por vendedor"; '
                '(2) "O sistema deve usar o banco de dados PostgreSQL"; '
                '(3) "Como cliente do banco, quero visualizar meu extrato dos últimos 90 dias, para controlar minhas '
                'despesas mensais".')],
)

banco.assercao(
    'medio',
    'Uma equipe que levanta os requisitos apenas lendo os manuais do sistema antigo, sem conversar com os stakeholders, '
    'corre o risco de chegar a requisitos incompletos.',
    'A elicitação é um processo humano e comunicativo, pois as pessoas nem sempre sabem exatamente o que querem ou têm '
    'dificuldade de expressar as suas necessidades.',
    0,
    'As duas são verdadeiras, e a II explica a I. Elicitar é descobrir as necessidades dos stakeholders. Como essas '
    'necessidades nem sempre estão claras nem escritas em algum lugar, elas precisam ser descobertas com as pessoas, '
    'por meio de entrevistas, workshops, observação e protótipos. Os manuais mostram como o sistema antigo funciona, '
    'mas não o que os usuários precisam hoje.',
    contexto=[p('Para substituir o sistema de uma transportadora, a equipe decidiu economizar tempo: em vez de falar com '
                'gerentes, motoristas e atendentes, levantou os requisitos lendo apenas os manuais do sistema antigo, '
                'escritos há quinze anos.')],
)

banco.multipla(
    'medio',
    'Os requisitos não funcionais 1, 2, 3 e 4 pertencem, respectivamente, às categorias',
    'escalabilidade, manutenibilidade, desempenho e confiabilidade.',
    [
        'desempenho, manutenibilidade, escalabilidade e confiabilidade.',
        'escalabilidade, usabilidade, desempenho e segurança.',
        'confiabilidade, manutenibilidade, desempenho e escalabilidade.',
        'escalabilidade, manutenibilidade, confiabilidade e desempenho.',
    ],
    'Crescer dez vezes sem refazer a arquitetura é escalabilidade, a capacidade de crescer sem degradação (1). Mudar '
    'uma regra de negócio alterando poucas classes é manutenibilidade, a facilidade de modificar e evoluir (2). '
    'Responder em 2 segundos com mil usuários é desempenho, que trata de tempo de resposta e throughput (3). Continuar '
    'funcionando, sem perder dados, quando um servidor cai é confiabilidade, que envolve disponibilidade, tolerância a '
    'falhas e recuperação (4).',
    contexto=[p('O documento de requisitos de um sistema de matrículas traz quatro requisitos não funcionais: '
                '(1) "O sistema deve suportar um crescimento de 10 vezes no volume de dados sem refatoração da '
                'arquitetura"; '
                '(2) "Alterações nas regras de matrícula não devem exigir mudanças em mais de 3 classes"; '
                '(3) "O sistema deve responder a qualquer consulta em até 2 segundos para até 1.000 usuários '
                'simultâneos"; '
                '(4) "Se um servidor falhar, outro deve assumir o atendimento sem perda de dados".')],
)

banco.multipla(
    'medio',
    'A forma mais adequada de verificar os requisitos 1 e 2 é, respectivamente:',
    'um teste funcional (caixa preta), comparando os valores calculados, e um teste de performance, medindo o tempo.',
    [
        'um teste de performance, medindo o tempo do cálculo, e um teste funcional, comparando os valores calculados.',
        'um teste funcional para os dois, pois ambos tratam do mesmo cálculo e podem ser conferidos pelo resultado.',
        'uma revisão do código para os dois, pois requisitos de cálculo não podem ser verificados com testes.',
        'um teste de usabilidade com contribuintes, para o primeiro, e um teste de segurança, para o segundo.',
    ],
    'O requisito 1 diz o que o sistema faz: é funcional e é verificado por testes funcionais (caixa preta), que '
    'conferem se o resultado está certo. O requisito 2 diz como o sistema se comporta: é não funcional, da categoria '
    'desempenho, e é verificado por um teste de performance, que mede o tempo. Conferir só o resultado não mostra se o '
    'cálculo levou menos de 1 segundo.',
    contexto=[p('Uma equipe vai planejar os testes de dois requisitos de um sistema de declaração de imposto: '
                '(1) "O sistema deve calcular o IRPF devido a partir dos rendimentos e deduções informados"; '
                '(2) "O cálculo deve ser concluído em menos de 1 segundo".')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Sobre os artefatos de documentação de requisitos, assinale a alternativa INCORRETA.',
    'O Backlog do Produto é aprovado uma única vez, no início, e não deve mudar, pois é o contrato técnico entre o '
    'cliente e a equipe.',
    [
        'O Documento de Visão descreve o problema, os stakeholders e a proposta de valor, de forma acessível a públicos '
        'técnicos e não técnicos.',
        'No contexto ágil, o Backlog do Produto substitui o SRS formal e é gerenciado continuamente pelo Product Owner.',
        'Os protótipos servem para documentar e validar requisitos de interface e de comportamento antes do '
        'desenvolvimento.',
        'O SRS é o artefato mais completo e formal, baseado na IEEE 830, com requisitos funcionais e não funcionais.',
    ],
    'A afirmação incorreta é a do Backlog do Produto: ele é vivo, cresce e se reorganiza ao longo do projeto, gerenciado '
    'continuamente pelo PO. O artefato que funciona como contrato técnico entre cliente e equipe é o SRS. As demais '
    'alternativas descrevem corretamente o Documento de Visão, o papel do backlog no ágil, os protótipos e o SRS.',
    contexto=[p('Na primeira reunião de um projeto, a equipe discutiu quais artefatos usaria para registrar os requisitos '
                'e qual o papel de cada um.')],
)

banco.afirmativas(
    'dificil',
    [
        ('Os protótipos são muito eficazes para refinar requisitos de interface e de interação.', True),
        ('Além de ajudar a levantar requisitos, os protótipos podem servir para documentá-los e validá-los com o '
         'usuário antes do desenvolvimento.', True),
        ('A prototipagem é a técnica mais adequada para conhecer as prioridades dos 40 mil clientes da rede, espalhados '
         'pelo país.', False),
        ('Por mostrar algo concreto, o protótipo ajuda quando o usuário não consegue definir o que quer sem ver a tela.',
         True),
    ],
    'I é verdadeira: os protótipos, de baixa ou alta fidelidade, permitem que o usuário reaja a algo concreto, o que '
    'refina os requisitos de interface. II é verdadeira: a apostila os cita também como artefato de documentação e '
    'validação. III é falsa: para muitos usuários dispersos geograficamente, a técnica indicada é o questionário. IV é '
    'verdadeira: é justamente o caso em que a prototipagem é a mais indicada.',
    contexto=[p('Uma rede de supermercados, com 40 mil clientes cadastrados no país inteiro, vai criar um aplicativo de '
                'compras. Os gerentes de marketing dizem que "só vão saber como querem a tela de ofertas quando virem '
                'uma". A equipe pretende usar protótipos.')],
)

banco.assercao(
    'dificil',
    'Como os requisitos não funcionais não descrevem funcionalidades isoladas, a violação deles não chega a afetar os '
    'usuários do aplicativo.',
    'Os requisitos não funcionais definem propriedades sistêmicas: qualidades, restrições e atributos que permeiam todo '
    'o sistema.',
    3,
    'A II é a definição correta, e é justamente por ela que a I é falsa. Por serem propriedades do sistema todo, os '
    'requisitos não funcionais afetam todas as funcionalidades ao mesmo tempo. Quando são violados, o sistema fica '
    'lento, inseguro, inacessível ou ilegal, como mostra o caso. Eles são tão críticos quanto os funcionais.',
    contexto=[p('Todas as funcionalidades de um aplicativo de delivery foram implementadas e passaram nos testes. Mesmo '
                'assim, depois do lançamento, as avaliações despencaram: cada tela leva dez segundos para abrir, e o '
                'aplicativo fica fora do ar nos horários de almoço e jantar.')],
)

banco.multipla(
    'dificil',
    'Na priorização do MVP pela técnica MoSCoW, os itens 1, 2, 3 e 4 são, respectivamente,',
    'Must Have, Should Have, Could Have e Won\'t Have.',
    [
        'Must Have, Must Have, Should Have e Could Have.',
        'Should Have, Must Have, Could Have e Won\'t Have.',
        'Must Have, Could Have, Should Have e Won\'t Have.',
        'Must Have, Should Have, Won\'t Have e Could Have.',
    ],
    'Sem login, o aplicativo não pode ser entregue: Must Have (1). A exportação em PDF é importante, mas existe um '
    'contorno, a impressão da tela: Should Have (2). O tema escuro é desejável, de menor impacto, e entra só se sobrar '
    'tempo: Could Have (3). A integração com o relógio está fora desta versão, mas fica documentada para o futuro: '
    'Won\'t Have (4), que significa "não agora", e não "nunca".',
    contexto=[p('Na lista do MVP de um aplicativo de academia, estão: '
                '(1) login com e-mail e senha, sem o qual ninguém consegue usar o aplicativo; '
                '(2) exportar o treino em PDF, que é importante, mas pode ser substituído por enquanto pela impressão da '
                'tela; '
                '(3) tema escuro, que "seria legal ter"; '
                '(4) integração com relógios inteligentes, que ficou para uma versão futura e foi registrada no backlog.')],
)

banco.multipla(
    'dificil',
    'A análise correta da situação é:',
    'Os requisitos tendem a ficar incompletos, pois elicitar é levantar as necessidades de todos os stakeholders, e '
    'não só de quem contrata.',
    [
        'O procedimento está correto, pois quem paga pelo sistema é o único stakeholder que pode definir os requisitos '
        'do aplicativo.',
        'O procedimento está correto, desde que o diretor aprove o SRS, pois a aprovação garante que os requisitos estão '
        'completos.',
        'O problema é só de priorização, que se resolve classificando os pedidos do diretor com a técnica MoSCoW antes '
        'do desenvolvimento.',
        'Pais e professores devem ser ouvidos apenas depois da implantação, na fase de manutenção, por meio de chamados '
        'de suporte.',
    ],
    'Stakeholders são todas as partes interessadas: clientes, usuários, gestores e equipe técnica. Ouvir apenas o '
    'diretor deixa de fora quem vai usar o aplicativo todos os dias, e os requisitos ficam incompletos. Os pais, que '
    'são muitos, poderiam responder a questionários; os professores, a entrevistas; e a equipe de TI traria as '
    'restrições técnicas. Aprovar o documento ou priorizar não corrige o que nunca foi levantado, e deixar para a '
    'manutenção sai muito mais caro.',
    contexto=[p('Para criar o aplicativo de comunicação entre uma escola e as famílias, o analista fez todas as reuniões '
                'apenas com o diretor, que é quem está contratando o sistema. Os 600 pais, os 40 professores e a pequena '
                'equipe de TI da escola não foram consultados.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"A user story describes functionality that will be valuable to either a user or purchaser of a '
                   'system or software."',
        'traducao': '(Tradução livre: "Uma história de usuário descreve uma funcionalidade que terá valor para um '
                    'usuário ou para quem compra um sistema ou software.")',
        'fonte': 'COHN, M. User Stories Applied: For Agile Software Development. Boston: Addison-Wesley, 2004.',
    },
    [
        'O backlog de um aplicativo de agendamento para salões de beleza tem itens como: "Criar a tabela de clientes no '
        'banco de dados", "Tela bonita", "Agenda" e "Como usuário, quero que tudo funcione". A equipe não sabe por onde '
        'começar, e a Product Owner não consegue dizer quando cada item estaria pronto.',
    ],
    'Com base no texto de Cohn e no caso apresentado, analise os itens desse backlog e explique como eles deveriam ser '
    'reescritos.',
    'Nenhum dos itens descreve uma funcionalidade com valor para o usuário. "Criar a tabela de clientes" é uma tarefa '
    'técnica, e não algo que o cliente do salão perceba. "Tela bonita" e "Agenda" são vagos: não dizem quem usa, o que '
    'quer fazer nem para quê. "Quero que tudo funcione" segue o formato, mas não descreve nenhuma funcionalidade. Os '
    'itens deveriam seguir o formato "Como [tipo de usuário], quero [ação], para [benefício]", que deixa claro quem '
    'ganha e qual é o valor. Por exemplo: "Como cliente do salão, quero agendar um horário pelo celular, para não '
    'precisar telefonar" e "Como cabeleireira, quero ver os agendamentos do dia, para organizar meu trabalho". Cada '
    'história deve vir com critérios de aceitação, que dizem quando ela está pronta; para a primeira: o cliente vê só '
    'os horários livres, escolhe o serviço e o profissional, e recebe uma confirmação. Assim a equipe sabe o que '
    'construir, e a PO consegue priorizar pelo valor e dizer quando cada item está concluído.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma empresa desenvolveu uma plataforma de venda de ingressos. Todos os requisitos funcionais foram '
        'implementados: buscar eventos, escolher o assento, pagar e receber o ingresso por e-mail. No dia da venda de '
        'um grande show, 200 mil pessoas acessaram o site ao mesmo tempo. As páginas passaram a levar mais de 40 '
        'segundos para abrir, o site saiu do ar duas vezes, e algumas compras foram cobradas, mas os ingressos não '
        'foram emitidos. O documento de requisitos dizia apenas que "o sistema deve ser rápido e estável".',
    ],
    'Analise o caso e explique quais requisitos não funcionais deveriam ter sido especificados, e de que forma, para '
    'evitar esses problemas.',
    'O sistema fazia tudo o que devia, mas falhou em como devia se comportar, o que mostra que os requisitos não '
    'funcionais são tão críticos quanto os funcionais. "Rápido e estável" é vago e não verificável. Deveriam ter sido '
    'especificados, de forma mensurável: desempenho, como "as páginas de compra devem abrir em até 3 segundos para até '
    '200 mil usuários simultâneos"; escalabilidade, como "o sistema deve suportar picos de 10 vezes o acesso normal sem '
    'degradação"; confiabilidade, como "disponibilidade de 99,9% durante as vendas" e "nenhuma compra paga pode ficar '
    'sem ingresso emitido; em caso de falha, a operação deve ser desfeita ou concluída"; e segurança, já que há '
    'pagamentos e dados pessoais, com conformidade com a LGPD. Escritos assim, cada requisito tem uma única '
    'interpretação e pode ser verificado com testes de performance, de carga e de recuperação antes do lançamento, e '
    'não descoberto no dia do show.',
)


if __name__ == '__main__':
    banco.gravar()
