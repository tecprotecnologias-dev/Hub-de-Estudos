import type { Disciplina } from './tipos'
import type { Nivel } from '../lib/niveis'

// Disciplinas da educação básica (pedido de 22/10/2026, lista provisória: "se for o caso,
// depois mudamos"). Por enquanto, cada disciplina vale para o nível inteiro: o "periodo" é o
// primeiro ano do nível, então o aluno de qualquer ano daquele nível a vê. Para separar por
// ano depois, basta criar uma entrada por ano com o "periodo" do ano.

const FUNDAMENTAL = [
  'Língua Portuguesa',
  'Arte',
  'Educação Física',
  'Língua Inglesa',
  'Matemática',
  'Geometria',
  'Ciências da Natureza',
  'Ciências',
  'Ciências Humanas',
  'História',
  'Geografia',
]

const MEDIO = [
  'Língua Portuguesa e Literatura',
  'Matemática',
  'Biologia',
  'Física',
  'Química',
  'História',
  'Geografia',
  'Filosofia e Sociologia',
  'Inglês',
  'Arte',
  'Educação Física',
]

/** "Língua Portuguesa e Literatura" -> "lingua-portuguesa-e-literatura" */
function slug(texto: string) {
  return texto
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
}

function criar(nivel: Nivel, prefixo: string, primeiroAno: number, nomes: string[]): Disciplina[] {
  return nomes.map((nome) => ({
    id: `${prefixo}-${slug(nome)}`,
    nivel,
    periodo: primeiroAno,
    nome,
    objetivos: [],
    habilidades: [],
    unidades: [],
    tecnologias: [],
  }))
}

export const disciplinasEscola: Disciplina[] = [
  ...criar('fundamental1', 'fund1', 1, FUNDAMENTAL),
  ...criar('fundamental2', 'fund2', 6, FUNDAMENTAL),
  ...criar('medio', 'medio', 1, MEDIO),
]
