"""Exercícios práticos do Capítulo 11 (Introdução às estruturas de dados)."""

CAPITULO = 'alg1-cap11'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Estoque com registros. Crie um registro Produto com nome (uma palavra), preço e quantidade. '
            'Leia N produtos para um vetor de registros e mostre o valor total do estoque (a soma de '
            'preço × quantidade) e o nome do produto mais caro.'
        ),
        'exemplos': [
            ('3\nCaneta 2.5 10\nCaderno 15 4\nMochila 89.9 1', 'Valor do estoque: 174.9\nMais caro: Mochila'),
            ('2\nLapis 1 100\nBorracha 0.5 40', 'Valor do estoque: 120\nMais caro: Lapis'),
        ],
        'resolucao': [
            ('p', 'Com um registro, os três dados de cada produto ficam juntos, e o vetor de registros '
                  'substitui três vetores paralelos (Seções 11.1 e 11.2). O campo é acessado com o ponto: '
                  'estoque[i].preco.'),
            ('C++', '''#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Produto {
    string nome;
    double preco;
    int quantidade;
};

int main() {
    int n;
    cin >> n;
    if (n < 1) return 0;
    vector<Produto> estoque(n);
    for (Produto &p : estoque) cin >> p.nome >> p.preco >> p.quantidade;

    double total = 0;
    size_t iMaisCaro = 0;
    for (size_t i = 0; i < estoque.size(); i++) {
        total += estoque[i].preco * estoque[i].quantidade;
        if (estoque[i].preco > estoque[iMaisCaro].preco) iMaisCaro = i;
    }
    cout << "Valor do estoque: " << total << endl;
    cout << "Mais caro: " << estoque[iMaisCaro].nome << endl;
    return 0;
}'''),
            ('Portugol', '''algoritmo "Estoque"
tipo Produto = registro
   nome: caractere
   preco: real
   quantidade: inteiro
fimregistro
var
   estoque: vetor[1..50] de Produto
   n, i, iCaro: inteiro
   total: real
inicio
   leia(n)
   total <- 0
   iCaro <- 1
   para i de 1 ate n faca
      leia(estoque[i].nome, estoque[i].preco, estoque[i].quantidade)
      total <- total + estoque[i].preco * estoque[i].quantidade
      se estoque[i].preco > estoque[iCaro].preco entao
         iCaro <- i
      fimse
   fimpara
   escreval("Valor do estoque: ", total)
   escreval("Mais caro: ", estoque[iCaro].nome)
fimalgoritmo'''),
            ('p', 'Na versão em C++, o for (Produto &p : estoque) usa uma referência para que a leitura '
                  'preencha os registros do próprio vetor, e não cópias. O suporte a registros varia entre '
                  'as ferramentas de Portugol (Seção 11.1).'),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'Inverter as palavras. Leia uma frase e mostre as suas palavras em ordem inversa, usando uma '
            'pilha: empilhe cada palavra e depois desempilhe todas.'
        ),
        'exemplos': [
            ('o rato roeu a roupa', 'roupa a roeu rato o'),
            ('primeiro segundo', 'segundo primeiro'),
        ],
        'resolucao': [
            ('p', 'A pilha devolve os elementos na ordem inversa da entrada (LIFO, Seção 11.4), que é '
                  'exatamente o que o exercício pede. As palavras podem ser lidas uma a uma com cin >>, '
                  'que para nos espaços, até a entrada acabar.'),
            ('C++', '''#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
    stack<string> pilha;
    string palavra;
    while (cin >> palavra) pilha.push(palavra);   // até o fim
    bool primeira = true;
    while (!pilha.empty()) {
        if (!primeira) cout << " ";
        cout << pilha.top();
        pilha.pop();
        primeira = false;
    }
    cout << endl;
    return 0;
}'''),
            ('p', 'Ao rodar no terminal, depois de digitar a frase, termine a entrada com Ctrl+Z e Enter (no '
                  'Windows) ou Ctrl+D (no Linux e no macOS). Outra opção é ler a linha inteira com getline e '
                  'separar as palavras com um istringstream.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Fila de atendimento. Simule a fila de um consultório com comandos digitados um por linha: '
            '"C nome" (um cliente chega), "A" (o próximo é atendido) e "F" (fim do expediente). A cada '
            '"A", mostre quem foi atendido ou "Fila vazia". No "F", mostre quantos ficaram sem '
            'atendimento.'
        ),
        'exemplos': [
            ('C Ana\nC Bruno\nA\nC Carla\nA\nA\nA\nF',
             'Atendendo: Ana\nAtendendo: Bruno\nAtendendo: Carla\nFila vazia\nSem atendimento: 0'),
            ('C Davi\nC Eva\nA\nF', 'Atendendo: Davi\nSem atendimento: 1'),
        ],
        'resolucao': [
            ('p', 'O primeiro a chegar é o primeiro a ser atendido: é uma fila (FIFO, Seção 11.5). O '
                  'comando é lido em um char, e o nome só é lido quando o comando é C. Antes de atender, '
                  'é preciso verificar se a fila não está vazia.'),
            ('C++', '''#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
    queue<string> fila;
    char comando;
    while (cin >> comando && comando != 'F') {
        if (comando == 'C') {
            string nome;
            cin >> nome;
            fila.push(nome);
        } else if (comando == 'A') {
            if (fila.empty()) {
                cout << "Fila vazia" << endl;
            } else {
                cout << "Atendendo: " << fila.front() << endl;
                fila.pop();
            }
        }
    }
    cout << "Sem atendimento: " << fila.size() << endl;
    return 0;
}'''),
            ('p', 'O cin >> comando && comando != \'F\' no while segue o padrão do laço com sentinela: o '
                  'laço termina no F ou se a entrada acabar. Sem o teste fila.empty(), chamar front em uma '
                  'fila vazia levaria a um comportamento indefinido.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Lista encadeada. Leia números inteiros até o 0 e insira cada um no FIM de uma lista '
            'encadeada feita por você (com struct No e ponteiros). Depois, mostre a lista no formato '
            '"1 -> 2 -> 3 -> fim", a soma dos valores e libere a memória.'
        ),
        'exemplos': [
            ('1 2 3 0', '1 -> 2 -> 3 -> fim\nSoma: 6'),
            ('0', 'fim\nSoma: 0'),
        ],
        'resolucao': [
            ('p', 'Para inserir no fim sem percorrer a lista toda a cada vez, guarde também um ponteiro para '
                  'o último nó. Se a lista está vazia, o novo nó é o primeiro e o último; senão, o último '
                  'passa a apontar para ele. Todo nó criado com new é devolvido com delete no fim (Seção '
                  '11.7).'),
            ('C++', '''#include <iostream>
using namespace std;

struct No {
    int valor;
    No *prox;
};

int main() {
    No *inicio = nullptr, *ultimo = nullptr;
    int x;
    while (cin >> x && x != 0) {
        No *novo = new No{x, nullptr};
        if (inicio == nullptr) inicio = novo;   // lista vazia
        else ultimo->prox = novo;               // liga no fim
        ultimo = novo;
    }
    int soma = 0;
    for (No *p = inicio; p != nullptr; p = p->prox) {
        cout << p->valor << " -> ";
        soma += p->valor;
    }
    cout << "fim" << endl;
    cout << "Soma: " << soma << endl;
    while (inicio != nullptr) {                 // libera a memória
        No *p = inicio;
        inicio = inicio->prox;
        delete p;
    }
    return 0;
}'''),
            ('p', 'A expressão new No{x, nullptr} cria o nó e já preenche os dois campos. O ponteiro p, usado '
                  'para percorrer, é separado de inicio, para não perder o começo da lista.'),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Calculadora pós-fixa. Na notação pós-fixa, o operador vem depois dos operandos: "3 4 +" '
            'significa 3 + 4, e "3 4 + 2 *" significa (3 + 4) × 2, sem precisar de parênteses. Leia uma '
            'expressão pós-fixa com números inteiros e os operadores + - * /, separados por espaços, e '
            'calcule o resultado usando uma pilha.'
        ),
        'exemplos': [
            ('3 4 + 2 *', 'Resultado: 14'),
            ('5 1 2 + 4 * + 3 -', 'Resultado: 14'),
            ('10 2 8 * + 3 -', 'Resultado: 23'),
        ],
        'resolucao': [
            ('p', 'Percorra a expressão item a item. Um número é empilhado. Um operador desempilha os dois '
                  'últimos números, faz a conta e empilha o resultado. Atenção à ordem: o primeiro '
                  'desempilhado é o operando da DIREITA. No fim, sobra um único número na pilha: o '
                  'resultado. Calculadoras científicas antigas e várias linguagens usam esse método.'),
            ('C++', '''#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
    stack<long long> pilha;
    string item;
    while (cin >> item) {
        if (item == "+" || item == "-" || item == "*" || item == "/") {
            if (pilha.size() < 2) {
                cout << "Expressão inválida" << endl;
                return 0;
            }
            long long b = pilha.top();   // operando da direita
            pilha.pop();
            long long a = pilha.top();
            pilha.pop();
            if (item == "+") pilha.push(a + b);
            else if (item == "-") pilha.push(a - b);
            else if (item == "*") pilha.push(a * b);
            else pilha.push(a / b);
        } else {
            pilha.push(stoll(item));     // número: empilha
        }
    }
    if (pilha.size() == 1) cout << "Resultado: " << pilha.top() << endl;
    else cout << "Expressão inválida" << endl;
    return 0;
}'''),
            ('p', 'Teste de mesa com "3 4 + 2 *": empilha 3, empilha 4; o + desempilha 4 e 3 e empilha 7; '
                  'empilha 2; o * desempilha 2 e 7 e empilha 14. A versão acima ainda trata expressões mal '
                  'formadas, com operadores ou números sobrando. Desafio extra: trate a divisão por zero.'),
        ],
    },
]
