"""Questões objetivas do Capítulo 1 (Lógica, algoritmos e o computador)."""

CAPITULO = 'alg1-cap1'

QUESTOES = [
    {
        'nivel': 'facil',
        'enunciado': 'Qual das definições descreve corretamente um algoritmo?',
        'certa': 'Uma sequência finita e ordenada de passos bem definidos que resolve um problema',
        'erradas': [
            'Um programa escrito obrigatoriamente em uma linguagem de programação',
            'Um componente físico do computador que executa os cálculos',
            'Uma lista de dados de entrada usada para testar um programa',
        ],
        'resolucao': 'Um algoritmo é a sequência de passos, não importa em que forma está escrito: '
                     'em português, em fluxograma, em Portugol ou em uma linguagem de programação. Uma '
                     'receita de bolo também é um algoritmo.',
    },
    {
        'nivel': 'facil',
        'enunciado': 'Em um fluxograma, qual forma representa uma decisão, como "nota >= 6?"?',
        'certa': 'O losango, com duas saídas identificadas',
        'erradas': [
            'O retângulo, que representa um cálculo ou atribuição',
            'O paralelogramo, que representa a leitura ou a exibição de dados',
            'O retângulo de cantos arredondados, que marca o início e o fim',
        ],
        'resolucao': 'O losango faz uma pergunta de sim ou não, e o caminho seguido depende da resposta. '
                     'Por isso toda decisão tem duas saídas, cada uma identificada (Seção 1.5).',
    },
    {
        'nivel': 'medio',
        'enunciado': 'Na arquitetura de Von Neumann, onde fica um programa enquanto está sendo executado?',
        'certa': 'Na memória principal (RAM), junto com os dados que ele usa',
        'erradas': [
            'Nos registradores da CPU, que guardam o programa inteiro',
            'No armazenamento (SSD ou disco), de onde a CPU busca cada instrução diretamente',
            'Em uma memória separada, exclusiva para programas, sem acesso aos dados',
        ],
        'resolucao': 'A grande ideia de Von Neumann foi guardar o programa na mesma memória que os dados. '
                     'Para executar um programa, o sistema o copia do armazenamento para a RAM, e a CPU '
                     'busca as instruções ali. Os registradores são pequenos e guardam só os valores em uso.',
    },
    {
        'nivel': 'medio',
        'codigo': '''a <- 5
b <- 3
a <- a + b
b <- a - b
a <- a - b''',
        'enunciado': 'Faça o teste de mesa do trecho em Portugol acima. Quais são os valores de a e b no fim?',
        'certa': 'a = 3 e b = 5',
        'erradas': ['a = 5 e b = 3', 'a = 8 e b = 5', 'a = 3 e b = 8'],
        'resolucao': 'Linha a linha: a vale 5 e b vale 3; a recebe 5 + 3 = 8; b recebe 8 - 3 = 5; a recebe '
                     '8 - 5 = 3. O trecho troca os valores das duas variáveis sem usar uma terceira.',
        'executar': '''int a = 5, b = 3;
a = a + b;
b = a - b;
a = a - b;
cout << "a = " << a << " e b = " << b;''',
    },
    {
        'nivel': 'dificil',
        'codigo': 'media <- nota1 + nota2 / 2',
        'enunciado': 'Um algoritmo usa a linha acima para calcular a média de duas notas. Com nota1 = 6 e '
                     'nota2 = 8, que valor ele calcula?',
        'certa': '10, porque a divisão é feita antes da soma',
        'erradas': [
            '7, que é a média correta das duas notas',
            '7, porque as operações são feitas da esquerda para a direita',
            '14, porque a divisão por 2 é ignorada',
        ],
        'resolucao': 'A divisão tem precedência sobre a soma, então só nota2 é dividida: 6 + 8 / 2 = 6 + 4 '
                     '= 10. Para a média, são necessários parênteses: (nota1 + nota2) / 2. O algoritmo roda '
                     'sem nenhum erro aparente, e só um teste de mesa revela o problema.',
        'executar': 'double nota1 = 6, nota2 = 8;\ncout << nota1 + nota2 / 2 << ", porque a divisão é feita antes da soma";',
    },
]
