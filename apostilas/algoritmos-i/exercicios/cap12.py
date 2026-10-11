"""Exercícios práticos do Capítulo 12 (Introdução à orientação a objetos, C++ e Java)."""

CAPITULO = 'alg1-cap12'

EXERCICIOS = [
    {
        'nivel': 'facil',
        'enunciado': (
            'Classe Retangulo. Crie uma classe Retangulo com os atributos privados largura e altura '
            '(inteiros), um construtor que recebe os dois valores e os métodos area() e perimetro(). O '
            'programa lê as medidas, cria o objeto e mostra os dois resultados. Faça em C++ ou em Java.'
        ),
        'exemplos': [
            ('5\n3', 'Área: 15\nPerímetro: 16'),
            ('10\n10', 'Área: 100\nPerímetro: 40'),
        ],
        'resolucao': [
            ('p', 'É o problema do Exercício 1 do Capítulo 1, agora organizado como uma classe: os dados '
                  'ficam privados, e o cálculo fica nos métodos, que pertencem ao próprio retângulo. Quem '
                  'usa a classe só pede r.area(), sem saber a fórmula.'),
            ('C++', '''#include <iostream>
using namespace std;

class Retangulo {
private:
    int largura, altura;
public:
    Retangulo(int l, int a) : largura(l), altura(a) {}
    int area() const { return largura * altura; }
    int perimetro() const { return 2 * (largura + altura); }
};

int main() {
    int l, a;
    cout << "Largura e altura: ";
    cin >> l >> a;
    Retangulo r(l, a);
    cout << "Área: " << r.area() << endl;
    cout << "Perímetro: " << r.perimetro() << endl;
    return 0;
}'''),
            ('Java', '''import java.util.Scanner;

public class Retangulo {
    private int largura, altura;

    public Retangulo(int largura, int altura) {
        this.largura = largura;
        this.altura = altura;
    }

    public int area() { return largura * altura; }
    public int perimetro() { return 2 * (largura + altura); }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Largura e altura: ");
        int l = entrada.nextInt();
        int a = entrada.nextInt();
        Retangulo r = new Retangulo(l, a);
        System.out.println("Área: " + r.area());
        System.out.println("Perímetro: " + r.perimetro());
    }
}'''),
            ('p', 'Em C++, o const depois de area() indica que o método não altera o objeto. Em Java, o this '
                  'diferencia o atributo do parâmetro de mesmo nome (Seção 12.7).'),
        ],
    },
    {
        'nivel': 'facil',
        'enunciado': (
            'Contador encapsulado. Crie uma classe Contador com um valor privado que começa em 0 e os '
            'métodos incrementar(), decrementar() e getValor(). O valor nunca pode ficar negativo: '
            'decrementar em 0 não faz nada. O programa lê uma sequência de sinais + e - (sem espaços) e '
            'mostra o valor final.'
        ),
        'exemplos': [
            ('++-+', 'Valor final: 2'),
            ('---+', 'Valor final: 1'),
            ('-----', 'Valor final: 0'),
        ],
        'resolucao': [
            ('p', 'A regra "nunca negativo" fica dentro de decrementar, em um único lugar. Como o valor é '
                  'privado e não há um setValor, nenhuma parte do programa consegue deixar o contador '
                  'negativo: é o encapsulamento garantindo uma regra (Seção 12.2).'),
            ('C++', '''#include <iostream>
#include <string>
using namespace std;

class Contador {
private:
    int valor = 0;
public:
    void incrementar() { valor++; }
    void decrementar() {
        if (valor > 0) valor--;     // nunca fica negativo
    }
    int getValor() const { return valor; }
};

int main() {
    string sinais;
    cin >> sinais;
    Contador c;
    for (char s : sinais) {
        if (s == '+') c.incrementar();
        else if (s == '-') c.decrementar();
    }
    cout << "Valor final: " << c.getValor() << endl;
    return 0;
}'''),
            ('Java', '''import java.util.Scanner;

public class Contador {
    private int valor = 0;

    public void incrementar() { valor++; }
    public void decrementar() {
        if (valor > 0) valor--;     // nunca fica negativo
    }
    public int getValor() { return valor; }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String sinais = entrada.next();
        Contador c = new Contador();
        for (char s : sinais.toCharArray()) {
            if (s == '+') c.incrementar();
            else if (s == '-') c.decrementar();
        }
        System.out.println("Valor final: " + c.getValor());
    }
}'''),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Extrato bancário. Usando uma classe ContaBancaria (saldo privado, depositar e sacar que '
            'recusam valores inválidos), processe comandos, um por linha: "D valor" (depósito), "S valor" '
            '(saque) e "F" (fim). Quando um saque for recusado, mostre "Saque recusado". No fim, mostre o '
            'saldo e quantas operações foram aceitas.'
        ),
        'exemplos': [
            ('D 100\nS 30\nS 500\nD 20\nF', 'Saque recusado\nSaldo: 90\nOperações aceitas: 3'),
            ('S 10\nF', 'Saque recusado\nSaldo: 0\nOperações aceitas: 0'),
        ],
        'resolucao': [
            ('p', 'A classe guarda as regras (não sacar mais que o saldo, não aceitar valores negativos) e '
                  'devolve verdadeiro ou falso para dizer se a operação foi feita. O programa principal só '
                  'interpreta os comandos e conta os sucessos. O saldo é inteiro para simplificar; em um '
                  'sistema real, valores em dinheiro costumam ser guardados em centavos.'),
            ('C++', '''#include <iostream>
using namespace std;

class ContaBancaria {
private:
    int saldo = 0;
public:
    bool depositar(int valor) {
        if (valor <= 0) return false;
        saldo += valor;
        return true;
    }
    bool sacar(int valor) {
        if (valor <= 0 || valor > saldo) return false;
        saldo -= valor;
        return true;
    }
    int getSaldo() const { return saldo; }
};

int main() {
    ContaBancaria conta;
    int aceitas = 0;
    char comando;
    while (cin >> comando && comando != 'F') {
        int valor;
        cin >> valor;
        if (comando == 'D' && conta.depositar(valor)) aceitas++;
        else if (comando == 'S') {
            if (conta.sacar(valor)) aceitas++;
            else cout << "Saque recusado" << endl;
        }
    }
    cout << "Saldo: " << conta.getSaldo() << endl;
    cout << "Operações aceitas: " << aceitas << endl;
    return 0;
}'''),
            ('Java', '''import java.util.Scanner;

public class Extrato {
    static class ContaBancaria {
        private int saldo = 0;

        public boolean depositar(int valor) {
            if (valor <= 0) return false;
            saldo += valor;
            return true;
        }
        public boolean sacar(int valor) {
            if (valor <= 0 || valor > saldo) return false;
            saldo -= valor;
            return true;
        }
        public int getSaldo() { return saldo; }
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        ContaBancaria conta = new ContaBancaria();
        int aceitas = 0;
        while (entrada.hasNext()) {
            String comando = entrada.next();
            if (comando.equals("F")) break;
            int valor = entrada.nextInt();
            if (comando.equals("D") && conta.depositar(valor)) aceitas++;
            else if (comando.equals("S")) {
                if (conta.sacar(valor)) aceitas++;
                else System.out.println("Saque recusado");
            }
        }
        System.out.println("Saldo: " + conta.getSaldo());
        System.out.println("Operações aceitas: " + aceitas);
    }
}'''),
            ('p', 'Na versão em Java, os comandos são comparados com equals, e não com == (Seção 12.6). A '
                  'classe ContaBancaria foi declarada dentro de Extrato (static class) só para caber tudo '
                  'em um único arquivo; em um projeto, ela ficaria no seu próprio arquivo.'),
        ],
    },
    {
        'nivel': 'medio',
        'enunciado': (
            'Herança: funcionários. Crie uma classe Funcionario com nome e salário base e um método '
            'salario() que devolve o salário base, e uma classe Gerente, filha de Funcionario, em que '
            'salario() devolve o base mais um bônus de 20%. Leia N funcionários no formato "tipo nome '
            'salário" (tipo F ou G), mostre o salário de cada um e o total da folha, usando polimorfismo.'
        ),
        'exemplos': [
            ('3\nF Ana 3000\nG Bruno 5000\nF Carla 2500',
             'Ana: 3000\nBruno: 6000\nCarla: 2500\nFolha total: 11500'),
            ('1\nG Davi 10000', 'Davi: 12000\nFolha total: 12000'),
        ],
        'resolucao': [
            ('p', 'Gerente herda tudo de Funcionario e substitui só o cálculo do salário (override). Com '
                  'polimorfismo, o laço que mostra a folha trata todos como Funcionario e chama salario() '
                  'sem perguntar o tipo: cada objeto responde com o seu próprio cálculo (Seção 12.3).'),
            ('Java', '''import java.util.ArrayList;
import java.util.Scanner;

public class Folha {
    static class Funcionario {
        protected String nome;
        protected int base;

        public Funcionario(String nome, int base) {
            this.nome = nome;
            this.base = base;
        }
        public int salario() { return base; }
        public String getNome() { return nome; }
    }

    static class Gerente extends Funcionario {
        public Gerente(String nome, int base) { super(nome, base); }
        @Override
        public int salario() { return base + base * 20 / 100; }
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int n = entrada.nextInt();
        ArrayList<Funcionario> equipe = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String tipo = entrada.next();
            String nome = entrada.next();
            int base = entrada.nextInt();
            if (tipo.equals("G")) equipe.add(new Gerente(nome, base));
            else equipe.add(new Funcionario(nome, base));
        }
        int total = 0;
        for (Funcionario f : equipe) {           // polimorfismo
            System.out.println(f.getNome() + ": " + f.salario());
            total += f.salario();
        }
        System.out.println("Folha total: " + total);
    }
}'''),
            ('C++', '''#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Funcionario {
protected:
    string nome;
    int base;
public:
    Funcionario(const string &n, int b) : nome(n), base(b) {}
    virtual ~Funcionario() {}
    virtual int salario() const { return base; }
    string getNome() const { return nome; }
};

class Gerente : public Funcionario {
public:
    Gerente(const string &n, int b) : Funcionario(n, b) {}
    int salario() const override { return base + base * 20 / 100; }
};

int main() {
    int n;
    cin >> n;
    vector<Funcionario*> equipe;
    for (int i = 0; i < n; i++) {
        char tipo;
        string nome;
        int base;
        cin >> tipo >> nome >> base;
        if (tipo == 'G') equipe.push_back(new Gerente(nome, base));
        else equipe.push_back(new Funcionario(nome, base));
    }
    int total = 0;
    for (Funcionario *f : equipe) {              // polimorfismo
        cout << f->getNome() << ": " << f->salario() << endl;
        total += f->salario();
    }
    cout << "Folha total: " << total << endl;
    for (Funcionario *f : equipe) delete f;
    return 0;
}'''),
            ('p', 'Os atributos são protected: privados para o resto do programa, mas acessíveis às classes '
                  'filhas, para que Gerente possa usar base. Em C++, para guardar objetos de classes '
                  'diferentes no mesmo vetor e ter polimorfismo, o vetor guarda ponteiros, e por isso '
                  'cada objeto criado com new é liberado com delete no fim.'),
        ],
    },
    {
        'nivel': 'dificil',
        'enunciado': (
            'Boletim da turma. Crie uma classe Aluno com nome e duas notas, e os métodos media() e '
            'situacao() (aprovado com média 6 ou mais, recuperação de 4 até menos de 6, reprovado abaixo '
            'de 4), e uma classe Turma que guarda os alunos em uma lista e calcula a média geral. Leia N '
            'alunos ("nome nota1 nota2"), mostre o boletim e a média da turma. Faça em Java (ou em C++).'
        ),
        'exemplos': [
            ('3\nAna 8 7\nBruno 5 4\nCarla 3 2',
             'Ana: 7.5 (aprovado)\nBruno: 4.5 (recuperação)\nCarla: 2.5 (reprovado)\nMédia da turma: 4.83'),
            ('2\nDavi 6 6\nEva 10 9', 'Davi: 6.0 (aprovado)\nEva: 9.5 (aprovado)\nMédia da turma: 7.75'),
        ],
        'resolucao': [
            ('p', 'Cada classe tem uma responsabilidade: Aluno sabe calcular a própria média e a situação; '
                  'Turma sabe guardar alunos e calcular a média geral; o main só lê os dados e mostra o '
                  'boletim. O Scanner usa Locale.US para aceitar notas com ponto decimal (Seção 12.6). A '
                  'média da turma é mostrada com duas casas decimais com String.format.'),
            ('Java', '''import java.util.ArrayList;
import java.util.Locale;
import java.util.Scanner;

public class Boletim {
    static class Aluno {
        private String nome;
        private double nota1, nota2;

        public Aluno(String nome, double nota1, double nota2) {
            this.nome = nome;
            this.nota1 = nota1;
            this.nota2 = nota2;
        }
        public String getNome() { return nome; }
        public double media() { return (nota1 + nota2) / 2; }
        public String situacao() {
            if (media() >= 6) return "aprovado";
            if (media() >= 4) return "recuperação";
            return "reprovado";
        }
    }

    static class Turma {
        private ArrayList<Aluno> alunos = new ArrayList<>();

        public void adicionar(Aluno a) { alunos.add(a); }
        public ArrayList<Aluno> getAlunos() { return alunos; }
        public double mediaGeral() {
            double soma = 0;
            for (Aluno a : alunos) soma += a.media();
            return alunos.isEmpty() ? 0 : soma / alunos.size();
        }
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);
        int n = entrada.nextInt();
        Turma turma = new Turma();
        for (int i = 0; i < n; i++) {
            turma.adicionar(new Aluno(entrada.next(), entrada.nextDouble(),
                                      entrada.nextDouble()));
        }
        for (Aluno a : turma.getAlunos()) {
            System.out.println(a.getNome() + ": " + a.media()
                               + " (" + a.situacao() + ")");
        }
        System.out.println("Média da turma: "
                           + String.format(Locale.US, "%.2f", turma.mediaGeral()));
    }
}'''),
            ('C++', '''#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
using namespace std;

class Aluno {
private:
    string nome;
    double nota1, nota2;
public:
    Aluno(const string &n, double a, double b) : nome(n), nota1(a), nota2(b) {}
    string getNome() const { return nome; }
    double media() const { return (nota1 + nota2) / 2; }
    string situacao() const {
        if (media() >= 6) return "aprovado";
        if (media() >= 4) return "recuperação";
        return "reprovado";
    }
};

class Turma {
private:
    vector<Aluno> alunos;
public:
    void adicionar(const Aluno &a) { alunos.push_back(a); }
    const vector<Aluno> &getAlunos() const { return alunos; }
    double mediaGeral() const {
        double soma = 0;
        for (const Aluno &a : alunos) soma += a.media();
        return alunos.empty() ? 0 : soma / alunos.size();
    }
};

int main() {
    int n;
    cin >> n;
    Turma turma;
    for (int i = 0; i < n; i++) {
        string nome;
        double a, b;
        cin >> nome >> a >> b;
        turma.adicionar(Aluno(nome, a, b));
    }
    cout << fixed << setprecision(1);
    for (const Aluno &al : turma.getAlunos()) {
        cout << al.getNome() << ": " << al.media() << " ("
             << al.situacao() << ")" << endl;
    }
    cout << setprecision(2) << "Média da turma: " << turma.mediaGeral()
         << endl;
    return 0;
}'''),
            ('p', 'O Java mostra um double sempre com casa decimal (6.0), e por isso o C++ usa fixed com '
                  'setprecision(1) para que as duas versões mostrem o mesmo boletim. Para continuar: '
                  'acrescente à Turma um método que devolve o aluno com a maior média, ou que conta '
                  'quantos estão em cada situação.'),
        ],
    },
]
