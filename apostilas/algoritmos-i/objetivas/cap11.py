"""Questões objetivas do Capítulo 11 (Introdução às estruturas de dados)."""

CAPITULO = 'alg1-cap11'

QUESTOES = [
    {
        'nivel': 'facil',
        'codigo': '''struct Aluno {
    string nome;
    double nota;
};

Aluno a = {"Ana", 8.5};''',
        'enunciado': 'Como se acessa a nota do aluno a?',
        'certa': 'a.nota',
        'erradas': ['Aluno.nota', 'a->nota', 'nota(a)'],
        'resolucao': 'Os campos de um registro são acessados com um ponto depois do nome da variável. Aluno é o '
                     'tipo, e não uma variável. A seta (->) é usada quando se tem um ponteiro para o registro '
                     '(Seções 11.1 e 11.7).',
        'executar': '''struct Aluno { string nome; double nota; };
Aluno a = {"Ana", 8.5};
if (a.nota == 8.5) cout << "a.nota";''',
    },
    {
        'nivel': 'facil',
        'enunciado': 'Em uma pilha, os valores 1, 2 e 3 são empilhados nessa ordem. Qual sai primeiro?',
        'certa': '3',
        'erradas': ['1', '2', 'O menor deles'],
        'resolucao': 'Na pilha, o último a entrar é o primeiro a sair (LIFO), como em uma pilha de pratos. Em uma '
                     'fila, sairia o 1.',
    },
    {
        'nivel': 'medio',
        'codigo': '''queue<int> f;
f.push(1);
f.push(2);
f.push(3);
f.pop();
f.push(4);
cout << f.front() << " " << f.size();''',
        'enunciado': 'O que o trecho acima mostra?',
        'certa': '2 3',
        'erradas': ['1 3', '4 3', '2 4'],
        'resolucao': 'Na fila, o primeiro a entrar é o primeiro a sair: o pop remove o 1, e o 4 entra no fim. A '
                     'fila fica 2, 3, 4: o primeiro é o 2, e há 3 elementos.',
        'executar': '#include <iostream>\n#include <queue>\nusing namespace std;\nint main() {\n'
                    'queue<int> f; f.push(1); f.push(2); f.push(3); f.pop(); f.push(4);\n'
                    'cout << f.front() << " " << f.size();\n}',
    },
    {
        'nivel': 'medio',
        'enunciado': 'O que acontece quando um programa cria nós de uma lista com new e nunca usa delete?',
        'certa': 'A memória dos nós fica reservada sem uso até o programa terminar: é um vazamento de memória',
        'erradas': [
            'O compilador acusa erro, porque todo new precisa de um delete',
            'Os nós são apagados automaticamente no fim de cada função',
            'O programa é interrompido no primeiro new que não tiver delete',
        ],
        'resolucao': 'A memória criada com new não some no fim do bloco, como as variáveis locais: ela só é '
                     'devolvida com delete. O compilador não confere isso. Em um programa que roda por muito '
                     'tempo, os vazamentos podem esgotar a memória (Seção 11.6).',
    },
    {
        'nivel': 'dificil',
        'codigo': '''struct No {
    int valor;
    No *prox;
};

No c = {3, nullptr};
No b = {2, &c};
No a = {1, &b};
b.prox = c.prox;
for (No *p = &a; p != nullptr; p = p->prox) {
    cout << p->valor << " ";
}''',
        'enunciado': 'O que o trecho acima mostra?',
        'certa': '1 2',
        'erradas': ['1 2 3', '1 3', '2 3'],
        'resolucao': 'A lista começa como a → b → c. A linha b.prox = c.prox faz b apontar para onde c apontava, '
                     'que é nullptr: o nó c sai da lista. O percurso a partir de a passa por 1 e 2 e para.',
        'executar': True,
    },
]
