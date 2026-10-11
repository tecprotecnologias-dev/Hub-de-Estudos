"""Questões objetivas do Capítulo 5 (Estruturas de repetição)."""

CAPITULO = 'alg1-cap5'

QUESTOES = [
    {
        'nivel': 'facil',
        'codigo': '''for (int i = 0; i < 10; i++) {
    cout << "*";
}''',
        'enunciado': 'Quantos asteriscos o laço acima mostra?',
        'certa': '10',
        'erradas': ['9', '11', 'Infinitos, porque o laço nunca termina'],
        'resolucao': 'O contador vai de 0 a 9: são 10 voltas. Começar em 0 e parar quando i < n é a forma padrão '
                     'de repetir n vezes em C++. Começando em 1 com i < 10, seriam 9.',
        'executar': 'int asteriscos = 0;\nfor (int i = 0; i < 10; i++) asteriscos++;\ncout << asteriscos;',
    },
    {
        'nivel': 'facil',
        'enunciado': 'Qual laço executa o seu bloco pelo menos uma vez, mesmo que a condição comece falsa?',
        'certa': 'do-while (repita ... ate, no Portugol)',
        'erradas': ['while (enquanto, no Portugol)', 'for (para, no Portugol)',
                    'Nenhum: todos testam a condição antes de executar'],
        'resolucao': 'O do-while executa o bloco e só depois testa a condição. Por isso é o laço ideal para pedir '
                     'um dado e repetir o pedido enquanto ele for inválido (Seção 5.2).',
    },
    {
        'nivel': 'medio',
        'codigo': '''int soma = 0;
for (int i = 1; i <= 10; i += 3) {
    soma += i;
}
cout << soma;''',
        'enunciado': 'Qual valor é mostrado?',
        'certa': '22',
        'erradas': ['12', '55', '21'],
        'resolucao': 'O contador anda de 3 em 3: 1, 4, 7 e 10 (10 <= 10 ainda é verdadeiro). A soma é '
                     '1 + 4 + 7 + 10 = 22. Esquecer a última volta, a do 10, dá 12.',
        'executar': True,
    },
    {
        'nivel': 'medio',
        'codigo': '''int conta = 0;
for (int i = 0; i < 4; i++) {
    for (int j = i; j < 4; j++) {
        conta++;
    }
}
cout << conta;''',
        'enunciado': 'Qual valor é mostrado?',
        'certa': '10',
        'erradas': ['16', '6', '4'],
        'resolucao': 'O laço de dentro começa em i, então dá 4 voltas quando i = 0, 3 quando i = 1, 2 quando '
                     'i = 2 e 1 quando i = 3: 4 + 3 + 2 + 1 = 10. Se j começasse sempre em 0, seriam 4 × 4 = 16.',
        'executar': True,
    },
    {
        'nivel': 'dificil',
        'codigo': '''for (int i = 1; i <= 6; i++) {
    if (i % 2 == 0) continue;
    if (i == 5) break;
    cout << i << " ";
}''',
        'enunciado': 'O que o laço acima mostra?',
        'certa': '1 3',
        'erradas': ['1 3 5', '2 4', '1 2 3 4'],
        'resolucao': 'Os pares são pulados pelo continue, que vai direto para a próxima volta. Sobram 1 e 3, que '
                     'são mostrados. No 5, o break encerra o laço antes do cout, e o 5 não aparece.',
        'executar': True,
    },
]
