"""Questões objetivas do Capítulo 6 (Funções e procedimentos)."""

CAPITULO = 'alg1-cap6'

QUESTOES = [
    {
        'nivel': 'facil',
        'enunciado': 'Qual é a diferença entre uma função e um procedimento?',
        'certa': 'A função devolve um valor com return; o procedimento executa uma tarefa sem devolver valor '
                 '(void, em C++)',
        'erradas': [
            'A função recebe parâmetros; o procedimento nunca recebe parâmetros',
            'A função só pode ser chamada dentro do main; o procedimento, de qualquer lugar',
            'Não há diferença: são dois nomes para a mesma coisa',
        ],
        'resolucao': 'Uma função é usada como um valor, dentro de uma expressão (x = media(a, b)); um '
                     'procedimento é usado como um comando, sozinho na linha (linha(30)). Os dois podem receber '
                     'parâmetros (Seção 6.3).',
    },
    {
        'nivel': 'facil',
        'codigo': '''void dobrar(int x) {
    x = x * 2;
}

int main() {
    int a = 5;
    dobrar(a);
    cout << a;
}''',
        'enunciado': 'O que o programa acima mostra?',
        'certa': '5',
        'erradas': ['10', '0', 'Nada, porque o programa não compila'],
        'resolucao': 'A passagem é por valor: x é uma cópia de a. Dobrar a cópia não altera a variável do main. '
                     'Para alterar a, o parâmetro precisaria ser uma referência: int &x (Seção 6.6).',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'codigo': '''void troca(int &a, int b) {
    int aux = a;
    a = b;
    b = aux;
}

int main() {
    int x = 1, y = 2;
    troca(x, y);
    cout << x << " " << y;
}''',
        'enunciado': 'O & foi colocado só no primeiro parâmetro. O que o programa mostra?',
        'certa': '2 2',
        'erradas': ['2 1', '1 2', '1 1'],
        'resolucao': 'a é uma referência para x, então a = b muda x para 2. Já b é uma cópia de y: b = aux muda '
                     'só a cópia, e y continua valendo 2. Resultado: x = 2 e y = 2. A troca correta usa & nos '
                     'dois parâmetros.',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'enunciado': 'Um programa chama media(a, b) dentro do main, mas a função media está escrita depois do '
                     'main e não há protótipo. Por que o programa não compila?',
        'certa': 'Porque o compilador lê o arquivo de cima para baixo e, ao chegar na chamada, ainda não conhece '
                 'a função',
        'erradas': [
            'Porque funções só podem ser escritas dentro do main',
            'Porque o main precisa ser sempre a última função do arquivo',
            'Porque media é uma palavra reservada do C++',
        ],
        'resolucao': 'Uma função precisa ser declarada antes de ser chamada. A solução é escrever a função antes '
                     'do main ou declarar só o seu cabeçalho no início, o protótipo: double media(double a, '
                     'double b); (Seção 6.7).',
    },
    {
        'nivel': 'dificil',
        'codigo': '''void linha(int n = 3, char c = '-') {
    for (int i = 0; i < n; i++) cout << c;
    cout << "|";
}

int main() {
    linha();
    linha(2);
    linha(1, '*');
}''',
        'enunciado': 'O que o programa acima mostra?',
        'certa': '---|--|*|',
        'erradas': ['|--|*|', '---|---|*|', 'Nada, porque linha() é chamada sem os argumentos'],
        'resolucao': 'Os parâmetros têm valores padrão, usados quando o argumento é omitido. linha() usa n = 3 e '
                     'c = \'-\'; linha(2) usa n = 2 e o c padrão; linha(1, \'*\') informa os dois. Cada chamada '
                     'termina com uma barra.',
        'executar': True,
    },
]
