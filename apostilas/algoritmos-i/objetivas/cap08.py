"""Questões objetivas do Capítulo 8 (Caracteres e strings)."""

CAPITULO = 'alg1-cap8'

QUESTOES = [
    {
        'nivel': 'facil',
        'enunciado': "Em C++, qual é a diferença entre 'A' e \"A\"?",
        'certa': "'A' é um único caractere (char); \"A\" é um texto (string) que contém um caractere",
        'erradas': [
            'Não há diferença: aspas simples e duplas são equivalentes',
            "'A' é um texto, e \"A\" é um caractere",
            "'A' é a letra maiúscula, e \"A\" é a letra minúscula",
        ],
        'resolucao': 'Aspas simples delimitam um caractere, guardado em um char; aspas duplas delimitam um texto. '
                     "Por isso 'Ana' não é válido: entre aspas simples cabe um único caractere (Seção 8.1).",
    },
    {
        'nivel': 'facil',
        'codigo': '''string s = "Algoritmo";
cout << s.size() << " " << s[0] << s[8];''',
        'enunciado': 'O que o trecho acima mostra?',
        'certa': '9 Ao',
        'erradas': ['8 Ao', '9 Am', '10 Ao'],
        'resolucao': '"Algoritmo" tem 9 caracteres, com índices de 0 a 8. s[0] é o "A" e s[8], o último, é o '
                     '"o". Quem conta a partir de 1 pega s[8] como o "m".',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'codigo': "cout << ('7' - '0') * 2;",
        'enunciado': 'O que o comando acima mostra?',
        'certa': '14',
        'erradas': ['110', '77', 'Nada, porque não se pode subtrair caracteres'],
        'resolucao': "Caracteres são números: '7' vale 55 e '0' vale 48 na tabela ASCII. Como os dígitos são "
                     "consecutivos, '7' - '0' = 7, o valor do dígito, e 7 × 2 = 14. Sem a subtração, '7' * 2 "
                     'daria 110.',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'codigo': '''int idade;
string nome;
cin >> idade;
getline(cin, nome);''',
        'enunciado': 'O usuário digita a idade, tecla Enter e o programa nem espera o nome: nome fica vazio. Por '
                     'quê?',
        'certa': 'O cin >> leu a idade e deixou o Enter na entrada; o getline encontrou esse Enter e leu uma '
                 'linha vazia',
        'erradas': [
            'O getline não funciona depois de um cin, em nenhuma situação',
            'O nome precisa ser declarado como char para ser lido com getline',
            'O getline só lê a primeira palavra, e o nome tinha duas',
        ],
        'resolucao': 'O cin >> para logo depois do número e deixa o Enter para trás. A solução é descartar os '
                     'espaços e quebras de linha pendentes antes do getline: getline(cin >> ws, nome) '
                     '(Seção 8.3).',
    },
    {
        'nivel': 'dificil',
        'codigo': '''string s = "ação";
cout << s.size();''',
        'enunciado': 'Em um arquivo salvo em UTF-8, o que o trecho acima mostra?',
        'certa': '6',
        'erradas': ['4', '5', '8'],
        'resolucao': 'Em UTF-8, as letras sem acento ocupam um byte, mas ç e ã ocupam dois cada. O string conta '
                     'bytes, e não letras: 1 + 2 + 2 + 1 = 6. Por isso processar letra por letra um texto com '
                     'acentos exige cuidado (Seção 8.7).',
        'executar': True,
    },
]
