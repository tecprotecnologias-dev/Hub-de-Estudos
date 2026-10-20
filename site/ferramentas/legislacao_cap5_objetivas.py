"""
Questões médias e difíceis do capítulo 5 (Marketing Digital e Publicidade) de Legislação em Negócios Digitais:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/legislacao_cap5_objetivas.py

Grava em src/data/questoes/legislacao.json, trocando só as questões legislacao-cap5-o* e
legislacao-cap5-d*; as que já existiam (q* e f*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import LEGISLACAO, Banco, p

banco = Banco('legislacao-cap5', LEGISLACAO)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As práticas 1, 2, 3 e 4 correspondem, respectivamente, aos dark patterns',
    'confirmshaming, hidden costs, privacy zuckering e trick questions.',
    ['roach motel, hidden costs, privacy zuckering e trick questions.',
     'confirmshaming, trick questions, privacy zuckering e hidden costs.',
     'confirmshaming, hidden costs, trick questions e privacy zuckering.',
     'trick questions, roach motel, privacy zuckering e confirmshaming.'],
    'O botão de recusa com texto que constrange é confirmshaming (1). Taxas reveladas só na última etapa do checkout são '
    'hidden costs (2). Uma interface confusa que leva a compartilhar mais dados do que se pretendia é privacy zuckering '
    '(3). Perguntas confusas, com dupla negação, que levam a aceitar comunicações sem perceber são trick questions (4). '
    'Todas comprometem a decisão livre e informada do consumidor.',
    contexto=[p('Em um aplicativo de compras, foram encontradas quatro práticas: '
                '(1) o botão para recusar o cupom diz "Não, prefiro pagar mais caro"; '
                '(2) uma "taxa de serviço" aparece só na última tela antes do pagamento; '
                '(3) as configurações são tão confusas que o usuário acaba liberando o acesso aos seus contatos; '
                '(4) a caixa do cadastro diz "Não quero deixar de receber ofertas" e já vem marcada.')],
)

banco.assercao(
    'medio',
    'Anunciar um produto como "carbono neutro" sem nenhuma comprovação técnica pode configurar publicidade enganosa.',
    'É enganosa a informação publicitária capaz de induzir o consumidor em erro sobre as propriedades do produto, ainda '
    'que por omissão.',
    0,
    'As duas são verdadeiras, e a II justifica a I. A alegação ambiental sem comprovação (greenwashing) é capaz de levar '
    'o consumidor a acreditar em uma propriedade que o produto talvez não tenha, o que se encaixa no conceito de '
    'publicidade enganosa do art. 37, § 1º, do CDC. Além disso, cabe a quem patrocina o anúncio provar a veracidade da '
    'informação (art. 38).',
    contexto=[p('Uma marca de garrafas plásticas lançou uma campanha nas redes sociais dizendo que os seus produtos são '
                '"100% carbono neutro", sem ter feito nenhum estudo ou certificação sobre as emissões.')],
)

banco.multipla(
    'medio',
    'Qual é a análise mais adequada sobre a base legal desses e-mails?',
    'Podem se apoiar no legítimo interesse (soft opt-in), se a compra é recente, o produto parecido e a saída fácil.',
    [
        'Exigem sempre o double opt-in, pois o e-mail marketing só é válido com confirmação dupla do consentimento.',
        'Dispensam qualquer base legal, pois quem já comprou na loja autorizou receber ofertas por tempo indeterminado.',
        'São proibidos, pois a LGPD veda o envio de qualquer comunicação comercial a clientes, salvo por ordem judicial.',
        'Podem ser enviados sem descadastramento, pois o cliente que comprou não tem o direito de se opor às ofertas.',
    ],
    'Para clientes atuais, a oferta de produtos semelhantes aos que eles já compraram pode se apoiar no legítimo '
    'interesse (art. 7º, IX), o chamado soft opt-in, desde que a relação seja recente, o uso seja esperado pelo cliente, '
    'haja transparência e cada e-mail traga um descadastramento fácil. O double opt-in é uma boa prática para o '
    'consentimento, mas não é a única base possível; e o titular sempre pode se opor ao tratamento.',
    contexto=[p('Uma loja virtual de artigos esportivos quer enviar, aos clientes que compraram tênis de corrida nos '
                'últimos três meses, e-mails com ofertas de outros produtos de corrida, com um link de descadastramento '
                'em cada mensagem.')],
)

banco.afirmativas(
    'medio',
    [
        ('A propaganda de cigarros é proibida na internet, restando apenas a exposição nos pontos de venda.', True),
        ('Os medicamentos de venda sob prescrição médica só podem ser anunciados a profissionais de saúde.', True),
        ('Anúncios de apostas podem apresentá-las como forma de investimento ou de renda, se trouxerem alerta.', False),
        ('Anúncios de crédito podem deixar de informar o CET, desde que mostrem a taxa de juros mensal.', False),
    ],
    'I e II estão de acordo com a Lei nº 9.294/1996 e com as normas da ANVISA (RDC nº 96/2008). III é falsa: a Lei nº '
    '14.790/2023 e as regras do Ministério da Fazenda proíbem apresentar as apostas como investimento ou fonte de renda, '
    'além de vedar a publicidade dirigida a menores. IV é falsa: as ofertas de crédito devem informar o Custo Efetivo '
    'Total, que inclui juros, tarifas e encargos.',
    contexto=[p('Uma agência de publicidade digital atende clientes de vários setores e preparou um guia sobre as regras '
                'específicas de cada um.')],
)

banco.multipla(
    'medio',
    'Pelas regras do CONAR, essa publicidade comparativa é',
    'admitida, se for objetiva e comprovável e não denegrir o concorrente nem causar confusão entre as marcas.',
    [
        'proibida, pois o CONAR não admite citar o nome de concorrentes em nenhum tipo de anúncio no Brasil.',
        'admitida só se o concorrente autorizar por escrito o uso da sua marca e dos resultados dos testes.',
        'admitida, mesmo sem comprovação, pois a comparação é uma opinião protegida pela liberdade de expressão.',
        'proibida, pois a comparação de preços e de desempenho é sempre considerada concorrência desleal.',
    ],
    'O Código do CONAR admite a publicidade comparativa quando o seu objetivo é esclarecer ou defender o consumidor, desde '
    'que a comparação seja objetiva, entre produtos equivalentes, e possa ser comprovada, sem denegrir a imagem do '
    'concorrente, causar confusão entre as marcas ou configurar concorrência desleal. Testes de laboratório independentes '
    'ajudam a comprovar a afirmação.',
    contexto=[p('Uma fabricante de celulares publicou anúncios dizendo que a bateria do seu modelo dura 30% mais que a do '
                'principal concorrente, citado pelo nome, com base em testes feitos por um laboratório independente.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Considerando o ECA Digital e a LGPD, a estratégia de anúncios do aplicativo é',
    'vedada: o ECA Digital proíbe o perfilamento para direcionar publicidade a crianças e adolescentes.',
    [
        'permitida, pois as regras especiais só protegem crianças de até 12 anos, e não adolescentes.',
        'permitida, desde que o próprio adolescente aceite os termos de uso ao instalar o aplicativo.',
        'permitida, desde que o aplicativo mostre um banner de cookies antes de exibir os anúncios.',
        'vedada só para os anúncios de jogos, sendo permitida para os demais produtos e serviços.',
    ],
    'A Lei nº 15.211/2025 (ECA Digital) reforçou a proteção de crianças e adolescentes em produtos e serviços digitais e '
    'proíbe usar técnicas de perfilamento para direcionar publicidade comercial a eles. Na LGPD, o tratamento de dados de '
    'crianças e adolescentes deve atender ao seu melhor interesse (art. 14). O aceite do próprio adolescente ou um banner '
    'de cookies não afasta essa proibição.',
    contexto=[p('Um aplicativo de jogos, usado principalmente por adolescentes de 13 a 16 anos, monta perfis de '
                'comportamento de cada usuário e os usa para exibir anúncios personalizados de lanches, roupas e outros '
                'jogos.')],
)

banco.multipla(
    'dificil',
    'Qual é a análise correta sobre essa prática?',
    'Os dados revelam saúde e são sensíveis, mesmo inferidos; o envio exige base do art. 11, que limita o uso econômico.',
    [
        'Não há dado sensível, pois a farmácia só enviou e-mails e telefones, e não diagnósticos dos clientes.',
        'É lícita, pois o legítimo interesse permite compartilhar qualquer dado para fins de publicidade digital.',
        'É lícita, pois a rede social é operadora da farmácia, e o envio entre operadores dispensa base legal.',
        'Só seria irregular se a farmácia vendesse a lista, pois o compartilhamento gratuito não é tratamento.',
    ],
    'Saber que alguém compra remédios para diabetes revela um dado referente à saúde, que é sensível (art. 5º, II), '
    'mesmo que a lista traga só e-mails e telefones. O tratamento de dados sensíveis só é possível nas hipóteses do art. '
    '11, que não incluem o legítimo interesse, e o § 4º restringe o compartilhamento de dados de saúde com o objetivo de '
    'obter vantagem econômica. Compartilhar, com ou sem pagamento, também é tratamento (art. 5º, X).',
    contexto=[p('Uma farmácia on-line separou os clientes que compram medicamentos para diabetes e enviou os e-mails e '
                'telefones deles a uma rede social, para criar um público de anúncios e encontrar pessoas parecidas '
                '(lookalike).')],
)

banco.afirmativas(
    'dificil',
    [
        ('Cabe ao controlador o ônus de provar que o consentimento foi obtido de acordo com a lei.', True),
        ('O consentimento deve ser dado por escrito ou por outro meio que demonstre a vontade do titular.', True),
        ('É vedado o tratamento de dados pessoais mediante vício de consentimento.', True),
        ('Autorizações genéricas são válidas, desde que o titular possa revogá-las depois.', False),
    ],
    'I, II e III estão no art. 8º da LGPD: o ônus da prova é do controlador (§ 2º), o consentimento deve ser fornecido '
    'por escrito ou por outro meio que demonstre a manifestação de vontade (caput), e o tratamento com vício de '
    'consentimento é vedado (§ 3º). IV é falsa: as autorizações genéricas são nulas, pois o consentimento deve se referir '
    'a finalidades determinadas (§ 4º); a possibilidade de revogação não corrige isso.',
    contexto=[p('Uma empresa de e-mail marketing foi questionada pela ANPD sobre a forma como obtém e registra o '
                'consentimento dos destinatários das suas campanhas.')],
)

banco.multipla(
    'dificil',
    'À luz do CDC, alterado pela Lei do Superendividamento, essa campanha é',
    'irregular: a lei proíbe anunciar crédito sem consulta ou sem avaliação financeira e assediar consumidores idosos.',
    [
        'regular, pois a oferta de crédito a aposentados é livre, e o CDC não traz regras específicas sobre o tema.',
        'regular, desde que o contrato final traga a taxa de juros, ainda que o anúncio não fale nos custos do crédito.',
        'irregular só porque usa ligações, pois ofertas de crédito por mensagem de texto são sempre permitidas.',
        'irregular só se algum aposentado ficar inadimplente, pois o superendividamento exige dano já ocorrido.',
    ],
    'A Lei nº 14.181/2021 incluiu no CDC o art. 54-C, que proíbe, na oferta de crédito, indicar que a operação pode ser '
    'concluída sem consulta a serviços de proteção ao crédito ou sem avaliação da situação financeira do consumidor, e '
    'assediar ou pressionar o consumidor, principalmente se for idoso. A oferta também deve informar o custo efetivo '
    'total e os encargos (art. 54-B). A proibição vale para a própria oferta, sem depender de dano.',
    contexto=[p('Uma financeira faz ligações e envia mensagens diárias a aposentados com o anúncio: "Crédito na hora para '
                'negativados, sem consulta ao SPC e sem análise de renda. Aproveite hoje!".')],
)

banco.multipla(
    'dificil',
    'Como se classifica esse anúncio pelo CDC?',
    'Publicidade enganosa por omissão: a redução da velocidade é dado essencial, e escondê-la induz o consumidor a erro.',
    [
        'Publicidade abusiva, pois explora o medo que o consumidor tem de ficar sem internet no fim do mês.',
        'Publicidade lícita, pois a regra sobre a redução da velocidade aparece no rodapé da própria página do plano.',
        'Publicidade enganosa só se a operadora cortar a internet por completo depois que a franquia acabar.',
        'Publicidade lícita, pois o consumidor pode desistir do plano em 7 dias se não gostar do serviço.',
    ],
    'Pelo art. 37, § 3º, do CDC, a publicidade é enganosa por omissão quando deixa de informar dado essencial do produto '
    'ou serviço. Anunciar "internet ilimitada" e esconder, em letras miúdas, que a velocidade cai a quase nada depois de '
    'uma franquia leva o consumidor a erro sobre a característica principal do plano. O direito de arrependimento não '
    'torna lícita uma publicidade enganosa.',
    contexto=[p('Uma operadora anuncia em destaque um plano de celular com "internet ilimitada". Só no rodapé da página, em '
                'letras pequenas, informa que, depois de 20 GB por mês, a velocidade é reduzida a um nível que impede '
                'assistir a vídeos ou fazer chamadas.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Uma marca de suplementos vai lançar um produto com uma campanha digital: vídeos de influenciadoras que receberão '
        'o produto e um pagamento, anúncios segmentados por interesse em academia e dieta, e-mails para uma lista de '
        'contatos comprada de uma agência e a frase "emagrece até 8 kg em um mês" na embalagem e nos anúncios. Parte do '
        'público das influenciadoras tem menos de 18 anos.',
    ],
    'Analise os riscos jurídicos dessa campanha e proponha os ajustes necessários.',
    'A promessa de emagrecimento sem comprovação pode ser publicidade enganosa (art. 37, § 1º, do CDC), e cabe à marca '
    'provar o que anuncia (art. 38); alegações sobre saúde também estão sujeitas às regras da ANVISA. Deve-se retirar a '
    'promessa ou sustentá-la com estudos válidos. Os vídeos das influenciadoras são publicidade, mesmo que a contrapartida '
    'fosse só o produto, e precisam ser identificados de forma clara, no início, com marcações como "#publi" (art. 36 do '
    'CDC e regras do CONAR); as influenciadoras devem ter experiência real com o produto e podem responder junto com a '
    'marca. Como parte do público é menor de idade, a campanha não deve ser dirigida a eles: o CDC considera abusiva a '
    'publicidade que se aproveita da inexperiência infantil, e o ECA Digital proíbe o perfilamento para publicidade a '
    'crianças e adolescentes, por isso a segmentação deve excluir menores. Nos anúncios segmentados, a marca precisa de '
    'base legal na LGPD e de consentimento para cookies e rastreadores não essenciais. A lista de e-mails comprada não traz '
    'consentimento válido e deve ser descartada; a marca deve formar uma lista própria, com opt-in e descadastramento '
    'fácil. O contrato com as influenciadoras deve prever a identificação, a aprovação prévia do conteúdo e a '
    'responsabilidade pelas afirmações.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Um aplicativo de cursos de idiomas oferece 7 dias grátis, mas exige o cartão de crédito no início e passa a cobrar '
        'automaticamente a assinatura anual depois do teste. O aviso da cobrança aparece só em letras pequenas. Para '
        'cancelar, o usuário passa por cinco telas, com mensagens como "Tem certeza de que quer desistir de aprender?", e o '
        'botão de cancelar é cinza e pequeno. No cadastro, a opção de receber ofertas de parceiros já vem marcada.',
    ],
    'Identifique os dark patterns presentes nesse aplicativo, explique por que são irregulares e proponha um redesenho '
    'conforme a legislação.',
    'O aplicativo reúne vários dark patterns. A cobrança automática da assinatura anual, informada só em letras pequenas, '
    'é um custo escondido e pode ser publicidade enganosa por omissão de dado essencial (art. 37, §§ 1º e 3º, do CDC), '
    'além de violar o dever de informação clara (art. 6º, III). As cinco telas para cancelar formam um roach motel, e a '
    'mensagem "Tem certeza de que quer desistir de aprender?" é confirmshaming: dificultar o cancelamento é prática '
    'abusiva (art. 39), e o consumidor ainda tem o direito de arrependimento em 7 dias (art. 49). A caixa já marcada para '
    'ofertas de parceiros não é consentimento válido, pois a LGPD exige manifestação inequívoca e para finalidade '
    'determinada (arts. 5º, XII, e 8º, § 4º). No redesenho, o aplicativo deve informar com destaque, antes de pedir o '
    'cartão, o preço e a data da cobrança, avisar o usuário antes do fim do teste, oferecer um botão de cancelamento '
    'simples e visível, que funcione em poucos passos, sem mensagens que constrangem, e deixar a caixa de ofertas '
    'desmarcada, separada por finalidade e fácil de revogar.',
)


if __name__ == '__main__':
    banco.gravar()
