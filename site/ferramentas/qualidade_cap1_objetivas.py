"""
Questões médias e difíceis do capítulo 1 (Conceitos Básicos de Qualidade de Software) de Qualidade e
Testes de Software: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas
com um único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/qualidade_cap1_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap1-o* e
qualidade-cap1-d*; as que já existiam (q* e m*) e as dos outros capítulos ficam como estão.
O Custo da Qualidade já tem cinco questões no capítulo: aqui ele não é cobrado de novo.
"""

from engsoft_questoes import QUALIDADE, Banco, p

banco = Banco('qualidade-cap1', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As definições 1, 2 e 3 são, respectivamente, de',
    'Philip Crosby, Joseph Juran e IEEE Std 610.12.',
    [
        'Joseph Juran, Philip Crosby e IEEE Std 610.12.',
        'Philip Crosby, IEEE Std 610.12 e Joseph Juran.',
        'IEEE Std 610.12, Joseph Juran e Philip Crosby.',
        'Philip Crosby, Joseph Juran e ISO/IEC 25010.',
    ],
    'Pelo quadro de definições clássicas da apostila, "conformidade com os requisitos" é de Crosby (1979) (1); "adequação '
    'ao uso" é de Juran (1988) (2); e o grau em que o sistema atende aos requisitos especificados e às necessidades e '
    'expectativas do cliente ou usuário é a definição do IEEE Std 610.12 (3). A ISO/IEC 25010 fala em necessidades '
    'explícitas e implícitas dos usuários.',
    contexto=[p('Em uma prova, foram apresentadas três definições de qualidade: '
                '(1) "qualidade é a conformidade com os requisitos"; '
                '(2) "qualidade é a adequação ao uso"; '
                '(3) "qualidade de software é o grau em que um sistema, componente ou processo atende aos requisitos '
                'especificados e às necessidades e expectativas do cliente ou usuário".')],
)

banco.afirmativas(
    'medio',
    [
        ('Na perspectiva de Revisão do Produto estão a manutenibilidade, a flexibilidade e a testabilidade.', True),
        ('Na perspectiva de Transição do Produto estão a portabilidade, a reusabilidade e a interoperabilidade.', True),
        ('Na perspectiva de Operação do Produto estão a correção, a confiabilidade, a eficiência, a integridade e a '
         'usabilidade.', True),
        ('A testabilidade pertence à Operação do Produto, pois os testes são feitos com o sistema em execução.', False),
    ],
    'I, II e III reproduzem a tabela do Modelo de McCall da apostila: a Revisão trata da capacidade de mudança; a '
    'Transição, da adaptação a novos ambientes; e a Operação, das características de execução. IV é falsa: a '
    'testabilidade é um fator da Revisão do Produto, pois mede a facilidade de verificar o software depois de uma mudança.',
    contexto=[p('Ao estudar o Modelo de Fatores de McCall, de 1977, um aluno anotou quais fatores pertencem a cada uma das '
                'três perspectivas.')],
)

banco.multipla(
    'medio',
    'Os problemas 1, 2, 3 e 4 correspondem, respectivamente, aos fatores internos',
    'competência da equipe, adoção de boas práticas, gestão de configuração e ferramentas e infraestrutura.',
    [
        'adoção de boas práticas, competência da equipe, gestão de configuração e ferramentas e infraestrutura.',
        'competência da equipe, gestão de configuração, adoção de boas práticas e ferramentas e infraestrutura.',
        'qualidade dos requisitos, adoção de boas práticas, gestão de configuração e ferramentas e infraestrutura.',
        'competência da equipe, adoção de boas práticas, ferramentas e infraestrutura e gestão de configuração.',
    ],
    'O conhecimento do domínio e a experiência dos desenvolvedores são a competência da equipe (1). Padrões de '
    'codificação, revisão por pares, integração contínua e testes automatizados são a adoção de boas práticas (2). '
    'Controle de versões, gerenciamento de mudanças e rastreabilidade são a gestão de configuração (3). Ambientes '
    'adequados, análise estática e plataformas de teste automatizado são as ferramentas e a infraestrutura (4).',
    contexto=[p('Em um projeto de sistema contábil, a equipe identificou quatro problemas: '
                '(1) os desenvolvedores nunca trabalharam com contabilidade e não entendem as regras do negócio; '
                '(2) não há revisão de código nem integração contínua; '
                '(3) ninguém sabe qual versão do código está em produção nem qual requisito cada mudança atende; '
                '(4) não existe ambiente de testes nem ferramenta de análise estática.')],
)

banco.assercao(
    'medio',
    'Uma ambiguidade encontrada na revisão dos requisitos custa muito menos para ser corrigida do que o mesmo problema '
    'descoberto pelos usuários em produção.',
    'O custo de corrigir um defeito encontrado em produção pode ser até 100 vezes maior do que se ele fosse detectado na '
    'análise de requisitos.',
    0,
    'As duas são verdadeiras, e a II explica a I. Na revisão de requisitos, corrigir a ambiguidade é reescrever uma '
    'frase; em produção, é preciso refazer código, testes e documentação, além de lidar com os usuários afetados. É o '
    'primeiro exemplo que a apostila usa para mostrar a importância da qualidade.',
    contexto=[p('Em uma revisão de requisitos, uma analista percebeu que a regra "o desconto vale para clientes antigos" '
                'não dizia o que é um cliente antigo, e a equipe definiu o critério antes de começar a programar.')],
)

banco.multipla(
    'medio',
    'Qual fator que afeta a qualidade explica esse resultado?',
    'A pressão de prazo, um fator externo: o cronograma agressivo levou ao corte de testes e revisões e gerou débito '
    'técnico.',
    [
        'A complexidade do domínio, pois sistemas de comércio eletrônico exigem mais precisão que os de outras áreas.',
        'A competência da equipe, pois uma equipe experiente nunca deixaria de fazer os testes antes do lançamento.',
        'O ambiente de execução, pois os defeitos só aparecem nos servidores de produção, e não nos de teste.',
        'As dependências externas, pois as bibliotecas de terceiros foram as responsáveis pelos defeitos.',
    ],
    'Na apostila, a pressão de prazo é um fator externo ao processo: cronogramas agressivos frequentemente levam ao corte '
    'das atividades de teste e de revisão, o que gera débito técnico e aumenta os defeitos. É exatamente o caso: a equipe '
    'trocou testes e revisões por velocidade, e o resultado veio depois do lançamento.',
    contexto=[p('Para lançar uma loja virtual antes do Natal, a diretoria reduziu o prazo do projeto de seis para três '
                'meses. A equipe deixou de fazer as revisões de código e testou só as telas principais. Depois do '
                'lançamento, os defeitos se multiplicaram, e cada nova correção ficou mais demorada.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.assercao(
    'dificil',
    'Um sistema que atende a 100% dos requisitos escritos no contrato pode, ainda assim, ter baixa qualidade.',
    'Pela ISO/IEC 25010, qualidade é apenas a conformidade com os requisitos explícitos que aparecem no contrato.',
    2,
    'A I é verdadeira: os requisitos escritos raramente cobrem tudo o que os usuários precisam, e um sistema conforme ao '
    'contrato pode ser difícil de usar ou inadequado ao uso real. A II é falsa: a ISO/IEC 25010 define a qualidade como '
    'a capacidade de satisfazer as necessidades explícitas e também as implícitas dos usuários. A definição apenas pela '
    'conformidade é a de Crosby, e a apostila mostra que ela não basta sozinha.',
    contexto=[p('Uma empresa entregou um sistema de agendamento que cumpre todos os itens do contrato, mas os pacientes '
                'reclamam que não conseguem remarcar consultas pelo celular, algo que ninguém escreveu no contrato porque '
                'parecia óbvio.')],
)

banco.afirmativas(
    'dificil',
    [
        ('O caso do Therac-25 mostra que falhas de software em medicina podem custar vidas humanas.', True),
        ('O NIST estimou que os defeitos de software custam à economia americana mais de 60 bilhões de dólares por ano.',
         True),
        ('Corrigir um defeito em produção pode custar até 100 vezes mais do que corrigi-lo na análise de requisitos.', True),
        ('A qualidade de software é uma questão puramente técnica, sem impacto na reputação nem nas vendas da empresa.',
         False),
    ],
    'I, II e III são os exemplos que a apostila usa para mostrar a importância da qualidade: a segurança crítica, o '
    'impacto financeiro e o custo da correção tardia. IV é falsa: a apostila diz que a importância da qualidade vai além '
    'do aspecto técnico, e produtos de baixa qualidade comprometem a imagem da empresa e levam à perda de clientes e de '
    'oportunidades.',
    contexto=[p('Para convencer a diretoria a investir em qualidade, uma gerente reuniu argumentos sobre a importância da '
                'qualidade de software.')],
)

banco.multipla(
    'dificil',
    'No Modelo de McCall, as necessidades 1, 2, 3 e 4 pertencem, respectivamente, às perspectivas',
    'Operação do Produto, Operação do Produto, Transição do Produto e Revisão do Produto.',
    [
        'Operação do Produto, Revisão do Produto, Transição do Produto e Revisão do Produto.',
        'Revisão do Produto, Operação do Produto, Transição do Produto e Operação do Produto.',
        'Operação do Produto, Operação do Produto, Revisão do Produto e Transição do Produto.',
        'Transição do Produto, Operação do Produto, Transição do Produto e Revisão do Produto.',
    ],
    'Calcular os impostos corretamente é o fator correção, e proteger o acesso aos dados é o fator integridade: os dois '
    'são características de execução, da Operação do Produto (1 e 2). Reaproveitar um módulo em outro sistema é a '
    'reusabilidade, da Transição do Produto, que trata da adaptação a novos ambientes (3). Verificar o sistema com '
    'facilidade depois de cada mudança é a testabilidade, da Revisão do Produto, que trata da capacidade de mudança (4).',
    contexto=[p('A equipe de um sistema fiscal levantou quatro necessidades: '
                '(1) os impostos devem ser calculados sem erros; '
                '(2) apenas os contadores autorizados podem acessar as declarações; '
                '(3) o módulo de cálculo de impostos deve ser reaproveitado em um novo sistema de folha de pagamento; '
                '(4) depois de cada mudança na legislação, o sistema deve ser fácil de testar de novo.')],
)

banco.assercao(
    'dificil',
    'Um software tecnicamente correto, mas difícil de usar, não atende plenamente às expectativas dos usuários.',
    'O Modelo de McCall, proposto em 1977, organiza os fatores de qualidade em três perspectivas.',
    1,
    'As duas são verdadeiras, mas a II não explica a I. A I é a ideia de que a qualidade deve ser pensada nas dimensões '
    'técnica, funcional e de experiência, ligada à satisfação do usuário. A II é um fato sobre o Modelo de McCall (que '
    'inclui a usabilidade entre os fatores de Operação), mas a existência das três perspectivas não é o motivo pelo qual '
    'um sistema difícil de usar decepciona os usuários.',
    contexto=[p('Um aplicativo de banco passou em todos os testes funcionais, mas os clientes mais velhos desistem de usá-lo '
                'porque não encontram as opções nas telas.')],
)

banco.multipla(
    'dificil',
    'Sobre os fatores que afetam a qualidade do software, assinale a alternativa INCORRETA.',
    'As dependências externas, como APIs de terceiros, ficam totalmente sob o controle da equipe e, por isso, são um fator '
    'interno.',
    [
        'Requisitos ambíguos, incompletos ou inconsistentes são a principal fonte de defeitos de software.',
        'Variações de hardware, redes e configurações dos usuários fazem parte do ambiente de execução, um fator externo.',
        'Mudanças frequentes de escopo são um fator externo, que pode comprometer a integridade arquitetural do sistema.',
        'Ambientes de desenvolvimento, análise estática e plataformas de teste são fatores internos, de ferramentas e '
        'infraestrutura.',
    ],
    'A afirmação incorreta é a das dependências externas: pela apostila, bibliotecas, APIs e serviços de terceiros '
    'introduzem riscos que estão parcialmente fora do controle da equipe, e são um fator externo ao processo. As demais '
    'alternativas classificam corretamente os fatores internos e externos apresentados no capítulo.',
    contexto=[p('Em uma aula sobre os fatores que afetam a qualidade, a turma classificou vários fatores como internos ou '
                'externos ao processo de desenvolvimento.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Uma empresa foi contratada para desenvolver o sistema de controle de uma linha de produção industrial. Os '
        'requisitos chegaram em um documento curto e cheio de termos vagos, e o cliente muda as prioridades quase toda '
        'semana. A equipe é experiente em sites, mas nunca trabalhou com automação industrial. O sistema depende da API '
        'de um fornecedor de sensores, que costuma ficar instável, e o prazo foi reduzido em um terço depois da '
        'assinatura do contrato.',
    ],
    'Identifique os fatores internos e externos que ameaçam a qualidade desse projeto e proponha uma ação para cada um '
    'deles.',
    'Fatores internos: a qualidade dos requisitos, pois requisitos vagos são a principal fonte de defeitos (ação: '
    'elicitação cuidadosa e validação com o cliente antes de desenvolver); e a competência da equipe, que não conhece o '
    'domínio industrial (ação: capacitação, apoio de especialistas e revisões técnicas). Também conta a adoção de boas '
    'práticas e ferramentas, como revisão de código, integração contínua e testes automatizados, e a gestão de '
    'configuração, para controlar versões e mudanças. Fatores externos: a complexidade do domínio, pois um sistema de '
    'controle industrial exige confiabilidade e precisão muito maiores (ação: estratégia de testes mais rigorosa); as '
    'mudanças de requisitos (ação: gestão formal de mudanças e rastreabilidade); as dependências externas, com a API '
    'instável dos sensores (ação: tratar falhas da API, simulá-la nos testes e acompanhar o fornecedor); e a pressão de '
    'prazo, que tende a levar ao corte de testes e revisões (ação: renegociar escopo ou prazo e deixar explícito, para o '
    'cliente, o risco de cortar atividades de qualidade).',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Um banco vai contratar o desenvolvimento de um novo aplicativo para os seus clientes. A diretoria pediu ao '
        'gerente de projeto que defina, antes do início, "o que vai significar qualidade" para esse aplicativo, para '
        'poder cobrar do fornecedor.',
    ],
    'Com base no Modelo de McCall e na ISO/IEC 25010, explique quais características de qualidade deveriam ser '
    'priorizadas nesse aplicativo e por quê.',
    'Por ser um aplicativo bancário, algumas características pesam mais. Pela ISO/IEC 25010: a segurança (no McCall, a '
    'integridade), porque o aplicativo lida com dinheiro e dados pessoais e precisa garantir confidencialidade e '
    'integridade; a adequação funcional (no McCall, a correção), porque cálculos de saldo, juros e transferências não '
    'podem ter erro; a confiabilidade, porque os clientes precisam do aplicativo a qualquer hora e ele deve se recuperar '
    'bem de falhas; a usabilidade, porque o público é amplo, inclusive idosos, e um aplicativo correto, mas difícil de '
    'usar, não atende às expectativas; a eficiência de desempenho, por causa dos picos de uso, como no dia do salário; a '
    'compatibilidade, para trocar dados com os sistemas do banco e do Pix; e a manutenibilidade (no McCall, a Revisão do '
    'Produto), porque as regras do Banco Central mudam e o aplicativo precisará ser alterado e testado com frequência. A '
    'portabilidade também conta, para funcionar nos diferentes celulares. Para poder cobrar do fornecedor, cada '
    'característica deve virar um requisito com medida, como tempo de resposta, disponibilidade e tempo para concluir '
    'uma transferência.',
)


if __name__ == '__main__':
    banco.gravar()
