"""
Questões médias e difíceis do capítulo 6 (Empreendedorismo Digital e Startups) de Legislação em Negócios Digitais:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/legislacao_cap6_objetivas.py

Grava em src/data/questoes/legislacao.json, trocando só as questões legislacao-cap6-o* e
legislacao-cap6-d*; as que já existiam (q* e f*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import LEGISLACAO, Banco, p

banco = Banco('legislacao-cap6', LEGISLACAO)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As cláusulas 1, 2, 3 e 4 correspondem, respectivamente, a',
    'tag along, liquidation preference, antidiluição e direito de preferência.',
    ['drag along, liquidation preference, antidiluição e direito de preferência.',
     'tag along, antidiluição, liquidation preference e direito de preferência.',
     'tag along, liquidation preference, vesting e não competição.',
     'direito de preferência, liquidation preference, antidiluição e tag along.'],
    'O tag along garante ao minoritário vender nas mesmas condições oferecidas ao majoritário (1). A liquidation '
    'preference define quem recebe primeiro em uma venda ou liquidação (2). A antidiluição protege o investidor quando '
    'novas participações são emitidas a preço menor, em um down round (3). O direito de preferência obriga a oferecer as '
    'quotas aos sócios antes de vendê-las a terceiros (4). O drag along é o oposto do tag along: o majoritário obriga o '
    'minoritário a vender junto.',
    contexto=[p('O acordo de sócios de uma startup traz as seguintes cláusulas: '
                '(1) se o sócio majoritário vender a sua parte, o minoritário pode vender a dele nas mesmas condições; '
                '(2) em uma venda da empresa, o fundo investidor recebe o valor aportado antes dos fundadores; '
                '(3) se a empresa emitir novas quotas a um preço menor, a participação do investidor é ajustada; '
                '(4) quem quiser vender as suas quotas deve oferecê-las primeiro aos outros sócios.')],
)

banco.multipla(
    'medio',
    'Com quantos por cento da empresa a fundadora fica ao sair?',
    '25%.',
    ['10%.', '40%.', '0%.', '30%.'],
    'Com vesting de 4 anos (48 meses) e cliff de 1 ano, a fundadora não adquire nada nos primeiros 12 meses; ao completar '
    'o cliff, adquire 12/48 da participação, e depois mais 1/48 por mês. Em 30 meses, adquiriu 30/48 de 40%, ou seja, '
    '25%. Ficar com 10% seria contar só o cliff; com 40%, seria ignorar o vesting; com 0%, seria aplicar a regra de quem '
    'sai antes do cliff.',
    contexto=[p('Uma fundadora tem 40% de uma startup, com vesting de 4 anos, cliff de 1 ano e aquisição mensal linear '
                'depois do cliff. Ela decide sair da empresa depois de 30 meses.')],
)

banco.afirmativas(
    'medio',
    [
        ('O MEI não pode ter sócio nem participar de outra empresa como sócio ou titular.', True),
        ('A sociedade limitada pode ser constituída por uma única pessoa.', True),
        ('O Simples Nacional admite empresas com receita bruta anual de até R$ 4,8 milhões.', True),
        ('A Eireli é a forma recomendada para startups com um só fundador, pela LC 182/2021.', False),
    ],
    'I, II e III estão corretas: o MEI é empresário individual, sem sócios; desde 2019, o Código Civil admite a sociedade '
    'limitada unipessoal; e o limite do Simples Nacional para a empresa de pequeno porte é de R$ 4,8 milhões por ano. '
    'IV é falsa: a Eireli foi extinta em 2021, e as que existiam foram transformadas em sociedades limitadas unipessoais.',
    contexto=[p('Uma desenvolvedora vai abrir sozinha uma empresa para lançar o seu aplicativo e quer conhecer as '
                'estruturas jurídicas disponíveis.')],
)

banco.assercao(
    'medio',
    'Uma startup pode captar recursos do público por equity crowdfunding, em plataforma autorizada pela CVM, até o limite '
    'de R$ 15 milhões por ano.',
    'A Resolução CVM nº 88/2022 dispensa essas ofertas de registro na CVM, desde que feitas por plataforma autorizada e '
    'dentro dos limites da norma.',
    0,
    'As duas são verdadeiras, e a II justifica a I. Em regra, oferecer investimentos ao público exige registro na CVM. A '
    'Resolução CVM nº 88/2022 cria um regime próprio para o investimento participativo: as ofertas de empresas de pequeno '
    'porte, feitas por plataformas autorizadas e até R$ 15 milhões por ano, são dispensadas de registro, o que permite '
    'à startup captar de muitos investidores.',
    contexto=[p('Uma startup de energia solar quer captar recursos de centenas de pequenos investidores, oferecendo uma '
                'participação futura no negócio.')],
)

banco.multipla(
    'medio',
    'Pela Lei Complementar nº 123/2006, como pode ser a remuneração do investidor-anjo?',
    'Pelos resultados, conforme o contrato, até 50% dos lucros, em um contrato de participação de até 7 anos.',
    [
        'Por pró-labore mensal fixo, como os sócios administradores, durante todo o tempo do contrato.',
        'Por juros fixos de 3% ao mês sobre o valor aportado, pagos mesmo que a empresa tenha prejuízo.',
        'Pela distribuição de todo o lucro da empresa, sem limite, até que o aporte seja devolvido em dobro.',
        'Por participação no capital social desde o aporte, com direito a voto nas decisões da empresa.',
    ],
    'Pelo art. 61-A da LC nº 123/2006, o investidor-anjo é remunerado pelos seus aportes conforme o contrato de '
    'participação, que tem vigência de até 7 anos (§ 1º), e a remuneração não pode passar de 50% dos lucros da sociedade '
    '(§ 6º). Ele não é sócio, não tem direito a voto nem gerência e não responde pelas dívidas da empresa.',
    contexto=[p('Um investidor quer aportar R$ 200 mil em uma microempresa de tecnologia como investidor-anjo e pergunta '
                'como será remunerado pelo investimento.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Pelo entendimento do STJ no Tema 1.226, como se dá a tributação pelo imposto de renda?',
    'Não há imposto como salário no exercício; na venda, paga-se ganho de capital sobre a diferença entre R$ 50 e R$ 10.',
    [
        'Paga-se imposto como salário no exercício, sobre a diferença entre R$ 30 e R$ 10, e nada na venda.',
        'Paga-se imposto como salário no exercício e ganho de capital na venda, sobre a diferença entre R$ 50 e R$ 30.',
        'Não há imposto nem no exercício nem na venda, pois as opções de compra de ações são isentas.',
        'Paga-se ganho de capital no exercício, sobre R$ 30, e de novo na venda, sobre os R$ 50 recebidos.',
    ],
    'No Tema 1.226 (2024), o STJ decidiu que os planos de opção de compra de ações (stock options) têm natureza '
    'mercantil, e não remuneratória: o exercício da opção não é tratado como salário. O imposto incide como ganho de '
    'capital na venda das ações, sobre a diferença entre o valor de venda (R$ 50) e o custo de aquisição, que é o preço '
    'pago no exercício (R$ 10), com as alíquotas de 15% a 22,5% da Lei nº 13.259/2016.',
    contexto=[p('Uma empregada de uma startup recebeu opções de compra de ações a R$ 10 por ação. Exerceu as opções quando '
                'a ação valia R$ 30 e, um ano depois, vendeu as ações por R$ 50 cada uma.')],
)

banco.multipla(
    'dificil',
    'Qual é a avaliação jurídica dessa captação?',
    'É oferta pública sem registro ou dispensa da CVM, e prometer retorno fixo agrava o risco de sanções e de crime.',
    [
        'É lícita, pois oferecer investimento em redes sociais não é oferta pública e não depende de nenhuma regra da CVM.',
        'É lícita, desde que a startup registre os contratos em cartório e entregue recibo aos investidores.',
        'É lícita, pois a LC 182/2021 permite que startups captem do público sem limite e sem nenhuma autorização.',
        'É irregular só se algum investidor perder dinheiro, pois a CVM só age depois que há prejuízo comprovado.',
    ],
    'Oferecer investimentos ao público em geral, como em redes sociais, é oferta pública e exige registro na CVM ou '
    'dispensa, como a do equity crowdfunding por plataforma autorizada (Resolução CVM nº 88/2022). Prometer rentabilidade '
    'fixa e garantida não combina com investimento de risco e pode indicar pirâmide financeira, crime contra a economia '
    'popular. A irregularidade existe na própria oferta, independentemente de perdas.',
    contexto=[p('Os fundadores de uma startup de logística publicaram em suas redes sociais: "Invista a partir de R$ 5 mil '
                'na nossa empresa e receba 3% ao mês garantidos". Mais de 200 pessoas transferiram dinheiro diretamente '
                'para a conta da startup.')],
)

banco.multipla(
    'dificil',
    'Pela Lei Complementar nº 123/2006, quais direitos o investidor-anjo tem nessa venda?',
    'Preferência na compra e direito de vender o seu aporte junto, nas mesmas condições oferecidas aos sócios.',
    [
        'Nenhum, pois o investidor-anjo não é sócio e por isso não participa de nenhuma decisão de venda.',
        'Direito de vetar a venda, pois o investidor-anjo tem voto nas decisões sobre o controle da empresa.',
        'Direito de receber o dobro do valor aportado, pago pelos sócios, sempre que a empresa for vendida.',
        'Só o resgate do aporte, desde que já tenham passado 2 anos, sem nenhum direito sobre o preço da venda.',
    ],
    'A LC nº 123/2006 garante ao investidor-anjo, se os sócios decidirem vender a empresa, o direito de preferência na '
    'aquisição (art. 61-C) e o direito de venda conjunta da titularidade do aporte, nos mesmos termos e condições '
    'oferecidos aos sócios regulares (art. 61-D), uma espécie de tag along. Ele não é sócio nem tem voto, por isso não '
    'pode vetar a venda.',
    contexto=[p('Os sócios de uma microempresa de software, que recebeu aporte de um investidor-anjo, decidiram vender a '
                'empresa a uma grande companhia de tecnologia por R$ 12 milhões.')],
)

banco.multipla(
    'dificil',
    'Pelo Código Civil, o que a startup pode exigir do ex-parceiro?',
    'A multa, sem provar o prejuízo; para cobrar mais que ela, o contrato teria de prever indenização suplementar.',
    [
        'Só o prejuízo de R$ 1 milhão, pois a cláusula penal perde o efeito quando o dano é maior que a multa.',
        'A multa e também R$ 1 milhão, pois a cláusula penal sempre se soma à indenização pelo prejuízo provado.',
        'Nada, pois NDAs não têm validade no Brasil quando não são registrados em cartório de títulos.',
        'A multa, mas só se provar que o prejuízo foi de pelo menos o mesmo valor, ou seja, R$ 200 mil.',
    ],
    'A cláusula penal pode ser exigida sem que o credor alegue ou prove prejuízo (art. 416 do Código Civil). Se o dano '
    'for maior, o credor só pode cobrar a indenização suplementar se isso estiver previsto no contrato, e a multa vale '
    'como mínimo da indenização, cabendo provar o prejuízo excedente (parágrafo único). Por isso, a cláusula penal '
    'facilita a cobrança, e o NDA não depende de registro para valer.',
    contexto=[p('Uma startup assinou um acordo de confidencialidade (NDA) com um parceiro, com multa de R$ 200 mil em caso '
                'de violação e sem cláusula sobre indenização adicional. O parceiro vazou o roadmap do produto a um '
                'concorrente, e a startup estima ter perdido R$ 1 milhão em contratos.')],
)

banco.multipla(
    'dificil',
    'As fintechs 1, 2, 3 e 4 devem se enquadrar, respectivamente, como',
    'SCD, SEP, instituição de pagamento emissora de moeda eletrônica e instituição de pagamento credenciadora.',
    [
        'SEP, SCD, instituição de pagamento emissora de moeda eletrônica e instituição de pagamento credenciadora.',
        'SCD, SEP, instituição de pagamento credenciadora e instituição de pagamento emissora de moeda eletrônica.',
        'SCD, plataforma de investimento participativo, instituição de pagamento emissora e banco comercial.',
        'Banco comercial, SEP, instituição de pagamento emissora de moeda eletrônica e SCD.',
    ],
    'A Sociedade de Crédito Direto (SCD) empresta com capital próprio, por plataforma eletrônica (1). A Sociedade de '
    'Empréstimo entre Pessoas (SEP) faz a ponte entre investidores e tomadores, o peer-to-peer lending (2). A '
    'instituição de pagamento emissora de moeda eletrônica guarda o saldo em conta de pagamento e permite transferências '
    '(3). A credenciadora habilita lojistas a aceitar cartões, como nas maquininhas (4). Todas seguem as regras do Banco '
    'Central.',
    contexto=[p('Quatro fintechs vão pedir autorização ao Banco Central: '
                '(1) uma que empresta o próprio dinheiro a pequenas empresas, por um aplicativo; '
                '(2) uma plataforma que conecta pessoas que querem investir a pessoas que querem empréstimos; '
                '(3) uma carteira digital em que o usuário guarda saldo e faz transferências; '
                '(4) uma empresa de maquininhas que habilita lojistas a aceitar pagamentos com cartão.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Três amigos vão fundar uma startup de educação: um cuida da tecnologia, outro do comercial e o terceiro entrou só '
        'com dinheiro e não vai trabalhar na empresa. Eles pretendem dividir as quotas em partes iguais e não querem "perder '
        'tempo com papelada", pois confiam uns nos outros. Daqui a dois anos, pretendem receber investimento de um fundo.',
    ],
    'Proponha as principais cláusulas do acordo de sócios dessa startup, justificando cada uma.',
    'O acordo de sócios é o contrato mais importante da startup e previne conflitos. Para os sócios que trabalham, convém '
    'o vesting, em geral de 4 anos com cliff de 1 ano, para que quem sair cedo não leve a participação inteira; o sócio '
    'que entrou só com capital pode ter regras diferentes, ligadas ao aporte. A divisão igual pode ser revista conforme a '
    'contribuição de cada um. O acordo deve prever o direito de preferência na venda de quotas, o tag along, que protege '
    'o minoritário, e o drag along, que permite vender 100% da empresa quando a maioria aprovar, algo que os investidores '
    'costumam exigir. Deve haver cláusulas de não competição e de confidencialidade, e a cessão à empresa da propriedade '
    'intelectual criada pelos sócios, em especial o código do sócio de tecnologia. Também são importantes as regras de '
    'saída e de apuração de haveres (por morte, desligamento ou conflito), a definição de quem decide o quê (alçadas) e '
    'formas de resolver impasses, como mediação ou arbitragem. Pensando no fundo, o acordo deve prever como novos '
    'investidores entram e a possibilidade de cláusulas de antidiluição e liquidation preference, além de manter a '
    'contabilidade e as contas separadas desde o início.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma startup de saúde, constituída como sociedade limitada, quer captar R$ 300 mil agora, com amigos e um '
        'investidor-anjo, e R$ 5 milhões em dois anos, com um fundo de venture capital. Os fundadores não querem definir '
        'o valor da empresa neste momento. Um deles sugere anunciar nas redes sociais um investimento "com retorno '
        'garantido" para acelerar a captação.',
    ],
    'Proponha uma estratégia jurídica de captação para essa startup, nas duas etapas, apontando os instrumentos adequados e '
    'os cuidados necessários.',
    'Na primeira etapa, a startup pode usar o contrato de mútuo conversível ou o SAFE, que adiam a definição do valuation '
    'para uma rodada futura, ou o contrato de investimento-anjo da LC nº 123/2006, em que o investidor não é sócio, não '
    'responde pelas dívidas, só pode resgatar após 2 anos e é remunerado pelos resultados, até 50% dos lucros. A LC nº '
    '182/2021 confirma que esses aportes podem não virar participação imediatamente (art. 5º). A sugestão de anunciar '
    'retorno garantido nas redes sociais deve ser descartada: seria uma oferta pública sem registro ou dispensa da CVM, e a '
    'promessa de rentabilidade fixa pode configurar crime. Para captar do público, o caminho seria o equity crowdfunding '
    'por plataforma autorizada (Resolução CVM nº 88/2022). Na segunda etapa, o fundo deve fazer uma due diligence: a '
    'startup precisa ter a propriedade intelectual em seu nome, contratos regulares com empregados e prestadores, '
    'conformidade com a LGPD, especialmente por tratar dados de saúde, e licenças setoriais. Para receber o fundo, '
    'costuma ser necessário transformar a LTDA em S.A., com um acordo de acionistas que trate de tag along, drag along, '
    'antidiluição e liquidation preference, e converter os mútuos conforme as condições combinadas.',
)


if __name__ == '__main__':
    banco.gravar()
