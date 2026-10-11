"""Questões objetivas do Capítulo 2 (Linguagens de programação)."""

CAPITULO = 'alg1-cap2'

QUESTOES = [
    {
        'nivel': 'facil',
        'enunciado': 'Qual é a diferença entre compilar e interpretar um programa?',
        'certa': 'O compilador traduz o programa inteiro antes de executá-lo, gerando um executável; o '
                 'interpretador traduz e executa o programa aos poucos, durante a execução',
        'erradas': [
            'O compilador executa o programa linha por linha; o interpretador gera um arquivo executável',
            'Não há diferença: compilador e interpretador são dois nomes para a mesma ferramenta',
            'O compilador só encontra erros de lógica; o interpretador só encontra erros de sintaxe',
        ],
        'resolucao': 'C++ é uma linguagem compilada: o g++ gera um executável, que depois roda sem precisar do '
                     'compilador. Python e JavaScript costumam ser interpretados (Seção 2.3).',
    },
    {
        'nivel': 'facil',
        'codigo': 'cout << "A" << 1 + 2 << "B" << endl;',
        'enunciado': 'O que o comando acima mostra na tela?',
        'certa': 'A3B',
        'erradas': ['A1+2B', 'A12B', 'A 3 B'],
        'resolucao': 'O que está entre aspas é mostrado como texto; 1 + 2 fora das aspas é uma conta, e o cout '
                     'mostra o resultado, 3. O cout não acrescenta espaços: só aparecem os que estão dentro '
                     'das aspas.',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'codigo': '''#include <iostream>
using namespace std;

int main() {
    cout << "Oi" << endl
    return 0;
}''',
        'enunciado': 'O programa acima esqueceu o ponto e vírgula no fim do cout. O que acontece ao compilar?',
        'certa': 'O compilador aponta um erro de sintaxe e não gera o executável',
        'erradas': [
            'O programa compila e mostra Oi, porque o ponto e vírgula é opcional antes do return',
            'O programa compila, mas trava ao chegar nessa linha',
            'O compilador acrescenta o ponto e vírgula sozinho e só mostra um aviso',
        ],
        'resolucao': 'Faltar o ponto e vírgula é um erro de sintaxe: o programa não segue as regras de escrita '
                     'da linguagem, e o compilador se recusa a continuar. A mensagem costuma apontar a linha '
                     'seguinte ("expected \';\' before \'return\'"), porque é ali que ele percebe o problema.',
    },
    {
        'nivel': 'medio',
        'codigo': '''int a = 7, b = 2;
cout << a / b;''',
        'enunciado': 'O que o trecho acima mostra?',
        'certa': '3',
        'erradas': ['3.5', '4', '3.0'],
        'resolucao': 'Em C++, a divisão entre dois inteiros descarta a parte decimal, sem arredondar: 7 / 2 vale '
                     '3. Não é um erro para o compilador, e sim o significado (a semântica) da divisão inteira. '
                     'Para obter 3.5, um dos lados precisa ser real, como em a / 2.0.',
        'executar': True,
    },
    {
        'nivel': 'dificil',
        'enunciado': 'Na compilação de um programa C++, qual é o papel do ligador (linker)?',
        'certa': 'Juntar o código-objeto com o código das bibliotecas usadas, como a do cout, e gerar o '
                 'executável',
        'erradas': [
            'Tratar as linhas que começam com #, como o #include',
            'Verificar a sintaxe e traduzir o código para linguagem de máquina',
            'Executar o programa e mostrar as mensagens de erro de execução',
        ],
        'resolucao': 'As três etapas são: o pré-processador trata as linhas com #; o compilador verifica a '
                     'sintaxe e gera o código-objeto; e o ligador junta esse código com as bibliotecas e gera '
                     'o executável. Um erro como "undefined reference" vem do ligador, e não do compilador.',
    },
]
