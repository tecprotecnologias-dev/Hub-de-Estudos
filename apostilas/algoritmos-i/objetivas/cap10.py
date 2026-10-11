"""Questões objetivas do Capítulo 10 (Busca e ordenação)."""

CAPITULO = 'alg1-cap10'

QUESTOES = [
    {
        'nivel': 'facil',
        'enunciado': 'Qual é a condição para usar a busca binária em um vetor?',
        'certa': 'O vetor precisa estar ordenado',
        'erradas': [
            'O vetor precisa ter um número par de elementos',
            'O valor procurado precisa estar no vetor',
            'O vetor precisa ter menos de mil elementos',
        ],
        'resolucao': 'A busca binária descarta metade do vetor a cada passo, comparando o valor procurado com o '
                     'elemento do meio. Isso só faz sentido se o vetor estiver ordenado. Em um vetor desordenado, '
                     'ela não dá erro: simplesmente responde errado.',
    },
    {
        'nivel': 'facil',
        'enunciado': 'Em um vetor ordenado com 1.000 elementos, qual é, aproximadamente, o número máximo de '
                     'comparações da busca binária?',
        'certa': 'Cerca de 10',
        'erradas': ['Cerca de 500', '1.000', 'Cerca de 100'],
        'resolucao': 'A cada comparação, a parte que resta cai pela metade: 1.000, 500, 250, 125... Em cerca de '
                     '10 passos sobra um único elemento, porque 2^10 = 1.024. A busca sequencial poderia precisar '
                     'das 1.000 comparações.',
    },
    {
        'nivel': 'medio',
        'codigo': '29 10 14 37 13',
        'enunciado': 'Aplicando a ordenação por seleção (crescente) ao vetor acima, como ele fica depois da '
                     'PRIMEIRA passada?',
        'certa': '10 29 14 37 13',
        'erradas': ['10 14 29 37 13', '10 13 14 37 29', '10 14 29 13 37'],
        'resolucao': 'A primeira passada procura o menor elemento do vetor inteiro (10) e o troca com o da posição '
                     '0 (29). Os outros elementos não mudam de lugar. Já 10 14 29 13 37 seria o resultado de '
                     'uma passada da bolha, que leva o maior para o fim (Seções 10.4 e 10.5).',
        'executar': '''int v[] = {29, 10, 14, 37, 13};
int iMenor = 0;
for (int j = 1; j < 5; j++) if (v[j] < v[iMenor]) iMenor = j;
swap(v[0], v[iMenor]);
for (int x : v) cout << x << " ";''',
    },
    {
        'nivel': 'medio',
        'enunciado': 'Qual destes algoritmos, aplicado a um vetor que já está ordenado, faz apenas n - 1 '
                     'comparações?',
        'certa': 'A ordenação por inserção',
        'erradas': [
            'A ordenação por seleção',
            'Nenhum: os algoritmos simples sempre fazem cerca de n² comparações',
            'Todos fazem n - 1: seleção, bolha e inserção',
        ],
        'resolucao': 'Na inserção, o laço de dentro para assim que encontra um elemento menor, e em um vetor '
                     'ordenado isso acontece logo na primeira comparação. A seleção faz sempre n(n - 1)/2 '
                     'comparações, ordenado ou não (Seção 10.7).',
    },
    {
        'nivel': 'dificil',
        'enunciado': 'Um algoritmo de ordenação O(n²) leva 1 segundo para ordenar 10.000 elementos. Quanto '
                     'tempo, aproximadamente, levará para 100.000 elementos?',
        'certa': '100 segundos',
        'erradas': ['10 segundos', '1.000 segundos', '20 segundos'],
        'resolucao': 'Com crescimento n², multiplicar n por 10 multiplica o tempo por 10² = 100. Um algoritmo '
                     'O(n log n), como o sort da biblioteca, ficaria só um pouco mais de 10 vezes mais lento '
                     '(Seção 10.3).',
    },
]
