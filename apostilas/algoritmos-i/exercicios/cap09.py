"""Exercícios práticos do Capítulo 9 (Recursão e backtracking)."""

CAPITULO = 'alg1-cap9'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Soma dos dígitos. Escreva uma função recursiva somaDigitos(n) que devolva a soma dos dígitos '
            'de um inteiro não negativo. Por exemplo, somaDigitos(1234) = 1 + 2 + 3 + 4 = 10. Não use '
            'laços.'
        ),
        'exemplos': [
            ('1234', 'Soma dos dígitos: 10'),
            ('7', 'Soma dos dígitos: 7'),
            ('9999', 'Soma dos dígitos: 36'),
        ],
        'resolucao': [
            ('p', 'Caso base: um número de um dígito (menor que 10) é a sua própria soma. Caso recursivo: o '
                  'último dígito (n % 10) mais a soma dos dígitos do resto do número (n / 10). Com 1234: '
                  '4 + somaDigitos(123) = 4 + 3 + somaDigitos(12) = ... = 10.'),
            ('Portugol', '''algoritmo "SomaDigitos"
var
   n: inteiro

funcao somaDigitos(k: inteiro): inteiro
inicio
   se k < 10 entao
      retorne k
   senao
      retorne (k mod 10) + somaDigitos(k div 10)
   fimse
fimfuncao

inicio
   escreva("Número: ")
   leia(n)
   escreval("Soma dos dígitos: ", somaDigitos(n))
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int somaDigitos(int n) {
    if (n < 10) return n;                     // caso base
    return n % 10 + somaDigitos(n / 10);      // último + resto
}

int main() {
    int n;
    cout << "Número: ";
    cin >> n;
    cout << "Soma dos dígitos: " << somaDigitos(n) << endl;
    return 0;
}'''),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'Potência recursiva. Escreva uma função recursiva potencia(b, e) que calcule b elevado a e, '
            'para e inteiro não negativo, usando a definição b^0 = 1 e b^e = b × b^(e-1).'
        ),
        'exemplos': [
            ('2\n10', '2^10 = 1024'),
            ('5\n0', '5^0 = 1'),
            ('3\n4', '3^4 = 81'),
        ],
        'resolucao': [
            ('p', 'A definição matemática já é o algoritmo: o caso base é e = 0, e o caso recursivo diminui o '
                  'expoente em 1 a cada chamada, caminhando para o caso base. São e + 1 chamadas no total.'),
            ('Portugol', '''algoritmo "PotenciaRecursiva"
var
   b, e: inteiro

funcao potencia(base, expoente: inteiro): inteiro
inicio
   se expoente = 0 entao
      retorne 1
   senao
      retorne base * potencia(base, expoente - 1)
   fimse
fimfuncao

inicio
   escreva("Base e expoente: ")
   leia(b, e)
   escreval(b, "^", e, " = ", potencia(b, e))
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

long long potencia(long long b, int e) {
    if (e == 0) return 1;
    return b * potencia(b, e - 1);
}

int main() {
    long long b;
    int e;
    cout << "Base e expoente: ";
    cin >> b >> e;
    cout << b << "^" << e << " = " << potencia(b, e) << endl;
    return 0;
}'''),
            ('p', 'Desafio extra: como b^e = (b^(e/2))² quando e é par, dá para calcular 2^1000000 com cerca '
                  'de 20 chamadas em vez de um milhão. Essa ideia se chama exponenciação rápida.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Número em binário. Escreva um procedimento recursivo que mostre um inteiro não negativo em '
            'binário. Dica: os dígitos binários de n são os dígitos de n / 2 seguidos do resto n % 2.'
        ),
        'exemplos': [
            ('13', '13 em binário: 1101'),
            ('8', '8 em binário: 1000'),
            ('0', '0 em binário: 0'),
        ],
        'resolucao': [
            ('p', 'As divisões sucessivas por 2 produzem os dígitos de trás para a frente: 13 % 2 = 1, '
                  '6 % 2 = 0, 3 % 2 = 1, 1 % 2 = 1. A recursão resolve a ordem de graça: o procedimento '
                  'primeiro mostra o binário de n / 2 (os dígitos da esquerda) e só DEPOIS, na volta da '
                  'chamada, mostra o seu próprio dígito. É o "ir e voltar" da Seção 9.2.'),
            ('Portugol', '''algoritmo "Binario"
var
   n: inteiro

procedimento binario(k: inteiro)
inicio
   se k >= 2 entao
      binario(k div 2)
   fimse
   escreva(k mod 2)
fimprocedimento

inicio
   escreva("Número: ")
   leia(n)
   escreva(n, " em binário: ")
   binario(n)
   escreval("")
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

void binario(int n) {
    if (n >= 2) binario(n / 2);   // primeiro os dígitos da esquerda
    cout << n % 2;                // depois o último, na volta
}

int main() {
    int n;
    cout << "Número: ";
    cin >> n;
    cout << n << " em binário: ";
    binario(n);
    cout << endl;
    return 0;
}'''),
            ('p', 'Troque a ordem das duas linhas de binario e o número sai invertido: 1011 para o 13. O caso '
                  'base (n menor que 2) faz o 0 e o 1 serem mostrados diretamente.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Contar uma letra. Escreva uma função recursiva que receba uma palavra e uma letra e devolva '
            'quantas vezes a letra aparece na palavra. Não use laços: pense na primeira letra e no resto '
            'da palavra.'
        ),
        'exemplos': [
            ('banana\na', 'A letra a aparece 3 vez(es)'),
            ('recursao\nr', 'A letra r aparece 2 vez(es)'),
            ('pilha\nz', 'A letra z aparece 0 vez(es)'),
        ],
        'resolucao': [
            ('p', 'Caso base: a palavra vazia não tem nenhuma ocorrência. Caso recursivo: conte 1 se a '
                  'primeira letra for a procurada (0 se não for) e some com a contagem no resto da palavra. '
                  'Em vez de criar uma string nova a cada chamada com substr, a versão em C++ passa a '
                  'posição de onde continuar, o que é mais eficiente.'),
            ('Portugol', '''algoritmo "ContarLetra"
var
   palavra, letra: caractere

funcao contar(p, l: caractere): inteiro
var
   primeira: inteiro
inicio
   se compr(p) = 0 entao
      retorne 0
   fimse
   primeira <- 0
   se copia(p, 1, 1) = l entao
      primeira <- 1
   fimse
   retorne primeira + contar(copia(p, 2, compr(p) - 1), l)
fimfuncao

inicio
   escreva("Palavra: ")
   leia(palavra)
   escreva("Letra: ")
   leia(letra)
   escreval("A letra ", letra, " aparece ", contar(palavra, letra), " vez(es)")
fimalgoritmo'''),
            ('C++', '''#include <iostream>
#include <string>
using namespace std;

// quantas vezes c aparece em p, da posição i até o fim
int contar(const string &p, char c, size_t i) {
    if (i == p.size()) return 0;                    // nada mais
    return (p[i] == c ? 1 : 0) + contar(p, c, i + 1);
}

int main() {
    string palavra;
    char letra;
    cout << "Palavra: ";
    cin >> palavra;
    cout << "Letra: ";
    cin >> letra;
    cout << "A letra " << letra << " aparece "
         << contar(palavra, letra, 0) << " vez(es)" << endl;
    return 0;
}'''),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Subconjuntos com soma alvo. Leia N, depois N inteiros positivos e, por fim, um valor alvo. '
            'Usando backtracking, mostre todos os subconjuntos dos números (respeitando a ordem da leitura) '
            'cuja soma é igual ao alvo, um por linha, e no fim a quantidade encontrada.'
        ),
        'exemplos': [
            ('6\n3 34 4 12 5 2\n9', '3 4 2\n4 5\n2 subconjunto(s)'),
            ('4\n1 2 3 4\n5', '1 4\n2 3\n2 subconjunto(s)'),
            ('3\n5 10 20\n4', '0 subconjunto(s)'),
        ],
        'resolucao': [
            ('p', 'Para cada número há duas escolhas: entra ou não entra no subconjunto. A função decide o '
                  'número da posição i, tenta as duas opções recursivamente e, ao voltar, desfaz a escolha '
                  '(Seção 9.7). Um vetor guarda os números escolhidos até o momento. Quando a soma chega '
                  'exatamente ao alvo, o subconjunto é mostrado; quando passa do alvo ou os números acabam, '
                  'aquele caminho é abandonado. Como os números são positivos, passar do alvo significa que '
                  'não adianta continuar.'),
            ('C++', '''#include <iostream>
#include <vector>
using namespace std;

void buscar(const vector<int> &v, size_t i, int falta,
            vector<int> &escolhidos, int &total) {
    if (falta == 0) {                       // soma exata: achou
        for (int x : escolhidos) cout << x << " ";
        cout << endl;
        total++;
        return;
    }
    if (falta < 0 || i == v.size()) return; // passou ou acabou
    escolhidos.push_back(v[i]);             // escolhe v[i]
    buscar(v, i + 1, falta - v[i], escolhidos, total);
    escolhidos.pop_back();                  // desfaz a escolha
    buscar(v, i + 1, falta, escolhidos, total);   // sem v[i]
}

int main() {
    int n, alvo;
    cin >> n;
    vector<int> v(n);
    for (int &x : v) cin >> x;
    cin >> alvo;
    vector<int> escolhidos;
    int total = 0;
    buscar(v, 0, alvo, escolhidos, total);
    cout << total << " subconjunto(s)" << endl;
    return 0;
}'''),
            ('p', 'O parâmetro falta é o quanto ainda falta somar, o que evita recalcular a soma dos escolhidos '
                  'a cada chamada. A ordem das duas tentativas, primeiro com v[i] e depois sem, faz os '
                  'subconjuntos aparecerem na ordem da leitura. Sem a poda (falta < 0), o programa ainda '
                  'funcionaria, mas examinaria todas as 2^N combinações.'),
        ],
    },
]
