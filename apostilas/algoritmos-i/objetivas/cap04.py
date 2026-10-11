"""Questões objetivas do Capítulo 4 (Estruturas de decisão)."""

CAPITULO = 'alg1-cap4'

QUESTOES = [
    {
        'nivel': 'facil',
        'codigo': '''int n = 7;
if (n % 2 == 0) cout << "par";
else cout << "ímpar";''',
        'enunciado': 'O que o trecho acima mostra?',
        'certa': 'ímpar',
        'erradas': ['par', 'parímpar', 'Nada, porque falta o bloco com chaves'],
        'resolucao': '7 % 2 vale 1, então a condição é falsa e o else é executado. As chaves são opcionais '
                     'quando o if ou o else têm um único comando.',
        'executar': True,
    },
    {
        'nivel': 'facil',
        'enunciado': 'Qual estrutura é a mais indicada para escolher entre vários valores exatos de uma variável '
                     'inteira, como os dias da semana de 1 a 7?',
        'certa': 'switch (escolha, no Portugol)',
        'erradas': ['while (enquanto, no Portugol)', 'for (para, no Portugol)', 'Um único if, sem else'],
        'resolucao': 'O switch compara uma variável com vários valores exatos, um caso para cada valor, e fica '
                     'mais legível que uma longa sequência de else if (Seção 4.5). While e for são laços, e não '
                     'decisões.',
    },
    {
        'nivel': 'medio',
        'codigo': '''int op = 2;
switch (op) {
    case 1: cout << "A";
    case 2: cout << "B";
    case 3: cout << "C";
    default: cout << "D";
}''',
        'enunciado': 'O que o trecho acima mostra?',
        'certa': 'BCD',
        'erradas': ['B', 'BC', 'ABCD'],
        'resolucao': 'Sem break, a execução começa no caso que corresponde ao valor (case 2) e continua pelos '
                     'casos seguintes, incluindo o default. Por isso cada caso costuma terminar com break.',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'codigo': '''double nota = 9.5;
if (nota >= 6) cout << "Aprovado";
else if (nota >= 9) cout << "Excelente";
else cout << "Reprovado";''',
        'enunciado': 'A intenção era mostrar "Excelente" para notas a partir de 9. O que o trecho mostra?',
        'certa': 'Aprovado',
        'erradas': ['Excelente', 'AprovadoExcelente', 'Reprovado'],
        'resolucao': 'Em uma cadeia de else if, só o primeiro teste verdadeiro é executado. Como 9.5 >= 6 já é '
                     'verdadeiro, o teste de 9 nunca é feito. A condição mais restrita (>= 9) precisa vir antes.',
        'executar': True,
    },
    {
        'nivel': 'dificil',
        'codigo': '''int x = 0;
if (x = 5) cout << "sim";
else cout << "não";
cout << " " << x;''',
        'enunciado': 'O que o trecho acima mostra?',
        'certa': 'sim 5',
        'erradas': ['não 0', 'não 5', 'sim 0'],
        'resolucao': 'x = 5 é uma atribuição, e não uma comparação: ela guarda 5 em x e vale 5, que é '
                     'verdadeiro (qualquer valor diferente de zero). Por isso o if executa, e x termina valendo '
                     '5. A comparação seria x == 5. Compilar com -Wall faz o g++ avisar desse engano.',
        'executar': True,
    },
]
