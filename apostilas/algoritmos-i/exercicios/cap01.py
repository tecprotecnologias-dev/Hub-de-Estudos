"""Exercícios práticos do Capítulo 1 (Lógica, algoritmos e o computador)."""

CAPITULO = 'alg1-cap1'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Área e perímetro do retângulo. Escreva um algoritmo que leia a base e a altura de um '
            'retângulo e mostre a sua área (base × altura) e o seu perímetro (a soma dos quatro lados).'
        ),
        'exemplos': [
            ('5\n3', 'Área: 15\nPerímetro: 16'),
            ('2.5\n4', 'Área: 10\nPerímetro: 13'),
        ],
        'resolucao': [
            ('p', 'Entradas: base e altura. Saídas: área e perímetro. Como os lados opostos do retângulo '
                  'são iguais, o perímetro é base + altura + base + altura, ou 2 × (base + altura). '
                  'Use o tipo real, porque as medidas podem ter casas decimais.'),
            ('Portugol', '''algoritmo "Retangulo"
var
   base, altura, area, perimetro: real
inicio
   escreva("Base: ")
   leia(base)
   escreva("Altura: ")
   leia(altura)
   area <- base * altura
   perimetro <- 2 * (base + altura)
   escreval("Área: ", area)
   escreval("Perímetro: ", perimetro)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    double base, altura, area, perimetro;
    cout << "Base: ";
    cin >> base;
    cout << "Altura: ";
    cin >> altura;
    area = base * altura;
    perimetro = 2 * (base + altura);
    cout << "Área: " << area << endl;
    cout << "Perímetro: " << perimetro << endl;
    return 0;
}'''),
            ('p', 'Os parênteses em 2 * (base + altura) são necessários: sem eles, a multiplicação seria '
                  'feita antes da soma, e o resultado seria 2 × base + altura.'),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'Conversor de temperatura. Escreva um algoritmo que leia uma temperatura em graus Celsius e '
            'mostre o valor equivalente em graus Fahrenheit, usando a fórmula F = C × 9 / 5 + 32.'
        ),
        'exemplos': [
            ('25', 'Fahrenheit: 77'),
            ('0', 'Fahrenheit: 32'),
            ('36.5', 'Fahrenheit: 97.7'),
            ('-40', 'Fahrenheit: -40'),
        ],
        'resolucao': [
            ('p', 'Uma entrada (a temperatura em Celsius), uma saída (em Fahrenheit) e um cálculo. Os '
                  'exemplos foram escolhidos para testar casos diferentes: o ponto de congelamento da '
                  'água (0 °C = 32 °F), um valor com casa decimal e −40, a temperatura em que as duas '
                  'escalas coincidem.'),
            ('Portugol', '''algoritmo "CelsiusParaFahrenheit"
var
   celsius, fahrenheit: real
inicio
   escreva("Temperatura em Celsius: ")
   leia(celsius)
   fahrenheit <- celsius * 9 / 5 + 32
   escreval("Fahrenheit: ", fahrenheit)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    double celsius, fahrenheit;
    cout << "Temperatura em Celsius: ";
    cin >> celsius;
    fahrenheit = celsius * 9 / 5 + 32;
    cout << "Fahrenheit: " << fahrenheit << endl;
    return 0;
}'''),
            ('p', 'Aqui não são necessários parênteses: a multiplicação e a divisão são feitas antes da '
                  'soma, que é exatamente o que a fórmula pede.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Custo de uma viagem de carro. Antes de escrever o algoritmo, aplique o roteiro da Seção 1.4: '
            'anote, como comentário no início do código, as entradas, as saídas e o processamento. O '
            'algoritmo deve ler a distância da viagem (em km), o consumo do carro (em km por litro) e o '
            'preço do litro de combustível, e mostrar quantos litros serão gastos e quanto custará a viagem.'
        ),
        'exemplos': [
            ('300\n12\n6', 'Litros: 25\nCusto: R$ 150'),
            ('450\n15\n5.89', 'Litros: 30\nCusto: R$ 176.7'),
        ],
        'resolucao': [
            ('p', 'Entradas: distância, consumo e preço do litro. Saídas: litros gastos e custo. '
                  'Processamento: litros ← distância / consumo; custo ← litros × preço. Resolvendo o '
                  'primeiro exemplo à mão: 300 km / 12 km/l = 25 litros, e 25 × R$ 6 = R$ 150.'),
            ('Portugol', '''algoritmo "CustoViagem"
// entradas: distancia (km), consumo (km/l), preco (R$ por litro)
// saidas: litros gastos e custo da viagem
// processamento: litros <- distancia / consumo
//                custo <- litros * preco
var
   distancia, consumo, preco, litros, custo: real
inicio
   escreva("Distância (km): ")
   leia(distancia)
   escreva("Consumo (km por litro): ")
   leia(consumo)
   escreva("Preço do litro: ")
   leia(preco)
   litros <- distancia / consumo
   custo <- litros * preco
   escreval("Litros: ", litros)
   escreval("Custo: R$ ", custo)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    // entradas: distancia, consumo e preco; saidas: litros e custo
    double distancia, consumo, preco, litros, custo;
    cout << "Distância (km): ";
    cin >> distancia;
    cout << "Consumo (km por litro): ";
    cin >> consumo;
    cout << "Preço do litro: ";
    cin >> preco;
    litros = distancia / consumo;
    custo = litros * preco;
    cout << "Litros: " << litros << endl;
    cout << "Custo: R$ " << custo << endl;
    return 0;
}'''),
            ('p', 'A ordem dos cálculos importa: o custo depende dos litros, então os litros precisam ser '
                  'calculados primeiro. Também daria para calcular tudo de uma vez, com '
                  'custo ← distância / consumo × preço, mas guardar os litros em uma variável deixa o '
                  'algoritmo mais claro e ainda fornece a primeira saída.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Desconto na loja. Uma loja dá 10% de desconto nas compras de R$ 100 ou mais. Escreva um '
            'algoritmo que leia o valor da compra e mostre o valor a pagar. Faça um teste de mesa com os '
            'valores 150, 80 e 100 antes de passar para o computador: o último está exatamente na fronteira.'
        ),
        'exemplos': [
            ('150', 'Valor a pagar: R$ 135'),
            ('80', 'Valor a pagar: R$ 80'),
            ('100', 'Valor a pagar: R$ 90'),
        ],
        'resolucao': [
            ('p', 'Há uma decisão: o desconto só vale a partir de R$ 100. Como o enunciado diz "R$ 100 ou '
                  'mais", a condição é valor >= 100, e não valor > 100. O teste de mesa com 100 mostra a '
                  'diferença: com >=, o cliente paga R$ 90; com >, pagaria R$ 100, o que estaria errado.'),
            ('Portugol', '''algoritmo "Desconto"
var
   valor, pagar: real
inicio
   escreva("Valor da compra: ")
   leia(valor)
   se valor >= 100 entao
      pagar <- valor * 0.9        // 10% de desconto
   senao
      pagar <- valor
   fimse
   escreval("Valor a pagar: R$ ", pagar)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    double valor, pagar;
    cout << "Valor da compra: ";
    cin >> valor;
    if (valor >= 100) {
        pagar = valor * 0.9;        // 10% de desconto
    } else {
        pagar = valor;
    }
    cout << "Valor a pagar: R$ " << pagar << endl;
    return 0;
}'''),
            ('p', 'Multiplicar por 0.9 é o mesmo que tirar 10%: valor − valor × 0.1 = valor × 0.9. A saída '
                  'fica depois do fimse porque é igual nos dois caminhos; só o cálculo muda.'),
        ],
    },
    {
        'nivel': 'dificil',
        'contexto': [
            ('p', 'Um colega escreveu o algoritmo abaixo para calcular a média de um aluno em que a prova '
                  'tem peso 2 e o trabalho tem peso 1. É aprovado quem tem média 6 ou mais. O algoritmo '
                  'tem dois erros.'),
            ('codigo', '''algoritmo "MediaPonderada"
var
   prova, trabalho, media: real
inicio
   escreva("Nota da prova: ")
   leia(prova)
   escreva("Nota do trabalho: ")
   leia(trabalho)
   media <- prova * 2 + trabalho / 3
   se media > 6 entao
      escreval("Aprovado. Média: ", media)
   senao
      escreval("Reprovado. Média: ", media)
   fimse
fimalgoritmo'''),
        ],
        'enunciado': (
            'Encontre os erros com um teste de mesa (use prova 9 e trabalho 6, e depois prova 6 e '
            'trabalho 6) e escreva a versão corrigida. Lembre: na média ponderada, cada nota é '
            'multiplicada pelo seu peso, e a soma é dividida pela soma dos pesos.'
        ),
        'exemplos': [
            ('9\n6', 'Aprovado. Média: 8'),
            ('6\n6', 'Aprovado. Média: 6'),
            ('4\n7', 'Reprovado. Média: 5'),
        ],
        'resolucao': [
            ('p', 'Primeiro erro: a precedência. Com prova 9 e trabalho 6, o teste de mesa dá '
                  'media = 9 × 2 + 6 / 3 = 18 + 2 = 20, uma média impossível. Como a multiplicação e a '
                  'divisão são feitas antes da soma, só o trabalho foi dividido por 3. A soma precisa de '
                  'parênteses: (prova × 2 + trabalho) / 3, que dá (18 + 6) / 3 = 8.'),
            ('p', 'Segundo erro: a fronteira. Com prova 6 e trabalho 6, a média correta é 6, e o aluno '
                  'deveria ser aprovado ("6 ou mais"). Mas 6 > 6 é falso, e ele seria reprovado. A '
                  'condição certa é media >= 6.'),
            ('Portugol', '''algoritmo "MediaPonderada"
var
   prova, trabalho, media: real
inicio
   escreva("Nota da prova: ")
   leia(prova)
   escreva("Nota do trabalho: ")
   leia(trabalho)
   media <- (prova * 2 + trabalho) / 3     // pesos 2 e 1
   se media >= 6 entao                       // 6 ou mais
      escreval("Aprovado. Média: ", media)
   senao
      escreval("Reprovado. Média: ", media)
   fimse
fimalgoritmo'''),
            ('C++', '''#include <iostream>
using namespace std;

int main() {
    double prova, trabalho, media;
    cout << "Nota da prova: ";
    cin >> prova;
    cout << "Nota do trabalho: ";
    cin >> trabalho;
    media = (prova * 2 + trabalho) / 3;     // pesos 2 e 1
    if (media >= 6) {                       // 6 ou mais
        cout << "Aprovado. Média: " << media << endl;
    } else {
        cout << "Reprovado. Média: " << media << endl;
    }
    return 0;
}'''),
            ('p', 'Repare que nenhum dos dois erros impede o algoritmo de rodar: ele executa normalmente e '
                  'mostra resultados errados. Erros de lógica só aparecem com testes, e por isso vale '
                  'sempre testar um caso comum e um caso na fronteira.'),
        ],
    },
]
