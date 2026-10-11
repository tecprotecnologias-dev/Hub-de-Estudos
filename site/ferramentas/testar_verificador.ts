// Testa src/lib/verificarCodigo.ts (rode na pasta site com: node ferramentas/testar_verificador.ts)
//   1. todo código das apostilas de Algoritmos I, das soluções dos exercícios e alguns códigos
//      incompletos ou com erro (mas que são código) precisam ser aceitos;
//   2. o que não lembra código (letras, números, frases) precisa ser recusado.
import { readFileSync, readdirSync } from 'node:fs'
import { verificarCodigo } from '../src/lib/verificarCodigo.ts'

let falhas = 0
let total = 0
const esperar = (rotulo: string, codigo: string, deveAceitar: boolean) => {
  total++
  const r = verificarCodigo(codigo)
  if (r.ok !== deveAceitar) {
    falhas++
    console.log(`FALHOU ${rotulo}: ${r.mensagem}\n${codigo.split('\n').slice(0, 6).join('\n')}\n`)
  }
}

// 1a. programas das apostilas
const pasta = '../apostilas/algoritmos-i/capitulos'
for (const arq of readdirSync(pasta)) {
  const tex = readFileSync(`${pasta}/${arq}`, 'utf-8')
  for (const m of tex.matchAll(/\\begin\{Verbatim\}(?:\[[^\]]*\])?\n([\s\S]*?)\\end\{Verbatim\}/g)) {
    const codigo = m[1]
    const programa = /^algoritmo "/.test(codigo) && /^\s*inicio\s*$/m.test(codigo)
    if (programa || /\bint main\s*\(/.test(codigo) || /static void main/.test(codigo)) esperar(arq, codigo, true)
  }
}

// 1b. soluções dos exercícios
const banco = JSON.parse(readFileSync('src/data/questoes/alg1.json', 'utf-8'))
for (const q of banco) for (const p of q.resolucao) if (p.linguagem) esperar(`${q.id} ${p.linguagem}`, p.texto, true)

// 1c. código incompleto ou com erro continua sendo código
const aceitar: [string, string][] = [
  ['Portugol sem fimalgoritmo', 'algoritmo "T"\ninicio\n   leia(x)\n   escreval(x * 2)'],
  ['Portugol com linha estranha', 'algoritmo "T"\ninicio\n   leia(x)\n   mmmm\nfimalgoritmo'],
  ['só o miolo', 'leia(base)\nleia(altura)\narea <- base * altura\nescreval(area)'],
  ['C++ sem ;', 'int main() {\n    double x\n    cin >> x\n    cout << x * 2\n}'],
  ['Python', 'c = float(input())\nf = c * 9 / 5 + 32\nprint(f)'],
]
for (const [rotulo, codigo] of aceitar) esperar(`aceitar: ${rotulo}`, codigo, true)

// 2. o que não é código
const recusar: [string, string][] = [
  ['letras', 'mmmmmmmmmmmm'],
  ['letras em várias linhas', 'mmmm\nmmmm\nmmmm\nmmmm\nmmmm'],
  ['números', '123\n456\n789\n1011'],
  ['letras e números', 'abc 123\nxyz 456\nqwe 789'],
  ['frase', 'não sei fazer\nvou tentar depois\nme ajuda'],
  ['frase com palavra-chave', 'se eu soubesse\nfaria para entregar\nmas ainda não sei'],
  ['símbolos soltos', ';;;;\n{}{}\n()()'],
  ['uma linha de código', 'leia(x)'],
]
for (const [rotulo, codigo] of recusar) esperar(`recusar: ${rotulo}`, codigo, false)

console.log(`${total} casos testados`)
console.log(falhas ? `${falhas} FALHAS` : 'tudo certo')
process.exit(falhas ? 1 : 0)
