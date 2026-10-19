"""
Questões médias e difíceis do capítulo 11 (Interação Humano-Computador) de Engenharia de Software
e da Usabilidade: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas
com um único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/engsoft_cap11_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap11-o* e
engsoft-cap11-d*; as que já existiam (engsoft-cap11-m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import Banco, p

banco = Banco('engsoft-cap11')


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Segundo a taxonomia de erros de Reason, os erros 1 e 2 são, respectivamente,',
    'um deslize, prevenido com distinção visual clara, e um engano, prevenido com educação e feedback.',
    [
        'um engano, prevenido com distinção visual clara, e um deslize, prevenido com educação e feedback.',
        'dois deslizes, pois nos dois casos o usuário clicou no lugar errado.',
        'dois enganos, pois nos dois casos o usuário tinha um modelo mental incorreto do sistema.',
        'um deslize, prevenido com educação e feedback, e um engano, prevenido com distinção visual clara.',
    ],
    'No erro 1, a intenção estava certa (editar), mas a ação saiu errada por falha de atenção, pois os ícones são quase '
    'iguais: é um deslize, prevenido com distinção visual clara. No erro 2, a própria intenção estava equivocada: o '
    'usuário acreditava que "Salvar rascunho" enviava a mensagem, um modelo mental incorreto. É um engano, prevenido '
    'com educação e feedback, como uma mensagem "Rascunho salvo, ainda não enviado".',
    contexto=[p('Em um sistema de e-mails corporativo, foram registrados dois erros: '
                '(1) um usuário queria editar uma mensagem, mas clicou em "Excluir", cujo ícone é quase igual ao de '
                '"Editar" e fica logo ao lado; '
                '(2) outro usuário clicou em "Salvar rascunho" acreditando que, com isso, a mensagem seria enviada ao '
                'cliente, e só descobriu dias depois que ela nunca saiu.')],
)

banco.afirmativas(
    'medio',
    [
        ('A busca, que responde em 0,05 segundo, é percebida como instantânea pelo usuário.', True),
        ('O filtro, que responde em 0,6 segundo, também é percebido como instantâneo.', False),
        ('O relatório, que leva 6 segundos para ser gerado, precisa de um indicador de carregamento.', True),
    ],
    'Pela regra dos três tempos do princípio de feedback imediato: menos de 0,1 segundo é percebido como instantâneo; '
    'menos de 1 segundo mantém o fluxo natural; e até 10 segundos é preciso um indicador de carregamento. I é '
    'verdadeira (0,05 s). II é falsa: 0,6 s não é instantâneo, mas ainda mantém o fluxo natural do usuário. III é '
    'verdadeira: com 6 segundos, sem indicador, o usuário não sabe se o sistema está trabalhando.',
    contexto=[p('Em testes de desempenho de um sistema de vendas, a equipe mediu três tempos de resposta: a busca de '
                'produtos responde em 0,05 segundo; o filtro por categoria, em 0,6 segundo; e a geração do relatório '
                'mensal, em 6 segundos.')],
)

banco.multipla(
    'medio',
    'A dificuldade dos usuários e a forma mais adequada de resolvê-la são:',
    'o Abismo da Execução, pois o usuário não descobre como realizar a ação; a solução é deixar a opção de legendas '
    'visível na tela de reprodução.',
    [
        'o Abismo da Avaliação, pois o sistema não comunica o resultado da ação; a solução é exibir uma mensagem de '
        'confirmação após ativar as legendas.',
        'o Abismo da Execução, pois o usuário não sabe o que aconteceu; a solução é incluir uma animação depois que as '
        'legendas forem ativadas.',
        'um engano do usuário, pois ele tem um modelo mental incorreto; a solução é oferecer um tutorial em vídeo sobre '
        'o aplicativo.',
        'um problema de acessibilidade que só afeta pessoas surdas; a solução é criar um aplicativo separado para esse '
        'público.',
    ],
    'O usuário sabe o que quer (ativar legendas), mas não consegue descobrir como fazer isso no sistema: é o Abismo '
    'da Execução, a distância entre "o que eu quero fazer" e "o que o sistema me permite fazer". O Abismo da '
    'Avaliação apareceria depois da ação, se o sistema não mostrasse o resultado. Pelo princípio da visibilidade, '
    'funções importantes nunca devem ficar escondidas em menus profundos.',
    contexto=[p('Em um aplicativo de filmes para TV, a opção de ativar legendas fica em Configurações > Avançado > '
                'Acessibilidade > Mídia > Legendas. Muitos usuários desistem de procurar e acabam assistindo sem '
                'legendas, embora a função exista.')],
)

banco.assercao(
    'medio',
    'Exigir que o usuário decore o código de 12 dígitos para digitá-lo na tela seguinte tende a provocar erros.',
    'A memória de trabalho humana é muito limitada: segundo George Miller, mantemos em mente apenas cerca de 7 ± 2 '
    'itens ao mesmo tempo.',
    0,
    'As duas são verdadeiras, e a II explica a I. Doze dígitos ultrapassam a capacidade da memória de trabalho, que '
    'guarda cerca de 7 ± 2 itens. Por isso o usuário esquece ou troca dígitos. O design deveria reduzir a carga '
    'cognitiva, por exemplo levando o código para a tela seguinte automaticamente ou oferecendo um botão para copiá-lo.',
    contexto=[p('Ao gerar um boleto, um sistema mostra um código de 12 dígitos e pede que o usuário clique em '
                '"Continuar". Na tela seguinte, o código não aparece mais, e o usuário precisa digitá-lo de memória '
                'para confirmar o pagamento.')],
)

banco.multipla(
    'medio',
    'Os paradigmas de interação mais adequados às situações 1, 2, 3 e 4 são, respectivamente,',
    'CLI, voz (VUI), realidade virtual (VR) e touchscreen.',
    [
        'GUI, touchscreen, realidade aumentada (AR) e voz (VUI).',
        'CLI, touchscreen, realidade virtual (VR) e voz (VUI).',
        'voz (VUI), CLI, touchscreen e realidade virtual (VR).',
        'GUI, voz (VUI), CLI e touchscreen.',
    ],
    'Comandos textuais (CLI) são muito eficientes para especialistas e dominantes em automação (1). A voz permite usar '
    'o sistema com as mãos livres, como na cozinha (2). A realidade virtual oferece imersão completa, útil para simular '
    'situações (3). O toque é direto e intuitivo para o público em geral, como em um quiosque (4). A AR sobrepõe '
    'informação ao mundo real, sem imersão completa.',
    contexto=[p('Uma empresa de tecnologia tem quatro projetos: '
                '(1) uma ferramenta para a equipe de infraestrutura automatizar a configuração de centenas de servidores; '
                '(2) um assistente de receitas para quem está cozinhando, com as mãos sujas de massa; '
                '(3) um treinamento de pilotos que simula, de forma imersiva, situações de emergência na cabine; '
                '(4) um quiosque de autoatendimento para o público geral fazer pedidos em uma lanchonete.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.afirmativas(
    'dificil',
    [
        ('A dificuldade com o fogão é um problema de mapeamento, a relação natural entre os controles e os seus efeitos.',
         True),
        ('O puxador na porta que precisa ser empurrada é um signifier enganoso, pois sinaliza uma ação diferente da que '
         'a porta permite.', True),
        ('Bloquear as datas passadas no calendário é um uso de restrição para prevenir erros.', True),
        ('O feedback é o sinal perceptível que torna a affordance visível antes de o usuário agir.', False),
    ],
    'I é verdadeira: com as bocas em quadrado e os botões em linha, não há relação natural entre cada botão e a boca '
    'que ele acende. II é verdadeira: o puxador "diz" puxe, mas a porta só abre empurrando. III é verdadeira: as '
    'restrições limitam as ações possíveis e, assim, evitam o erro. IV é falsa: o sinal que torna a affordance visível '
    'é o signifier; o feedback é a resposta do sistema depois da ação, confirmando o resultado.',
    contexto=[p('Em uma aula sobre os conceitos de Norman, a professora mostrou três exemplos: '
                '(1) um fogão com as quatro bocas dispostas em quadrado e os quatro botões em uma única linha, em que as '
                'pessoas vivem acendendo a boca errada; '
                '(2) uma porta de vidro com puxadores dos dois lados, mas que só abre quando empurrada; '
                '(3) um calendário de agendamento que não deixa escolher datas que já passaram.')],
)

banco.assercao(
    'dificil',
    'O curb-cut effect mostra que projetar para as limitações de alguns usuários pode beneficiar todos os usuários.',
    'A Lei Brasileira de Inclusão (LBI) estabelece a acessibilidade digital como direito da pessoa com deficiência.',
    1,
    'As duas são verdadeiras, mas a II não explica a I. A I descreve o Design Inclusivo: as legendas, criadas para '
    'pessoas surdas, hoje são usadas por qualquer pessoa em ambientes barulhentos. A II também é verdadeira, mas trata '
    'de uma obrigação legal. O benefício para todos não vem da lei; vem do fato de que soluções para limitações '
    'resolvem também situações vividas por qualquer pessoa.',
    contexto=[p('Depois de incluir legendas em todos os seus vídeos para atender aos clientes surdos, uma empresa '
                'descobriu que a maior parte das pessoas que ativam as legendas não tem deficiência auditiva: são '
                'usuários que assistem aos vídeos no ônibus, no trabalho ou em lugares barulhentos.')],
)

banco.multipla(
    'dificil',
    'Os problemas 1, 2, 3 e 4 violam, respectivamente, os princípios da WCAG',
    'Perceptível, Operável, Compreensível e Robusto.',
    [
        'Perceptível, Compreensível, Operável e Robusto.',
        'Robusto, Operável, Compreensível e Perceptível.',
        'Perceptível, Operável, Robusto e Compreensível.',
        'Compreensível, Operável, Perceptível e Robusto.',
    ],
    'Um gráfico sem texto alternativo não pode ser percebido por quem usa leitor de tela: Perceptível (1). Um menu que '
    'só abre com o mouse não pode ser usado pelo teclado: Operável (2). Uma página que muda sozinha, sem aviso, tem '
    'comportamento imprevisível: Compreensível (3). Botões sem HTML semântico não são reconhecidos pelos leitores de '
    'tela: Robusto (4). Juntos, os quatro formam o acrônimo POUR.',
    contexto=[p('Uma auditoria de acessibilidade em um portal de notícias encontrou quatro problemas: '
                '(1) os gráficos das reportagens são imagens sem texto alternativo; '
                '(2) o menu principal só se abre quando o mouse passa por cima dele, sem opção pelo teclado; '
                '(3) ao escolher uma cidade na lista, a página muda sozinha para outra seção, sem nenhum aviso; '
                '(4) os botões foram feitos com elementos genéricos, sem HTML semântico, e os leitores de tela não os '
                'reconhecem como botões.')],
)

banco.multipla(
    'dificil',
    'Os problemas 1, 2, 3 e 4 estão ligados, respectivamente, às dimensões do design de interação de Crampton Smith',
    'Palavras, Representações Visuais, Espaço Físico e Tempo.',
    [
        'Representações Visuais, Palavras, Tempo e Espaço Físico.',
        'Palavras, Representações Visuais, Tempo e Comportamento.',
        'Comportamento, Representações Visuais, Espaço Físico e Tempo.',
        'Palavras, Espaço Físico, Representações Visuais e Tempo.',
    ],
    'A mensagem "Exception 500" usa a linguagem do desenvolvedor, e não a do usuário: Palavras (1). Ícones que ninguém '
    'reconhece são Representações Visuais (2). Um aplicativo que exige as duas mãos para quem está em pé no metrô '
    'ignora o contexto de uso: Espaço Físico (3). A falta de animação ou transição que mostre que a compra está em '
    'andamento é a dimensão Tempo (4). O Comportamento é a síntese que surge da combinação das quatro anteriores.',
    contexto=[p('Os usuários do aplicativo de recarga do cartão de metrô de uma cidade relataram quatro problemas: '
                '(1) quando o pagamento falha, aparece a mensagem "Exception 500"; '
                '(2) os ícones do menu são abstratos, e ninguém sabe o que cada um faz; '
                '(3) para recarregar, é preciso usar as duas mãos e tocar em botões minúsculos, o que é difícil para '
                'quem está em pé no vagão, segurando a barra; '
                '(4) depois de tocar em "Comprar", nada se mexe na tela por alguns segundos, sem nenhuma animação ou '
                'transição.')],
)

banco.multipla(
    'dificil',
    'Sobre a acessibilidade digital e a legislação brasileira, assinale a alternativa INCORRETA.',
    'O e-MAG é um guia internacional, criado pelo W3C, que substitui as WCAG nos sites brasileiros.',
    [
        'A Lei Brasileira de Inclusão (Lei 13.146/2015) estabelece a acessibilidade digital como direito da pessoa com '
        'deficiência, e sites e aplicativos inacessíveis configuram discriminação.',
        'O Decreto 5.296/2004 torna obrigatória a acessibilidade nos sítios do governo federal.',
        'O nível A da WCAG é o mínimo, obrigatório em sítios de governo; o AA é o padrão de mercado; e o AAA, o máximo.',
        'Um contraste mínimo de 4,5:1 entre texto e fundo faz parte do princípio Perceptível da WCAG.',
    ],
    'A afirmação incorreta é a do e-MAG: ele é o Modelo de Acessibilidade em Governo Eletrônico, um guia brasileiro, '
    'e não do W3C, e é baseado nas WCAG, sem substituí-las. As demais estão corretas: a LBI trata a acessibilidade '
    'digital como direito, o Decreto 5.296/2004 obriga os sítios do governo federal, os níveis vão de A a AAA, e o '
    'contraste de 4,5:1 é um requisito do princípio Perceptível.',
    contexto=[p('Uma empresa foi contratada para refazer o portal de um ministério e precisa garantir que ele seja '
                'acessível. Na reunião inicial, a equipe revisou as normas e as diretrizes que o projeto deve seguir.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"Two of the most important characteristics of good design are discoverability and understanding."',
        'traducao': '(Tradução livre: "Duas das características mais importantes de um bom design são a facilidade de '
                    'descoberta e a compreensão.")',
        'fonte': 'NORMAN, D. The Design of Everyday Things. Edição revista e ampliada. New York: Basic Books, 2013.',
    },
    [
        'Um hospital instalou totens de autoatendimento para que os pacientes confirmem a chegada às consultas. Muitos '
        'pacientes idosos ficam parados diante da tela inicial sem saber onde tocar, pois os botões são retângulos '
        'cinza, todos iguais e sem texto. Quando conseguem tocar em "Confirmar", a tela não muda por vários segundos, e '
        'muitos tocam de novo, gerando confirmações duplicadas. Ao lado de "Confirmar" fica o botão "Cancelar consulta", '
        'do mesmo tamanho e da mesma cor, e há pacientes que cancelam a consulta sem querer.',
    ],
    'Com base no texto de Norman e no caso apresentado, analise os problemas do totem e explique como a interface '
    'deveria ser redesenhada.',
    'Os problemas aparecem nos dois abismos de Norman. No Abismo da Execução, falta facilidade de descoberta: botões '
    'cinza, iguais e sem texto não têm signifiers que mostrem o que cada um faz. Eles deveriam ter rótulos claros, na '
    'linguagem do paciente, cores e tamanhos diferentes, e as funções principais deveriam estar visíveis logo na tela '
    'inicial. No Abismo da Avaliação, falta compreensão do resultado: sem feedback, o paciente não sabe se a '
    'confirmação funcionou e toca de novo. Pela regra dos três tempos, uma espera de vários segundos exige um '
    'indicador de carregamento, e ao final deve aparecer uma confirmação clara, como "Chegada confirmada". O '
    'cancelamento sem querer é um deslize: a intenção era confirmar, mas o botão errado foi tocado porque os dois são '
    'iguais e vizinhos. Ele se previne com distinção visual clara, afastando os botões, e com reversibilidade, '
    'pedindo confirmação ou permitindo desfazer. Botões grandes, com bom contraste (4,5:1), também ajudam os idosos. '
    'O redesenho deveria ser avaliado com um percurso cognitivo, pela perspectiva de um usuário iniciante, e com '
    'testes com pacientes reais.',
)

banco.discursiva(
    'dificil',
    {
        'citacao': '"É obrigatória a acessibilidade nos sítios da internet mantidos por empresas com sede ou '
                   'representação comercial no País ou por órgãos de governo, para uso da pessoa com deficiência, '
                   'garantindo-lhes acesso às informações disponíveis, conforme as melhores práticas e diretrizes de '
                   'acessibilidade adotadas internacionalmente."',
        'fonte': 'BRASIL. Lei nº 13.146, de 6 de julho de 2015. Lei Brasileira de Inclusão da Pessoa com Deficiência '
                 '(Estatuto da Pessoa com Deficiência). Art. 63.',
    },
    [
        'Uma loja virtual brasileira recebeu reclamações de clientes cegos, que não conseguem concluir compras com '
        'leitores de tela: as fotos dos produtos não têm texto alternativo, o menu de categorias só funciona com o '
        'mouse, e a verificação de segurança no fim da compra é uma imagem com letras distorcidas, sem outra opção.',
        'O diretor da loja respondeu que "acessibilidade é obrigação de site do governo, e não de empresa privada".',
    ],
    'Com base no texto da lei e no caso apresentado, avalie a posição do diretor e explique o que a loja deveria fazer '
    'para tornar o site acessível.',
    'O diretor está errado. Pelo artigo 63 da LBI, a acessibilidade é obrigatória também nos sites de empresas com sede '
    'ou representação no País, e não só nos do governo. A lei trata a acessibilidade digital como direito da pessoa com '
    'deficiência, e um site inacessível configura discriminação. As "diretrizes adotadas internacionalmente" citadas '
    'pela lei são as WCAG, e o nível AA é o padrão de mercado. Os problemas da loja ferem dois dos princípios POUR: '
    'fotos sem texto alternativo e a verificação só por imagem ferem o Perceptível, pois o cliente cego não tem como '
    'perceber o conteúdo (a verificação precisa de uma alternativa, como áudio); o menu que só funciona com o mouse '
    'fere o Operável, pois toda funcionalidade deve ser acessível pelo teclado. A loja deveria também usar HTML '
    'semântico (Robusto), garantir comportamento previsível (Compreensível) e testar o site com leitores de tela e com '
    'usuários com deficiência. Além de cumprir a lei, isso amplia o público: pelo efeito rampa, recursos acessíveis '
    'acabam ajudando todos os clientes.',
)


if __name__ == '__main__':
    banco.gravar()
