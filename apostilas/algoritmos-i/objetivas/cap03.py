"""Questões objetivas do Capítulo 3 (Variáveis, tipos e operadores)."""

CAPITULO = 'alg1-cap3'

QUESTOES = [
    {
        'nivel': 'facil',
        'enunciado': 'Qual tipo do C++ é o mais adequado para guardar a altura de uma pessoa em metros, como 1.75?',
        'certa': 'double',
        'erradas': ['int', 'char', 'bool'],
        'resolucao': 'A altura tem casas decimais, então precisa de um tipo real: double. Com int, 1.75 viraria '
                     '1; char guarda um caractere, e bool, só verdadeiro ou falso.',
    },
    {
        'nivel': 'facil',
        'codigo': 'cout << 17 / 5 << " " << 17 % 5;',
        'enunciado': 'O que o comando acima mostra?',
        'certa': '3 2',
        'erradas': ['3.4 2', '3 0.4', '3.4 0'],
        'resolucao': 'Com dois inteiros, / é a divisão inteira (17 / 5 = 3) e % é o resto da divisão '
                     '(17 = 5 × 3 + 2, então o resto é 2).',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'codigo': '''int x = 5;
x += 3;
x *= 2;
cout << x;''',
        'enunciado': 'Qual valor é mostrado?',
        'certa': '16',
        'erradas': ['13', '11', '10'],
        'resolucao': 'x += 3 é o mesmo que x = x + 3, e x passa a valer 8. Depois, x *= 2 é x = x * 2, e x '
                     'passa a valer 16.',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'codigo': 'cout << 2 + 3 * 4 - 6 / 2;',
        'enunciado': 'Qual valor é mostrado?',
        'certa': '11',
        'erradas': ['7', '17', '8'],
        'resolucao': 'Multiplicação e divisão vêm antes de soma e subtração: 3 * 4 = 12 e 6 / 2 = 3, e então '
                     '2 + 12 - 3 = 11. Quem calcula da esquerda para a direita, sem precedência, chega a 7.',
        'executar': True,
    },
    {
        'nivel': 'dificil',
        'codigo': '''int pessoas = 0;
double total = 100;
bool caro = pessoas > 0 && total / pessoas > 50;''',
        'enunciado': 'O que acontece quando o trecho acima é executado?',
        'certa': 'caro recebe false, e a divisão nem é calculada, porque o lado esquerdo do && já é falso',
        'erradas': [
            'O programa é interrompido com um erro de divisão por zero',
            'caro recebe true, porque 100 dividido por 0 é infinito',
            'O compilador recusa o código por causa da possível divisão por zero',
        ],
        'resolucao': 'Os operadores && e || fazem avaliação em curto-circuito: se o lado esquerdo já decide o '
                     'resultado, o direito não é calculado. Como pessoas > 0 é falso, o && só pode dar falso, '
                     'e a divisão por zero nunca acontece (Seção 3.6). Por isso a ordem das condições importa.',
    },
]
