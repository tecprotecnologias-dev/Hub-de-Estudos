"""Exercícios práticos do Capítulo 10 (Busca e ordenação)."""

CAPITULO = 'alg1-cap10'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Todas as ocorrências. Leia N (até 50), N números inteiros e um valor x. Usando busca '
            'sequencial, mostre em que posições (contando a partir de 1) x aparece e quantas vezes. Se '
            'não aparecer, mostre "Não encontrado".'
        ),
        'exemplos': [
            ('8\n5 3 5 1 5 2 4 5\n5', 'Posições: 1 3 5 8\nAparece 4 vez(es)'),
            ('4\n1 2 3 4\n9', 'Não encontrado'),
        ],
        'resolucao': [
            ('p', 'A busca sequencial da Seção 10.1 para na primeira ocorrência. Para achar todas, o laço '
                  'precisa ir até o fim, sem return no meio, contando e mostrando cada posição em que o '
                  'valor aparece.'),
            ('Portugol', '''algoritmo "Ocorrencias"
var
   v: vetor[1..50] de inteiro
   n, i, x, vezes: inteiro
inicio
   leia(n)
   para i de 1 ate n faca
      leia(v[i])
   fimpara
   leia(x)
   vezes <- 0
   para i de 1 ate n faca
      se v[i] = x entao
         se vezes = 0 entao
            escreva("Posições: ")
         fimse
         escreva(i, " ")
         vezes <- vezes + 1
      fimse
   fimpara
   se vezes > 0 entao
      escreval("")
      escreval("Aparece ", vezes, " vez(es)")
   senao
      escreval("Não encontrado")
   fimse
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    const int MAX = 50;
    int v[MAX];
    int n, x;
    cin >> n;
    if (n < 1 || n > MAX) return 0;
    for (int i = 0; i < n; i++) cin >> v[i];
    cin >> x;
    int vezes = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] == x) {
            if (vezes == 0) cout << "Posições: ";
            cout << i + 1 << " ";
            vezes++;
        }
    }
    if (vezes > 0) {
        cout << endl << "Aparece " << vezes << " vez(es)" << endl;
    } else {
        cout << "Não encontrado" << endl;
    }
    return 0;
}'''),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'Está ordenado? Leia N e N números, e diga se eles estão em ordem crescente (valores iguais '
            'seguidos são permitidos). Essa verificação é útil antes de usar a busca binária, que só '
            'funciona com vetores ordenados.'
        ),
        'exemplos': [
            ('5\n1 3 3 7 9', 'Está em ordem crescente'),
            ('4\n2 1 3 4', 'Não está em ordem (posição 2)'),
            ('1\n42', 'Está em ordem crescente'),
        ],
        'resolucao': [
            ('p', 'Basta comparar cada elemento com o seguinte. Se algum for maior que o seguinte, o vetor '
                  'não está ordenado, e a busca pode parar ali. O laço vai até n - 2 (ou i + 1 < n), porque '
                  'o último elemento não tem seguinte. A mensagem mostra a posição (a partir de 1) do '
                  'primeiro elemento fora de ordem.'),
            ('Portugol', '''algoritmo "EstaOrdenado"
var
   v: vetor[1..50] de inteiro
   n, i, erro: inteiro
inicio
   leia(n)
   para i de 1 ate n faca
      leia(v[i])
   fimpara
   erro <- 0
   i <- 1
   enquanto (i < n) e (erro = 0) faca
      se v[i] > v[i + 1] entao
         erro <- i + 1
      fimse
      i <- i + 1
   fimenquanto
   se erro = 0 entao
      escreval("Está em ordem crescente")
   senao
      escreval("Não está em ordem (posição ", erro, ")")
   fimse
fimalgoritmo'''),
            ('C++', '''#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int &x : v) cin >> x;
    for (int i = 0; i + 1 < n; i++) {
        if (v[i] > v[i + 1]) {
            cout << "Não está em ordem (posição " << i + 2 << ")"
                 << endl;
            return 0;
        }
    }
    cout << "Está em ordem crescente" << endl;
    return 0;
}'''),
            ('p', 'A condição i + 1 < n também funciona com n = 1 (o laço não executa nenhuma vez) e com '
                  'n = 0. Já i < n - 1 seria igual com int, mas com o tipo size_t daria problema para n = 0, '
                  'porque 0 - 1 vira um número enorme.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Ordem decrescente. Leia N (até 50) e N números, ordene-os do maior para o menor usando a '
            'ordenação por seleção (escrita por você, sem o sort da biblioteca) e mostre o resultado.'
        ),
        'exemplos': [
            ('6\n4 9 1 7 3 8', '9 8 7 4 3 1'),
            ('3\n5 5 2', '5 5 2'),
        ],
        'resolucao': [
            ('p', 'É a seleção da Seção 10.4 com uma única mudança: em vez de procurar o menor elemento da '
                  'parte que falta, procura-se o maior. A comparação < vira >.'),
            ('Portugol', '''algoritmo "SelecaoDecrescente"
var
   v: vetor[1..50] de inteiro
   n, i, j, iMaior, aux: inteiro
inicio
   leia(n)
   para i de 1 ate n faca
      leia(v[i])
   fimpara
   para i de 1 ate n - 1 faca
      iMaior <- i
      para j de i + 1 ate n faca
         se v[j] > v[iMaior] entao
            iMaior <- j
         fimse
      fimpara
      aux <- v[i]
      v[i] <- v[iMaior]
      v[iMaior] <- aux
   fimpara
   para i de 1 ate n faca
      escreva(v[i], " ")
   fimpara
   escreval("")
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

void selecaoDecrescente(int v[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int iMaior = i;
        for (int j = i + 1; j < n; j++) {
            if (v[j] > v[iMaior]) iMaior = j;   // > em vez de <
        }
        swap(v[i], v[iMaior]);
    }
}

int main() {
    const int MAX = 50;
    int v[MAX];
    int n;
    cin >> n;
    if (n < 1 || n > MAX) return 0;
    for (int i = 0; i < n; i++) cin >> v[i];
    selecaoDecrescente(v, n);
    for (int i = 0; i < n; i++) cout << v[i] << " ";
    cout << endl;
    return 0;
}'''),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Busca binária com passos. Leia N, N números já em ordem crescente e um valor x. Faça a busca '
            'binária e mostre em que posição (a partir de 1) x foi encontrado e quantos passos (comparações '
            'com o elemento do meio) foram necessários, ou "Não encontrado" e o número de passos.'
        ),
        'exemplos': [
            ('15\n3 8 11 15 19 23 27 32 36 41 47 52 58 63 70\n41', 'Encontrado na posição 10 em 3 passos'),
            ('15\n3 8 11 15 19 23 27 32 36 41 47 52 58 63 70\n40', 'Não encontrado (4 passos)'),
            ('15\n3 8 11 15 19 23 27 32 36 41 47 52 58 63 70\n32', 'Encontrado na posição 8 em 1 passo'),
        ],
        'resolucao': [
            ('p', 'É a busca binária da Seção 10.2, com um contador incrementado a cada vez que o elemento do '
                  'meio é examinado. Com 15 elementos, nunca são necessários mais que 4 passos, porque 15 '
                  'cabe em 4 divisões ao meio (2^4 = 16). Faça o teste de mesa com x = 40 para ver os índices '
                  'ini e fim se cruzarem.'),
            ('C++', '''#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, x;
    cin >> n;
    vector<int> v(n);
    for (int &e : v) cin >> e;
    cin >> x;
    int ini = 0, fim = n - 1, passos = 0;
    while (ini <= fim) {
        int meio = ini + (fim - ini) / 2;
        passos++;
        if (v[meio] == x) {
            cout << "Encontrado na posição " << meio + 1 << " em "
                 << passos << (passos == 1 ? " passo" : " passos")
                 << endl;
            return 0;
        }
        if (v[meio] < x) ini = meio + 1;
        else fim = meio - 1;
    }
    cout << "Não encontrado (" << passos << " passos)" << endl;
    return 0;
}'''),
            ('Portugol', '''algoritmo "BuscaBinaria"
var
   v: vetor[1..50] de inteiro
   n, i, x, ini, fim, meio, passos, pos: inteiro
inicio
   leia(n)
   para i de 1 ate n faca
      leia(v[i])
   fimpara
   leia(x)
   ini <- 1
   fim <- n
   passos <- 0
   pos <- 0
   enquanto (ini <= fim) e (pos = 0) faca
      meio <- (ini + fim) div 2
      passos <- passos + 1
      se v[meio] = x entao
         pos <- meio
      senao
         se v[meio] < x entao
            ini <- meio + 1
         senao
            fim <- meio - 1
         fimse
      fimse
   fimenquanto
   se pos > 0 entao
      se passos = 1 entao
         escreval("Encontrado na posição ", pos, " em 1 passo")
      senao
         escreval("Encontrado na posição ", pos, " em ", passos, " passos")
      fimse
   senao
      escreval("Não encontrado (", passos, " passos)")
   fimse
fimalgoritmo'''),
            ('p', 'A posição encontrada é igual nas duas versões, mas os passos podem variar em 1 no Portugol, '
                  'porque com o vetor começando em 1 o elemento do meio de cada faixa às vezes é outro. O '
                  'que não muda é o máximo: cerca de log₂ N passos.'),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Mediana. A mediana de um conjunto de números é o valor do meio depois de ordená-los; quando a '
            'quantidade é par, é a média dos dois valores do meio. Leia N e N números, ordene-os com a '
            'ordenação por inserção (escrita por você) e mostre a lista ordenada e a mediana.'
        ),
        'exemplos': [
            ('5\n7 1 9 3 5', 'Ordenado: 1 3 5 7 9\nMediana: 5'),
            ('4\n8 2 6 4', 'Ordenado: 2 4 6 8\nMediana: 5'),
            ('6\n10 1 4 4 9 2', 'Ordenado: 1 2 4 4 9 10\nMediana: 4'),
        ],
        'resolucao': [
            ('p', 'Depois de ordenar com a inserção da Seção 10.6, a mediana depende da paridade de N: com '
                  'N ímpar, é o elemento de índice N / 2 (em C++, com índices a partir de 0); com N par, é a '
                  'média dos elementos de índices N / 2 - 1 e N / 2. Com N = 4, são os índices 1 e 2.'),
            ('C++', '''#include <iostream>
#include <vector>
using namespace std;

void insercao(vector<double> &v) {
    for (size_t i = 1; i < v.size(); i++) {
        double atual = v[i];
        size_t j = i;
        while (j > 0 && v[j - 1] > atual) {   // os maiores andam
            v[j] = v[j - 1];
            j--;
        }
        v[j] = atual;
    }
}

int main() {
    int n;
    cin >> n;
    if (n < 1) return 0;
    vector<double> v(n);
    for (double &x : v) cin >> x;
    insercao(v);
    cout << "Ordenado:";
    for (double x : v) cout << " " << x;
    cout << endl;
    double mediana;
    if (n % 2 == 1) mediana = v[n / 2];
    else mediana = (v[n / 2 - 1] + v[n / 2]) / 2;
    cout << "Mediana: " << mediana << endl;
    return 0;
}'''),
            ('p', 'Esta versão da inserção usa size_t, um tipo sem sinal, e por isso compara j > 0 e usa '
                  'v[j - 1], em vez de deixar j chegar a -1 como na Seção 10.6: um size_t não pode ser '
                  'negativo. A mediana é muito usada em estatística porque, ao contrário da média, não é '
                  'puxada por um valor extremo: em 1, 2, 3, 4 e 1000, a média é 202, e a mediana, 3.'),
        ],
    },
]
