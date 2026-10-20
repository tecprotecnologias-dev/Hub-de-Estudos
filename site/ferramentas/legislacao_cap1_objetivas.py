"""
Questões médias e difíceis do capítulo 1 (Proteção de Dados Pessoais) de Legislação em Negócios Digitais:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/legislacao_cap1_objetivas.py

Grava em src/data/questoes/legislacao.json, trocando só as questões legislacao-cap1-o* e
legislacao-cap1-d*; as que já existiam (q* e f*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import LEGISLACAO, Banco, p

banco = Banco('legislacao-cap1', LEGISLACAO)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As situações 1, 2, 3 e 4 violam, respectivamente, os princípios da LGPD chamados',
    'necessidade, qualidade dos dados, transparência e responsabilização.',
    [
        'finalidade, qualidade dos dados, transparência e prevenção.',
        'necessidade, adequação, livre acesso e responsabilização.',
        'necessidade, qualidade dos dados, segurança e responsabilização.',
        'adequação, transparência, qualidade dos dados e não discriminação.',
    ],
    'Pedir religião e estado civil para entregar comida vai além do mínimo necessário (necessidade). Manter um endereço '
    'errado depois do pedido de correção fere a exatidão e a atualização dos dados (qualidade dos dados). Uma política '
    'escondida e confusa não dá informações claras e acessíveis (transparência). Não conseguir demonstrar as medidas '
    'adotadas fere a demonstração de cumprimento da lei (responsabilização e prestação de contas). Todos estão no art. 6º.',
    contexto=[p('Em uma fiscalização, foram encontradas quatro situações: '
                '(1) um aplicativo de delivery exige, no cadastro, a religião e o estado civil do usuário; '
                '(2) uma loja mantém por meses um endereço errado, mesmo depois de o cliente pedir a correção; '
                '(3) a política de privacidade de um site está em um link escondido, com linguagem confusa; '
                '(4) uma empresa não consegue mostrar à ANPD nenhum registro das medidas de proteção que diz adotar.')],
)

banco.multipla(
    'medio',
    'As bases legais que amparam os tratamentos 1, 2, 3 e 4 são, respectivamente,',
    'tutela da saúde, proteção do crédito, exercício regular de direitos e cumprimento de obrigação legal.',
    [
        'consentimento, proteção do crédito, legítimo interesse e cumprimento de obrigação legal.',
        'tutela da saúde, legítimo interesse, exercício regular de direitos e execução de contrato.',
        'proteção da vida, proteção do crédito, cumprimento de obrigação legal e exercício regular de direitos.',
        'tutela da saúde, consentimento, execução de contrato e cumprimento de obrigação legal.',
    ],
    'O acesso ao prontuário por profissionais de saúde, durante o atendimento, é tutela da saúde (art. 7º, VIII, e '
    'art. 11, II, f). A consulta a um birô para conceder crédito é proteção do crédito (art. 7º, X). Guardar dados para '
    'se defender em processo é exercício regular de direitos (art. 7º, VI). Enviar as informações exigidas pelo eSocial '
    'é cumprimento de obrigação legal ou regulatória (art. 7º, II).',
    contexto=[p('Considere os tratamentos de dados a seguir: '
                '(1) a equipe médica de um hospital consulta o prontuário de um paciente durante o atendimento; '
                '(2) um banco consulta um birô de crédito antes de aprovar um empréstimo; '
                '(3) uma empresa guarda os registros de jornada de um ex-empregado para se defender em uma ação '
                'trabalhista; '
                '(4) uma empresa envia ao eSocial os dados da folha de pagamento dos empregados.')],
)

banco.multipla(
    'medio',
    'Como se classificam a loja e a plataforma de e-mail e qual é a consequência da conduta da plataforma?',
    'A loja é controladora e a plataforma, operadora; ao usar os dados para fins próprios, esta responde como '
    'controladora.',
    [
        'As duas são controladoras desde o início, pois ambas têm acesso à lista de clientes e participam dos envios.',
        'A loja é operadora e a plataforma, controladora, pois é a plataforma que executa de fato o tratamento dos dados.',
        'A loja é controladora e a plataforma, operadora; a conduta da plataforma é lícita, pois os dados já estavam '
        'com ela.',
        'Nenhuma das duas é agente de tratamento, pois o envio de e-mails marketing não é regulado pela LGPD.',
    ],
    'O controlador decide sobre o tratamento (a loja define o que enviar e a quem), e o operador trata os dados em nome '
    'dele (a plataforma) (art. 5º, VI e VII). Pelo art. 42, § 1º, I, o operador que descumpre a lei ou não segue as '
    'instruções lícitas do controlador responde solidariamente pelos danos e é equiparado ao controlador. Vender anúncios '
    'com a lista da loja é usar os dados para finalidade própria.',
    contexto=[p('Uma loja virtual contrata uma plataforma de e-mail marketing para enviar suas campanhas aos clientes. A '
                'loja define o conteúdo, a frequência e quem recebe cada mensagem, e a plataforma apenas executa os '
                'envios. Meses depois, descobre-se que a plataforma passou a usar a lista de clientes da loja para '
                'vender anúncios de outras empresas.')],
)

banco.assercao(
    'medio',
    'Um aplicativo de rede social cujo perfil do usuário já nasce configurado como privado pratica privacy by default.',
    'Privacy by default é a incorporação da privacidade na arquitetura do sistema, desde a fase de projeto, como na '
    'criptografia de ponta a ponta.',
    2,
    'A I é verdadeira: privacy by default é a configuração inicial mais protetiva, que só muda por ação do usuário, como '
    'o perfil que nasce privado. A II é falsa: a incorporação da privacidade desde a concepção, como a criptografia de '
    'ponta a ponta, é o privacy by design. O primeiro é uma decisão sobre a configuração entregue ao usuário; o segundo, '
    'uma decisão de arquitetura.',
    contexto=[p('Uma equipe de produto discute como aplicar os conceitos de privacy by design e privacy by default em um '
                'novo aplicativo.')],
)

banco.afirmativas(
    'medio',
    [
        ('A advertência é aplicada com a indicação de prazo para a adoção de medidas corretivas.', True),
        ('A multa simples chega a 2% do faturamento no Brasil, limitada a R$ 50 milhões por infração.', True),
        ('A publicização da infração é feita antes da apuração, para alertar os titulares o quanto antes.', False),
        ('A suspensão parcial do banco de dados pode durar até 6 meses, prorrogável por igual período.', True),
    ],
    'I, II e IV estão de acordo com o art. 52 da LGPD. III é falsa: a publicização da infração só ocorre depois de '
    'devidamente apurada e confirmada a sua ocorrência (art. 52, IV), com processo administrativo que assegure a ampla '
    'defesa.',
    contexto=[p('Depois de uma fiscalização, uma empresa quer entender as sanções administrativas que a ANPD pode aplicar '
                'com base no art. 52 da LGPD.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Pela LGPD, como a empresa deve atender ao pedido?',
    'Deve fornecer a declaração clara e completa em até 15 dias, contados do requerimento do titular (art. 19, II).',
    [
        'Pode responder em até 60 dias, pois a LGPD não fixa prazo para os pedidos feitos pelos titulares.',
        'Deve responder em até 30 dias, prorrogáveis por mais 60, que é o prazo previsto na LGPD para o acesso.',
        'Deve responder em até 72 horas, o mesmo prazo previsto para a comunicação de incidentes de segurança.',
        'Pode cobrar uma taxa pela declaração completa, pois a gratuidade vale só para a confirmação simples.',
    ],
    'O art. 19 da LGPD prevê que a confirmação da existência ou o acesso aos dados seja dado em formato simplificado, '
    'imediatamente, ou por declaração clara e completa, em até 15 dias contados do requerimento (inciso II). O prazo de '
    'um mês, prorrogável, é do GDPR, e o de 72 horas é o da notificação de incidentes no regulamento europeu. O acesso '
    'deve ser facilitado e gratuito (art. 6º, IV, e art. 18, § 5º).',
    contexto=[p('Um cliente pede a uma operadora de telefonia uma declaração completa de todos os seus dados pessoais '
                'tratados, com a origem dos dados e os critérios usados. A operadora responde que vai analisar o pedido '
                'e enviar a declaração em até 60 dias, mediante pagamento de uma taxa de emissão.')],
)

banco.multipla(
    'dificil',
    'Quais são os limites máximos de multa por essa infração em cada lei?',
    'Até € 80 milhões pelo GDPR e até R$ 50 milhões pela LGPD.',
    [
        'Até € 20 milhões pelo GDPR e até R$ 80 milhões pela LGPD.',
        'Até € 80 milhões pelo GDPR e até R$ 80 milhões pela LGPD.',
        'Até € 40 milhões pelo GDPR e até R$ 50 milhões pela LGPD.',
        'Até € 20 milhões pelo GDPR e até R$ 50 milhões pela LGPD.',
    ],
    'Nas infrações mais graves, o GDPR permite multa de até € 20 milhões ou 4% do faturamento mundial, o que for maior: '
    '4% de € 2 bilhões são € 80 milhões. Na LGPD, a multa simples é de até 2% do faturamento no Brasil (2% de R$ 4 '
    'bilhões são R$ 80 milhões), mas limitada a R$ 50 milhões por infração. Usar 2% no GDPR (€ 40 milhões) seria aplicar '
    'o nível das infrações menos graves.',
    contexto=[p('Um grupo de comércio eletrônico tem faturamento mundial de € 2 bilhões, dos quais o equivalente a R$ 4 '
                'bilhões vêm do Brasil. Uma mesma falha grave, que violou princípios e direitos dos titulares, foi '
                'cometida na Europa e no Brasil.')],
)

banco.afirmativas(
    'dificil',
    [
        ('A ANPD pode determinar que o controlador elabore o RIPD, inclusive de dados sensíveis.', True),
        ('O RIPD deve descrever os dados coletados, a metodologia, as medidas de segurança e a análise do controlador.',
         True),
        ('O RIPD é exigido apenas de órgãos públicos, e não de empresas privadas como o hospital.', False),
        ('O tratamento com base no legítimo interesse nunca pode levar a ANPD a pedir o RIPD.', False),
    ],
    'I e II estão no art. 38 da LGPD: a ANPD pode determinar ao controlador a elaboração do relatório de impacto, '
    'inclusive de dados sensíveis, e o parágrafo único lista o seu conteúdo mínimo. III é falsa: o RIPD vale para '
    'qualquer controlador. IV é falsa: quando o tratamento se baseia no legítimo interesse, a ANPD pode solicitar o RIPD '
    '(art. 10, § 3º).',
    contexto=[p('Um hospital privado passou a usar um sistema de inteligência artificial para priorizar o atendimento de '
                'pacientes no pronto-socorro, a partir de dados de saúde. A ANPD pediu informações sobre o Relatório de '
                'Impacto à Proteção de Dados Pessoais (RIPD).')],
)

banco.multipla(
    'dificil',
    'Sobre a comparação entre a LGPD e o GDPR, assinale a alternativa INCORRETA.',
    'O GDPR prevê dez bases legais para o tratamento de dados, enquanto a LGPD prevê apenas seis hipóteses.',
    [
        'O GDPR exige que a autoridade seja notificada de um incidente em até 72 horas, quando houver risco.',
        'Na LGPD, a multa simples é calculada sobre o faturamento da empresa ou do grupo no Brasil.',
        'As duas leis podem ser aplicadas a empresas de fora do seu território, em certas situações.',
        'Na LGPD, a indicação do encarregado é obrigação do controlador, com dispensa para pequenos agentes.',
    ],
    'A afirmação incorreta inverte os números: a LGPD prevê dez hipóteses de tratamento (art. 7º), e o GDPR, seis bases '
    'legais (art. 6º). As demais estão corretas: o prazo de 72 horas do GDPR (art. 33), a multa ligada ao faturamento no '
    'Brasil (art. 52, II), o alcance extraterritorial das duas leis e a obrigação do controlador de indicar o encarregado '
    '(art. 41), com a dispensa prevista pela ANPD para agentes de tratamento de pequeno porte.',
    contexto=[p('Uma empresa brasileira que vai começar a vender para a Europa preparou um quadro comparativo entre as '
                'duas leis de proteção de dados.')],
)

banco.multipla(
    'dificil',
    'Considerando o art. 12 da LGPD, a base publicada pode ser tratada como anonimizada?',
    'Não: se é possível reidentificar as pessoas com esforços razoáveis, cruzando dados públicos, ela continua sendo de '
    'dados pessoais.',
    [
        'Sim: como os nomes e os CPFs foram retirados, a base deixa de ter dados pessoais, qualquer que seja o risco.',
        'Sim: só haveria dado pessoal se a própria universidade conseguisse reverter a base com meios exclusivamente seus.',
        'Não: qualquer base com informação sobre pessoas é sempre dado pessoal, mesmo que a reidentificação seja '
        'impossível.',
        'Sim, desde que a universidade publique uma nota pedindo que ninguém tente identificar as pessoas da base.',
    ],
    'Pelo art. 12, os dados anonimizados não são dados pessoais, salvo quando o processo puder ser revertido com '
    'esforços razoáveis, inclusive por terceiros. CEP, data de nascimento e sexo, combinados com registros públicos, '
    'permitem apontar uma única pessoa: são identificadores indiretos. Por isso, a base continua sujeita à LGPD. Uma base '
    'realmente anonimizada, sem possibilidade razoável de reversão, deixaria de ser dado pessoal.',
    contexto=[p('Uma universidade publicou, para pesquisas, uma base de atendimentos de saúde da qual retirou nomes e '
                'CPFs, mas manteve o CEP, a data de nascimento e o sexo de cada paciente. Um pesquisador mostrou que, '
                'cruzando esses campos com listas públicas, conseguia identificar a maior parte dos pacientes.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Uma startup vai lançar um aplicativo de apoio à saúde mental. No cadastro, o usuário informa nome, e-mail, data '
        'de nascimento e CPF; depois, registra diariamente o humor, as horas de sono e anotações sobre crises de '
        'ansiedade. A empresa quer usar inteligência artificial para sugerir exercícios e pretende, no futuro, firmar '
        'parcerias com planos de saúde. Os dados ficarão em uma nuvem contratada e ainda não há nenhuma política de '
        'privacidade.',
    ],
    'Proponha um plano de adequação desse aplicativo à LGPD, antes do lançamento.',
    'O plano começa pelo mapeamento dos dados e das finalidades: os dados de cadastro são pessoais comuns, e os registros '
    'de humor, sono e crises são dados sensíveis de saúde. Cada finalidade precisa de base legal; para os dados sensíveis, '
    'só valem as hipóteses do art. 11, e a mais adequada aqui é o consentimento específico e destacado, livre e '
    'informado. Deve-se aplicar a necessidade, coletando só o indispensável (o CPF, por exemplo, só se houver motivo), e '
    'o privacy by design e by default, com segurança desde a concepção, como criptografia e controle de acesso (art. 46). '
    'Como há dados sensíveis e uso de IA, convém elaborar o RIPD. A política de privacidade deve ser clara e informar '
    'dados, finalidades, bases, prazos de guarda, compartilhamentos e o encarregado indicado. A nuvem é operadora e '
    'precisa de contrato com cláusulas de proteção de dados e, se os servidores ficarem fora do Brasil, de garantias '
    'para a transferência internacional. A parceria com planos de saúde exige muito cuidado: a LGPD restringe o '
    'compartilhamento de dados de saúde para obter vantagem econômica (art. 11, § 4º) e proíbe as operadoras de usá-los '
    'para selecionar riscos (art. 11, § 5º). Por fim, a startup deve criar um canal para os direitos dos titulares, '
    'permitir revogar o consentimento com facilidade, garantir a revisão de decisões automatizadas (art. 20) e ter um '
    'plano de resposta a incidentes, com comunicação à ANPD em até 3 dias úteis quando houver risco relevante.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma empresa brasileira de software, que hoje atende só clientes no Brasil e já segue a LGPD, vai começar a vender '
        'assinaturas para pessoas na Alemanha e na França, com site em alemão e francês e preços em euros. Um dos sócios '
        'afirma que "quem cumpre a LGPD já cumpre automaticamente o GDPR, porque as duas leis são iguais".',
    ],
    'Avalie a afirmação do sócio, apontando as semelhanças e as diferenças entre a LGPD e o GDPR que a empresa precisa '
    'considerar.',
    'A afirmação é exagerada. O GDPR se aplica à empresa, mesmo sem sede na Europa, porque ela vai oferecer serviços a '
    'pessoas que estão na União Europeia (art. 3º, nº 2). As leis têm muito em comum, pois o GDPR inspirou a LGPD: '
    'conceitos de dado pessoal e sensível, controlador e operador, princípios parecidos, direitos dos titulares, '
    'segurança e responsabilização. Mas há diferenças: o GDPR tem seis bases legais, e a LGPD, dez hipóteses; o GDPR '
    'exige notificar a autoridade de um incidente em até 72 horas, e a LGPD, em até 3 dias úteis; as respostas aos '
    'titulares têm prazo de um mês no GDPR e de 15 dias para a declaração completa na LGPD; o encarregado (DPO) é '
    'obrigatório só em casos específicos no GDPR; e as multas do GDPR chegam a € 20 milhões ou 4% do faturamento mundial, '
    'enquanto as da LGPD têm teto de R$ 50 milhões por infração. A empresa também pode precisar indicar um representante '
    'na União Europeia (art. 27 do GDPR), seguir as regras europeias de cookies e garantir mecanismos para transferir os '
    'dados dos europeus ao Brasil, como as cláusulas contratuais padrão. Por isso, precisa revisar sua conformidade à luz '
    'do GDPR, e não presumir que a LGPD basta.',
)


if __name__ == '__main__':
    banco.gravar()
