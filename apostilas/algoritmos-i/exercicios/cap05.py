"""Exercícios práticos do Capítulo 5 (Estruturas de repetição)."""

CAPITULO = 'alg1-cap5'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Soma de 1 até N. Escreva um programa que leia um número inteiro positivo N e mostre a soma '
            'de todos os inteiros de 1 até N, usando um laço.'
        ),
        'exemplos': [
            ('10', 'Soma: 55'),
            ('100', 'Soma: 5050'),
            ('1', 'Soma: 1'),
        ],
        'resolucao': [
            ('p', 'É o padrão do acumulador (Seção 5.4): uma variável começa em 0 e, a cada volta, recebe o '
                  'valor do contador. Como o número de voltas é conhecido (N), o laço mais claro é o for '
                  '(para, no Portugol).'),
            ('Portugol', '''algoritmo "SomaAteN"
var
   n, i, soma: inteiro
inicio
   escreva("N: ")
   leia(n)
   soma <- 0
   para i de 1 ate n faca
      soma <- soma + i
   fimpara
   escreval("Soma: ", soma)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "N: ";
    cin >> n;
    int soma = 0;
    for (int i = 1; i <= n; i++) {
        soma += i;
    }
    cout << "Soma: " << soma << endl;
    return 0;
}'''),
            ('p', 'Para conferir, existe uma fórmula: a soma de 1 até N é N × (N + 1) / 2. Com N = 100, '
                  '100 × 101 / 2 = 5050. O laço é o objetivo do exercício, mas a fórmula é um ótimo teste.'),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'Tabuada. Escreva um programa que leia um número e mostre a sua tabuada de 1 a 10, uma '
            'linha por multiplicação, no formato "7 x 3 = 21".'
        ),
        'exemplos': [
            ('7', '7 x 1 = 7\n7 x 2 = 14\n7 x 10 = 70'),
            ('9', '9 x 1 = 9\n9 x 9 = 81\n9 x 10 = 90'),
        ],
        'resolucao': [
            ('p', 'Um laço com contador de 1 a 10, em que cada volta mostra uma linha. Os exemplos mostram só '
                  'algumas das dez linhas: confira as outras no seu programa.'),
            ('Portugol', '''algoritmo "Tabuada"
var
   n, i: inteiro
inicio
   escreva("Tabuada do: ")
   leia(n)
   para i de 1 ate 10 faca
      escreval(n, " x ", i, " = ", n * i)
   fimpara
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Tabuada do: ";
    cin >> n;
    for (int i = 1; i <= 10; i++) {
        cout << n << " x " << i << " = " << n * i << endl;
    }
    return 0;
}'''),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Notas até a sentinela. Escreva um programa que leia notas até o usuário digitar -1. No '
            'fim, mostre a média das notas e quantas foram de aprovação (6 ou mais). Se nenhuma nota '
            'for digitada, mostre "Nenhuma nota".'
        ),
        'exemplos': [
            ('7\n4\n9\n6\n-1', 'Média: 6.5\nAprovados: 3'),
            ('5.5\n8\n-1', 'Média: 6.75\nAprovados: 1'),
            ('-1', 'Nenhuma nota'),
        ],
        'resolucao': [
            ('p', 'Como não se sabe quantas notas virão, o laço é um while com sentinela (Seção 5.1). A '
                  'leitura fica antes do laço e no fim do bloco, para que o -1 nunca entre nas contas. Um '
                  'acumulador soma as notas, um contador conta todas e outro conta só as aprovadas.'),
            ('Portugol', '''algoritmo "NotasSentinela"
var
   nota, soma: real
   quantas, aprovados: inteiro
inicio
   soma <- 0
   quantas <- 0
   aprovados <- 0
   escreva("Notas (-1 para terminar): ")
   leia(nota)
   enquanto nota <> -1 faca
      soma <- soma + nota
      quantas <- quantas + 1
      se nota >= 6 entao
         aprovados <- aprovados + 1
      fimse
      leia(nota)
   fimenquanto
   se quantas > 0 entao
      escreval("Média: ", soma / quantas)
      escreval("Aprovados: ", aprovados)
   senao
      escreval("Nenhuma nota")
   fimse
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    double nota, soma = 0;
    int quantas = 0, aprovados = 0;
    cout << "Notas (-1 para terminar): ";
    while (cin >> nota && nota != -1) {
        soma += nota;
        quantas++;
        if (nota >= 6) aprovados++;
    }
    if (quantas > 0) {
        cout << "Média: " << soma / quantas << endl;
        cout << "Aprovados: " << aprovados << endl;
    } else {
        cout << "Nenhuma nota" << endl;
    }
    return 0;
}'''),
            ('p', 'O if (quantas > 0) evita dividir por zero quando o primeiro valor já é a sentinela. Em '
                  'C++, ler dentro da condição do while também faz o laço parar se a entrada acabar sem o '
                  '-1.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Senha com tentativas. A senha de um cofre é 1234. Escreva um programa que peça a senha até o '
            'usuário acertar, com no máximo 3 tentativas. Se acertar, mostre "Acesso liberado"; se errar '
            'as três, mostre "Cofre bloqueado".'
        ),
        'exemplos': [
            ('1234', 'Acesso liberado'),
            ('1111\n1234', 'Senha incorreta\nAcesso liberado'),
            ('1\n2\n3', 'Cofre bloqueado'),
        ],
        'resolucao': [
            ('p', 'A senha precisa ser pedida pelo menos uma vez, então o do-while (repita, no Portugol) é '
                  'natural. O laço tem duas condições de parada: acertar ou esgotar as tentativas. Depois '
                  'do laço, é preciso descobrir qual das duas aconteceu, comparando de novo a última senha.'),
            ('Portugol', '''algoritmo "Cofre"
var
   senha, tentativas: inteiro
inicio
   tentativas <- 0
   repita
      escreva("Senha: ")
      leia(senha)
      tentativas <- tentativas + 1
      se senha <> 1234 entao
         escreval("Senha incorreta")
      fimse
   ate (senha = 1234) ou (tentativas = 3)
   se senha = 1234 entao
      escreval("Acesso liberado")
   senao
      escreval("Cofre bloqueado")
   fimse
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    const int SENHA = 1234;
    int senha = 0, tentativas = 0;
    do {
        cout << "Senha: ";
        cin >> senha;
        tentativas++;
        if (senha != SENHA) cout << "Senha incorreta" << endl;
    } while (senha != SENHA && tentativas < 3);
    if (senha == SENHA) {
        cout << "Acesso liberado" << endl;
    } else {
        cout << "Cofre bloqueado" << endl;
    }
    return 0;
}'''),
            ('p', 'Compare as condições: o do-while continua enquanto a senha está errada E ainda há '
                  'tentativas; o repita do Portugol para quando a senha está certa OU as tentativas '
                  'acabaram. Uma é a negação da outra (Seção 5.2).'),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Fatoração em primos. Todo inteiro maior que 1 pode ser escrito como um produto de números '
            'primos: 360 = 2 x 2 x 2 x 3 x 3 x 5. Escreva um programa que leia um inteiro maior que 1 e '
            'mostre a sua fatoração nesse formato.'
        ),
        'exemplos': [
            ('360', '360 = 2 x 2 x 2 x 3 x 3 x 5'),
            ('97', '97 = 97'),
            ('1024', '1024 = 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2'),
        ],
        'resolucao': [
            ('p', 'A ideia é tentar dividir o número pelos candidatos d = 2, 3, 4...: enquanto d dividir o '
                  'número, d é um fator, e o número é dividido por ele. Quando d não divide mais, passa-se '
                  'ao próximo. Não é preciso testar se d é primo: quando chegar a vez do 4, todos os fatores '
                  '2 já foram retirados, e o 4 não divide mais nada. São dois laços aninhados: o de fora '
                  'avança o candidato, o de dentro retira o mesmo fator várias vezes.'),
            ('Portugol', '''algoritmo "Fatoracao"
var
   n, resto, d: inteiro
   primeiro: logico
inicio
   escreva("Número: ")
   leia(n)
   escreva(n, " = ")
   resto <- n
   d <- 2
   primeiro <- verdadeiro
   enquanto resto > 1 faca
      enquanto resto mod d = 0 faca
         se nao primeiro entao
            escreva(" x ")
         fimse
         escreva(d)
         primeiro <- falso
         resto <- resto div d
      fimenquanto
      d <- d + 1
   fimenquanto
   escreval("")
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Número: ";
    cin >> n;
    cout << n << " = ";
    int resto = n;
    bool primeiro = true;
    for (int d = 2; resto > 1; d++) {
        while (resto % d == 0) {
            if (!primeiro) cout << " x ";
            cout << d;
            primeiro = false;
            resto /= d;
        }
    }
    cout << endl;
    return 0;
}'''),
            ('p', 'A variável primeiro controla o separador: o " x " vai antes de cada fator, menos do '
                  'primeiro. É um truque muito comum para mostrar listas sem um separador sobrando no fim. '
                  'Com um número primo, como 97, o laço de fora vai até o próprio 97, que divide uma vez.'),
        ],
    },
]
