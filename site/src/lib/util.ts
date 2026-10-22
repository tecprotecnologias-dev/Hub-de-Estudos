import { disciplinas } from '../data/disciplinas'
import type { Disciplina, Questao } from '../data/tipos'
import { nomeEtapa, type Nivel } from './niveis'

export const LETRAS = ['A', 'B', 'C', 'D', 'E', 'F']

export const PERIODOS = [...new Set(disciplinas.map((d) => d.periodo))].sort((a, b) => (a || 99) - (b || 99))

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
  /** '' = todos */
  periodo: string
  disciplinaId: string
  capituloId: string
  tipo: string
}

export const FILTRO_VAZIO: Filtro = { periodo: '', disciplinaId: '', capituloId: '', tipo: '' }

export function filtrar(lista: Questao[], f: Filtro): Questao[] {
  return lista.filter(
    (q) =>
      (!f.periodo || String(porId.get(q.disciplinaId)?.periodo) === f.periodo) &&
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
