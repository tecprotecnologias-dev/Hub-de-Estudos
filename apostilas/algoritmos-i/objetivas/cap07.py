"""Questões objetivas do Capítulo 7 (Vetores e matrizes)."""

CAPITULO = 'alg1-cap7'

QUESTOES = [
    {
        'nivel': 'facil',
        'codigo': 'int v[10];',
        'enunciado': 'Quais são o primeiro e o último índices válidos do vetor declarado acima?',
        'certa': '0 e 9',
        'erradas': ['1 e 10', '0 e 10', '1 e 9'],
        'resolucao': 'Em C++, os índices começam sempre em 0. Um vetor de 10 elementos vai de v[0] a v[9]; v[10] '
                     'já está fora dele. No Portugol, quem escolhe os limites é a declaração, como vetor[1..10].',
    },
    {
        'nivel': 'facil',
        'codigo': '''int v[5] = {2, 4, 6, 8, 10};
cout << v[1] + v[3];''',
        'enunciado': 'O que o trecho acima mostra?',
        'certa': '12',
        'erradas': ['10', '6', '14'],
        'resolucao': 'Contando a partir de 0, v[1] é o segundo elemento (4) e v[3] é o quarto (8): 4 + 8 = 12. '
                     'Quem conta a partir de 1 soma 2 + 6 = 8, ou pega v[3] como 6.',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'codigo': 'int v[4] = {7};',
        'enunciado': 'Quais valores ficam no vetor depois da declaração acima?',
        'certa': '7, 0, 0, 0',
        'erradas': ['7, 7, 7, 7', '7 e três valores imprevisíveis (lixo)',
                    'Nenhum: o código não compila, porque faltam valores'],
        'resolucao': 'A lista entre chaves preenche os elementos na ordem, e os que sobram ficam com 0. Por isso '
                     '= {} é a forma curta de zerar um vetor inteiro (Seção 7.1). Sem nenhuma lista, aí sim os '
                     'valores seriam lixo.',
        'executar': 'int v[4] = {7};\ncout << v[0] << ", " << v[1] << ", " << v[2] << ", " << v[3];',
    },
    {
        'nivel': 'medio',
        'codigo': 'int m[3][4];',
        'enunciado': 'Quantos elementos tem a matriz acima, e como se acessa o último deles?',
        'certa': '12 elementos; o último é m[2][3]',
        'erradas': ['12 elementos; o último é m[3][4]', '7 elementos; o último é m[2][3]',
                    '12 elementos; o último é m[4][3]'],
        'resolucao': 'São 3 linhas de 4 colunas: 3 × 4 = 12 elementos. As linhas vão de 0 a 2 e as colunas de 0 '
                     'a 3, então o último elemento é m[2][3]. O primeiro índice é sempre a linha.',
    },
    {
        'nivel': 'dificil',
        'codigo': '''int v[5] = {1, 2, 3, 4, 5};
for (int i = 0; i <= 5; i++) {
    cout << v[i] << " ";
}''',
        'enunciado': 'O que se pode afirmar sobre o trecho acima?',
        'certa': 'A última volta acessa v[5], fora do vetor: é comportamento indefinido, e o programa pode '
                 'mostrar lixo, alterar outra variável ou travar',
        'erradas': [
            'O C++ detecta o índice inválido e interrompe o programa com uma mensagem de erro',
            'O compilador recusa o programa, porque o laço passa do tamanho do vetor',
            'v[5] vale 0, porque as posições depois do fim do vetor são sempre zeradas',
        ],
        'resolucao': 'O C++ não confere os índices dos vetores comuns: ele calcula onde estaria v[5] e lê aquela '
                     'posição da memória, que pertence a outra coisa. O erro está no <=: para percorrer 5 '
                     'elementos, a condição é i < 5 (Seção 7.3). O vector com at() confere o índice.',
    },
]
