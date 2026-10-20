"""
Questões médias e difíceis do capítulo 2 (Propriedade Intelectual) de Legislação em Negócios Digitais:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/legislacao_cap2_objetivas.py

Grava em src/data/questoes/legislacao.json, trocando só as questões legislacao-cap2-o* e
legislacao-cap2-d*; as que já existiam (q* e f*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import LEGISLACAO, Banco, p

banco = Banco('legislacao-cap2', LEGISLACAO)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'A partir de quando as obras desse escritor entram em domínio público?',
    'Em 1º de janeiro de 2025.',
    ['Em 10 de março de 2024.', 'Em 1º de janeiro de 2024.', 'Em 10 de março de 2034.', 'Em 1º de janeiro de 2005.'],
    'Pelo art. 41 da Lei nº 9.610/1998, os direitos patrimoniais duram por toda a vida do autor e por 70 anos contados '
    'de 1º de janeiro do ano seguinte ao da sua morte. Como ele morreu em 1954, a contagem começa em 1º de janeiro de 1955 '
    'e termina em 31 de dezembro de 2024: as obras entram em domínio público em 1º de janeiro de 2025. Contar da data da '
    'morte ou usar 50 anos, prazo do software, leva às respostas erradas.',
    contexto=[p('Um escritor brasileiro morreu em 10 de março de 1954, deixando romances que continuam sendo vendidos por '
                'uma editora. Uma plataforma de livros digitais quer publicá-los gratuitamente, sem pedir autorização aos '
                'herdeiros.')],
)

banco.afirmativas(
    'medio',
    [
        ('Ideias, métodos e conceitos não são protegidos; a proteção recai sobre a forma de expressão.', True),
        ('Textos de leis, decretos e decisões judiciais não são objeto de proteção pelo direito autoral.', True),
        ('Um texto publicado em blog sem o símbolo © não é protegido pelo direito autoral.', False),
        ('O aproveitamento industrial ou comercial das ideias contidas em uma obra é protegido pela LDA.', False),
    ],
    'I e II estão no art. 8º da Lei nº 9.610/1998, que exclui da proteção as ideias, os métodos e os conceitos (inciso I) '
    'e os textos de leis, decretos e decisões judiciais (inciso IV). III é falsa: a proteção nasce com a criação, sem '
    'registro nem símbolo. IV é falsa: o aproveitamento industrial ou comercial das ideias contidas nas obras também '
    'está fora da proteção autoral (inciso VII).',
    contexto=[p('Uma equipe de conteúdo de uma startup quer saber o que pode usar livremente ao produzir artigos e cursos '
                'para o seu blog.')],
)

banco.assercao(
    'medio',
    'O registro de um programa de computador no INPI é facultativo.',
    'A proteção dos direitos sobre o programa de computador independe de registro.',
    0,
    'As duas são verdadeiras, e a II justifica a I. Pela Lei nº 9.609/1998 (art. 2º, § 3º), a proteção independe de '
    'registro, como no direito autoral em geral. Por isso o registro no INPI é facultativo: ele não cria o direito, mas '
    'serve como prova de autoria e da data da criação em caso de disputa.',
    contexto=[p('O fundador de uma startup acredita que, sem registrar o código no INPI, qualquer concorrente pode copiar '
                'o seu aplicativo sem consequências.')],
)

banco.multipla(
    'medio',
    'As licenças mais adequadas às necessidades 1, 2, 3 e 4 são, respectivamente,',
    'MIT, LGPL, GPL e CC0.',
    ['GPL, LGPL, MIT e CC0.', 'MIT, GPL, LGPL e CC0.', 'LGPL, MIT, GPL e CC BY.', 'MIT, LGPL, CC BY-SA e GPL.'],
    'A MIT é permissiva: permite usar o código em produtos fechados, bastando manter o aviso de copyright (1). A LGPL é '
    'copyleft fraco: permite usar a biblioteca em software proprietário, mas as mudanças na própria biblioteca devem ser '
    'abertas (2). A GPL é copyleft forte: obras derivadas distribuídas devem seguir a mesma licença (3). A CC0 é a '
    'renúncia a todos os direitos, equivalente ao domínio público (4).',
    contexto=[p('Uma desenvolvedora vai publicar quatro projetos e quer escolher a licença de cada um: '
                '(1) uma biblioteca que qualquer empresa possa usar até em produtos fechados, desde que mantenha o aviso '
                'de copyright; '
                '(2) uma biblioteca que possa ser usada em produtos fechados, mas cujas modificações nela mesma sejam '
                'abertas; '
                '(3) um programa cujas versões derivadas distribuídas tenham de continuar abertas, sob a mesma licença; '
                '(4) um conjunto de ícones que ela quer liberar sem reservar nenhum direito.')],
)

banco.multipla(
    'medio',
    'As condutas 1, 2, 3 e 4 correspondem, respectivamente, a',
    'typosquatting, username squatting, keyword advertising e cybersquatting.',
    [
        'cybersquatting, username squatting, keyword advertising e typosquatting.',
        'typosquatting, cybersquatting, metatags e username squatting.',
        'typosquatting, username squatting, cybersquatting e keyword advertising.',
        'username squatting, typosquatting, keyword advertising e cybersquatting.',
    ],
    'Registrar domínios com erros de digitação de uma marca famosa é typosquatting (1). Criar perfis em redes sociais com '
    'o nome de uma marca alheia é username squatting (2). Comprar como palavra-chave de anúncio a marca de um concorrente '
    'é keyword advertising, cujo tratamento varia conforme o país e a plataforma (3). Registrar um domínio com a marca de '
    'outra empresa para vendê-lo a ela é cybersquatting (4).',
    contexto=[p('Uma rede de lojas chamada "Casa Prática" identificou quatro condutas de terceiros: '
                '(1) o registro do domínio "casapratka.com.br", com uma letra trocada; '
                '(2) a criação do perfil @casapratica_oficial em uma rede social por alguém sem ligação com a rede; '
                '(3) a compra da expressão "Casa Prática" como palavra-chave de anúncios por um concorrente; '
                '(4) o registro do domínio "casapratica.com" por uma pessoa que ofereceu vendê-lo à rede por R$ 80 mil.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Em abril de 2031, sem nenhuma renovação ou prorrogação, quais direitos continuam em vigor?',
    'Somente a patente de invenção, que dura 20 anos a contar do depósito.',
    [
        'A patente de invenção e o modelo de utilidade, que duram 20 anos a contar do depósito.',
        'A patente de invenção e a marca, pois a marca vale enquanto a empresa continuar usando o nome.',
        'Somente a marca, pois as patentes duram 10 anos, e o registro de marca não tem prazo.',
        'Nenhum, pois todos os direitos de propriedade industrial duram no máximo 15 anos.',
    ],
    'A patente de invenção dura 20 anos do depósito (art. 40 da Lei nº 9.279/1996): depositada em 2015, vai até 2035. O '
    'modelo de utilidade dura 15 anos do depósito: terminou em 2030. O registro de marca vale 10 anos a contar da '
    'concessão e pode ser prorrogado por períodos iguais (art. 133): concedido em 2019, venceu em 2029 sem renovação. O '
    'uso da marca não renova o registro.',
    contexto=[p('Uma empresa de tecnologia depositou no INPI, em março de 2015, um pedido de patente de invenção e um '
                'pedido de modelo de utilidade, ambos concedidos depois. O registro da sua marca foi concedido em março de '
                '2019. Desde então, a empresa não fez nenhum pedido de prorrogação.')],
)

banco.multipla(
    'dificil',
    'Considerando a Lei nº 9.609/1998, o desenvolvedor pode impedir as alterações com base no direito moral de '
    'integridade?',
    'Em regra, não: no software, a lei só preserva a paternidade e a oposição a alterações que deformem o programa ou '
    'atinjam a honra.',
    [
        'Sim, pois os direitos morais da LDA valem integralmente para o software, inclusive o de impedir qualquer alteração.',
        'Sim, pois a cessão dos direitos patrimoniais não inclui o direito de alterar o código, que fica sempre com o autor.',
        'Não, pois quem cede os direitos patrimoniais de um software também perde o direito de ser reconhecido como autor.',
        'Não, pois o software não é obra intelectual, e por isso não tem direitos morais nem direitos patrimoniais.',
    ],
    'O art. 2º, § 1º, da Lei nº 9.609/1998 afasta do software os direitos morais da LDA, ressalvados o direito de '
    'reivindicar a paternidade do programa e o de se opor a alterações não autorizadas que impliquem deformação, '
    'mutilação ou outra modificação que prejudique a honra ou a reputação do autor. Atualizar o código para uma nova '
    'versão, depois de ceder os direitos patrimoniais, em regra não viola esses direitos. O software é obra intelectual '
    'e continua tendo direitos patrimoniais, que foram cedidos.',
    contexto=[p('Um desenvolvedor criou um sistema de gestão e cedeu à empresa contratante todos os direitos '
                'patrimoniais sobre ele. Dois anos depois, a empresa reescreveu partes do código para lançar uma nova '
                'versão, mantendo o nome do desenvolvedor nos créditos. Ele quer impedir as mudanças, invocando o direito '
                'de assegurar a integridade da obra (art. 24, IV, da LDA).')],
)

banco.afirmativas(
    'dificil',
    [
        ('Vender cópias piratas de filmes com intuito de lucro é crime com pena de reclusão de 2 a 4 anos e multa.', True),
        ('A cópia de uma obra em um só exemplar, para uso privado do copista e sem intuito de lucro, não é esse crime.',
         True),
        ('Violar direito autoral sem intuito de lucro nunca é crime, gerando apenas indenização na esfera civil.', False),
        ('Sem saber quantos exemplares foram vendidos, a indenização considera o valor de 3.000 exemplares.', True),
    ],
    'I e II estão no art. 184 do Código Penal: a reprodução com intuito de lucro tem pena de reclusão de 2 a 4 anos e '
    'multa (§ 1º), e o § 4º exclui do crime a cópia em um só exemplar para uso privado do copista, sem intuito de lucro '
    'direto ou indireto. III é falsa: o caput pune a violação simples com detenção de 3 meses a 1 ano, ou multa. IV é '
    'verdadeira: é o art. 103, parágrafo único, da Lei nº 9.610/1998.',
    contexto=[p('Uma operação policial encontrou, em uma feira, uma banca que vendia cópias piratas de filmes. Os '
                'investigadores discutem as consequências penais e civis da violação de direitos autorais.')],
)

banco.multipla(
    'dificil',
    'Qual é a análise mais adequada sobre a proteção autoral dessas imagens?',
    'Autor é a pessoa física criadora: o que a IA gerou sozinha tende a ficar sem proteção, mas a edição humana pode ser '
    'protegida.',
    [
        'As imagens são protegidas integralmente, pois quem escreve o prompt é sempre o autor de tudo o que a IA vier a gerar.',
        'As imagens pertencem à empresa dona da IA, que é a autora das obras geradas pelo seu sistema, por força da LDA.',
        'As imagens são protegidas automaticamente por 50 anos, como os programas de computador, por serem geradas por '
        'software.',
        'As imagens caem em domínio público só depois de 70 anos, contados da data em que foram geradas pela IA.',
    ],
    'O art. 11 da Lei nº 9.610/1998 define o autor como a pessoa física criadora de obra literária, artística ou '
    'científica. A lei brasileira ainda não trata da IA de forma específica, e o entendimento predominante é de que o '
    'material gerado sem contribuição criativa humana não se qualifica para proteção; nos EUA, o Copyright Office tem '
    'negado o registro dessas obras. Já a seleção, a organização e a edição feitas pela artista podem ser protegidas.',
    contexto=[p('Uma ilustradora usa uma ferramenta de inteligência artificial generativa para criar imagens apenas a '
                'partir de prompts de texto, sem desenhar nem editar o resultado. Depois, monta com algumas dessas imagens '
                'um livro, escolhendo, ordenando e editando o conjunto, e quer saber se as imagens estão protegidas.')],
)

banco.multipla(
    'dificil',
    'Qual é o motivo mais provável do indeferimento do pedido de patente?',
    'Falta de novidade: a divulgação pelo próprio inventor só é perdoada se feita até 12 meses antes do depósito.',
    [
        'Falta de atividade inventiva, pois toda invenção apresentada em congresso passa a ser óbvia para os técnicos.',
        'Falta de aplicação industrial, pois invenções apresentadas em eventos científicos não podem ser fabricadas.',
        'Patente de software, pois o art. 10 da Lei nº 9.279/1996 proíbe proteger qualquer invenção que use sensores.',
        'Nenhum, pois a divulgação feita pelo próprio inventor nunca prejudica a novidade do pedido de patente.',
    ],
    'A invenção precisa ser nova, isto é, não pode estar no estado da técnica (art. 11 da Lei nº 9.279/1996). O art. 12 '
    'cria o período de graça: a divulgação feita pelo próprio inventor nos 12 meses anteriores ao depósito não tira a '
    'novidade. Como a apresentação ocorreu 2 anos antes, a invenção já fazia parte do estado da técnica. A lei veda o '
    'programa de computador em si, e não as invenções com efeito técnico que usam sensores.',
    contexto=[p('Uma pesquisadora apresentou, em um congresso científico aberto ao público, um novo sensor para detectar '
                'vazamentos de gás. Dois anos depois, depositou no INPI um pedido de patente para esse sensor, que foi '
                'indeferido.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Três amigos vão lançar um aplicativo de entregas chamado "LevaJá". Um deles escreveu o código antes de a empresa '
        'existir; um freelancer está criando o design das telas; e a equipe desenvolveu um algoritmo de roteirização que '
        'reduz o consumo de combustível da frota. O aplicativo usa várias bibliotecas de código aberto, e a marca ainda não '
        'foi registrada.',
    ],
    'Proponha uma estratégia de proteção da propriedade intelectual para essa startup.',
    'A marca "LevaJá" deve ser depositada no INPI antes do lançamento, nas classes ligadas ao serviço, porque o Brasil '
    'adota o sistema first to file; também convém registrar o domínio e os perfis nas redes sociais. O código é protegido '
    'pelo direito autoral de software, sem necessidade de registro (Lei nº 9.609/1998), mas o registro facultativo no INPI '
    'ajuda a provar a autoria e a data. Como o sócio escreveu o código antes de a empresa existir, ele precisa ceder os '
    'direitos à startup por escrito; o mesmo vale para o freelancer do design, com contrato que preveja a cessão dos '
    'direitos sobre as telas, e para os futuros empregados e prestadores, com cláusulas de PI. O algoritmo de roteirização '
    'pode ser protegido como segredo industrial, com controle de acesso e acordos de confidencialidade (NDAs), ou, se '
    'tiver efeito técnico e for novo, por um pedido de patente de invenção implementada por software, que não pode ser '
    'divulgada antes do depósito. A startup deve ter uma política de código aberto, conferindo as licenças: as '
    'permissivas, como MIT, exigem só manter os avisos, enquanto a GPL pode obrigar a abrir o código se o produto for '
    'distribuído. Por fim, deve verificar se não viola marcas e patentes de terceiros, o que costuma ser checado na due '
    'diligence de investidores.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma agência de publicidade passou a usar ferramentas de inteligência artificial generativa para criar imagens, '
        'textos e jingles para campanhas dos clientes. Em uma das campanhas, a imagem gerada ficou muito parecida com a '
        'obra de um ilustrador conhecido, e o jingle lembrava uma música famosa. A agência entrega o material aos clientes '
        'dizendo que eles "passam a ser donos de tudo".',
    ],
    'Analise os riscos de propriedade intelectual dessa prática e proponha cuidados que a agência deveria adotar.',
    'Há riscos em várias frentes. Primeiro, a autoria: pela LDA, autor é a pessoa física criadora (art. 11), e o material '
    'gerado só pela IA, sem contribuição criativa humana, tende a não ter proteção autoral, o que torna frágil a promessa '
    'de que o cliente "passa a ser dono de tudo"; o que pode ser protegido é a contribuição humana de seleção, edição e '
    'composição. Segundo, a violação de direitos de terceiros: uma imagem muito parecida com a obra de um ilustrador e um '
    'jingle que reproduz trechos de uma música podem ser considerados reprodução ou obra derivada não autorizada, com '
    'responsabilidade civil (indenização, remoção) e até penal (art. 184 do CP), além do uso indevido de marcas que '
    'apareçam no material. Terceiro, o treino dos modelos com obras protegidas é tema em disputa judicial, e os termos de '
    'uso de cada ferramenta definem o que pode ser feito com o resultado. A agência deveria revisar os termos de uso das '
    'ferramentas, evitar prompts que peçam o estilo de artistas ou obras específicas, checar semelhanças antes de entregar, '
    'ter intervenção criativa humana documentada, licenciar trilhas e imagens quando necessário e ajustar os contratos com '
    'os clientes, explicando o uso de IA e limitando garantias sobre a titularidade.',
)


if __name__ == '__main__':
    banco.gravar()
