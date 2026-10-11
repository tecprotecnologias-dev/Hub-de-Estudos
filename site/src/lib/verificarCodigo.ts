// Verifica se o que o aluno escreveu em um exercício prático parece CÓDIGO, em qualquer
// linguagem. Não executa nem confere se a solução está certa: só barra o que não lembra
// código (letras soltas, números, frases), para que isso não libere o gabarito.
//
// Para ser aceito, o texto precisa ter as três marcas de um código:
//   1. pelo menos MIN_LINHAS linhas preenchidas;
//   2. alguma palavra-chave de programação (algoritmo, leia, se, int, cout, if, for, print...);
//   3. alguma construção típica de código: chamada com parênteses, atribuição, ; no fim de
//      linha ou chaves.

export interface Verificacao {
  ok: boolean
  mensagem: string
}

const MIN_LINHAS = 3

const PALAVRAS_CHAVE = new RegExp(
  '\\b(' +
    [
      // Portugol
      'algoritmo', 'inicio', 'início', 'fimalgoritmo', 'var', 'leia', 'escreva', 'escreval', 'se', 'entao',
      'senao', 'fimse', 'enquanto', 'faca', 'fimenquanto', 'para', 'ate', 'fimpara', 'repita', 'escolha',
      'caso', 'funcao', 'procedimento', 'retorne', 'inteiro', 'real', 'caractere', 'logico', 'vetor',
      // C, C++, Java, Python, JavaScript...
      'int', 'double', 'float', 'char', 'bool', 'boolean', 'string', 'String', 'void', 'main', 'include',
      'using', 'namespace', 'cout', 'cin', 'endl', 'printf', 'scanf', 'if', 'else', 'for', 'while', 'do',
      'switch', 'case', 'return', 'class', 'struct', 'public', 'private', 'static', 'new', 'import', 'def',
      'print', 'input', 'function', 'let', 'const', 'System',
    ].join('|') +
    ')\\b',
  'i',
)

const CONSTRUCOES = [
  /[A-Za-z_]\w*\s*\(.*\)/, // chamada ou cabeçalho: leia(x), main(), print("oi")
  /[A-Za-z_]\w*(\[[^\]]*\])?\s*(<-|:=|=(?!=)|\+=|-=)\s*\S/, // atribuição: x <- 1, x = 1
  /;\s*$/m, // comando terminado em ;
  /[{}]/, // blocos com chaves
]

export function verificarCodigo(codigo: string): Verificacao {
  if (!codigo.trim()) return { ok: false, mensagem: 'Em branco.' }
  const linhas = codigo.split('\n').filter((l) => l.trim()).length
  const pareceCodigo = PALAVRAS_CHAVE.test(codigo) && CONSTRUCOES.some((re) => re.test(codigo))
  if (!pareceCodigo) {
    return { ok: false, mensagem: 'Isso não parece código. Escreva o seu algoritmo em Portugol ou C++.' }
  }
  if (linhas < MIN_LINHAS) {
    return { ok: false, mensagem: `Muito curto para um algoritmo: escreva pelo menos ${MIN_LINHAS} linhas.` }
  }
  return { ok: true, mensagem: 'Pronto.' }
}
