"""
Questões médias e difíceis do capítulo 9 (Usabilidade e Experiência do Usuário) de Engenharia de
Software e da Usabilidade: 10 objetivas no estilo de concursos públicos e exames nacionais e
2 discursivas com um único comando. As funções comuns ficam em engsoft_questoes.py.
Uso (dentro de site/):

    python ferramentas/engsoft_cap9_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap9-o* e
engsoft-cap9-d*; as que já existiam (engsoft-cap9-m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import Banco, p

banco = Banco('engsoft-cap9')


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Os recursos 1, 2, 3 e 4 aplicam, respectivamente, os princípios de Gestalt de',
    'proximidade, similaridade, fechamento e figura e fundo.',
    [
        'similaridade, proximidade, continuidade e figura e fundo.',
        'proximidade, similaridade, figura e fundo e fechamento.',
        'continuidade, similaridade, fechamento e proximidade.',
        'proximidade, continuidade, fechamento e similaridade.',
    ],
    'Separar os grupos de campos só pelo espaço faz o usuário perceber como relacionados os que estão próximos: '
    'proximidade (1). Dar a mesma aparência a todos os links indica que pertencem ao mesmo grupo: similaridade (2). '
    'O cérebro completa o círculo interrompido: fechamento (3). Escurecer o fundo destaca a janela como o elemento '
    'principal: figura e fundo (4). A continuidade trata do olho seguindo linhas e curvas.',
    contexto=[p('No redesenho de um site de compras, a equipe: '
                '(1) separou os campos de "Dados pessoais" e de "Endereço" apenas com um espaço maior entre os dois grupos, '
                'sem linhas nem caixas; '
                '(2) deixou todos os links do site azuis e sublinhados; '
                '(3) criou um logotipo em forma de círculo com uma pequena abertura, que todos continuam vendo como círculo; '
                '(4) passou a escurecer o restante da tela quando abre a janela de confirmação da compra.')],
)

banco.afirmativas(
    'medio',
    [
        ('A situação 1 viola principalmente a heurística de Consistência e Padrões.', False),
        ('Na situação 2, trocar o campo de texto por um seletor de datas atende à heurística de Prevenção de Erros, pois '
         'um design que evita o problema é melhor do que uma boa mensagem de erro.', True),
        ('A mensagem "Erro 0x8F" viola a heurística de Reconhecer, Diagnosticar e Recuperar Erros, pois não está em '
         'linguagem simples nem sugere uma solução.', True),
    ],
    'I é falsa: a tela parada, sem indicar que o envio está acontecendo, viola a Visibilidade do Status do Sistema, '
    'que pede feedback em tempo razoável, como uma barra de progresso. II é verdadeira: com um seletor, a data errada '
    'nem chega a ser digitada. III é verdadeira: a mensagem só faz sentido para a equipe técnica; ela deveria dizer, em '
    'linguagem simples, o que houve e como corrigir.',
    contexto=[p('Em um sistema de envio de documentos: '
                '(1) ao enviar um arquivo grande, a tela fica parada por dois minutos, sem nenhuma indicação do que está '
                'acontecendo; '
                '(2) o campo "Data de emissão" aceita qualquer texto, e só ao final, depois de o usuário clicar em '
                '"Enviar", aparece a mensagem "Erro 0x8F".')],
)

banco.assercao(
    'medio',
    'O sistema tem um problema de usabilidade, mesmo que todos os funcionários consigam registrar o ponto.',
    'Pela ISO 9241-210, a usabilidade envolve eficácia, eficiência e satisfação; alcançar o objetivo, que é a '
    'eficácia, não é suficiente.',
    0,
    'As duas são verdadeiras, e a II explica a I. Todos conseguem registrar o ponto, então há eficácia. Mas gastar '
    'quatro minutos para uma tarefa tão simples mostra baixa eficiência, e as reclamações mostram baixa satisfação. '
    'Pela definição da norma, o sistema precisa atender às três dimensões no seu contexto de uso.',
    contexto=[p('Em uma fábrica, 100% dos funcionários conseguem registrar o ponto no novo sistema eletrônico. Cada '
                'registro, porém, leva cerca de quatro minutos, forma filas na troca de turno, e as reclamações sobre o '
                'sistema não param de chegar ao setor de recursos humanos.')],
)

banco.multipla(
    'medio',
    'As etapas 1 e 2 correspondem, respectivamente, às técnicas de',
    'Card Sorting, ligada ao sistema de organização, e Tree Testing, ligada ao sistema de navegação.',
    [
        'Tree Testing, ligada ao sistema de organização, e Card Sorting, ligada ao sistema de navegação.',
        'Teste A/B, ligado ao sistema de rotulação, e Eye Tracking, ligado ao sistema de busca.',
        'Avaliação Heurística, ligada ao sistema de organização, e SUS, ligado ao sistema de navegação.',
        'Persona, ligada ao sistema de rotulação, e Jornada do Usuário, ligada ao sistema de busca.',
    ],
    'No Card Sorting, os participantes agrupam cartões com os conteúdos e nomeiam os grupos, mostrando como eles '
    'organizam a informação: é a técnica do sistema de organização (1). No Tree Testing, os participantes procuram um '
    'item navegando só pela hierarquia de menus, sem o visual do site, o que avalia o sistema de navegação (2).',
    contexto=[p('A prefeitura de uma cidade vai reorganizar o menu do seu site. '
                '(1) Primeiro, pediu a moradores que agrupassem cartões com os nomes de 60 serviços, como "segunda via do '
                'IPTU" e "matrícula escolar", da forma que achassem mais lógica, e que dessem um nome a cada grupo. '
                '(2) Depois, com o novo menu montado só em texto, sem cores nem imagens, pediu a outros moradores que '
                'encontrassem serviços como "segunda via do IPTU" navegando pelos níveis do menu.')],
)

banco.multipla(
    'medio',
    'A interpretação correta dos resultados do teste é:',
    'A taxa de sucesso na tarefa foi de 75%, e o SUS de 84 pontos é considerado bom, por estar acima de 80.',
    [
        'A taxa de sucesso na tarefa foi de 6%, pois seis participantes concluíram a tarefa.',
        'A taxa de sucesso na tarefa foi de 75%, e o SUS de 84 pontos indica que 84% dos participantes ficaram '
        'satisfeitos.',
        'A taxa de sucesso na tarefa foi de 80%, e o SUS de 84 pontos é considerado ruim, por estar abaixo de 90.',
        'Com só oito participantes, nenhuma das métricas pode ser calculada, pois o teste não tem validade.',
    ],
    'A taxa de sucesso na tarefa é o percentual de participantes que a concluíram: 6 de 8, ou 75%. O SUS é um '
    'questionário de dez perguntas que gera uma pontuação de 0 a 100, e acima de 80 é considerado bom. Essa pontuação '
    'não é a porcentagem de pessoas satisfeitas. E oito participantes são suficientes: cinco já revelam cerca de 85% '
    'dos problemas de usabilidade.',
    contexto=[p('Em um teste de usabilidade do novo aplicativo de uma farmácia, oito participantes tentaram comprar um '
                'remédio com receita digital. Seis conseguiram concluir a compra. Ao final, todos responderam ao '
                'questionário SUS, e a pontuação média foi de 84.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.afirmativas(
    'dificil',
    [
        ('As atividades 1, 2, 3 e 4 correspondem, nessa ordem, às quatro fases do Design Centrado no Usuário da '
         'ISO 9241-210.', True),
        ('Voltar a redesenhar depois do teste mostra que o processo falhou, pois o DCU deve chegar à solução final na '
         'primeira passagem pelas fases.', False),
        ('Começar por protótipos de baixa fidelidade, como desenhos em papel, permite avaliar as ideias mais cedo, '
         'antes de investir em telas de alta fidelidade.', True),
        ('Como a equipe testou com apenas cinco idosos, os resultados não têm valor, pois testes de usabilidade exigem '
         'amostras grandes.', False),
    ],
    'I é verdadeira: entrevistar e observar é compreender o contexto de uso (1); definir a meta de três minutos é '
    'especificar requisitos do usuário (2); os protótipos são a produção de soluções de design (3); e o teste é a '
    'avaliação (4). II é falsa: o DCU é iterativo, e os resultados da avaliação alimentam a próxima volta até chegar ao '
    'nível adequado de usabilidade. III é verdadeira: os protótipos vão de baixa a alta fidelidade justamente para '
    'testar cedo. IV é falsa: cinco usuários bastam para encontrar cerca de 85% dos problemas.',
    contexto=[p('Para criar um aplicativo de agendamento de vacinas, uma equipe: '
                '(1) entrevistou agentes de saúde e observou o atendimento nos postos; '
                '(2) definiu que um idoso deve conseguir concluir um agendamento em até três minutos; '
                '(3) desenhou as telas em papel e, depois, fez um protótipo navegável de alta fidelidade; '
                '(4) testou o protótipo com cinco idosos, encontrou vários problemas e voltou a redesenhar as telas.')],
)

banco.assercao(
    'dificil',
    'O mapa da jornada do usuário pode revelar problemas que não aparecem quando se avalia apenas a tela do aplicativo.',
    'A jornada do usuário é uma representação fictícia, mas baseada em dados reais, de um segmento típico de usuários.',
    2,
    'A I é verdadeira: a jornada mapeia todos os passos até o objetivo, inclusive os que acontecem fora da tela, e '
    'por isso revela pain points que a interface sozinha não mostra, como a cancela que não lê o código. A II é falsa: '
    'ela descreve a persona. A jornada do usuário é a sequência de passos que o usuário percorre para alcançar um objetivo.',
    contexto=[p('As telas do aplicativo de um estacionamento foram muito bem avaliadas em testes de usabilidade. Mesmo '
                'assim, os clientes continuam insatisfeitos. Ao mapear todo o percurso, da chegada até a saída, a '
                'equipe descobriu que, na saída, a cancela muitas vezes não lê o código do celular em dias de sol forte, '
                'e o cliente precisa ir até o caixa e enfrentar fila.')],
)

banco.multipla(
    'dificil',
    'Os problemas 1, 2 e 3 violam, respectivamente, as heurísticas de',
    'consistência e padrões, reconhecimento em vez de lembrança, e flexibilidade e eficiência de uso.',
    [
        'estética e design minimalista, reconhecimento em vez de lembrança, e controle e liberdade do usuário.',
        'consistência e padrões, visibilidade do status do sistema, e flexibilidade e eficiência de uso.',
        'correspondência com o mundo real, prevenção de erros, e ajuda e documentação.',
        'consistência e padrões, ajuda e documentação, e estética e design minimalista.',
    ],
    'O mesmo botão com cores e posições diferentes em cada tela viola a consistência e padrões: elementos parecidos '
    'devem se comportar de forma parecida (1). Obrigar o usuário a decorar um número que estava na tela anterior viola '
    'o reconhecimento em vez de lembrança, que pede para reduzir a carga de memória deixando a informação visível (2). '
    'A falta de atalhos para quem usa o sistema o dia inteiro viola a flexibilidade e eficiência de uso, que prevê '
    'aceleradores para usuários experientes sem atrapalhar os iniciantes (3).',
    contexto=[p('Em uma avaliação heurística de um sistema de atendimento ao cliente, os especialistas registraram: '
                '(1) o botão "Excluir" é vermelho e fica à direita em algumas telas, mas é cinza e fica à esquerda em outras; '
                '(2) para abrir um chamado, o atendente precisa digitar o número de protocolo de 12 dígitos que apareceu '
                'na tela anterior, que já foi fechada; '
                '(3) os atendentes, que usam o sistema o dia inteiro, não têm nenhum atalho de teclado e precisam passar '
                'por cinco menus para cada operação.')],
)

banco.multipla(
    'dificil',
    'Sobre as duas propostas, assinale a alternativa INCORRETA.',
    'Pela Lei de Hick, o tempo de decisão cresce de forma linear com o número de opções; por isso, a proposta B reduz '
    'o tempo de decisão a um terço do tempo da proposta A.',
    [
        'Pela Lei de Hick, reduzir de 12 para 4 o número de opções em cada tela tende a diminuir o tempo de decisão em '
        'cada tela.',
        'Pela Lei de Fitts, os botões maiores da proposta B tendem a ser alcançados mais rapidamente, o que ajuda '
        'especialmente quem tem dificuldade motora.',
        'A Lei de Fitts considera tanto o tamanho do alvo quanto a distância até ele.',
        'Dividir as escolhas em etapas menores, como na proposta B, segue a mesma ideia de dividir um formulário longo '
        'em etapas para reduzir a carga de decisão.',
    ],
    'A afirmação incorreta é a da Lei de Hick: o tempo de decisão cresce de forma logarítmica, e não linear, com o '
    'número de opções. Por isso, não dá para dizer que três vezes menos opções dão um terço do tempo. As demais estão '
    'corretas: menos opções por tela reduzem o tempo de decisão (Hick), e alvos maiores e mais próximos são alcançados '
    'mais rápido (Fitts).',
    contexto=[p('Para a tela inicial de um caixa eletrônico, há duas propostas. Na A, as 12 operações aparecem de uma '
                'vez, em botões pequenos. Na B, a primeira tela mostra só 4 botões grandes (Saque, Depósito, Pagamentos '
                'e Outros), e as demais operações ficam em uma segunda tela.')],
)

banco.multipla(
    'dificil',
    'A análise correta da situação é:',
    'A acessibilidade faz parte da usabilidade, pois o produto deve atender aos usuários do seu contexto de uso, '
    'e o nível AA da WCAG, padrão de mercado, é uma meta adequada para o site.',
    [
        'O gerente está certo: acessibilidade é uma questão à parte, e a usabilidade se preocupa apenas com a maioria '
        'dos usuários.',
        'O site deve buscar o nível A da WCAG, que é o nível máximo de acessibilidade e o padrão de mercado.',
        'A acessibilidade é responsabilidade do próprio usuário, que deve usar programas que adaptem o site às suas '
        'necessidades.',
        'A acessibilidade é apenas uma questão de UI, ligada a cores e tamanhos de fonte, e não afeta a UX.',
    ],
    'A ISO 9241-210 define usabilidade para usuários específicos em um contexto específico de uso. O site de uma '
    'prefeitura atende a todos os moradores, inclusive pessoas com deficiência visual, que fazem parte desse contexto. '
    'A WCAG garante que o design seja utilizável por pessoas com diferentes capacidades e tem três níveis: A (mínimo), '
    'AA (padrão de mercado) e AAA (máximo). A acessibilidade afeta toda a experiência, e não só o visual.',
    contexto=[p('Moradores com deficiência visual reclamaram que não conseguem emitir a segunda via do IPTU no site da '
                'prefeitura usando leitores de tela. O gerente do projeto respondeu: "acessibilidade atende a uma '
                'minoria e não é um problema de usabilidade, que é o foco do nosso trabalho".')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"Good design is actually a lot harder to notice than poor design, in part because good designs fit '
                   'our needs so well that the design is invisible."',
        'traducao': '(Tradução livre: "O bom design é, na verdade, muito mais difícil de notar do que o design ruim, em '
                    'parte porque os bons designs se ajustam tão bem às nossas necessidades que o design fica invisível.")',
        'fonte': 'NORMAN, D. The Design of Everyday Things. Edição revista e ampliada. New York: Basic Books, 2013.',
    },
    [
        'Com pouco tempo até o lançamento, a equipe de um banco digital decidiu não fazer testes com usuários e confiar '
        'na experiência do designer, cujas telas eram elogiadas por todos na empresa. Um mês depois do lançamento, '
        '40% dos clientes que começam uma transferência desistem antes de concluí-la, e a central de atendimento '
        'recebe centenas de ligações por dia de pessoas que não encontram o comprovante.',
    ],
    'Com base no texto de Norman e no caso apresentado, explique como a equipe poderia ter identificado e evitado esses '
    'problemas antes do lançamento.',
    'Telas bonitas e elogiadas dentro da empresa não garantem uma boa experiência: quem conhece o sistema não tem as '
    'dificuldades de quem o usa pela primeira vez. Como diz Norman, o bom design passa despercebido porque se ajusta à '
    'necessidade do usuário; o que os clientes notaram foi o design ruim. A equipe deveria ter seguido o Design '
    'Centrado no Usuário, processo iterativo da ISO 9241-210: compreender o contexto de uso (quem são os clientes e '
    'como fazem transferências), especificar requisitos do usuário, produzir protótipos, de baixa a alta fidelidade, e '
    'avaliá-los com usuários reais, voltando ao design a cada problema encontrado. Mesmo com pouco tempo, cinco usuários '
    'bastam para revelar cerca de 85% dos problemas, e um teste remoto não moderado é barato e rápido. As métricas, como '
    'taxa de sucesso na tarefa, tempo de conclusão, taxa de erros e SUS, mostrariam antes do lançamento a desistência '
    'na transferência e a dificuldade de achar o comprovante. Uma avaliação heurística também ajudaria, mas sem '
    'substituir os testes com usuários.',
)

banco.discursiva(
    'dificil',
    {
        'citacao': '"The best results come from testing no more than 5 users and running as many small tests as you can '
                   'afford."',
        'traducao': '(Tradução livre: "Os melhores resultados vêm de testar com no máximo 5 usuários e fazer tantos '
                    'testes pequenos quanto você puder pagar.")',
        'fonte': 'NIELSEN, J. Why You Only Need to Test with 5 Users. Nielsen Norman Group, 2000. Disponível em: nngroup.com.',
    },
    [
        'Uma empresa que está criando um sistema de matrículas on-line tem orçamento para testar com quinze usuários. '
        'O gerente do projeto planeja um único teste, com os quinze, quando o sistema estiver pronto, uma semana antes '
        'de começarem as matrículas.',
    ],
    'Com base no texto de Nielsen e no caso apresentado, avalie o plano do gerente e proponha uma forma melhor de '
    'usar o orçamento disponível.',
    'O plano gasta mal o orçamento e deixa os testes tarde demais. Como cinco usuários já revelam cerca de 85% dos '
    'problemas, os outros dez participantes de um único teste tendem a repetir os mesmos problemas, trazendo pouca '
    'informação nova. Além disso, com o sistema pronto e a uma semana das matrículas, não haverá tempo nem dinheiro '
    'para mudar muita coisa. O melhor é dividir o orçamento em três rodadas de cinco usuários, encaixadas no ciclo '
    'iterativo do Design Centrado no Usuário: testar cedo, com protótipos, corrigir os problemas encontrados e testar '
    'de novo. Cada nova rodada confirma se as correções funcionaram, encontra problemas que as próprias mudanças '
    'criaram e revela parte dos que ficaram de fora. Comparar as métricas entre as rodadas, como taxa de sucesso, tempo '
    'de conclusão, erros e SUS, mostra se a usabilidade está melhorando de verdade.',
)


if __name__ == '__main__':
    banco.gravar()
