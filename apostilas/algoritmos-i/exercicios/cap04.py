"""Exercícios práticos do Capítulo 4 (Estruturas de decisão)."""

CAPITULO = 'alg1-cap4'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Par ou ímpar. Escreva um programa que leia um número inteiro e informe se ele é par ou '
            'ímpar. Teste também com zero e com um número negativo.'
        ),
        'exemplos': [
            ('7', '7 é ímpar'),
            ('10', '10 é par'),
            ('0', '0 é par'),
            ('-3', '-3 é ímpar'),
        ],
        'resolucao': [
            ('p', 'Um número é par quando o resto da divisão por 2 é zero. Testar se o resto é 0 é mais '
                  'seguro do que testar se ele é 1: em C++, o resto de um número negativo é negativo '
                  '(-3 % 2 vale -1), e o teste n % 2 == 1 diria que -3 não é ímpar.'),
            ('Portugol', '''algoritmo "ParOuImpar"
var
   n: inteiro
inicio
   escreva("Número: ")
   leia(n)
   se n mod 2 = 0 entao
      escreval(n, " é par")
   senao
      escreval(n, " é ímpar")
   fimse
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Número: ";
    cin >> n;
    if (n % 2 == 0) {
        cout << n << " é par" << endl;
    } else {
        cout << n << " é ímpar" << endl;
    }
    return 0;
}'''),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'O maior de três. Escreva um programa que leia três números e mostre o maior deles. '
            'Garanta que funciona também quando há números iguais.'
        ),
        'exemplos': [
            ('3\n9\n5', 'Maior: 9'),
            ('7\n7\n2', 'Maior: 7'),
            ('-4\n-1\n-8', 'Maior: -1'),
        ],
        'resolucao': [
            ('p', 'Uma forma simples, que evita muitos ifs aninhados, é supor que o primeiro é o maior e '
                  'depois comparar os outros com ele, trocando quando aparecer um maior. É o mesmo padrão '
                  'do maior valor que o Capítulo 5 usa dentro dos laços.'),
            ('Portugol', '''algoritmo "MaiorDeTres"
var
   a, b, c, maior: real
inicio
   escreva("Três números: ")
   leia(a, b, c)
   maior <- a
   se b > maior entao
      maior <- b
   fimse
   se c > maior entao
      maior <- c
   fimse
   escreval("Maior: ", maior)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    double a, b, c;
    cout << "Três números: ";
    cin >> a >> b >> c;
    double maior = a;
    if (b > maior) maior = b;
    if (c > maior) maior = c;
    cout << "Maior: " << maior << endl;
    return 0;
}'''),
            ('p', 'Os dois ifs são independentes, e não um else if: depois de comparar b, ainda é preciso '
                  'comparar c com o maior encontrado até ali. Com números iguais, nenhuma troca acontece e '
                  'o resultado continua certo.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Classificação do IMC. Leia o peso e a altura, calcule o IMC (peso / altura²) e mostre a '
            'classificação: abaixo de 18.5, "Abaixo do peso"; de 18.5 até menos de 25, "Peso normal"; de '
            '25 até menos de 30, "Sobrepeso"; 30 ou mais, "Obesidade".'
        ),
        'exemplos': [
            ('50\n1.7', 'Abaixo do peso'),
            ('70\n1.75', 'Peso normal'),
            ('85\n1.75', 'Sobrepeso'),
            ('100\n1.7', 'Obesidade'),
        ],
        'resolucao': [
            ('p', 'Faixas consecutivas pedem decisões encadeadas (else if). Como cada teste só é feito '
                  'quando os anteriores falharam, não é preciso repetir o limite de baixo: no segundo '
                  'teste, já se sabe que o IMC é pelo menos 18.5.'),
            ('Portugol', '''algoritmo "ClassificaIMC"
var
   peso, altura, imc: real
inicio
   escreva("Peso e altura: ")
   leia(peso, altura)
   imc <- peso / (altura * altura)
   se imc < 18.5 entao
      escreval("Abaixo do peso")
   senao
      se imc < 25 entao
         escreval("Peso normal")
      senao
         se imc < 30 entao
            escreval("Sobrepeso")
         senao
            escreval("Obesidade")
         fimse
      fimse
   fimse
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    double peso, altura;
    cout << "Peso e altura: ";
    cin >> peso >> altura;
    double imc = peso / (altura * altura);
    if (imc < 18.5) {
        cout << "Abaixo do peso" << endl;
    } else if (imc < 25) {
        cout << "Peso normal" << endl;
    } else if (imc < 30) {
        cout << "Sobrepeso" << endl;
    } else {
        cout << "Obesidade" << endl;
    }
    return 0;
}'''),
            ('p', 'Para testar as fronteiras, use pesos que deem IMC exatamente 25 ou 30 (com altura 2, '
                  'pesos 100 e 120): devem sair "Sobrepeso" e "Obesidade".'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Calculadora. Escreva um programa que leia uma conta no formato número operador número '
            '(por exemplo, 8 / 2) e mostre o resultado. Os operadores válidos são +, -, * e /. Use '
            'switch (escolha, no Portugol). Trate a divisão por zero e o operador inválido.'
        ),
        'exemplos': [
            ('8 / 2', 'Resultado: 4'),
            ('5 * 3', 'Resultado: 15'),
            ('7 / 0', 'Erro: divisão por zero'),
            ('2 ^ 3', 'Operador inválido'),
        ],
        'resolucao': [
            ('p', 'O operador é um único caractere, então pode ser lido em uma variável char e usado no '
                  'switch. O cin >> a >> op >> b lê os três valores separados por espaços. A divisão '
                  'precisa de um if dentro do seu caso, para não dividir por zero.'),
            ('Portugol', '''algoritmo "Calculadora"
var
   a, b: real
   op: caractere
inicio
   escreva("Conta (número operador número): ")
   leia(a, op, b)
   escolha op
   caso "+"
      escreval("Resultado: ", a + b)
   caso "-"
      escreval("Resultado: ", a - b)
   caso "*"
      escreval("Resultado: ", a * b)
   caso "/"
      se b = 0 entao
         escreval("Erro: divisão por zero")
      senao
         escreval("Resultado: ", a / b)
      fimse
   outrocaso
      escreval("Operador inválido")
   fimescolha
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    double a, b;
    char op;
    cout << "Conta (número operador número): ";
    cin >> a >> op >> b;
    switch (op) {
        case '+':
            cout << "Resultado: " << a + b << endl;
            break;
        case '-':
            cout << "Resultado: " << a - b << endl;
            break;
        case '*':
            cout << "Resultado: " << a * b << endl;
            break;
        case '/':
            if (b == 0) {
                cout << "Erro: divisão por zero" << endl;
            } else {
                cout << "Resultado: " << a / b << endl;
            }
            break;
        default:
            cout << "Operador inválido" << endl;
    }
    return 0;
}'''),
            ('p', 'Não esqueça o break no fim de cada caso: sem ele, a execução continua no caso de baixo. '
                  'No VisuAlg, o leia de três valores espera que eles sejam digitados um por linha.'),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Ano bissexto. Um ano é bissexto quando é divisível por 4, mas não por 100, a não ser que '
            'também seja divisível por 400. Por isso 2024 é bissexto, 1900 não é e 2000 é. Escreva um '
            'programa que leia um ano e diga se ele é bissexto, usando uma única condição com os '
            'operadores lógicos.'
        ),
        'exemplos': [
            ('2024', '2024 é bissexto'),
            ('1900', '1900 não é bissexto'),
            ('2000', '2000 é bissexto'),
            ('2023', '2023 não é bissexto'),
        ],
        'resolucao': [
            ('p', 'A regra tem duas formas de um ano ser bissexto: (divisível por 4 E não divisível por 100) '
                  'OU divisível por 400. Os parênteses deixam a intenção clara, mesmo que o && já tenha '
                  'precedência sobre o ||. Os quatro exemplos cobrem cada caminho da regra: o caso comum '
                  '(2024), a exceção dos séculos (1900), a exceção da exceção (2000) e um ano qualquer (2023).'),
            ('Portugol', '''algoritmo "Bissexto"
var
   ano: inteiro
inicio
   escreva("Ano: ")
   leia(ano)
   se ((ano mod 4 = 0) e (ano mod 100 <> 0)) ou (ano mod 400 = 0) entao
      escreval(ano, " é bissexto")
   senao
      escreval(ano, " não é bissexto")
   fimse
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int ano;
    cout << "Ano: ";
    cin >> ano;
    bool bissexto = (ano % 4 == 0 && ano % 100 != 0) || ano % 400 == 0;
    if (bissexto) {
        cout << ano << " é bissexto" << endl;
    } else {
        cout << ano << " não é bissexto" << endl;
    }
    return 0;
}'''),
            ('p', 'Guardar a condição em uma variável bool com um nome que diz o que ela significa deixa o if '
                  'muito mais fácil de ler. Uma versão com ifs aninhados também funciona, mas costuma ter '
                  'mais pontos onde errar.'),
        ],
    },
]
