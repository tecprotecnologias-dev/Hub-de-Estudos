"""
Questões médias e difíceis do capítulo 7 (Regulação Internacional e Jurisdição) de Legislação em Negócios Digitais:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/legislacao_cap7_objetivas.py

Grava em src/data/questoes/legislacao.json, trocando só as questões legislacao-cap7-o* e
legislacao-cap7-d*; as que já existiam (q* e f*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import LEGISLACAO, Banco, p

banco = Banco('legislacao-cap7', LEGISLACAO)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As situações 1, 2 e 3 aplicam, respectivamente, os critérios de jurisdição',
    'do efeito, da nacionalidade e territorial.',
    ['territorial, da nacionalidade e do efeito.', 'do efeito, territorial e da nacionalidade.',
     'da nacionalidade, do efeito e territorial.', 'territorial, do efeito e da nacionalidade.'],
    'Aplicar uma lei a uma conduta praticada no exterior porque ela produz efeitos no território, como no GDPR para quem '
    'oferece serviços a pessoas na União, segue o critério do efeito (1). Aplicar a lei do país a um nacional dele, onde '
    'quer que esteja, é o critério da nacionalidade (2). Aplicar a lei ao fato ocorrido no próprio território é o critério '
    'territorial (3).',
    contexto=[p('Considere as situações: '
                '(1) uma autoridade europeia aplica o GDPR a uma empresa de fora da Europa que oferece serviços a pessoas '
                'na União Europeia; '
                '(2) a lei brasileira é aplicada a um brasileiro que cometeu um crime enquanto morava no exterior; '
                '(3) a lei brasileira é aplicada a um ataque contra servidores que ficam em São Paulo.')],
)

banco.multipla(
    'medio',
    'Pelo AI Act europeu, os sistemas 1, 2, 3 e 4 são, respectivamente, de risco',
    'inaceitável, alto, limitado e mínimo.',
    ['alto, inaceitável, limitado e mínimo.', 'inaceitável, limitado, alto e mínimo.', 'inaceitável, alto, mínimo e '
     'limitado.', 'alto, alto, limitado e mínimo.'],
    'A pontuação social de pessoas é uma prática proibida, de risco inaceitável (1). A IA usada em recrutamento, como a '
    'triagem de currículos, é de alto risco, com registro, avaliação e supervisão humana (2). Chatbots são de risco '
    'limitado, com dever de transparência: o usuário deve saber que fala com uma IA (3). Filtros de spam são de risco '
    'mínimo, sem obrigações específicas (4).',
    contexto=[p('Uma consultoria analisa quatro sistemas de IA que serão usados na União Europeia: '
                '(1) um sistema que dá notas aos cidadãos conforme o seu comportamento social; '
                '(2) um sistema que faz a triagem de currículos em processos seletivos; '
                '(3) um chatbot de atendimento ao cliente; '
                '(4) um filtro de spam de e-mails.')],
)

banco.afirmativas(
    'medio',
    [
        ('O DSA prevê multas de até 6% do faturamento global da plataforma.', True),
        ('O DMA prevê multas de até 10% do faturamento global, e de até 20% em caso de reincidência.', True),
        ('O DMA se aplica a qualquer plataforma com mais de 45 milhões de usuários mensais na União Europeia.', False),
        ('O DSA proíbe direcionar anúncios com base em dados sensíveis dos usuários.', True),
    ],
    'I, II e IV estão corretas. III é falsa: o limite de 45 milhões de usuários mensais é o critério do DSA para as '
    'plataformas de muito grande dimensão (VLOPs). O DMA se aplica aos gatekeepers, grandes plataformas que controlam o '
    'acesso a mercados digitais e que a Comissão Europeia designa por critérios próprios, como faturamento e número de '
    'usuários empresariais e finais.',
    contexto=[p('Uma empresa brasileira de tecnologia quer entender as duas principais leis europeias sobre plataformas '
                'digitais antes de expandir para a Europa.')],
)

banco.assercao(
    'medio',
    'A transferência de dados da União Europeia para uma empresa americana certificada no Data Privacy Framework '
    'dispensa as cláusulas contratuais padrão.',
    'Em 2020, no caso Schrems II, o Tribunal de Justiça da União Europeia invalidou o Privacy Shield.',
    1,
    'As duas são verdadeiras, mas a II não justifica a I. A I é verdadeira porque, em 2023, a Comissão Europeia adotou '
    'uma decisão de adequação para as empresas americanas certificadas no Data Privacy Framework, o que permite a '
    'transferência sem outros mecanismos. A II é um fato histórico verdadeiro: foi a invalidação do Privacy Shield que '
    'levou à negociação do novo acordo, mas não é ela que explica a dispensa das cláusulas.',
    contexto=[p('Uma empresa europeia vai contratar um serviço de nuvem de uma empresa americana e quer saber se precisa '
                'assinar cláusulas contratuais padrão para transferir dados pessoais.')],
)

banco.multipla(
    'medio',
    'Sobre a localização de dados (data localization), é correto afirmar que',
    'o Brasil não exige guardar dados no país, e a União Europeia restringe transferências sem obrigar a localização.',
    [
        'o Brasil exige que todos os dados de brasileiros fiquem em servidores no país, como determina a LGPD.',
        'a União Europeia exige que os dados de europeus fiquem guardados em servidores dentro do bloco.',
        'a China e a Rússia não têm regras de localização, pois seguem o modelo liberal de governança da internet.',
        'a localização de dados foi proibida pela OMC, e nenhum país pode exigir que os dados fiquem no território.',
    ],
    'O Brasil não tem obrigação geral de localização: a LGPD permite a transferência internacional com as garantias do '
    'art. 33. A União Europeia também não exige localização, mas só permite transferir dados para países com proteção '
    'equivalente ou com garantias. China e Rússia exigem servidores locais para vários tipos de dados, e o LinkedIn chegou '
    'a ser bloqueado na Rússia por descumprir essa regra.',
    contexto=[p('Uma startup brasileira de nuvem quer atender clientes em vários países e precisa saber onde será obrigada '
                'a manter servidores locais.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Pela LINDB, qual lei um juiz brasileiro tende a aplicar ao contrato?',
    'A lei brasileira, pois o contrato se considera constituído no lugar em que reside o proponente (art. 9º, § 2º).',
    [
        'A lei alemã, pois o contrato se considera constituído no lugar em que reside quem aceitou a proposta.',
        'A lei alemã, pois o software será usado na Alemanha, e a LINDB manda aplicar a lei do lugar de uso.',
        'A lei brasileira, pois a LINDB obriga a aplicar a lei do Brasil a todo contrato com empresa brasileira.',
        'O Regulamento Roma I, que a LINDB manda aplicar a qualquer contrato entre empresas da Europa e do Brasil.',
    ],
    'O art. 9º da LINDB manda aplicar às obrigações a lei do país em que se constituírem, e o § 2º diz que a obrigação '
    'resultante do contrato se considera constituída no lugar em que residir o proponente. Como a proposta partiu da '
    'empresa brasileira, um juiz brasileiro tende a aplicar a lei do Brasil. Um tribunal alemão, porém, usaria as regras '
    'do Roma I, o que mostra a importância da cláusula de lei aplicável.',
    contexto=[p('Uma empresa brasileira enviou por e-mail uma proposta de licença de software a uma empresa alemã, que a '
                'aceitou. O contrato não tem cláusula de lei aplicável, e surgiu um conflito que será julgado no Brasil.')],
)

banco.multipla(
    'dificil',
    'Qual é a análise mais adequada sobre o pedido, no Brasil e na União Europeia?',
    'No Brasil, o STF rejeitou o direito ao esquecimento (Tema 786), e abusos se veem caso a caso; na UE, cabe a '
    'desindexação.',
    [
        'No Brasil e na UE, todo cidadão pode exigir que notícias verdadeiras sobre ele sejam apagadas depois de 10 anos.',
        'No Brasil, a LGPD garante expressamente o direito ao esquecimento, que obriga os jornais a apagar as notícias.',
        'Na UE, o caso Google Spain proibiu os buscadores de mostrar qualquer notícia que cite o nome de uma pessoa.',
        'No Brasil, o Marco Civil obriga os buscadores a remover links verdadeiros a pedido de qualquer pessoa citada.',
    ],
    'Em 2021, no Tema 786, o STF decidiu que é incompatível com a Constituição a ideia de um direito ao esquecimento que '
    'impeça, pela passagem do tempo, a divulgação de fatos verdadeiros e licitamente obtidos; eventuais excessos devem ser '
    'analisados caso a caso, com base na proteção da honra, da imagem e da privacidade. Na União Europeia, o caso Google '
    'Spain (2014) reconheceu o direito de pedir aos buscadores a desindexação de resultados, sem apagar a notícia.',
    contexto=[p('Um empresário pede que um buscador deixe de mostrar, quando alguém pesquisa o seu nome, notícias '
                'verdadeiras de 15 anos atrás sobre um processo em que ele foi absolvido. O mesmo pedido é feito por uma '
                'filial dele na Espanha.')],
)

banco.multipla(
    'dificil',
    'Qual desses argumentos pode levar o STJ a negar a homologação do laudo arbitral?',
    'A empresa não foi notificada do procedimento arbitral, o que a impediu de se defender (art. 38, III).',
    [
        'Os árbitros avaliaram mal as provas e decidiram contra a empresa, que tinha razão no mérito.',
        'O laudo foi proferido em inglês, e a lei brasileira só homologa laudos escritos em português.',
        'A arbitragem ocorreu em Paris, e o Brasil só reconhece laudos proferidos no próprio território.',
        'O valor da condenação é muito alto e vai comprometer o caixa da empresa por vários anos.',
    ],
    'Na homologação de laudo estrangeiro, o STJ não reexamina o mérito. A Lei nº 9.307/1996, em linha com a Convenção de '
    'Nova York, permite negar a homologação em hipóteses específicas, como a falta de notificação do procedimento ou a '
    'violação do contraditório que impediu a ampla defesa (art. 38, III), ou a ofensa à ordem pública nacional (art. 39, '
    'II). A tradução do laudo é apresentada no pedido, e o Brasil reconhece laudos de outros países.',
    contexto=[p('Uma empresa brasileira foi condenada por um laudo arbitral proferido em Paris, em inglês, a pagar uma '
                'indenização elevada a uma empresa americana. Ao contestar o pedido de homologação no STJ, apresentou '
                'vários argumentos.')],
)

banco.multipla(
    'dificil',
    'Por que o caso Microsoft Corp. v. United States perdeu o objeto em 2018?',
    'Porque o CLOUD Act passou a obrigar os provedores americanos a entregar dados sob seu controle, mesmo no exterior.',
    [
        'Porque a Suprema Corte decidiu que nenhum dado guardado fora dos EUA pode ser pedido pela Justiça americana.',
        'Porque a Irlanda entregou os e-mails ao governo americano depois de um pedido feito pela própria Microsoft.',
        'Porque o GDPR passou a valer e proibiu qualquer transferência de dados da Europa para os Estados Unidos.',
        'Porque a Microsoft transferiu os servidores para os EUA, o que tornou desnecessário julgar a questão.',
    ],
    'No caso, a Microsoft se recusava a entregar e-mails guardados em servidores na Irlanda, alegando que uma ordem '
    'americana não alcançava dados no exterior. Em 2018, antes da decisão da Suprema Corte, o Congresso aprovou o CLOUD '
    'Act, que obriga os provedores sujeitos à lei americana a fornecer dados sob sua posse ou controle, onde quer que '
    'estejam guardados, e prevê acordos com outros países. Com isso, o caso perdeu o objeto.',
    contexto=[p('Em uma investigação de tráfico de drogas, autoridades americanas pediram à Microsoft os e-mails de um '
                'usuário guardados em servidores na Irlanda, e a empresa contestou o pedido na Justiça.')],
)

banco.multipla(
    'dificil',
    'De forma simplificada, qual é o imposto complementar (top-up tax) devido sobre esse lucro?',
    '€ 6 milhões.',
    ['€ 15 milhões.', '€ 9 milhões.', '€ 1,35 milhão.', '€ 24 milhões.'],
    'Pelo Pillar Two, a tributação mínima é de 15% sobre o lucro. Se o grupo paga, na prática, 9% em um país, falta '
    'completar 6 pontos percentuais: 6% de € 100 milhões são € 6 milhões. Aplicar os 15% sobre todo o lucro daria € 15 '
    'milhões; € 9 milhões é o imposto já pago; € 1,35 milhão seria 15% de 9%. O cálculo real tem ajustes, como exclusões '
    'ligadas à substância econômica, mas a lógica é completar o que falta para 15%.',
    contexto=[p('Um grupo multinacional com receita acima de 750 milhões de euros tem, em um país de baixa tributação, um '
                'lucro de € 100 milhões, sobre o qual paga, na prática, 9% de imposto.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Uma startup brasileira de recrutamento usa inteligência artificial para analisar currículos e entrevistas em '
        'vídeo. Ela vai começar a atender empresas na Alemanha e na Califórnia, guardará os dados em uma nuvem americana e '
        'quer usar o mesmo contrato e a mesma política de privacidade que usa no Brasil.',
    ],
    'Identifique os principais marcos legais internacionais que a startup precisará observar e os cuidados que deve '
    'tomar nessa expansão.',
    'Na Europa, o GDPR se aplica porque a startup vai tratar dados de pessoas que estão na União, mesmo sem sede lá, e '
    'exige base legal, direitos dos titulares, notificação de incidentes em 72 horas e, possivelmente, um representante na '
    'União; como a análise de candidatos é uma decisão com efeitos relevantes, o titular tem direito a não ficar sujeito '
    'só a decisões automatizadas e a obter intervenção humana. O AI Act classifica a IA usada em recrutamento como de alto '
    'risco, com gestão de riscos, documentação técnica, registro, transparência e supervisão humana. Na Califórnia, a '
    'CCPA/CPRA dá aos consumidores direitos de acesso, exclusão e oposição à venda ou ao compartilhamento de dados. A '
    'nuvem americana exige mecanismos de transferência: a decisão de adequação do Data Privacy Framework, se o provedor '
    'for certificado, ou cláusulas contratuais padrão; para os dados de brasileiros, as garantias do art. 33 da LGPD. Há '
    'ainda o risco do CLOUD Act, que permite às autoridades americanas pedir dados ao provedor. Por isso, o contrato e a '
    'política de privacidade brasileiros não bastam: precisam ser adaptados a cada mercado, com cláusulas de lei '
    'aplicável, foro ou arbitragem e proteção de dados, e a startup deve observar a tributação dos serviços digitais em '
    'cada país.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma empresa brasileira de software vai assinar um contrato de licença SaaS de longo prazo com uma rede de lojas da '
        'Alemanha. O modelo de contrato que ela usa no Brasil não tem cláusula de lei aplicável, nem de foro ou de '
        'arbitragem, e não trata da proteção de dados. A empresa alemã propôs que eventuais conflitos sejam julgados pela '
        'Justiça de Berlim.',
    ],
    'Proponha as principais cláusulas que esse contrato internacional deve ter, justificando cada uma.',
    'A cláusula de lei aplicável é essencial: sem ela, cada país aplica as próprias regras de direito internacional '
    'privado (no Brasil, a LINDB; na Alemanha, o Roma I), com resultados diferentes. As partes devem escolher uma lei '
    'previsível e conhecida. Para resolver conflitos, a arbitragem internacional tende a ser melhor que a Justiça de '
    'Berlim: é neutra, especializada e sigilosa, e o laudo pode ser executado nos dois países pela Convenção de Nova York, '
    'da qual o Brasil faz parte; a cláusula deve indicar a instituição (como a ICC), a sede, o idioma, o número de árbitros '
    'e a lei aplicável, e, por ser B2B, é válida. O contrato deve definir o idioma que prevalece, a forma de notificação '
    'entre as partes, o nível de serviço (SLA), a limitação de responsabilidade, respeitando a ordem pública de cada '
    'país, e a propriedade intelectual sobre o software. Também precisa de um acordo de tratamento de dados (DPA), pois a '
    'empresa brasileira será operadora de dados de europeus, com as cláusulas contratuais padrão da Comissão Europeia para '
    'a transferência internacional e regras de segurança e de comunicação de incidentes, além de tratar de tributos, '
    'confidencialidade, prazo e rescisão.',
)


if __name__ == '__main__':
    banco.gravar()
