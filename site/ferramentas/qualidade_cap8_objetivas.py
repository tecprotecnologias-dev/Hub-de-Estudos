"""
Questões médias e difíceis do capítulo 8 (Testes de Performance e Carga) de Qualidade e Testes de
Software: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um
único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/qualidade_cap8_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap8-o* e
qualidade-cap8-d*; as que já existiam (m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import QUALIDADE, Banco, codigo, p

banco = Banco('qualidade-cap8', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As medições 1, 2, 3 e 4 se referem, respectivamente, a',
    'desempenho, escalabilidade, capacidade e disponibilidade.',
    [
        'escalabilidade, desempenho, capacidade e disponibilidade.',
        'desempenho, capacidade, escalabilidade e disponibilidade.',
        'desempenho, escalabilidade, disponibilidade e capacidade.',
        'capacidade, escalabilidade, desempenho e disponibilidade.',
    ],
    'Quão rápido o sistema responde a uma carga específica é o desempenho (1). Manter um desempenho aceitável quando a '
    'carga cresce é a escalabilidade (2). O volume máximo suportado antes de degradar é a capacidade (3). O percentual '
    'do tempo em que o sistema está operacional e acessível é a disponibilidade (4).',
    contexto=[p('No relatório de um e-commerce, a equipe registrou quatro medições: '
                '(1) o checkout responde em 1,2 segundo com 500 usuários; '
                '(2) o tempo de resposta quase não muda quando os usuários passam de 500 para 5.000; '
                '(3) o sistema suporta até 8.000 usuários simultâneos antes de começar a degradar; '
                '(4) o sistema ficou no ar 99,95% do tempo nos últimos 12 meses.')],
)

banco.multipla(
    'medio',
    'As estratégias 1, 2 e 3 correspondem, respectivamente, à escalabilidade',
    'vertical, horizontal e elástica.',
    [
        'horizontal, vertical e elástica.',
        'vertical, elástica e horizontal.',
        'elástica, horizontal e vertical.',
        'horizontal, elástica e vertical.',
    ],
    'Aumentar os recursos de uma única máquina, com mais CPU e mais memória, é a escalabilidade vertical (scale up), '
    'limitada pelo hardware disponível (1). Adicionar mais máquinas ao conjunto de servidores é a horizontal (scale out), '
    'a preferida em arquiteturas de nuvem (2). Aumentar e diminuir os recursos automaticamente, conforme a demanda, é a '
    'elástica, com auto-scaling (3).',
    contexto=[p('Três empresas resolveram problemas de lentidão de formas diferentes: '
                '(1) a primeira trocou o servidor por um com o dobro de processadores e de memória; '
                '(2) a segunda passou a distribuir os acessos entre seis servidores iguais; '
                '(3) a terceira configurou a nuvem para criar servidores nos horários de pico e removê-los quando o '
                'movimento cai.')],
)

banco.afirmativas(
    'medio',
    [
        ('A latência é o tempo de ida e volta de um pacote pela rede, sem incluir o tempo de processamento.', True),
        ('O throughput é o tempo médio que cada requisição leva para receber a resposta completa.', False),
        ('O TTFB é o tempo até o primeiro byte da resposta chegar ao cliente, com meta típica abaixo de 200 ms.', True),
        ('O Apdex é um índice de satisfação de 0 a 1, baseado no tempo de resposta, com meta acima de 0,85.', True),
    ],
    'I, III e IV estão de acordo com a tabela de métricas da apostila. II é falsa: o throughput (vazão) é o número de '
    'requisições processadas por unidade de tempo, como requisições por segundo; o tempo até a resposta completa é o '
    'tempo de resposta.',
    contexto=[p('Ao montar o painel de monitoramento de uma API, a equipe revisou as definições das métricas de '
                'performance que vai acompanhar.')],
)

banco.assercao(
    'medio',
    'Um SLA de 99,9% de disponibilidade permite cerca de 8,7 horas de indisponibilidade por ano.',
    'Um ano tem 8.760 horas, e 0,1% desse tempo corresponde a aproximadamente 8,76 horas.',
    0,
    'As duas são verdadeiras, e a II explica a I. Se o sistema deve ficar disponível 99,9% do tempo, pode ficar fora do '
    'ar 0,1% dele: 8.760 × 0,001 ≈ 8,76 horas por ano, o valor citado no exemplo de SLA da apostila.',
    contexto=[p('O contrato de um sistema de pagamentos exige disponibilidade superior a 99,9%. O gerente quer saber '
                'quanto tempo de indisponibilidade isso permite em um ano.')],
)

banco.multipla(
    'medio',
    'As fases 1, 2, 3 e 4 do teste de carga correspondem, respectivamente, aos perfis',
    'ramp-up, steady state, ramp-down e completo.',
    [
        'steady state, ramp-up, ramp-down e completo.',
        'ramp-up, ramp-down, steady state e completo.',
        'ramp-up, steady state, completo e ramp-down.',
        'completo, steady state, ramp-down e ramp-up.',
    ],
    'No ramp-up, a carga aumenta aos poucos até o volume alvo, evitando um choque inicial (1). No steady state, a carga é '
    'mantida constante, para verificar a estabilidade (2). No ramp-down, a carga diminui até zero, para observar como o '
    'sistema libera recursos (3). O perfil completo junta os três em sequência, formando uma curva em trapézio (4).',
    contexto=[p('O teste de carga de um portal foi dividido em quatro partes: '
                '(1) os usuários virtuais aumentam de 0 a 3.000 ao longo de 15 minutos; '
                '(2) os 3.000 usuários são mantidos por uma hora; '
                '(3) os usuários diminuem de 3.000 até 0; '
                '(4) no relatório final, as três fases anteriores foram executadas em sequência.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Qual tipo de teste de performance é o mais adequado para investigar esse problema?',
    'O teste de volume, que avalia o comportamento com grandes volumes de dados, e não com muitos usuários.',
    [
        'O teste de carga, que simula o número de usuários esperado em produção, no uso normal e no pico.',
        'O teste de estresse, que leva o sistema além dos limites de usuários para descobrir o ponto de falha.',
        'O teste de pico, que avalia a reação do sistema a um aumento repentino e drástico do número de usuários.',
        'O teste de resistência, que mantém a carga normal por horas para encontrar vazamentos de memória.',
    ],
    'O problema aparece com poucos usuários e cresce com a quantidade de dados: é o cenário do teste de volume, que '
    'avalia o tempo de processamento, o uso de disco e o desempenho das consultas sobre bases enormes. O exemplo da '
    'apostila é justamente um relatório sobre 500 milhões de registros. Carga, estresse e pico variam o número de '
    'usuários, e a resistência varia o tempo de execução.',
    contexto=[p('O relatório anual de um sistema de notas fiscais demorava 5 segundos quando a base tinha 1 milhão de '
                'registros. Hoje, com 500 milhões de registros, ele leva 40 minutos, mesmo quando apenas cinco '
                'funcionários usam o sistema.')],
)

banco.afirmativas(
    'dificil',
    [
        ('O padrão em escada aumenta a carga em degraus fixos e mostra o comportamento do sistema em cada nível.', True),
        ('O pico instantâneo aumenta a carga de forma linear e contínua até o sistema falhar.', False),
        ('A carga assimétrica distribui o estresse igualmente por todos os componentes do sistema.', False),
        ('O estresse prolongado mantém a carga acima do limite por horas, para ver se o sistema se recupera sozinho.',
         True),
    ],
    'I é verdadeira: o step load (por exemplo, mais 500 usuários a cada 5 minutos) identifica gargalos por camada. II é '
    'falsa: o pico instantâneo aplica a carga máxima de uma vez, sem ramp-up; aumentar de forma linear até a falha é a '
    'rampa constante. III é falsa: a carga assimétrica estressa só uma parte do sistema, como o banco, para isolar '
    'gargalos. IV é verdadeira: o estresse prolongado revela a capacidade de recuperação e a degradação progressiva.',
    contexto=[p('Uma equipe vai planejar os testes de estresse de um sistema de ingressos e revisou os padrões para '
                'aumentar a carga.')],
)

banco.assercao(
    'dificil',
    'Ao mudar ao mesmo tempo o tamanho do pool de conexões, a configuração do cache e a versão do banco, a equipe não '
    'consegue saber qual mudança melhorou o desempenho.',
    'A boa prática em testes de performance é mudar várias coisas de uma vez, para economizar ciclos de teste.',
    2,
    'A I é verdadeira: com três mudanças juntas, a melhora pode ter vindo de qualquer uma delas, ou de uma combinação, e '
    'uma delas pode até ter piorado o resultado sem que se perceba. A II é falsa: a apostila recomenda isolar variáveis, '
    'mudando só uma coisa de cada vez, e comparar com uma baseline registrada.',
    contexto=[p('Depois de um teste de carga ruim, a equipe aumentou o pool de conexões, ativou um cache e atualizou o '
                'banco de dados, tudo de uma vez. No novo teste, o P95 caiu de 3 segundos para 1 segundo.')],
)

banco.multipla(
    'dificil',
    'A análise correta do resultado é:',
    'Faltou o think time: sem pausas entre as ações, os usuários virtuais geram uma carga bem maior que a real.',
    [
        'O teste está correto, pois 500 usuários virtuais representam exatamente 500 usuários reais, com pausas ou sem.',
        'O teste está correto e é até mais seguro, pois uma carga maior que a real garante que o sistema aguenta o uso '
        'normal.',
        'O resultado mostra um vazamento de memória, pois a quantidade de requisições cresceu sem aumento de usuários.',
        'O problema é a ferramenta, pois o JMeter sempre gera dez vezes mais requisições que o número de usuários '
        'virtuais.',
    ],
    'Usuários reais leem, pensam e preenchem formulários entre uma ação e outra. A apostila recomenda configurar um think '
    'time realista para simular esse comportamento. Sem pausas, cada usuário virtual dispara requisições sem parar, e '
    'os 500 geram 3.000 requisições por segundo, dez vezes o padrão real. O teste passa a ser outro, mais próximo de um '
    'estresse, e não responde à pergunta sobre o uso normal.',
    contexto=[p('Em produção, 500 usuários simultâneos de um sistema geram cerca de 300 requisições por segundo. No teste '
                'de carga, o script com 500 usuários virtuais, que repetem as ações sem nenhuma pausa entre elas, gerou '
                '3.000 requisições por segundo, e o sistema ficou lento.')],
)

banco.multipla(
    'dificil',
    'Sobre as ferramentas de teste de performance, assinale a alternativa INCORRETA.',
    'O Locust define os cenários em JavaScript e é implementado em Go, o que o torna a ferramenta mais eficiente em '
    'recursos.',
    [
        'O JMeter tem interface gráfica para criar os planos e linha de comando para rodar em CI/CD, e consome muita memória '
        'em larga escala.',
        'O Gatling usa uma DSL em Scala ou Java e simula muito mais usuários que o JMeter com os mesmos recursos.',
        'O k6 tem scripts em JavaScript ou TypeScript, é implementado em Go e integra-se nativamente ao Grafana.',
        'O Locust define os cenários em Python e tem uma interface web para acompanhar e ajustar a carga em tempo real.',
    ],
    'A afirmação incorreta descreve o k6, e não o Locust: o Locust usa Python, tem eficiência de recursos média no '
    'comparativo e uma interface web em tempo real. JavaScript, Go e a maior eficiência de recursos são características '
    'do k6. As demais alternativas descrevem corretamente o JMeter, o Gatling, o k6 e o Locust.',
    contexto=[p('Uma equipe comparou quatro ferramentas antes de escolher a que vai usar nos testes de performance.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'A prefeitura de uma cidade grande abriu as matrículas da rede municipal por um portal novo. O sistema foi testado '
        'por cinco servidores da secretaria, que fizeram matrículas de teste durante uma semana, sem problemas. No primeiro '
        'dia, às 8 horas, 50 mil famílias tentaram acessar o portal ao mesmo tempo: as páginas levaram mais de um minuto '
        'para abrir, o site saiu do ar várias vezes, e a matrícula precisou ser adiada. A apostila cita um caso parecido, o '
        'do Healthcare.gov, que colapsou no lançamento por falta de testes de carga adequados.',
    ],
    'Proponha um plano de testes de performance que teria permitido à prefeitura identificar e evitar esses problemas '
    'antes da abertura das matrículas.',
    'O plano começaria pelos objetivos e SLAs com números, como P95 abaixo de 3 segundos, taxa de erros abaixo de 1% e '
    'alta disponibilidade no período de matrículas, e pela modelagem de carga: quantas famílias, em que horário, quais '
    'páginas e em que proporção, com think time realista. O ambiente e os dados de teste deveriam ser parecidos com os da '
    'produção. Depois, os testes: de carga, com o volume esperado de famílias, em ramp-up, steady state e ramp-down; de '
    'pico, porque às 8 horas a carga sai de quase zero para 50 mil de uma vez; de estresse, para descobrir o ponto de '
    'falha, a margem de segurança e se o sistema degrada de forma graciosa (por exemplo, com uma fila de espera, em vez de '
    'sair do ar); e de resistência, para ver se ele se mantém estável ao longo de todo o dia. A execução seria '
    'incremental, com monitoramento de CPU, memória, banco e logs, análise da causa dos gargalos, correção e novo teste. '
    'Cinco pessoas testando funções não dizem nada sobre o comportamento com 50 mil acessos simultâneos.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma equipe executou um teste de carga de 6 horas em uma API de pedidos e anotou os resultados abaixo.',
    ],
    'Interprete os resultados e explique quais são os prováveis problemas do sistema e o que a equipe deve investigar '
    'em seguida.',
    'Até 2.000 usuários, o throughput cresce junto com a carga e o P95 fica estável. A partir daí, o throughput para em '
    'cerca de 900 requisições por segundo, mesmo com mais usuários, e o P95 dispara: o sistema chegou ao ponto de '
    'saturação. Como a CPU continua por volta de 40%, o gargalo não é o processamento; as suspeitas são o pool de '
    'conexões com o banco esgotado, filas cheias ou bloqueios (locks), a investigar com thread dump, métricas do pool e '
    'logs do banco. Há um segundo problema, independente da carga: a memória cresce sem parar ao longo das 6 horas, mesmo '
    'nos períodos estáveis, o que indica um vazamento de memória. Ele pede um teste de resistência mais longo e análise '
    'com heap dump e profiler. A equipe deve atacar um problema de cada vez, mudando uma variável por teste, e comparar '
    'cada resultado com a baseline.',
)
banco.discursivas[-1]['contexto'] = [
    codigo('''
Usuários  Throughput  P95       CPU   Memória
500       240 req/s   400 ms    15%   2,1 GB
1.000     480 req/s   420 ms    22%   2,6 GB
2.000     900 req/s   450 ms    38%   3,2 GB
3.000     905 req/s   2.800 ms  40%   3,9 GB
4.000     900 req/s   6.100 ms  41%   4,7 GB
'''),
    p('Durante todo o teste, inclusive nos períodos em que a carga ficou estável, a memória não parou de crescer.'),
]


if __name__ == '__main__':
    banco.gravar()
