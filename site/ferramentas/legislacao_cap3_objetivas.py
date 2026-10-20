"""
Questões médias e difíceis do capítulo 3 (E-commerce e Contratos Digitais) de Legislação em Negócios Digitais:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/legislacao_cap3_objetivas.py

Grava em src/data/questoes/legislacao.json, trocando só as questões legislacao-cap3-o* e
legislacao-cap3-d*; as que já existiam (q* e f*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import LEGISLACAO, Banco, p

banco = Banco('legislacao-cap3', LEGISLACAO)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Os negócios 1, 2, 3 e 4 correspondem, respectivamente, aos modelos',
    'D2C, C2C, B2B e social commerce.',
    ['B2C, C2C, B2B e marketplace.', 'D2C, B2C, B2B e social commerce.', 'D2C, C2C, marketplace e B2C.',
     'B2B, C2C, D2C e social commerce.'],
    'Quando o próprio fabricante vende ao consumidor final, sem intermediários, o modelo é D2C (1). Consumidores vendendo '
    'entre si é C2C (2). Transações entre empresas são B2B (3). Vendas feitas diretamente nas redes sociais, como em '
    'transmissões ao vivo, são social commerce (4). Uma mesma empresa pode atuar em vários modelos ao mesmo tempo.',
    contexto=[p('Considere os negócios a seguir: '
                '(1) uma fábrica de tênis vende seus produtos diretamente ao consumidor, pelo próprio site; '
                '(2) um aplicativo em que pessoas vendem roupas usadas umas às outras; '
                '(3) uma indústria que vende embalagens para outras empresas por um portal de pedidos; '
                '(4) uma marca de cosméticos que vende por transmissões ao vivo em uma rede social.')],
)

banco.afirmativas(
    'medio',
    [
        ('No clickwrap, o usuário marca "Li e aceito", e o registro de IP, data e hora ajuda a provar o aceite.', True),
        ('No browsewrap, os termos ficam só no rodapé e o uso do site é tratado como aceite, o modelo mais frágil.', True),
        ('Os contratos por clique são inválidos, pois o Código Civil exige assinatura manuscrita nos contratos.', False),
        ('Um contrato fechado por troca de e-mails só vale se as partes usarem assinatura eletrônica qualificada.', False),
    ],
    'I e II descrevem corretamente o clickwrap e o browsewrap; este é o mais frágil como prova, porque não há uma '
    'manifestação clara de aceite. III é falsa: o Código Civil adota a liberdade de forma (art. 107), e o contrato por '
    'clique é válido quando a lei não exige forma especial. IV é falsa: proposta e aceitação expressas por e-mail formam '
    'um contrato válido, sem exigir assinatura qualificada.',
    contexto=[p('Uma loja virtual está revisando a forma como os clientes aceitam os seus termos de uso e quer saber o '
                'valor jurídico de cada modelo de contratação eletrônica.')],
)

banco.multipla(
    'medio',
    'Pelo Decreto nº 7.962/2013, em quanto tempo a loja deveria ter respondido à reclamação?',
    'Em até 5 dias, prazo para o fornecedor encaminhar ao consumidor a resposta às reclamações.',
    [
        'Em até 30 dias, prazo para o fornecedor sanar vícios do produto previsto no art. 18 do CDC.',
        'Em até 10 dias, prazo que as empresas têm para responder às reclamações do consumidor.gov.br.',
        'Em até 7 dias, prazo para o exercício do direito de arrependimento nas compras fora da loja.',
        'Não há prazo, pois o decreto exige apenas um canal de atendimento, sem fixar tempo de resposta.',
    ],
    'O art. 4º do Decreto nº 7.962/2013 obriga o fornecedor a manter atendimento adequado e eficaz em meio eletrônico, e '
    'o seu parágrafo único fixa que a manifestação do fornecedor às reclamações deve ser encaminhada ao consumidor em até '
    '5 dias. O decreto também exige o sumário do contrato antes da compra e a confirmação imediata do pedido. Os demais '
    'prazos existem, mas tratam de outras situações.',
    contexto=[p('Uma consumidora enviou, pelo canal de atendimento de uma loja virtual, uma reclamação sobre a cobrança de '
                'um valor diferente do anunciado. A loja só respondeu 20 dias depois, dizendo que "não há prazo legal '
                'para responder a reclamações".')],
)

banco.multipla(
    'medio',
    'Quanto à validade das compras, é correto afirmar que',
    'a compra do adolescente de 15 anos é nula, e a do de 17 anos é anulável, por incapacidade de cada um.',
    [
        'as duas compras são válidas, pois quem compra pela internet presume-se maior de idade e capaz.',
        'as duas compras são nulas, pois qualquer menor de 18 anos é absolutamente incapaz para contratar.',
        'a compra do adolescente de 15 anos é anulável, e a do de 17 anos é nula, pela regra do Código Civil.',
        'as duas compras são anuláveis, e só os pais podem pedir a anulação, no prazo de 7 dias da entrega.',
    ],
    'Pelo art. 104 do Código Civil, a validade do negócio exige agente capaz. Os menores de 16 anos são absolutamente '
    'incapazes (art. 3º), e o negócio feito por eles é nulo (art. 166, I). Os maiores de 16 e menores de 18 são '
    'relativamente incapazes (art. 4º, I), e o negócio feito sem assistência é anulável (art. 171, I). O prazo de 7 dias '
    'é o do arrependimento, que é outra coisa.',
    contexto=[p('Dois irmãos, um de 15 e outro de 17 anos, compraram, cada um, um videogame de R$ 4.000 em uma loja '
                'virtual, usando o cartão de crédito dos pais sem que eles soubessem. Os pais querem desfazer as compras.')],
)

banco.assercao(
    'medio',
    'Exercido o arrependimento em uma compra com cartão de crédito, o fornecedor deve comunicar imediatamente a '
    'administradora para que a transação não seja lançada ou seja estornada.',
    'O Decreto nº 7.962/2013 obriga o fornecedor a informar, de forma clara e ostensiva, os meios adequados e eficazes '
    'para o exercício do direito de arrependimento.',
    1,
    'As duas são verdadeiras, mas a II não justifica a I. A I é o art. 5º, § 3º, do Decreto nº 7.962/2013, que trata do '
    'efeito do arrependimento sobre o pagamento com cartão. A II é o caput do mesmo artigo, que trata do dever de '
    'informar como o consumidor pode desistir. São deveres distintos: informar os meios não explica a obrigação de '
    'avisar a administradora do cartão.',
    contexto=[p('Um consumidor desistiu, no terceiro dia após o recebimento, de um fone de ouvido comprado em 10 parcelas no '
                'cartão de crédito, e a loja disse que ele teria de continuar pagando as parcelas até o estorno.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Qual é a situação mais provável da loja ao contestar o chargeback?',
    'Tende a perder: cabe a ela provar que entregou o produto, e sem rastreio nem assinatura ela não tem essa prova.',
    [
        'Tende a ganhar: cabe ao cliente provar que não recebeu o produto, pois ninguém é obrigado a provar fato negativo.',
        'Tende a ganhar: o chargeback só é aceito quando o cliente apresenta um boletim de ocorrência da não entrega.',
        'Tende a perder, mas pode cobrar o valor da transportadora sozinha, pois a loja não responde pela entrega.',
        'Não pode contestar, pois o chargeback é definitivo e a loja não tem nenhum meio de discutir a cobrança.',
    ],
    'No chargeback, o portador contesta a compra diretamente com o emissor do cartão, e o lojista precisa demonstrar que a '
    'transação foi legítima e cumprida. Sem rastreamento, comprovante de entrega ou assinatura, a loja não tem como provar '
    'a entrega, e, num processo de consumo, o juiz ainda pode inverter o ônus da prova (art. 6º, VIII, do CDC). A '
    'transportadora integra a cadeia de fornecimento, mas a loja responde perante o cliente.',
    contexto=[p('Uma loja virtual envia seus produtos por uma transportadora, sem rastreamento e sem exigir assinatura na '
                'entrega. Um cliente pediu ao banco o chargeback de uma compra de R$ 2.500, alegando que nunca recebeu o '
                'produto. A loja quer contestar.')],
)

banco.multipla(
    'dificil',
    'Pela Lei nº 9.099/1995, qual é a situação da empresa no Juizado Especial Cível?',
    'Pode usar o Juizado, que julga causas de até 40 salários mínimos, mas precisa de advogado, por passar de 20.',
    [
        'Não pode usar o Juizado, pois ele só julga causas de até 20 salários mínimos, sem advogado.',
        'Pode usar o Juizado sem advogado, pois a assistência só é obrigatória acima de 40 salários mínimos.',
        'Não pode usar o Juizado, pois empresas nunca podem ser autoras de ações nos Juizados Especiais.',
        'Pode usar o Juizado sem advogado, pois a dispensa vale para qualquer causa de consumo, em qualquer valor.',
    ],
    'O Juizado Especial Cível julga causas de até 40 salários mínimos (art. 3º, I). Nas de até 20 salários mínimos, a '
    'parte pode ir sem advogado; acima disso, a assistência é obrigatória (art. 9º). Microempresas e empresas de pequeno '
    'porte podem ser autoras no Juizado (art. 8º, § 1º, II), por isso a startup, sendo microempresa, pode usá-lo, mas '
    'com advogado.',
    contexto=[p('Uma startup de software, registrada como microempresa, quer cobrar de um cliente uma dívida equivalente a '
                '30 salários mínimos, referente a um contrato digital de prestação de serviços que não foi pago.')],
)

banco.afirmativas(
    'dificil',
    [
        ('As prestadoras de serviços de ativos virtuais só podem funcionar com autorização do Banco Central.', True),
        ('A lei criou o crime de fraude com utilização de ativos virtuais, com pena de reclusão de 4 a 8 anos.', True),
        ('Desde 2022, os criptoativos são moeda de curso legal no Brasil, ao lado do real.', False),
        ('A lei proíbe as pessoas físicas de comprar e vender criptomoedas, permitindo isso só a empresas.', False),
    ],
    'I e II estão de acordo com a Lei nº 14.478/2022: as prestadoras de serviços de ativos virtuais dependem de '
    'autorização de órgão federal, que o Decreto nº 11.563/2023 definiu como o Banco Central, e a lei incluiu no Código '
    'Penal o art. 171-A, com reclusão de 4 a 8 anos e multa. III é falsa: o real continua sendo a única moeda de curso '
    'legal. IV é falsa: a lei regula as prestadoras desses serviços, e não proíbe as pessoas de negociar criptoativos.',
    contexto=[p('Uma loja virtual quer aceitar pagamentos em criptomoedas por meio de uma corretora (exchange) e pediu ao '
                'jurídico um resumo do marco legal dos ativos virtuais.')],
)

banco.multipla(
    'dificil',
    'Considerando a MP nº 2.200-2/2001, a alegação da empresa contestante procede?',
    'Não: a MP admite outros meios aceitos pelas partes; só falta a presunção legal, e a prova vem da trilha de auditoria.',
    [
        'Sim: só a assinatura com certificado ICP-Brasil tem validade jurídica, e qualquer outra é nula para todos os fins.',
        'Sim: contratos acima de R$ 1 milhão só podem ser assinados com certificado ICP-Brasil, por exigência expressa da MP.',
        'Não: a assinatura avançada tem a mesma presunção de veracidade da ICP-Brasil, e a empresa nem pode contestar.',
        'Não: assinaturas eletrônicas não podem ser contestadas em juízo depois de 30 dias da data da assinatura.',
    ],
    'O art. 10, § 1º, da MP nº 2.200-2/2001 dá presunção de veracidade apenas às assinaturas com certificado ICP-Brasil. '
    'Mas o § 2º não impede o uso de outros meios de comprovar a autoria e a integridade, desde que admitidos pelas partes '
    'como válidos ou aceitos por quem recebe o documento. Como as empresas escolheram a plataforma, o contrato vale; sem a '
    'presunção legal, a prova se faz pela trilha de auditoria, com biometria, IP, data, hora e hash do documento.',
    contexto=[p('Duas empresas assinaram um contrato de R$ 2 milhões em uma plataforma de assinatura eletrônica avançada, '
                'com verificação por biometria facial, que elas mesmas escolheram. Meses depois, uma delas alega que o '
                'contrato não vale, porque "só a assinatura com certificado ICP-Brasil tem validade jurídica".')],
)

banco.multipla(
    'dificil',
    'A cobrança da multa de fidelidade é válida?',
    'Tende a não ser: cláusula que limita direitos deve vir em destaque, ou não obriga o consumidor.',
    [
        'É válida, pois o consumidor marcou "Li e aceito", o que torna obrigatórias todas as cláusulas do contrato.',
        'É válida, pois os contratos de adesão de serviços digitais não seguem as regras de destaque previstas no CDC.',
        'Tende a não ser, mas só porque o valor da multa passa de 10% do total, limite fixado pelo CDC para multas.',
        'É válida, desde que a empresa ofereça um desconto de 50% na multa para quem cancelar no primeiro ano.',
    ],
    'Nos contratos de adesão, as cláusulas que limitam direitos do consumidor devem ser redigidas com destaque, para fácil '
    'compreensão (art. 54, § 4º, do CDC). Além disso, o contrato não obriga o consumidor se ele não teve a oportunidade de '
    'conhecer o seu conteúdo previamente ou se o texto dificulta a compreensão (art. 46), e as cláusulas são interpretadas '
    'a favor dele (art. 47). Uma multa escondida no meio de 30 páginas, sem destaque, não cumpre essas regras.',
    contexto=[p('Um aplicativo de academia on-line vende planos mensais. No meio dos termos de uso, de 30 páginas, sem '
                'nenhum destaque, há uma cláusula de fidelidade de 24 meses com multa de R$ 600 em caso de cancelamento. '
                'O aceite é feito por um único clique em "Li e aceito". Um cliente cancelou no terceiro mês e recebeu a '
                'cobrança da multa.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Uma pequena marca de roupas vai abrir a sua loja virtual própria e também vender em um marketplace. O site terá '
        'cadastro de clientes, pagamento por cartão, Pix e boleto, entrega pelos Correios e cupons de desconto enviados por '
        'e-mail. As sócias pretendem usar um modelo de termos de uso copiado da internet e ainda não pensaram no '
        'atendimento ao cliente.',
    ],
    'Proponha as medidas jurídicas que a marca deve adotar para lançar a loja virtual em conformidade com a legislação.',
    'Pelo Decreto nº 7.962/2013, o site deve mostrar em local visível o nome empresarial, o CNPJ e os endereços físico e '
    'eletrônico, inclusive na página do marketplace, e informar com clareza as características dos produtos, o preço '
    'total com frete e encargos, as condições de pagamento e o prazo de entrega. Antes da compra, deve apresentar um '
    'sumário do contrato, com destaque para as cláusulas que limitam direitos, permitir corrigir erros, confirmar '
    'imediatamente o pedido e manter um canal de atendimento eficaz, respondendo às reclamações em até 5 dias. Deve '
    'informar como exercer o arrependimento em 7 dias (art. 49 do CDC), com devolução integral, inclusive do frete, e '
    'aviso imediato à administradora do cartão. A oferta vincula (art. 30), e os termos de uso não podem ser copiados: '
    'precisam refletir o negócio, sem cláusulas abusivas (art. 51), como as que excluem responsabilidade por vícios ou '
    'impõem arbitragem. Na LGPD, a loja precisa de política de privacidade, de base legal para cada finalidade e de '
    'consentimento próprio para os cupons por e-mail, além de medidas de segurança; os pagamentos devem passar por '
    'instituições autorizadas pelo Banco Central, com cuidado contra fraudes. Por fim, a marca responde pelos vícios dos '
    'produtos, inclusive vendidos no marketplace, que também pode responder solidariamente.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma construtora quer eliminar o papel e assinar tudo digitalmente: os contratos com fornecedores de material, a '
        'venda de um galpão de R$ 2 milhões, o aceite dos termos de uso do aplicativo pelos clientes e as notas fiscais '
        'eletrônicas que emite. O diretor sugere usar, para todos esses casos, a mesma assinatura simples por e-mail, que '
        'é a mais barata.',
    ],
    'Avalie a sugestão do diretor, indicando a forma de assinatura ou de contratação adequada a cada situação.',
    'A sugestão não serve para todos os casos. Contratos digitais são válidos quando cumprem o art. 104 do Código Civil e '
    'a lei não exige forma especial, e a escolha da assinatura depende do risco e da exigência legal. Para os contratos '
    'com fornecedores, uma assinatura avançada, por plataforma que registre autenticidade, integridade e não repúdio '
    '(biometria, IP, hash, trilha de auditoria), é adequada; a simples até vale, mas é mais fácil de contestar, e só a '
    'qualificada, com certificado ICP-Brasil, tem presunção legal de veracidade (MP nº 2.200-2/2001). O aceite dos '
    'termos do aplicativo pode ser por clique (clickwrap), com registro do aceite, desde que os termos sejam claros e as '
    'cláusulas limitativas venham em destaque. A venda do galpão, acima de 30 salários mínimos, exige escritura pública '
    '(art. 108 do Código Civil), que pode ser feita eletronicamente, mas por um tabelião, e depois registrada no cartório '
    'de imóveis; nenhuma assinatura eletrônica substitui isso. As notas fiscais eletrônicas exigem certificado digital '
    'ICP-Brasil, ou seja, assinatura qualificada. Assim, a empresa economiza onde a lei permite, mas usa a forma exigida '
    'onde há risco ou obrigação legal.',
)


if __name__ == '__main__':
    banco.gravar()
