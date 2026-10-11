"""Exercícios práticos do Capítulo 3 (Variáveis, tipos e operadores)."""

CAPITULO = 'alg1-cap3'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Duração de um filme. Escreva um programa que leia a duração de um filme em minutos (um '
            'número inteiro) e mostre essa duração em horas e minutos. Use a divisão inteira e o resto.'
        ),
        'exemplos': [
            ('135', '2 h 15 min'),
            ('90', '1 h 30 min'),
            ('45', '0 h 45 min'),
        ],
        'resolucao': [
            ('p', 'As horas são quantas vezes 60 cabe na duração: a divisão inteira, 135 / 60 = 2. Os '
                  'minutos que sobram são o resto dessa divisão: 135 % 60 = 15. Em C++, como os dois lados '
                  'são inteiros, o / já faz a divisão inteira; no Portugol, ela se escreve div, e o resto, '
                  'mod.'),
            ('Portugol', '''algoritmo "DuracaoFilme"
var
   total, horas, minutos: inteiro
inicio
   escreva("Duração em minutos: ")
   leia(total)
   horas <- total div 60
   minutos <- total mod 60
   escreval(horas, " h ", minutos, " min")
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int total;
    cout << "Duração em minutos: ";
    cin >> total;
    int horas = total / 60;       // divisão inteira
    int minutos = total % 60;     // o que sobra
    cout << horas << " h " << minutos << " min" << endl;
    return 0;
}'''),
            ('p', 'Para conferir: horas × 60 + minutos precisa dar a duração original. Com 135: 2 × 60 + 15 '
                  '= 135.'),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'Índice de massa corporal. Escreva um programa que leia o peso (em kg) e a altura (em metros) '
            'de uma pessoa e mostre o IMC, calculado como peso dividido pela altura ao quadrado.'
        ),
        'exemplos': [
            ('70\n1.75', 'IMC: 22.8571'),
            ('50\n1.6', 'IMC: 19.5312'),
        ],
        'resolucao': [
            ('p', 'Os dois valores e o resultado têm casas decimais, então o tipo é double (real). O cuidado '
                  'está na precedência: peso / altura * altura divide pela altura e depois multiplica de '
                  'novo, o que dá o próprio peso. São necessários parênteses no denominador.'),
            ('Portugol', '''algoritmo "IMC"
var
   peso, altura, imc: real
inicio
   escreva("Peso (kg): ")
   leia(peso)
   escreva("Altura (m): ")
   leia(altura)
   imc <- peso / (altura * altura)
   escreval("IMC: ", imc)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    double peso, altura;
    cout << "Peso (kg): ";
    cin >> peso;
    cout << "Altura (m): ";
    cin >> altura;
    double imc = peso / (altura * altura);
    cout << "IMC: " << imc << endl;
    return 0;
}'''),
            ('p', 'O cout mostra até 6 algarismos significativos, por isso aparece 22.8571. O VisuAlg mostra '
                  'o número de outro jeito, com mais ou menos casas, mas o valor é o mesmo.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Os dígitos de um número. Escreva um programa que leia um número inteiro de três dígitos '
            '(de 100 a 999) e mostre, em linhas separadas, o dígito das centenas, o das dezenas, o das '
            'unidades e o número com os dígitos invertidos. Use apenas operações aritméticas.'
        ),
        'exemplos': [
            ('472', 'Centenas: 4\nDezenas: 7\nUnidades: 2\nInvertido: 274'),
            ('305', 'Centenas: 3\nDezenas: 0\nUnidades: 5\nInvertido: 503'),
        ],
        'resolucao': [
            ('p', 'O resto da divisão por 10 é sempre o último dígito: 472 % 10 = 2. A divisão inteira por '
                  '10 tira o último dígito: 472 / 10 = 47. Combinando as duas: as centenas são 472 / 100 = '
                  '4; as dezenas são (472 / 10) % 10 = 7; e as unidades, 472 % 10 = 2. O número invertido '
                  'é montado com as unidades valendo 100, as dezenas 10 e as centenas 1.'),
            ('Portugol', '''algoritmo "Digitos"
var
   n, c, d, u: inteiro
inicio
   escreva("Número de três dígitos: ")
   leia(n)
   c <- n div 100
   d <- (n div 10) mod 10
   u <- n mod 10
   escreval("Centenas: ", c)
   escreval("Dezenas: ", d)
   escreval("Unidades: ", u)
   escreval("Invertido: ", u * 100 + d * 10 + c)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Número de três dígitos: ";
    cin >> n;
    int c = n / 100;
    int d = (n / 10) % 10;
    int u = n % 10;
    cout << "Centenas: " << c << endl;
    cout << "Dezenas: " << d << endl;
    cout << "Unidades: " << u << endl;
    cout << "Invertido: " << u * 100 + d * 10 + c << endl;
    return 0;
}'''),
            ('p', 'Com 120, o invertido seria 0 × 100 + 2 × 10 + 1 = 21: o zero à esquerda some, como '
                  'acontece com qualquer número inteiro.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Divisão inteira e divisão real. Escreva um programa que leia dois números inteiros, a e b '
            '(com b diferente de zero), e mostre: o quociente da divisão inteira, o resto e o resultado '
            'da divisão real. As três contas devem usar as mesmas variáveis inteiras a e b.'
        ),
        'exemplos': [
            ('7\n2', 'Quociente: 3\nResto: 1\nDivisão real: 3.5'),
            ('20\n8', 'Quociente: 2\nResto: 4\nDivisão real: 2.5'),
        ],
        'resolucao': [
            ('p', 'Em C++, a / b com dois inteiros descarta a parte decimal. Para obter a divisão real '
                  'sem mudar o tipo das variáveis, basta converter um dos lados para double antes de '
                  'dividir: static_cast<double>(a) / b (Seção 3.3). Se a conversão viesse depois, como em '
                  'static_cast<double>(a / b), a divisão inteira já teria acontecido, e o resultado seria 3.'),
            ('Portugol', '''algoritmo "Divisoes"
var
   a, b: inteiro
inicio
   escreva("a: ")
   leia(a)
   escreva("b: ")
   leia(b)
   escreval("Quociente: ", a div b)
   escreval("Resto: ", a mod b)
   escreval("Divisão real: ", a / b)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "a: ";
    cin >> a;
    cout << "b: ";
    cin >> b;
    cout << "Quociente: " << a / b << endl;
    cout << "Resto: " << a % b << endl;
    cout << "Divisão real: " << static_cast<double>(a) / b
         << endl;
    return 0;
}'''),
            ('p', 'No Portugol do VisuAlg a situação é a inversa do C++: / é sempre a divisão real, e a '
                  'inteira tem um operador próprio, div.'),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Caixa eletrônico. Um caixa tem notas de 100, 50, 20, 10, 5 e 2 reais e moedas de 1 real. '
            'Escreva um programa que leia um valor inteiro de saque e mostre quantas notas (e moedas) de '
            'cada valor devem ser entregues, usando sempre a maior nota possível.'
        ),
        'exemplos': [
            ('388', 'Notas de 100: 3\nNotas de 50: 1\nNotas de 20: 1\nNotas de 10: 1\n'
                    'Notas de 5: 1\nNotas de 2: 1\nMoedas de 1: 1'),
            ('90', 'Notas de 100: 0\nNotas de 50: 1\nNotas de 20: 2\nNotas de 10: 0\n'
                   'Notas de 5: 0\nNotas de 2: 0\nMoedas de 1: 0'),
        ],
        'resolucao': [
            ('p', 'Para cada nota, da maior para a menor: a quantidade é a divisão inteira do valor que '
                  'falta pagar pela nota, e o que continua faltando é o resto dessa divisão. Com 388: '
                  '388 / 100 = 3 notas, sobram 388 % 100 = 88; 88 / 50 = 1, sobram 38; 38 / 20 = 1, '
                  'sobram 18; e assim por diante.'),
            ('Portugol', '''algoritmo "CaixaEletronico"
var
   resto: inteiro
inicio
   escreva("Valor do saque: ")
   leia(resto)
   escreval("Notas de 100: ", resto div 100)
   resto <- resto mod 100
   escreval("Notas de 50: ", resto div 50)
   resto <- resto mod 50
   escreval("Notas de 20: ", resto div 20)
   resto <- resto mod 20
   escreval("Notas de 10: ", resto div 10)
   resto <- resto mod 10
   escreval("Notas de 5: ", resto div 5)
   resto <- resto mod 5
   escreval("Notas de 2: ", resto div 2)
   resto <- resto mod 2
   escreval("Moedas de 1: ", resto)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int resto;
    cout << "Valor do saque: ";
    cin >> resto;
    cout << "Notas de 100: " << resto / 100 << endl;
    resto %= 100;
    cout << "Notas de 50: " << resto / 50 << endl;
    resto %= 50;
    cout << "Notas de 20: " << resto / 20 << endl;
    resto %= 20;
    cout << "Notas de 10: " << resto / 10 << endl;
    resto %= 10;
    cout << "Notas de 5: " << resto / 5 << endl;
    resto %= 5;
    cout << "Notas de 2: " << resto / 2 << endl;
    resto %= 2;
    cout << "Moedas de 1: " << resto << endl;
    return 0;
}'''),
            ('p', 'O operador resto %= 100 é a forma curta de resto = resto % 100 (Seção 3.3). O código '
                  'repete o mesmo par de linhas para cada nota; no Capítulo 7, com um vetor guardando os '
                  'valores das notas, ele vira um laço de poucas linhas.'),
        ],
    },
]
