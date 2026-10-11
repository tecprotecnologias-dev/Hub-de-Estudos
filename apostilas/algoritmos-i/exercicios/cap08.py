"""Exercícios práticos do Capítulo 8 (Caracteres e strings)."""

CAPITULO = 'alg1-cap8'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Contar vogais. Escreva um programa que leia uma frase (com espaços) e mostre quantas vogais '
            'ela tem, contando maiúsculas e minúsculas. Considere frases sem acentos.'
        ),
        'exemplos': [
            ('Programar e divertido', 'Vogais: 8'),
            ('AEIOU aeiou', 'Vogais: 10'),
            ('xyz', 'Vogais: 0'),
        ],
        'resolucao': [
            ('p', 'A frase tem espaços, então a leitura é com getline (Seção 8.3). Cada caractere é '
                  'convertido para minúscula com tolower antes da comparação, para que "A" e "a" contem '
                  'igual. No Portugol, copia(frase, i, 1) pega o caractere da posição i, e minusc o '
                  'converte.'),
            ('Portugol', '''algoritmo "ContarVogais"
var
   frase, c: caractere
   i, vogais: inteiro
inicio
   escreva("Frase: ")
   leia(frase)
   vogais <- 0
   para i de 1 ate compr(frase) faca
      c <- minusc(copia(frase, i, 1))
      se (c = "a") ou (c = "e") ou (c = "i") ou (c = "o") ou (c = "u") entao
         vogais <- vogais + 1
      fimse
   fimpara
   escreval("Vogais: ", vogais)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string frase;
    cout << "Frase: ";
    getline(cin, frase);
    int vogais = 0;
    for (unsigned char c : frase) {
        char m = tolower(c);
        if (m == 'a' || m == 'e' || m == 'i' || m == 'o' || m == 'u') {
            vogais++;
        }
    }
    cout << "Vogais: " << vogais << endl;
    return 0;
}'''),
            ('p', 'Uma alternativa à condição longa é procurar o caractere em uma string com as vogais: '
                  'string("aeiou").find(m) != string::npos.'),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'Iniciais do nome. Escreva um programa que leia um nome completo e mostre as iniciais em '
            'maiúsculas, juntas. Considere que as palavras são separadas por um espaço.'
        ),
        'exemplos': [
            ('Ada Lovelace King', 'Iniciais: ALK'),
            ('alan turing', 'Iniciais: AT'),
        ],
        'resolucao': [
            ('p', 'A primeira letra do nome é sempre uma inicial. As outras são as letras que vêm logo depois '
                  'de um espaço. Basta percorrer o nome e, a cada espaço, pegar o caractere seguinte, '
                  'convertido com toupper.'),
            ('Portugol', '''algoritmo "Iniciais"
var
   nome, iniciais: caractere
   i: inteiro
inicio
   escreva("Nome completo: ")
   leia(nome)
   iniciais <- maiusc(copia(nome, 1, 1))
   para i de 2 ate compr(nome) faca
      se copia(nome, i - 1, 1) = " " entao
         iniciais <- iniciais + maiusc(copia(nome, i, 1))
      fimse
   fimpara
   escreval("Iniciais: ", iniciais)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string nome, iniciais;
    cout << "Nome completo: ";
    getline(cin, nome);
    for (size_t i = 0; i < nome.size(); i++) {
        if (i == 0 || nome[i - 1] == ' ') {
            iniciais += char(toupper((unsigned char) nome[i]));
        }
    }
    cout << "Iniciais: " << iniciais << endl;
    return 0;
}'''),
            ('p', 'O teste i == 0 vem antes de nome[i - 1] no ||: quando i é 0, a primeira parte já é '
                  'verdadeira e a segunda nem é avaliada, o que evita acessar nome[-1] (curto-circuito, '
                  'Seção 3.6).'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Contar palavras. Escreva um programa que leia uma frase e mostre quantas palavras ela tem. '
            'Atenção: a frase pode ter espaços no começo, no fim e vários espaços seguidos entre as '
            'palavras.'
        ),
        'exemplos': [
            ('o rato roeu a roupa', 'Palavras: 5'),
            ('   muitos     espaços   aqui  ', 'Palavras: 3'),
            ('sozinha', 'Palavras: 1'),
        ],
        'resolucao': [
            ('p', 'Contar espaços não funciona quando há espaços sobrando. O que define uma palavra é o seu '
                  'começo: um caractere que não é espaço e que vem logo depois de um espaço (ou no início '
                  'da frase). Uma variável lógica, dentroDePalavra, guarda se o caractere anterior fazia '
                  'parte de uma palavra.'),
            ('Portugol', '''algoritmo "ContarPalavras"
var
   frase: caractere
   i, palavras: inteiro
   dentro: logico
inicio
   escreva("Frase: ")
   leia(frase)
   palavras <- 0
   dentro <- falso
   para i de 1 ate compr(frase) faca
      se copia(frase, i, 1) = " " entao
         dentro <- falso
      senao
         se nao dentro entao
            palavras <- palavras + 1
            dentro <- verdadeiro
         fimse
      fimse
   fimpara
   escreval("Palavras: ", palavras)
fimalgoritmo'''),
            ('C++', '''#include <iostream>
#include <string>
using namespace std;

int main() {
    string frase;
    cout << "Frase: ";
    getline(cin, frase);
    int palavras = 0;
    bool dentroDePalavra = false;
    for (char c : frase) {
        if (c == ' ') {
            dentroDePalavra = false;
        } else if (!dentroDePalavra) {   // começo de palavra
            palavras++;
            dentroDePalavra = true;
        }
    }
    cout << "Palavras: " << palavras << endl;
    return 0;
}'''),
            ('p', 'Esse padrão, uma variável que lembra o estado anterior enquanto o laço percorre o texto, '
                  'resolve muitos problemas de processamento de texto.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Senha forte. Uma senha é forte quando tem pelo menos 8 caracteres, uma letra maiúscula, uma '
            'minúscula e um dígito. Escreva um programa que leia uma senha e mostre "Senha forte" ou '
            '"Senha fraca", e, no segundo caso, liste o que falta, um item por linha.'
        ),
        'exemplos': [
            ('Senha123', 'Senha forte'),
            ('abc', 'Senha fraca\n- pelo menos 8 caracteres\n- uma letra maiúscula\n- um dígito'),
            ('SENHASEGURA9', 'Senha fraca\n- uma letra minúscula'),
        ],
        'resolucao': [
            ('p', 'Percorra a senha uma vez marcando, em variáveis lógicas, o que foi encontrado: isupper, '
                  'islower e isdigit (Seção 8.4) testam cada caractere. Depois do laço, cada variável '
                  'falsa vira uma linha da lista do que falta.'),
            ('C++', '''#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string senha;
    cout << "Senha: ";
    cin >> senha;
    bool maiuscula = false, minuscula = false, digito = false;
    for (unsigned char c : senha) {
        if (isupper(c)) maiuscula = true;
        if (islower(c)) minuscula = true;
        if (isdigit(c)) digito = true;
    }
    bool tamanho = senha.size() >= 8;
    if (tamanho && maiuscula && minuscula && digito) {
        cout << "Senha forte" << endl;
    } else {
        cout << "Senha fraca" << endl;
        if (!tamanho) cout << "- pelo menos 8 caracteres" << endl;
        if (!maiuscula) cout << "- uma letra maiúscula" << endl;
        if (!minuscula) cout << "- uma letra minúscula" << endl;
        if (!digito) cout << "- um dígito" << endl;
    }
    return 0;
}'''),
            ('Portugol', '''algoritmo "SenhaForte"
var
   senha, c: caractere
   i: inteiro
   mai, mins, dig: logico
inicio
   escreva("Senha: ")
   leia(senha)
   mai <- falso
   mins <- falso
   dig <- falso
   para i de 1 ate compr(senha) faca
      c <- copia(senha, i, 1)
      se (c >= "A") e (c <= "Z") entao
         mai <- verdadeiro
      fimse
      se (c >= "a") e (c <= "z") entao
         mins <- verdadeiro
      fimse
      se (c >= "0") e (c <= "9") entao
         dig <- verdadeiro
      fimse
   fimpara
   se (compr(senha) >= 8) e mai e mins e dig entao
      escreval("Senha forte")
   senao
      escreval("Senha fraca")
      se compr(senha) < 8 entao
         escreval("- pelo menos 8 caracteres")
      fimse
      se nao mai entao
         escreval("- uma letra maiúscula")
      fimse
      se nao mins entao
         escreval("- uma letra minúscula")
      fimse
      se nao dig entao
         escreval("- um dígito")
      fimse
   fimse
fimalgoritmo'''),
            ('p', 'No Portugol, sem funções como isupper, a comparação usa a ordem da tabela de caracteres: '
                  'uma letra maiúscula está entre "A" e "Z" (Seção 8.1).'),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Compactação de texto. Escreva um programa que leia uma palavra e a compacte trocando cada '
            'sequência de letras iguais pela letra seguida do número de repetições. Essa técnica, chamada '
            'de codificação por comprimento de sequência (RLE), é usada em formatos de imagem.'
        ),
        'exemplos': [
            ('aaabccdddd', 'a3b1c2d4'),
            ('abc', 'a1b1c1'),
            ('zzzzzzzzzzzz', 'z12'),
        ],
        'resolucao': [
            ('p', 'Percorra a palavra contando quantas vezes seguidas o caractere atual se repete. Quando o '
                  'próximo caractere for diferente (ou a palavra acabar), a sequência terminou: acrescente '
                  'o caractere e a contagem ao resultado e recomece a contagem. O número pode ter mais de '
                  'um dígito, por isso é convertido com to_string.'),
            ('C++', '''#include <iostream>
#include <string>
using namespace std;

int main() {
    string palavra, resultado;
    cout << "Palavra: ";
    cin >> palavra;
    int conta = 1;
    for (size_t i = 0; i < palavra.size(); i++) {
        bool fimDaSequencia = i + 1 == palavra.size()
                              || palavra[i + 1] != palavra[i];
        if (fimDaSequencia) {
            resultado += palavra[i];
            resultado += to_string(conta);
            conta = 1;
        } else {
            conta++;
        }
    }
    cout << resultado << endl;
    return 0;
}'''),
            ('Portugol', '''algoritmo "RLE"
var
   palavra, resultado: caractere
   i, conta: inteiro
inicio
   escreva("Palavra: ")
   leia(palavra)
   resultado <- ""
   conta <- 1
   para i de 1 ate compr(palavra) faca
      se (i = compr(palavra)) ou (copia(palavra, i + 1, 1) <> copia(palavra, i, 1)) entao
         resultado <- resultado + copia(palavra, i, 1) + numpcarac(conta)
         conta <- 1
      senao
         conta <- conta + 1
      fimse
   fimpara
   escreval(resultado)
fimalgoritmo'''),
            ('p', 'A condição testa primeiro se i é a última posição. Só quando não é, palavra[i + 1] é '
                  'acessado, o que evita ler além do fim da string. Um bom desafio extra: escreva o '
                  'programa que faz o caminho inverso, de "a3b1c2d4" de volta para "aaabccdddd".'),
        ],
    },
]
