"""Questões objetivas do Capítulo 9 (Recursão e backtracking)."""

CAPITULO = 'alg1-cap9'

QUESTOES = [
    {
        'nivel': 'facil',
        'enunciado': 'Do que toda função recursiva bem escrita precisa?',
        'certa': 'De um caso base, resolvido sem recursão, e de um caso recursivo que se aproxima dele',
        'erradas': [
            'De um laço for dentro da função para controlar as chamadas',
            'De variáveis globais para guardar os resultados intermediários',
            'De pelo menos duas chamadas recursivas em cada execução',
        ],
        'resolucao': 'Sem caso base, ou sem que cada chamada se aproxime dele, a recursão nunca para e o programa '
                     'termina com estouro de pilha (Seções 9.1 e 9.2).',
    },
    {
        'nivel': 'facil',
        'codigo': '''int f(int n) {
    if (n == 0) return 0;
    return n + f(n - 1);
}

int main() {
    cout << f(4);
}''',
        'enunciado': 'O que o programa acima mostra?',
        'certa': '10',
        'erradas': ['4', '24', '0'],
        'resolucao': 'f(4) = 4 + f(3) = 4 + 3 + f(2) = 4 + 3 + 2 + 1 + f(0) = 10. A função soma os números de 1 '
                     'até n. Com uma multiplicação no lugar da soma (e caso base 1), seria o fatorial, 24.',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'codigo': '''void p(int n) {
    if (n == 0) return;
    p(n - 1);
    cout << n << " ";
}

int main() {
    p(3);
}''',
        'enunciado': 'O que o programa acima mostra?',
        'certa': '1 2 3',
        'erradas': ['3 2 1', '3', '0 1 2 3'],
        'resolucao': 'O cout vem depois da chamada recursiva, então só é executado na volta. p(3) chama p(2), que '
                     'chama p(1), que chama p(0) e retorna. Na volta, p(1) mostra 1, depois p(2) mostra 2 e p(3) '
                     'mostra 3. Com o cout antes da chamada, a saída seria 3 2 1.',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'enunciado': 'Por que a versão recursiva simples de fib(n), com fib(n - 1) + fib(n - 2), fica muito '
                     'lenta para n = 40?',
        'certa': 'Porque recalcula os mesmos valores muitas vezes, e o número de chamadas cresce quase tão rápido '
                 'quanto a própria sequência',
        'erradas': [
            'Porque a recursão é sempre mais lenta que um laço, qualquer que seja o problema',
            'Porque fib(40) não cabe em uma variável do tipo int',
            'Porque a pilha de chamadas chega a ter milhões de registros ao mesmo tempo',
        ],
        'resolucao': 'Cada chamada faz duas outras, que repetem o mesmo trabalho: fib(40) faz mais de 300 milhões '
                     'de chamadas. A pilha, porém, nunca passa de 40 registros ao mesmo tempo, e fib(40) cabe em '
                     'um int. A memoização ou um laço resolvem o problema (Seção 9.4).',
    },
    {
        'nivel': 'dificil',
        'enunciado': 'Quantos movimentos são necessários para resolver as Torres de Hanói com 5 discos?',
        'certa': '31',
        'erradas': ['25', '32', '10'],
        'resolucao': 'Para mover n discos, movem-se n - 1 para o pino de apoio, o maior para o destino e os n - 1 '
                     'de novo por cima: M(n) = 2 × M(n - 1) + 1, com M(1) = 1. Isso dá 2^n - 1: com 5 discos, '
                     '2^5 - 1 = 31 (Seção 9.6).',
        'executar': '''int m = 0;
for (int n = 1; n <= 5; n++) m = 2 * m + 1;
cout << m;''',
    },
]
