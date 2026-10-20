"""
Questões médias e difíceis do capítulo 8 (Direito do Consumidor no Ambiente Digital) de Legislação em Negócios
Digitais: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/legislacao_cap8_objetivas.py

Grava em src/data/questoes/legislacao.json, trocando só as questões legislacao-cap8-o* e
legislacao-cap8-d*; as que já existiam (q* e f*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import LEGISLACAO, Banco, p

banco = Banco('legislacao-cap8', LEGISLACAO)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Pelo CDC, o consumidor precisa esperar o prazo de 30 dias para o conserto?',
    'Não: por ser produto essencial, ele pode exigir de imediato a troca, a devolução do dinheiro ou o abatimento.',
    [
        'Sim: o fornecedor sempre tem 30 dias para consertar, e só depois o consumidor pode escolher outra solução.',
        'Sim: como a geladeira é um produto durável, o fornecedor tem 90 dias para fazer o conserto.',
        'Não: o consumidor pode exigir de imediato só o abatimento do preço, pois a troca depende do conserto.',
        'Não: ele pode desistir da compra pelo arrependimento, mas só se o defeito aparecer nos primeiros 7 dias.',
    ],
    'Em regra, o fornecedor tem 30 dias para sanar o vício (art. 18, § 1º). Mas o § 3º permite ao consumidor usar de '
    'imediato as alternativas de troca, restituição ou abatimento quando se tratar de produto essencial ou quando a '
    'troca das partes puder comprometer a qualidade ou diminuir o valor do produto. Uma geladeira, que guarda alimentos, '
    'costuma ser tratada como produto essencial.',
    contexto=[p('Uma família comprou uma geladeira em uma loja virtual, e o aparelho parou de gelar no terceiro dia de uso. '
                'A loja disse que vai mandar um técnico e que a família deve esperar até 30 dias pelo conserto.')],
)

banco.multipla(
    'medio',
    'O que o CDC exige da fabricante ao descobrir o defeito depois de colocar o produto no mercado?',
    'Comunicar o fato imediatamente às autoridades e aos consumidores, inclusive por anúncios, e fazer o recall.',
    [
        'Apenas trocar o produto de quem reclamar, sem precisar avisar as autoridades nem os outros consumidores.',
        'Apenas publicar um aviso no próprio site, pois anúncios em outros meios só são exigidos de remédios.',
        'Esperar a primeira ação judicial de um consumidor ferido, pois antes disso não há dever de agir.',
        'Apenas avisar as lojas que vendem o produto, que ficam responsáveis por informar os seus clientes.',
    ],
    'Pelo art. 10, § 1º, do CDC, o fornecedor que, depois de colocar o produto no mercado, tiver conhecimento da sua '
    'periculosidade deve comunicar o fato imediatamente às autoridades competentes e aos consumidores, por meio de '
    'anúncios publicitários (§ 2º), e o chamamento (recall) é gratuito para o consumidor. O dever existe antes de '
    'qualquer acidente ou ação judicial.',
    contexto=[p('Uma fabricante de patinetes elétricos descobriu, depois de vender milhares de unidades pela internet, que '
                'um defeito na bateria pode causar superaquecimento e incêndio.')],
)

banco.assercao(
    'medio',
    'Condicionar a assinatura de um serviço de streaming à contratação de um seguro de celular é prática abusiva.',
    'O CDC proíbe condicionar o fornecimento de um produto ou serviço ao fornecimento de outro produto ou serviço.',
    0,
    'As duas são verdadeiras, e a II justifica a I. A II é o art. 39, I, do CDC, que veda a venda casada, ou seja, '
    'condicionar o fornecimento de um produto ou serviço à compra de outro, sem justa causa. Exigir o seguro de celular '
    'para liberar o streaming é exatamente essa prática, por isso é abusiva.',
    contexto=[p('Uma plataforma de streaming passou a vender a sua assinatura apenas em um pacote junto com um seguro de '
                'celular, sem oferecer a assinatura sozinha.')],
)

banco.afirmativas(
    'medio',
    [
        ('O fornecedor deve enviar ao consumidor a confirmação imediata do recebimento do pedido de arrependimento.', True),
        ('Em compras com cartão, o fornecedor deve avisar imediatamente a administradora para o estorno.', True),
        ('O arrependimento pode ser exercido pela mesma ferramenta usada na contratação, sem prejuízo de outras.', True),
        ('Para exercer o arrependimento, o consumidor deve justificar o motivo da desistência.', False),
    ],
    'I, II e III estão no art. 5º do Decreto nº 7.962/2013: a confirmação imediata (§ 4º), o aviso à administradora do '
    'cartão (§ 3º) e o uso da mesma ferramenta da contratação (§ 1º). IV é falsa: o art. 49 do CDC permite desistir no '
    'prazo de 7 dias sem nenhuma justificativa.',
    contexto=[p('Uma loja virtual está revisando o seu procedimento para os clientes que desistem da compra nos 7 dias '
                'seguintes ao recebimento.')],
)

banco.multipla(
    'medio',
    'A exigência da operadora é regular?',
    'Não: as regras do SAC garantem cancelar pelo mesmo meio usado para contratar, com efeito imediato.',
    [
        'Sim: a operadora pode escolher o canal de cancelamento, desde que atenda por telefone 24 horas por dia.',
        'Sim: o cancelamento de planos de telefonia só pode ser feito por ligação, para evitar fraudes.',
        'Não: o cancelamento deve ser feito só nas lojas físicas da operadora, com documento de identidade.',
        'Sim: a operadora pode exigir a ligação, desde que conceda um desconto para o cliente desistir.',
    ],
    'O Decreto nº 11.034/2022 traz as regras gerais do SAC para os setores regulados pelo governo federal, como '
    'telefonia: o pedido de cancelamento deve ser aceito pelos mesmos meios disponíveis para a contratação, e seus '
    'efeitos são imediatos. Dificultar o cancelamento também é prática abusiva pelo CDC. Ofertas para manter o cliente '
    'não podem impedir o cancelamento.',
    contexto=[p('Uma consumidora contratou um plano de celular pelo aplicativo da operadora. Ao tentar cancelar pelo mesmo '
                'aplicativo, foi informada de que o cancelamento só pode ser feito por ligação para a central.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Pelo CDC e pelo entendimento do STJ, o consumidor ainda pode reclamar do vício?',
    'Sim: a garantia contratual se soma à legal, e os 90 dias para reclamar só contam depois do fim da contratual.',
    [
        'Não: a garantia contratual de 1 ano substitui a legal, e ela terminou dois meses antes do defeito aparecer.',
        'Não: os 90 dias da garantia legal contam da entrega e terminaram muito antes de o defeito aparecer.',
        'Sim, mas só se o defeito for oculto, pois os vícios aparentes nunca têm garantia depois de 90 dias.',
        'Sim, pois a garantia contratual de qualquer produto durável é estendida por lei para 2 anos.',
    ],
    'A garantia contratual é complementar à legal (art. 50 do CDC). Para o STJ, o prazo decadencial de 90 dias para '
    'reclamar de vícios em produto durável (art. 26, II) só começa a correr depois que termina a garantia contratual. '
    'Como a garantia de 1 ano terminou há dois meses, o consumidor ainda está dentro dos 90 dias que vêm depois dela.',
    contexto=[p('Um consumidor comprou um notebook com garantia contratual de 1 ano, dada pelo fabricante. Catorze meses '
                'depois da compra, o teclado parou de funcionar, e a loja disse que "a garantia acabou".')],
)

banco.multipla(
    'dificil',
    'Considerando o CDC e a Súmula 359 do STJ, qual é a análise correta?',
    'O consumidor devia ser avisado por escrito antes da inscrição, e esse aviso cabe ao órgão mantenedor do cadastro.',
    [
        'Não há irregularidade, pois a dívida existe, e o aviso prévio só é exigido para dívidas acima de R$ 1.000.',
        'O aviso prévio cabe sempre à loja credora, e o órgão mantenedor do cadastro nunca responde pela falta dele.',
        'O aviso prévio só é exigido se o consumidor for idoso, e pode ser feito por telefone, sem nenhum registro.',
        'A inscrição é nula, e o consumidor deixa de dever o valor, pois a falta do aviso extingue a dívida.',
    ],
    'Pelo art. 43, § 2º, do CDC, a abertura de cadastro de dados do consumidor deve ser comunicada a ele por escrito, '
    'quando não solicitada por ele. A Súmula 359 do STJ diz que cabe ao órgão mantenedor do cadastro de proteção ao '
    'crédito notificar o devedor antes de fazer a inscrição. A falta do aviso pode gerar o cancelamento da inscrição e '
    'indenização, mas não extingue a dívida.',
    contexto=[p('Uma consumidora deixou de pagar duas parcelas de uma compra em uma loja virtual e descobriu, ao pedir um '
                'empréstimo, que o seu nome tinha sido incluído em um cadastro de inadimplentes sem nenhum aviso prévio.')],
)

banco.afirmativas(
    'dificil',
    [
        ('Na cobrança de dívidas, o consumidor não pode ser exposto a ridículo nem a constrangimento ou ameaça.', True),
        ('Publicar a lista de devedores nas redes sociais é permitido, desde que as dívidas sejam verdadeiras.', False),
        ('A quantia cobrada indevidamente e paga deve ser devolvida em dobro, salvo engano justificável.', True),
        ('A cobrança pode ser feita por e-mail ou mensagem, desde que sem constrangimento nem abuso.', True),
    ],
    'I e III estão no art. 42 do CDC: o caput proíbe expor o consumidor inadimplente a ridículo ou submetê-lo a '
    'constrangimento ou ameaça, e o parágrafo único prevê a devolução em dobro do que foi cobrado e pago indevidamente. '
    'IV é verdadeira: a cobrança em si é legítima, desde que respeite esses limites. II é falsa: expor os devedores '
    'publicamente é cobrança vexatória, mesmo com dívidas reais, e pode ser até crime (art. 71 do CDC).',
    contexto=[p('Uma escola de cursos on-line, com muitos alunos inadimplentes, discute formas de cobrar as mensalidades '
                'atrasadas. Um dos sócios sugeriu publicar no Instagram da escola a lista dos devedores.')],
)

banco.multipla(
    'dificil',
    'A cláusula que amplia o prazo de conserto para 120 dias é válida?',
    'Não: o prazo pode ir de 7 a 180 dias, mas, em contrato de adesão, deve ser combinado em separado, com aceite expresso.',
    [
        'Sim: o fornecedor pode fixar qualquer prazo nos termos de uso, pois o consumidor aceitou o contrato.',
        'Não: o prazo de 30 dias para o conserto é fixo e não pode ser ampliado nem reduzido em nenhum contrato.',
        'Sim: a lei permite ampliar o prazo até 180 dias em qualquer contrato, sem nenhuma outra exigência.',
        'Não: o prazo só pode ser ampliado se a loja oferecer, ao mesmo tempo, um produto reserva ao consumidor.',
    ],
    'O art. 18, § 2º, do CDC permite que as partes reduzam ou ampliem o prazo de 30 dias para sanar o vício, desde que '
    'ele não seja inferior a 7 nem superior a 180 dias. Mas, nos contratos de adesão, essa cláusula deve ser convencionada '
    'em separado, por manifestação expressa do consumidor. Uma regra perdida no meio dos termos de uso, aceitos por um '
    'clique, não cumpre essa exigência.',
    contexto=[p('Os termos de uso de uma loja virtual de eletrônicos, aceitos com um clique na finalização da compra, dizem, '
                'no meio de várias outras regras, que "a loja terá 120 dias para consertar produtos com defeito".')],
)

banco.multipla(
    'dificil',
    'Quem responde pelos danos sofridos pelo consumidor?',
    'A fabricante, que é conhecida; a loja só responderia se a fabricante não pudesse ser identificada (art. 13).',
    [
        'Só a loja virtual, pois foi ela quem vendeu o celular e recebeu o pagamento do consumidor.',
        'A loja e a fabricante, sempre de forma solidária, como em qualquer vício do produto vendido.',
        'Ninguém, pois o consumidor estava carregando o celular, e a explosão é culpa exclusiva dele.',
        'Só a fabricante, e o consumidor tem só 90 dias para entrar na Justiça, por ser produto durável.',
    ],
    'A explosão que causa queimaduras é fato do produto, um acidente de consumo: a fabricante responde, independentemente '
    'de culpa, pelos danos causados pelo defeito (art. 12). No fato do produto, o comerciante só responde quando o '
    'fabricante não puder ser identificado, quando o produto não tiver identificação clara ou quando ele não conservar '
    'bem produtos perecíveis (art. 13). O prazo para a ação de reparação é de 5 anos (art. 27), e carregar o celular é uso '
    'normal.',
    contexto=[p('Um consumidor comprou um celular de uma marca conhecida em uma loja virtual. Meses depois, o aparelho '
                'explodiu enquanto carregava, causando queimaduras na mão dele. O consumidor processou apenas a loja.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Uma loja virtual de eletrônicos tem hoje a seguinte política de trocas: "Não aceitamos devoluções de produtos '
        'abertos. Em caso de defeito, o cliente deve enviar o produto ao fabricante por conta própria. O frete nunca é '
        'devolvido. O estorno no cartão será feito em até 90 dias. Produtos em promoção não têm garantia".',
    ],
    'Avalie essa política à luz do CDC e do Decreto nº 7.962/2013 e proponha uma nova política de trocas e devoluções.',
    'Quase todas as regras são irregulares. No arrependimento, o consumidor pode desistir em até 7 dias do recebimento, '
    'sem justificativa, mesmo que tenha aberto o produto para conhecê-lo (art. 49 do CDC), com devolução imediata e '
    'integral dos valores, inclusive o frete; o custo do retorno é do fornecedor, e a loja deve avisar imediatamente a '
    'administradora do cartão, confirmando o pedido ao consumidor (art. 5º do Decreto nº 7.962/2013). Nos vícios, a loja '
    'responde solidariamente com o fabricante (art. 18) e não pode mandar o cliente resolver sozinho; o consumidor tem 30 '
    'dias para reclamar de produtos não duráveis e 90 dias para duráveis (art. 26), e, se o vício não for sanado em 30 '
    'dias, escolhe entre troca, devolução do dinheiro ou abatimento, ou pode exigir isso de imediato em produtos '
    'essenciais. Produtos em promoção têm a mesma garantia legal, que não pode ser excluída (arts. 24 e 51, I). A nova '
    'política deve informar com clareza esses direitos e os canais para exercê-los, aceitar a desistência pela mesma '
    'ferramenta da compra, oferecer a coleta do produto sem custo para o cliente e prever o estorno imediato.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma empresa de assinaturas de software para pessoas físicas recebe centenas de reclamações por mês: cobranças '
        'depois do cancelamento, demora no atendimento e entregas de acesso que não acontecem. Muitos clientes vão direto ao '
        'Procon e aos Juizados, e a empresa costuma perder as ações porque não guarda registros do atendimento nem das '
        'entregas.',
    ],
    'Proponha uma estratégia para que a empresa resolva os conflitos com os consumidores e reduza os riscos jurídicos.',
    'A empresa deve tratar a causa das reclamações e melhorar o atendimento. Pelo Decreto nº 7.962/2013, precisa manter '
    'um atendimento eficaz em meio eletrônico, respondendo às reclamações em até 5 dias, e permitir o cancelamento '
    'simples, com efeito imediato. As cobranças depois do cancelamento são indevidas e geram devolução em dobro, salvo '
    'engano justificável (art. 42, parágrafo único, do CDC), por isso o sistema de cobrança deve ser corrigido e os '
    'valores devolvidos sem esperar a Justiça. Como o juiz pode inverter o ônus da prova (art. 6º, VIII), a empresa deve '
    'guardar registros de cada contratação, atendimento, cancelamento e entrega de acesso, como logs, protocolos e '
    'e-mails. Vale cadastrar-se no consumidor.gov.br, onde a empresa tem até 10 dias para responder e muitos conflitos se '
    'resolvem sem processo, acompanhar as reclamações no Procon e propor acordos, inclusive nos Juizados, que julgam '
    'causas de até 40 salários mínimos. Por fim, deve medir os motivos das reclamações, treinar a equipe, revisar os termos '
    'de uso para retirar cláusulas abusivas e informar com clareza preços, renovações e prazos.',
)


if __name__ == '__main__':
    banco.gravar()
