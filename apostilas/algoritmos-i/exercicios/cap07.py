"""Exercícios práticos do Capítulo 7 (Vetores e matrizes)."""

CAPITULO = 'alg1-cap7'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Ordem inversa. Escreva um programa que leia 5 números inteiros, guarde-os em um vetor e '
            'mostre-os na ordem inversa da leitura, na mesma linha.'
        ),
        'exemplos': [
            ('1\n2\n3\n4\n5', '5 4 3 2 1'),
            ('10\n-3\n7\n0\n8', '8 0 7 -3 10'),
        ],
        'resolucao': [
            ('p', 'Sem um vetor, seria preciso guardar cada número em uma variável separada. Com ele, um laço '
                  'lê do índice 0 ao 4 e outro mostra do 4 ao 0. No Portugol, com o vetor de 1 a 5, os '
                  'laços vão de 1 a 5 e de 5 a 1 (passo -1).'),
            ('Portugol', '''algoritmo "OrdemInversa"
var
   v: vetor[1..5] de inteiro
   i: inteiro
inicio
   para i de 1 ate 5 faca
      escreva("Número ", i, ": ")
      leia(v[i])
   fimpara
   para i de 5 ate 1 passo -1 faca
      escreva(v[i], " ")
   fimpara
   escreval("")
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int v[5];
    for (int i = 0; i < 5; i++) {
        cout << "Número " << i + 1 << ": ";
        cin >> v[i];
    }
    for (int i = 4; i >= 0; i--) {
        cout << v[i] << " ";
    }
    cout << endl;
    return 0;
}'''),
            ('p', 'O segundo laço começa em 4, e não em 5: em um vetor de 5 elementos, o último índice é '
                  'tamanho - 1 (Seção 7.1).'),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'Maior e menor. Escreva um programa que leia a quantidade N de valores (até 50) e depois os N '
            'valores, e mostre o maior e o menor, cada um com a sua posição na leitura (contando a partir '
            'de 1).'
        ),
        'exemplos': [
            ('5\n7\n3\n9\n2\n8', 'Maior: 9 (posição 3)\nMenor: 2 (posição 4)'),
            ('3\n-1\n-5\n-2', 'Maior: -1 (posição 1)\nMenor: -5 (posição 2)'),
        ],
        'resolucao': [
            ('p', 'Em vez de guardar o maior valor, guarde o índice dele (Seção 7.4): com o índice, o valor '
                  'é v[iMaior], e a posição para o usuário é iMaior + 1. Começar pelo primeiro elemento '
                  'funciona com qualquer valor, inclusive negativos.'),
            ('Portugol', '''algoritmo "MaiorMenor"
var
   v: vetor[1..50] de real
   n, i, iMaior, iMenor: inteiro
inicio
   escreva("Quantos valores (até 50)? ")
   leia(n)
   para i de 1 ate n faca
      leia(v[i])
   fimpara
   iMaior <- 1
   iMenor <- 1
   para i de 2 ate n faca
      se v[i] > v[iMaior] entao
         iMaior <- i
      fimse
      se v[i] < v[iMenor] entao
         iMenor <- i
      fimse
   fimpara
   escreval("Maior: ", v[iMaior], " (posição ", iMaior, ")")
   escreval("Menor: ", v[iMenor], " (posição ", iMenor, ")")
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    const int MAX = 50;
    double v[MAX] = {};
    int n;
    cout << "Quantos valores (até 50)? ";
    cin >> n;
    if (n < 1 || n > MAX) {
        cout << "Quantidade inválida" << endl;
        return 0;
    }
    for (int i = 0; i < n; i++) cin >> v[i];
    int iMaior = 0, iMenor = 0;
    for (int i = 1; i < n; i++) {
        if (v[i] > v[iMaior]) iMaior = i;
        if (v[i] < v[iMenor]) iMenor = i;
    }
    cout << "Maior: " << v[iMaior] << " (posição " << iMaior + 1
         << ")" << endl;
    cout << "Menor: " << v[iMenor] << " (posição " << iMenor + 1
         << ")" << endl;
    return 0;
}'''),
            ('p', 'O if que confere n protege o vetor: com n maior que 50, a leitura escreveria fora dele '
                  '(Seção 7.3).'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Acima da média. Leia N (até 50) e depois N números. Mostre a média e quantos números ficaram '
            'acima dela. Por que este exercício precisa de um vetor, e o de somar notas do Capítulo 5 '
            'não precisava?'
        ),
        'exemplos': [
            ('6\n4\n8\n6\n10\n2\n6', 'Média: 6\nAcima da média: 2'),
            ('4\n5\n5\n5\n5', 'Média: 5\nAcima da média: 0'),
        ],
        'resolucao': [
            ('p', 'A média só é conhecida depois de ler todos os números, e só então é possível comparar cada '
                  'um com ela. Por isso os números precisam ficar guardados: são dois laços, um para ler e '
                  'somar, outro para contar. No Capítulo 5, cada nota podia ser somada e esquecida.'),
            ('Portugol', '''algoritmo "AcimaDaMedia"
var
   v: vetor[1..50] de real
   n, i, acima: inteiro
   soma, media: real
inicio
   leia(n)
   soma <- 0
   para i de 1 ate n faca
      leia(v[i])
      soma <- soma + v[i]
   fimpara
   media <- soma / n
   acima <- 0
   para i de 1 ate n faca
      se v[i] > media entao
         acima <- acima + 1
      fimse
   fimpara
   escreval("Média: ", media)
   escreval("Acima da média: ", acima)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    const int MAX = 50;
    double v[MAX] = {};
    int n;
    cin >> n;
    if (n < 1 || n > MAX) return 0;
    double soma = 0;
    for (int i = 0; i < n; i++) {
        cin >> v[i];
        soma += v[i];
    }
    double media = soma / n;
    int acima = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > media) acima++;
    }
    cout << "Média: " << media << endl;
    cout << "Acima da média: " << acima << endl;
    return 0;
}'''),
            ('p', 'O segundo exemplo testa o caso em que todos os valores são iguais à média: como a condição '
                  'é estritamente maior (>), nenhum conta.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Somas de uma matriz. Leia uma matriz 3 × 3 de inteiros, linha por linha, e mostre a soma de '
            'cada linha, a soma de cada coluna e a soma da diagonal principal.'
        ),
        'exemplos': [
            ('1 2 3\n4 5 6\n7 8 9',
             'Linha 1: 6\nLinha 2: 15\nLinha 3: 24\nColuna 1: 12\nColuna 2: 15\nColuna 3: 18\nDiagonal: 15'),
            ('2 0 0\n0 2 0\n0 0 2',
             'Linha 1: 2\nColuna 3: 2\nDiagonal: 6'),
        ],
        'resolucao': [
            ('p', 'A soma de uma linha fixa a linha i e varia a coluna j; a de uma coluna faz o contrário '
                  '(Seção 7.6). A diagonal principal é formada pelos elementos em que a linha e a coluna '
                  'são iguais, m[0][0], m[1][1], m[2][2], e precisa de um laço só.'),
            ('Portugol', '''algoritmo "SomasMatriz"
var
   m: vetor[1..3, 1..3] de inteiro
   i, j, soma: inteiro
inicio
   para i de 1 ate 3 faca
      para j de 1 ate 3 faca
         leia(m[i, j])
      fimpara
   fimpara
   para i de 1 ate 3 faca
      soma <- 0
      para j de 1 ate 3 faca
         soma <- soma + m[i, j]
      fimpara
      escreval("Linha ", i, ": ", soma)
   fimpara
   para j de 1 ate 3 faca
      soma <- 0
      para i de 1 ate 3 faca
         soma <- soma + m[i, j]
      fimpara
      escreval("Coluna ", j, ": ", soma)
   fimpara
   soma <- 0
   para i de 1 ate 3 faca
      soma <- soma + m[i, i]
   fimpara
   escreval("Diagonal: ", soma)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int m[3][3];
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            cin >> m[i][j];
    for (int i = 0; i < 3; i++) {
        int soma = 0;
        for (int j = 0; j < 3; j++) soma += m[i][j];
        cout << "Linha " << i + 1 << ": " << soma << endl;
    }
    for (int j = 0; j < 3; j++) {
        int soma = 0;
        for (int i = 0; i < 3; i++) soma += m[i][j];
        cout << "Coluna " << j + 1 << ": " << soma << endl;
    }
    int diagonal = 0;
    for (int i = 0; i < 3; i++) diagonal += m[i][i];
    cout << "Diagonal: " << diagonal << endl;
    return 0;
}'''),
            ('p', 'Para a diagonal secundária (de cima à direita até embaixo à esquerda), o elemento da linha '
                  'i é m[i][2 - i]: a linha e a coluna somam 2.'),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Sem repetidos. Leia N (até 50) e N números inteiros, e mostre os números sem repetições, na '
            'ordem em que apareceram pela primeira vez. Use um segundo vetor para guardar os números já '
            'vistos.'
        ),
        'exemplos': [
            ('8\n3 1 3 2 1 5 2 3', '3 1 2 5'),
            ('4\n7 7 7 7', '7'),
            ('3\n1 2 3', '1 2 3'),
        ],
        'resolucao': [
            ('p', 'Para cada número lido, procure-o no vetor dos já vistos (uma busca sequencial, que o '
                  'Capítulo 10 aprofunda). Se não estiver lá, ele é novo: acrescente-o no fim desse vetor. '
                  'O vetor dos vistos tem o seu próprio contador, porque fica menor que o original sempre '
                  'que há repetições.'),
            ('Portugol', '''algoritmo "SemRepetidos"
var
   unicos: vetor[1..50] de inteiro
   n, i, j, x, total: inteiro
   achou: logico
inicio
   leia(n)
   total <- 0
   para i de 1 ate n faca
      leia(x)
      achou <- falso
      para j de 1 ate total faca
         se unicos[j] = x entao
            achou <- verdadeiro
         fimse
      fimpara
      se nao achou entao
         total <- total + 1
         unicos[total] <- x
      fimse
   fimpara
   para i de 1 ate total faca
      escreva(unicos[i], " ")
   fimpara
   escreval("")
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    const int MAX = 50;
    int unicos[MAX];
    int n, total = 0;
    cin >> n;
    if (n < 1 || n > MAX) return 0;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        bool achou = false;
        for (int j = 0; j < total; j++) {
            if (unicos[j] == x) {
                achou = true;
                break;
            }
        }
        if (!achou) {
            unicos[total] = x;     // novo: vai para o fim
            total++;
        }
    }
    for (int i = 0; i < total; i++) cout << unicos[i] << " ";
    cout << endl;
    return 0;
}'''),
            ('p', 'Repare que o número lido nem precisa ser guardado em um vetor de entrada: basta o vetor '
                  'dos únicos. Com N números todos diferentes, o laço de dentro faz cerca de N²/2 '
                  'comparações; o Capítulo 10 explica por que isso importa quando N é grande.'),
        ],
    },
]
