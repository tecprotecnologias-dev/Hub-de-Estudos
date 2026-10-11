"""Questões objetivas do Capítulo 12 (Introdução à orientação a objetos)."""

CAPITULO = 'alg1-cap12'

QUESTOES = [
    {
        'nivel': 'facil',
        'enunciado': 'Qual é a relação entre uma classe e um objeto?',
        'certa': 'A classe é o molde que descreve atributos e métodos; o objeto é um exemplar concreto da classe, '
                 'com os seus próprios valores',
        'erradas': [
            'O objeto é o molde, e a classe é um exemplar criado a partir dele',
            'Classe e objeto são a mesma coisa, com nomes diferentes em C++ e em Java',
            'A classe guarda só os métodos, e o objeto guarda só os atributos',
        ],
        'resolucao': 'A classe ContaBancaria descreve que toda conta tem titular e saldo e sabe depositar e sacar; '
                     'a conta da Ana e a do Bruno são dois objetos dessa classe, cada um com o seu saldo '
                     '(Seção 12.1).',
    },
    {
        'nivel': 'facil',
        'enunciado': 'Por que os atributos de uma classe costumam ser privados?',
        'certa': 'Para que só os métodos da própria classe possam alterá-los, garantindo as suas regras, como um '
                 'saldo que nunca fica negativo',
        'erradas': [
            'Para que o programa fique mais rápido',
            'Porque as linguagens orientadas a objetos não permitem atributos públicos',
            'Para que os objetos ocupem menos memória',
        ],
        'resolucao': 'Esse é o encapsulamento: o resto do programa só mexe nos dados por meio dos métodos '
                     'públicos, que validam cada operação. Assim as regras ficam em um único lugar, e a forma de '
                     'guardar os dados pode mudar sem quebrar o resto (Seção 12.2).',
    },
    {
        'nivel': 'medio',
        'codigo': '''String a = new String("oi");
String b = new String("oi");
System.out.println((a == b) + " " + a.equals(b));''',
        'enunciado': 'O que o trecho em Java acima mostra?',
        'certa': 'false true',
        'erradas': ['true true', 'true false', 'false false'],
        'resolucao': 'Em Java, == compara se as duas variáveis apontam para o MESMO objeto, e a e b são dois '
                     'objetos diferentes. Já equals compara o conteúdo, que é igual. Por isso textos são '
                     'comparados com equals (Seção 12.6).',
        'executar_java': '''public class Comparar {
    public static void main(String[] args) {
        String a = new String("oi");
        String b = new String("oi");
        System.out.println((a == b) + " " + a.equals(b));
    }
}''',
    },
    {
        'nivel': 'medio',
        'codigo': '''class Animal {
public:
    virtual string som() const { return "..."; }
    virtual ~Animal() {}
};

class Gato : public Animal {
public:
    string som() const override { return "miau"; }
};

void falar(const Animal &a) { cout << a.som(); }

int main() {
    Gato g;
    falar(g);
}''',
        'enunciado': 'O que o programa em C++ acima mostra?',
        'certa': 'miau',
        'erradas': ['...', '...miau', 'Nada, porque falar recebe um Animal, e não um Gato'],
        'resolucao': 'Como som() é virtual, a chamada a.som() usa o tipo real do objeto, um Gato, mesmo que a '
                     'função receba um Animal: é o polimorfismo. Sem o virtual, seria chamado o método de Animal, '
                     'e a saída seria "..." (Seção 12.3).',
        'executar': True,
    },
    {
        'nivel': 'dificil',
        'codigo': '''ContaBancaria a = new ContaBancaria("Ana", 100);
ContaBancaria c = a;
c.depositar(50);
System.out.println(a.getSaldo());''',
        'enunciado': 'Usando a classe ContaBancaria do Capítulo 12 em Java, o que o trecho acima mostra?',
        'certa': '150.0',
        'erradas': ['100.0', '50.0', 'Nada: c é uma cópia, e o depósito não aparece em a'],
        'resolucao': 'Em Java, uma variável de objeto guarda uma referência. c = a não copia a conta: c e a passam '
                     'a ser dois nomes para o mesmo objeto, e o depósito feito por c aparece no saldo de a '
                     '(Seção 12.7). O Java mostra o double com a casa decimal: 150.0.',
        'executar_java': '''public class Referencia {
    static class ContaBancaria {
        private String titular;
        private double saldo;
        public ContaBancaria(String titular, double inicial) {
            this.titular = titular;
            this.saldo = inicial >= 0 ? inicial : 0;
        }
        public boolean depositar(double valor) {
            if (valor <= 0) return false;
            saldo += valor;
            return true;
        }
        public double getSaldo() { return saldo; }
        public String getTitular() { return titular; }
    }

    public static void main(String[] args) {
        ContaBancaria a = new ContaBancaria("Ana", 100);
        ContaBancaria c = a;
        c.depositar(50);
        System.out.println(a.getSaldo());
    }
}''',
    },
]
