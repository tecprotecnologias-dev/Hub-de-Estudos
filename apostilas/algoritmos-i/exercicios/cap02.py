"""Exercícios práticos do Capítulo 2 (Linguagens de programação: estrutura, cout, cin, erros)."""

CAPITULO = 'alg1-cap2'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Idade em dias. Escreva um programa que leia a idade de uma pessoa em anos e mostre '
            'quantos dias ela já viveu, aproximadamente, considerando anos de 365 dias.'
        ),
        'exemplos': [
            ('20', 'Você viveu cerca de 7300 dias'),
            ('1', 'Você viveu cerca de 365 dias'),
        ],
        'resolucao': [
            ('p', 'Um programa com a estrutura básica do capítulo: lê um número com cin, faz uma conta e '
                  'mostra o resultado com cout. Como idade e dias são números inteiros, o tipo é int.'),
            ('Portugol', '''algoritmo "IdadeEmDias"
var
   anos, dias: inteiro
inicio
   escreva("Sua idade em anos: ")
   leia(anos)
   dias <- anos * 365
   escreval("Você viveu cerca de ", dias, " dias")
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int anos, dias;
    cout << "Sua idade em anos: ";
    cin >> anos;
    dias = anos * 365;
    cout << "Você viveu cerca de " << dias << " dias" << endl;
    return 0;
}'''),
            ('p', 'Repare nos espaços dentro das aspas: "cerca de " termina com espaço e " dias" começa com '
                  'espaço. Sem eles, o número sairia grudado no texto.'),
        ],
    },
    {
        'nivel': 'facil',
        'contexto': [
            ('p', 'O programa abaixo deveria ler dois números inteiros e mostrar a soma, mas não compila. '
                  'Ele tem quatro erros de sintaxe.'),
            ('codigo', '''#include <iostream>
using namespace std

int main() {
    int a, b
    cout << "Digite dois números: ";
    cin >> a >> b;
    cout << "Soma: << a + b << endl;
    retun 0;
}'''),
        ],
        'enunciado': (
            'Encontre e corrija os quatro erros. Compile o programa, leia as mensagens do compilador '
            '(Seção 2.9) e corrija um erro de cada vez, começando pelo primeiro.'
        ),
        'exemplos': [
            ('3\n4', 'Soma: 7'),
            ('10\n-2', 'Soma: 8'),
        ],
        'resolucao': [
            ('p', 'Os erros: falta o ponto e vírgula depois de using namespace std; falta o ponto e '
                  'vírgula depois de int a, b; falta fechar as aspas do texto "Soma: " (sem elas, o '
                  'compilador acha que << a + b << endl faz parte do texto); e return está escrito '
                  'errado (retun).'),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Digite dois números: ";
    cin >> a >> b;
    cout << "Soma: " << a + b << endl;
    return 0;
}'''),
            ('p', 'Um único erro pode gerar várias mensagens, porque o compilador se confunde com o que vem '
                  'depois. Por isso vale corrigir o primeiro erro apontado e compilar de novo, em vez de '
                  'tentar entender todas as mensagens de uma vez.'),
            ('Portugol', '''algoritmo "Soma"
var
   a, b: inteiro
inicio
   escreva("Digite dois números: ")
   leia(a, b)
   escreval("Soma: ", a + b)
fimalgoritmo'''),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Troco. Escreva um programa que leia o preço de um produto e o valor pago pelo cliente, '
            'e mostre o troco. Os valores podem ter centavos.'
        ),
        'exemplos': [
            ('37.5\n50', 'Troco: R$ 12.5'),
            ('19.9\n20', 'Troco: R$ 0.1'),
        ],
        'resolucao': [
            ('p', 'Como os valores têm centavos, as variáveis precisam ser double (real no Portugol), e não '
                  'int. Com int, 37.5 viraria 37 e o troco sairia errado. Lembre que, ao digitar, o '
                  'separador decimal é o ponto.'),
            ('Portugol', '''algoritmo "Troco"
var
   preco, pago, troco: real
inicio
   escreva("Preço: ")
   leia(preco)
   escreva("Valor pago: ")
   leia(pago)
   troco <- pago - preco
   escreval("Troco: R$ ", troco)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    double preco, pago, troco;
    cout << "Preço: ";
    cin >> preco;
    cout << "Valor pago: ";
    cin >> pago;
    troco = pago - preco;
    cout << "Troco: R$ " << troco << endl;
    return 0;
}'''),
            ('p', 'O cout mostra 12.5, e não 12.50. Mostrar sempre duas casas decimais é possível com '
                  'fixed e setprecision, recursos que aparecem nos próximos capítulos.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Recibo de compra. Escreva um programa que leia a quantidade e o preço unitário de dois '
            'produtos e mostre o subtotal de cada um e o total da compra, um em cada linha.'
        ),
        'exemplos': [
            ('2\n10.5\n3\n4', 'Subtotal 1: 21\nSubtotal 2: 12\nTotal: 33'),
            ('1\n99.9\n5\n2', 'Subtotal 1: 99.9\nSubtotal 2: 10\nTotal: 109.9'),
        ],
        'resolucao': [
            ('p', 'Entradas: quantidade e preço de cada produto (quatro valores). Saídas: dois subtotais e o '
                  'total. A quantidade é inteira, mas o preço tem centavos, então os subtotais e o total '
                  'são reais.'),
            ('Portugol', '''algoritmo "Recibo"
var
   qtd1, qtd2: inteiro
   preco1, preco2, sub1, sub2: real
inicio
   escreva("Quantidade e preço do produto 1: ")
   leia(qtd1, preco1)
   escreva("Quantidade e preço do produto 2: ")
   leia(qtd2, preco2)
   sub1 <- qtd1 * preco1
   sub2 <- qtd2 * preco2
   escreval("Subtotal 1: ", sub1)
   escreval("Subtotal 2: ", sub2)
   escreval("Total: ", sub1 + sub2)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int qtd1, qtd2;
    double preco1, preco2, sub1, sub2;
    cout << "Quantidade e preço do produto 1: ";
    cin >> qtd1 >> preco1;
    cout << "Quantidade e preço do produto 2: ";
    cin >> qtd2 >> preco2;
    sub1 = qtd1 * preco1;
    sub2 = qtd2 * preco2;
    cout << "Subtotal 1: " << sub1 << endl;
    cout << "Subtotal 2: " << sub2 << endl;
    cout << "Total: " << sub1 + sub2 << endl;
    return 0;
}'''),
            ('p', 'Um único cin pode ler vários valores: cin >> qtd1 >> preco1 lê os dois, separados por '
                  'espaço ou por Enter. O total pode ser calculado direto no cout, sem uma variável a '
                  'mais.'),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Troca de valores. Escreva um programa que leia dois números inteiros para as variáveis a e '
            'b, troque o conteúdo delas (a passa a ter o valor de b, e b o valor de a) e mostre os '
            'valores depois da troca. Atenção: fazer só a = b e depois b = a não funciona. Descubra por '
            'quê com um teste de mesa.'
        ),
        'exemplos': [
            ('3\n5', 'Depois da troca: a = 5, b = 3'),
            ('-1\n8', 'Depois da troca: a = 8, b = -1'),
        ],
        'resolucao': [
            ('p', 'O teste de mesa com a = 3 e b = 5 mostra o problema: depois de a = b, a vale 5, e o 3 se '
                  'perdeu. Então b = a coloca 5 em b, e as duas variáveis terminam com 5. A solução é '
                  'guardar o valor de a em uma variável auxiliar antes de sobrescrevê-lo, como quem troca o '
                  'conteúdo de dois copos usando um terceiro.'),
            ('Portugol', '''algoritmo "Troca"
var
   a, b, aux: inteiro
inicio
   escreva("a: ")
   leia(a)
   escreva("b: ")
   leia(b)
   aux <- a      // guarda o valor de a
   a <- b
   b <- aux
   escreval("Depois da troca: a = ", a, ", b = ", b)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    int a, b, aux;
    cout << "a: ";
    cin >> a;
    cout << "b: ";
    cin >> b;
    aux = a;      // guarda o valor de a
    a = b;
    b = aux;
    cout << "Depois da troca: a = " << a << ", b = " << b << endl;
    return 0;
}'''),
            ('p', 'Teste de mesa da solução, com a = 3 e b = 5: aux recebe 3; a recebe 5; b recebe aux, '
                  'que é 3. No fim, a = 5 e b = 3. Essa troca com auxiliar volta várias vezes nos próximos '
                  'capítulos, na ordenação de vetores e nas funções com passagem por referência.'),
        ],
    },
]
