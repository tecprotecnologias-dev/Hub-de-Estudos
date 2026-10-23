// Níveis de ensino do cadastro (pedido de 22/10/2026). Cada aluno escolhe o nível e o ano ou
// período em que está; ele vê as disciplinas do seu nível, do ano/período atual e dos
// anteriores. Disciplinas e contas sem nível são da Graduação (o conteúdo que já existia).

export type Nivel = 'fundamental1' | 'fundamental2' | 'medio' | 'graduacao'

export interface DadosNivel {
  id: Nivel
  nome: string
  /** anos ou períodos possíveis, em ordem */
  etapas: number[]
  /** como a etapa é chamada: "1º ano" ou "1º período" */
  rotulo: 'ano' | 'período'
}

export const NIVEIS: DadosNivel[] = [
  { id: 'fundamental1', nome: 'Ensino Fundamental I', etapas: [1, 2, 3, 4, 5], rotulo: 'ano' },
  { id: 'fundamental2', nome: 'Ensino Fundamental II', etapas: [6, 7, 8, 9], rotulo: 'ano' },
  { id: 'medio', nome: 'Ensino Médio', etapas: [1, 2, 3], rotulo: 'ano' },
  { id: 'graduacao', nome: 'Graduação', etapas: [1, 2, 3, 4, 5], rotulo: 'período' },
]

/** Nível de quem não tem nível gravado (contas e disciplinas anteriores aos níveis). */
export const NIVEL_PADRAO: Nivel = 'graduacao'

export function dadosNivel(nivel: Nivel | null | undefined): DadosNivel {
  return NIVEIS.find((n) => n.id === (nivel ?? NIVEL_PADRAO)) ?? NIVEIS[NIVEIS.length - 1]
}

/** "3º ano" ou "3º período" (0 = optativas) */
export function nomeEtapa(nivel: Nivel | null | undefined, etapa: number): string {
  if (etapa === 0) return 'Optativas'
  return `${etapa}º ${dadosNivel(nivel).rotulo}`
}

/** "Ano" ou "Período", para rótulos de campos */
export function rotuloEtapa(nivel: Nivel | null | undefined): string {
  const r = dadosNivel(nivel).rotulo
  return r.charAt(0).toUpperCase() + r.slice(1)
}

// Cursos da Graduação (pedido de 23/10/2026). O aluno da Graduação escolhe o curso no
// cadastro e vê só as disciplinas dele. Contas e disciplinas da Graduação sem curso gravado
// são de Sistemas para Internet (o conteúdo que já existia). Para um curso novo, basta
// acrescentá-lo aqui e marcar as disciplinas dele com `curso` em src/data/disciplinas.ts.

export interface DadosCurso {
  id: string
  nome: string
}

export const CURSOS: DadosCurso[] = [{ id: 'sistemas-para-internet', nome: 'Sistemas para Internet' }]

export const CURSO_PADRAO = 'sistemas-para-internet'

export function nomeCurso(curso: string | null | undefined): string {
  return CURSOS.find((c) => c.id === (curso ?? CURSO_PADRAO))?.nome ?? curso ?? '—'
}
