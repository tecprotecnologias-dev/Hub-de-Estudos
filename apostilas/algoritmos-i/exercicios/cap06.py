"""Exercícios práticos do Capítulo 6 (Funções e procedimentos)."""

CAPITULO = 'alg1-cap6'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Hipotenusa. Escreva uma função hipotenusa que receba os dois catetos de um triângulo '
            'retângulo e devolva a hipotenusa (a raiz quadrada da soma dos quadrados dos catetos). O '
            'programa principal lê os catetos, chama a função e mostra o resultado.'
        ),
        'exemplos': [
            ('3\n4', 'Hipotenusa: 5'),
            ('5\n12', 'Hipotenusa: 13'),
            ('1\n1', 'Hipotenusa: 1.41421'),
        ],
        'resolucao': [
            ('p', 'A função recebe dois valores e devolve um: o tipo de retorno é double, e o cálculo termina '
                  'com return. A raiz quadrada vem da função sqrt, da biblioteca <cmath> (raizq, no '
                  'Portugol). O main só cuida da entrada e da saída.'),
            ('Portugol', '''algoritmo "Hipotenusa"
var
   a, b: real

funcao hipotenusa(c1, c2: real): real
inicio
   retorne raizq(c1 * c1 + c2 * c2)
fimfuncao

inicio
   escreva("Catetos: ")
   leia(a, b)
   escreval("Hipotenusa: ", hipotenusa(a, b))
fimalgoritmo'''),
            ('C++', '''#include <iostream>
#include <cmath>
using namespace std;

double hipotenusa(double c1, double c2) {
    return sqrt(c1 * c1 + c2 * c2);
}

int main() {
    double a, b;
    cout << "Catetos: ";
    cin >> a >> b;
    cout << "Hipotenusa: " << hipotenusa(a, b) << endl;
    return 0;
}'''),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'Moldura. Escreva um procedimento linha(n) que mostre uma linha com n asteriscos, e use-o '
            'para desenhar uma moldura em volta de um título: uma linha de asteriscos, o título entre '
            'asteriscos e outra linha. O programa lê o título (uma palavra) e calcula o tamanho da '
            'moldura.'
        ),
        'exemplos': [
            ('Algoritmos', '**************\n* Algoritmos *\n**************'),
            ('C++', '*******\n* C++ *\n*******'),
        ],
        'resolucao': [
            ('p', 'O procedimento não devolve nada, então é void. O tamanho da linha é o tamanho do título '
                  'mais 4: um asterisco e um espaço de cada lado. Em C++, o tamanho de uma string é dado '
                  'por size() (Capítulo 8 traz mais detalhes); no Portugol, por compr.'),
            ('Portugol', '''algoritmo "Moldura"
var
   titulo: caractere

procedimento linha(n: inteiro)
var
   i: inteiro
inicio
   para i de 1 ate n faca
      escreva("*")
   fimpara
   escreval("")
fimprocedimento

inicio
   escreva("Título: ")
   leia(titulo)
   linha(compr(titulo) + 4)
   escreval("* ", titulo, " *")
   linha(compr(titulo) + 4)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
#include <string>
using namespace std;

void linha(int n) {
    for (int i = 0; i < n; i++) cout << "*";
    cout << endl;
}

int main() {
    string titulo;
    cout << "Título: ";
    cin >> titulo;
    int tamanho = titulo.size() + 4;
    linha(tamanho);
    cout << "* " << titulo << " *" << endl;
    linha(tamanho);
    return 0;
}'''),
            ('p', 'Escrever linha uma vez e chamá-la duas vezes é a principal vantagem dos subprogramas: se a '
                  'moldura mudar de asterisco para outro símbolo, a alteração é feita em um só lugar.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Primos em um intervalo. Escreva uma função ehPrimo(n) que devolva verdadeiro se n é primo, '
            'e use-a para mostrar todos os primos entre dois números a e b lidos do teclado, na mesma '
            'linha, separados por espaço.'
        ),
        'exemplos': [
            ('10\n30', '11 13 17 19 23 29'),
            ('1\n10', '2 3 5 7'),
        ],
        'resolucao': [
            ('p', 'A função recebe um inteiro e devolve um lógico (bool). Ela pode ter vários return: '
                  'assim que um divisor aparece, a resposta já é falso. O main só percorre o intervalo e '
                  'pergunta à função, sem saber como ela decide.'),
            ('Portugol', '''algoritmo "PrimosNoIntervalo"
var
   a, b, n: inteiro

funcao ehPrimo(k: inteiro): logico
var
   d: inteiro
inicio
   se k < 2 entao
      retorne falso
   fimse
   d <- 2
   enquanto d * d <= k faca
      se k mod d = 0 entao
         retorne falso
      fimse
      d <- d + 1
   fimenquanto
   retorne verdadeiro
fimfuncao

inicio
   escreva("Intervalo: ")
   leia(a, b)
   para n de a ate b faca
      se ehPrimo(n) entao
         escreva(n, " ")
      fimse
   fimpara
   escreval("")
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

bool ehPrimo(int n) {
    if (n < 2) return false;
    for (int d = 2; d * d <= n; d++) {
        if (n % d == 0) return false;   // achou um divisor
    }
    return true;
}

int main() {
    int a, b;
    cout << "Intervalo: ";
    cin >> a >> b;
    for (int n = a; n <= b; n++) {
        if (ehPrimo(n)) cout << n << " ";
    }
    cout << endl;
    return 0;
}'''),
            ('p', 'O teste d * d <= n é o da Seção 5.8: se n tiver um divisor, terá um menor ou igual à sua '
                  'raiz quadrada.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Ordenar três números. Escreva um procedimento ordenar3 que receba três variáveis inteiras '
            'por referência e as deixe em ordem crescente. O programa principal lê os três números, '
            'chama o procedimento e mostra as variáveis.'
        ),
        'exemplos': [
            ('9\n2\n5', '2 5 9'),
            ('1\n2\n3', '1 2 3'),
            ('7\n7\n1', '1 7 7'),
        ],
        'resolucao': [
            ('p', 'O procedimento precisa alterar as variáveis de quem chama, então os parâmetros são por '
                  'referência (& em C++, var no Portugol). Com uma função auxiliar troca, também por '
                  'referência, bastam três comparações: depois das duas primeiras, o menor está em a; a '
                  'terceira coloca b e c em ordem.'),
            ('Portugol', '''algoritmo "Ordenar3"
var
   x, y, z: inteiro

procedimento troca(var a, b: inteiro)
var
   aux: inteiro
inicio
   aux <- a
   a <- b
   b <- aux
fimprocedimento

procedimento ordenar3(var a, b, c: inteiro)
inicio
   se a > b entao
      troca(a, b)
   fimse
   se a > c entao
      troca(a, c)
   fimse
   se b > c entao
      troca(b, c)
   fimse
fimprocedimento

inicio
   escreva("Três números: ")
   leia(x, y, z)
   ordenar3(x, y, z)
   escreval(x, " ", y, " ", z)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

void troca(int &a, int &b) {
    int aux = a;
    a = b;
    b = aux;
}

void ordenar3(int &a, int &b, int &c) {
    if (a > b) troca(a, b);
    if (a > c) troca(a, c);   // agora a é o menor
    if (b > c) troca(b, c);
}

int main() {
    int x, y, z;
    cout << "Três números: ";
    cin >> x >> y >> z;
    ordenar3(x, y, z);
    cout << x << " " << y << " " << z << endl;
    return 0;
}'''),
            ('p', 'Faça o teste sem o &: o programa compila, mas mostra os números na ordem original, porque '
                  'o procedimento passa a ordenar apenas cópias (Seção 6.6).'),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Simplificar frações. Escreva uma função mdc(a, b) que devolva o máximo divisor comum de dois '
            'inteiros positivos e um procedimento simplificar que receba numerador e denominador por '
            'referência e os divida pelo MDC. O programa lê uma fração e mostra a forma simplificada no '
            'formato numerador/denominador.'
        ),
        'exemplos': [
            ('18\n24', '18/24 = 3/4'),
            ('7\n13', '7/13 = 7/13'),
            ('10\n5', '10/5 = 2/1'),
        ],
        'resolucao': [
            ('p', 'O MDC pode ser calculado pelo algoritmo de Euclides: enquanto b não for zero, o par '
                  '(a, b) é trocado por (b, resto de a por b); quando b chega a zero, a é o MDC. Com 18 e '
                  '24: (18, 24) → (24, 18) → (18, 6) → (6, 0), e o MDC é 6. Dividindo os dois termos por 6, '
                  'a fração 18/24 vira 3/4.'),
            ('Portugol', '''algoritmo "Simplificar"
var
   num, den, n0, d0: inteiro

funcao mdc(a, b: inteiro): inteiro
var
   r: inteiro
inicio
   enquanto b <> 0 faca
      r <- a mod b
      a <- b
      b <- r
   fimenquanto
   retorne a
fimfuncao

procedimento simplificar(var n, d: inteiro)
var
   m: inteiro
inicio
   m <- mdc(n, d)
   n <- n div m
   d <- d div m
fimprocedimento

inicio
   escreva("Numerador e denominador: ")
   leia(num, den)
   n0 <- num
   d0 <- den
   simplificar(num, den)
   escreval(n0, "/", d0, " = ", num, "/", den)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int mdc(int a, int b) {
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

void simplificar(int &num, int &den) {
    int m = mdc(num, den);
    num /= m;
    den /= m;
}

int main() {
    int num, den;
    cout << "Numerador e denominador: ";
    cin >> num >> den;
    int n0 = num, d0 = den;    // guarda a fração original
    simplificar(num, den);
    cout << n0 << "/" << d0 << " = " << num << "/" << den << endl;
    return 0;
}'''),
            ('p', 'Dentro de mdc, a e b são cópias (passagem por valor), e por isso podem ser alterados à '
                  'vontade sem afetar quem chamou. Já simplificar precisa mudar as variáveis do main, e por '
                  'isso usa referência. Como num e den são alterados, o main guarda a fração original antes '
                  'de chamar o procedimento. No Capítulo 9, o mesmo mdc aparece em versão recursiva.'),
        ],
    },
]
