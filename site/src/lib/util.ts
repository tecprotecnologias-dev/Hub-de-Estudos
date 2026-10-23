import { disciplinas } from '../data/disciplinas'
import type { Disciplina, Questao } from '../data/tipos'
import { CURSO_PADRAO, CURSOS, dadosNivel, NIVEIS, NIVEL_PADRAO, nomeCurso, nomeEtapa, etapasDoCurso, tipoDoCurso, type Nivel, type TipoGraduacao } from './niveis'

export const LETRAS = ['A', 'B', 'C', 'D', 'E', 'F']

/**
 * Grupo em que a disciplina aparece nas listas: na educação básica, o nível e a série
 * ("fundamental1:3", "medio:2"...); na Graduação, também o curso
 * ("graduacao:sistemas-para-internet:3"; período 0 = optativas).
 */
export function grupoDe(d: Disciplina): string {
  return chaveGrupo({ nivel: d.nivel ?? NIVEL_PADRAO, curso: d.curso ?? null, etapa: d.periodo })
}

export interface PartesGrupo {
  nivel: Nivel
  /** só na Graduação; null nos outros níveis */
  curso: string | null
  etapa: number
}

export function chaveGrupo({ nivel, curso, etapa }: PartesGrupo): string {
  return nivel === 'graduacao' ? `${nivel}:${curso ?? CURSO_PADRAO}:${etapa}` : `${nivel}:${etapa}`
}

/** Nível, curso e ano/período de um grupo ("medio:2" -> medio, null, 2) */
export function partesDoGrupo(chave: string): PartesGrupo {
  const partes = chave.split(':')
  if (partes.length === 3) return { nivel: partes[0] as Nivel, curso: partes[1], etapa: Number(partes[2]) }
  return { nivel: partes[0] as Nivel, curso: null, etapa: Number(partes[1]) }
}

/** "Ensino Médio – 2º ano" ou "Sistemas para Internet – 3º período" */
export function nomeGrupo(chave: string): string {
  const { nivel, curso, etapa } = partesDoGrupo(chave)
  const antes = nivel === 'graduacao' ? nomeCurso(curso) : dadosNivel(nivel).nome
  return `${antes} – ${nomeEtapa(nivel, etapa)}`
}

/**
 * Todos os grupos possíveis, na ordem das listas: as séries da educação básica, depois, para
 * cada curso da Graduação, os períodos e as optativas.
 */
export const TODOS_GRUPOS: string[] = NIVEIS.flatMap((n) =>
  n.id === 'graduacao'
    ? CURSOS.flatMap((c) => [...etapasDoCurso(c.id), 0].map((etapa) => chaveGrupo({ nivel: n.id, curso: c.id, etapa })))
    : n.etapas.map((etapa) => chaveGrupo({ nivel: n.id, curso: null, etapa })),
)

/** Filtro por turma, nas caixas Nível de ensino, Tipo de graduação e Curso (só na Graduação) e Ano/período; '' = todos. */
export interface FiltroTurma {
  nivel: Nivel | ''
  /** tipo de graduação: bacharelado, licenciatura ou tecnologo */
  tipo: TipoGraduacao | ''
  curso: string
  etapa: string
}

export const TURMA_VAZIA: FiltroTurma = { nivel: '', tipo: '', curso: '', etapa: '' }

export function partesDaDisciplina(d: Disciplina): PartesGrupo {
  return partesDoGrupo(grupoDe(d))
}

/** A disciplina (ou a pessoa) com estas partes passa no filtro? */
export function confereTurma(p: PartesGrupo, f: FiltroTurma): boolean {
  return (
    (!f.nivel || p.nivel === f.nivel) &&
    (!f.tipo || tipoDoCurso(p.curso) === f.tipo) &&
    (!f.curso || p.curso === f.curso) &&
    (!f.etapa || String(p.etapa) === f.etapa)
  )
}

/** Só os grupos que têm disciplina, na mesma ordem. */
export const GRUPOS: string[] = (() => {
  const existentes = new Set(disciplinas.map(grupoDe))
  return TODOS_GRUPOS.filter((g) => existentes.has(g))
})()

/** "3º período" na Graduação, "3º ano" nos outros níveis; 0 = optativas */
export function nomePeriodo(p: number, nivel?: Nivel) {
  return nomeEtapa(nivel, p)
}

const porId = new Map(disciplinas.map((d) => [d.id, d]))

export function buscarDisciplina(id: string): Disciplina | undefined {
  return porId.get(id)
}

export function nomeDisciplina(id: string) {
  return porId.get(id)?.nome ?? id
}


/** Retorna uma cópia embaralhada do array (Fisher-Yates). */
export function embaralhar<T>(lista: T[]): T[] {
  const copia = [...lista]
  for (let i = copia.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[copia[i], copia[j]] = [copia[j], copia[i]]
  }
  return copia
}

/** Embaralha as alternativas de uma questão objetiva, mantendo o gabarito correto. */
export function embaralharAlternativas(q: Questao): Questao {
  if (q.tipo !== 'objetiva') return q
  const ordem = embaralhar(q.alternativas.map((_, i) => i))
  return {
    ...q,
    alternativas: ordem.map((i) => q.alternativas[i]),
    correta: ordem.indexOf(q.correta),
    resolucao: q.resolucao && trocarLetras(q.resolucao, ordem),
  }
}

/**
 * Resoluções citam alternativas com marcas {{A}}...{{E}} (letra original do Word).
 * Troca cada marca pela letra que a alternativa recebeu depois de embaralhada.
 */
export function trocarLetras(texto: string, ordem?: number[]): string {
  return texto.replace(/\{\{([A-F])\}\}/g, (_, letra: string) => {
    const original = LETRAS.indexOf(letra)
    return LETRAS[ordem ? ordem.indexOf(original) : original]
  })
}

export interface Filtro {
  /** nível, curso e ano/período da disciplina */
  turma: FiltroTurma
  disciplinaId: string
  capituloId: string
  tipo: string
}

export const FILTRO_VAZIO: Filtro = { turma: TURMA_VAZIA, disciplinaId: '', capituloId: '', tipo: '' }

export function filtrar(lista: Questao[], f: Filtro): Questao[] {
  return lista.filter(
    (q) =>
      (porId.has(q.disciplinaId) ? confereTurma(partesDaDisciplina(porId.get(q.disciplinaId)!), f.turma) : !f.turma.nivel) &&
      (!f.disciplinaId || q.disciplinaId === f.disciplinaId) &&
      (!f.capituloId || q.capituloId === f.capituloId) &&
      (!f.tipo || q.tipo === f.tipo),
  )
}

/** Primeiro parágrafo de texto da apresentação (pula subtítulos e listas), sem formatação, para o cartão. */
export function resumoApresentacao(texto: string) {
  const blocos = texto.trim().split(/\n\s*\n/)
  const paragrafo = blocos.find((b) => !b.startsWith('## ') && !/^(- |\d+\.\s)/.test(b.trim())) ?? ''
  return paragrafo.replace(/\*\*/g, '').trim()
}
