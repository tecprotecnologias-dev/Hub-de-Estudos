import type { Disciplina } from './tipos'
import type { Nivel } from '../lib/niveis'

// Disciplinas da educação básica (pedido de 22/10/2026, lista provisória: "se for o caso,
// depois mudamos"). Cada disciplina existe uma vez por série (ano): o aluno da educação
// básica vê somente as disciplinas da sua série (regra em podeVerDisciplina, lib/auth.tsx).

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

/** Uma disciplina para cada série: id como "fund1-3ano-matematica". */
function criar(nivel: Nivel, prefixo: string, anos: number[], nomes: string[]): Disciplina[] {
  return anos.flatMap((ano) =>
    nomes.map((nome) => ({
      id: `${prefixo}-${ano}ano-${slug(nome)}`,
      nivel,
      periodo: ano,
      nome,
      objetivos: [],
      habilidades: [],
      unidades: [],
      tecnologias: [],
    })),
  )
}

export const disciplinasEscola: Disciplina[] = [
  ...criar('fundamental1', 'fund1', [1, 2, 3, 4, 5], FUNDAMENTAL),
  ...criar('fundamental2', 'fund2', [6, 7, 8, 9], FUNDAMENTAL),
  ...criar('medio', 'medio', [1, 2, 3], MEDIO),
]
