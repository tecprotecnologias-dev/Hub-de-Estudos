// Níveis de ensino do cadastro (pedido de 22/10/2026). Cada aluno escolhe o nível e o ano ou
// período em que está; ele vê somente as disciplinas do seu nível e do ano/período atual
// (regra de acesso em podeVerDisciplina, lib/auth.tsx). Disciplinas e contas sem nível são da Graduação (o conteúdo que já existia).

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
  // na Graduação, o número de períodos depende do tipo do curso (veja etapasDoCurso)
  { id: 'graduacao', nome: 'Graduação', etapas: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], rotulo: 'período' },
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

export type TipoGraduacao = 'bacharelado' | 'licenciatura' | 'tecnologo'

export const TIPOS_GRADUACAO: { id: TipoGraduacao; nome: string }[] = [
  { id: 'bacharelado', nome: 'Bacharelado' },
  { id: 'licenciatura', nome: 'Licenciatura' },
  { id: 'tecnologo', nome: 'Tecnólogo' },
]

export interface DadosCurso {
  id: string
  nome: string
  tipo: TipoGraduacao
}

// O id é gravado no cadastro do aluno: não mude o id de um curso que já tem alunos.
export const CURSOS: DadosCurso[] = [
  { id: 'administracao', nome: 'Administração', tipo: 'bacharelado' },
  { id: 'direito', nome: 'Direito', tipo: 'bacharelado' },
  { id: 'medicina', nome: 'Medicina', tipo: 'bacharelado' },
  { id: 'engenharia-civil', nome: 'Engenharia Civil', tipo: 'bacharelado' },
  { id: 'psicologia', nome: 'Psicologia', tipo: 'bacharelado' },
  { id: 'ciencia-da-computacao', nome: 'Ciência da Computação', tipo: 'bacharelado' },
  { id: 'enfermagem', nome: 'Enfermagem', tipo: 'bacharelado' },
  { id: 'pedagogia', nome: 'Pedagogia', tipo: 'licenciatura' },
  { id: 'letras', nome: 'Letras', tipo: 'licenciatura' },
  { id: 'matematica', nome: 'Matemática', tipo: 'licenciatura' },
  { id: 'historia', nome: 'História', tipo: 'licenciatura' },
  { id: 'biologia', nome: 'Biologia', tipo: 'licenciatura' },
  { id: 'analise-e-desenvolvimento-de-sistemas', nome: 'Análise e Desenvolvimento de Sistemas', tipo: 'tecnologo' },
  { id: 'gestao-de-recursos-humanos', nome: 'Gestão de Recursos Humanos', tipo: 'tecnologo' },
  { id: 'gestao-financeira', nome: 'Gestão Financeira', tipo: 'tecnologo' },
  { id: 'marketing', nome: 'Marketing', tipo: 'tecnologo' },
  { id: 'logistica', nome: 'Logística', tipo: 'tecnologo' },
  { id: 'sistemas-para-internet', nome: 'Sistemas para Internet', tipo: 'tecnologo' },
]

export function tipoDoCurso(curso: string | null | undefined): TipoGraduacao | null {
  return CURSOS.find((c) => c.id === curso)?.tipo ?? null
}

/**
 * Em que período o aluno cursa as optativas de cada curso (pela matriz; em Sistemas para
 * Internet, a "Optativa I" fica no 4º período). Só os alunos desse período veem as
 * optativas; os outros podem pedir acesso. Curso sem período aqui: optativas para todos.
 */
export const PERIODO_DAS_OPTATIVAS: Record<string, number> = {
  'sistemas-para-internet': 4,
}

/** Períodos do curso: Tecnólogo até o 5º; Bacharelado e Licenciatura até o 10º (pedido de 23/10/2026). */
export function etapasDoCurso(curso: string | null | undefined): number[] {
  const ultimo = tipoDoCurso(curso ?? CURSO_PADRAO) === 'tecnologo' ? 5 : 10
  return Array.from({ length: ultimo }, (_, i) => i + 1)
}

/** Anos ou períodos possíveis para o nível (e, na Graduação, para o curso). */
export function etapasDe(nivel: Nivel | null | undefined, curso: string | null | undefined): number[] {
  return (nivel ?? NIVEL_PADRAO) === 'graduacao' ? etapasDoCurso(curso) : dadosNivel(nivel).etapas
}

/** Cursos separados por tipo de graduação, para as caixas de seleção (<optgroup>). */
export function cursosPorTipo(cursos: DadosCurso[] = CURSOS) {
  return TIPOS_GRADUACAO.map((t) => ({ ...t, cursos: cursos.filter((c) => c.tipo === t.id) })).filter(
    (t) => t.cursos.length > 0,
  )
}

export const CURSO_PADRAO = 'sistemas-para-internet'

export function nomeCurso(curso: string | null | undefined): string {
  return CURSOS.find((c) => c.id === (curso ?? CURSO_PADRAO))?.nome ?? curso ?? '—'
}
