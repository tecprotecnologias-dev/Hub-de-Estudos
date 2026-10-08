import { apostilas } from '../data/apostilas'
import type { Apostila, ConteudoCapitulo } from '../data/tipos'

// Cada capítulo é carregado só quando o aluno abre, para o site continuar leve.
const arquivos = import.meta.glob<ConteudoCapitulo>('../data/capitulos/*.json', { import: 'default' })

export async function carregarCapitulo(id: string): Promise<ConteudoCapitulo | null> {
  const carregar = arquivos[`../data/capitulos/${id}.json`]
  return carregar ? carregar() : null
}

/** Apostilas da disciplina, com os capítulos em ordem. */
export function apostilasDaDisciplina(disciplinaId: string): Apostila[] {
  return apostilas
    .filter((a) => a.disciplinaId === disciplinaId)
    .sort((a, b) => (a.capitulo ?? 999) - (b.capitulo ?? 999) || a.titulo.localeCompare(b.titulo, 'pt-BR'))
}

export function linkApostila(a: Apostila) {
  return a.arquivo ? import.meta.env.BASE_URL + a.arquivo : `#/apostila/${a.id}`
}

export function rotuloApostila(a: Apostila) {
  if (!a.capitulo) return a.rotulo ?? 'Apostila'
  return `${a.rotulo ?? 'Capítulo'} ${a.capitulo}`
}

/** Separa os capítulos principais dos grupos complementares (ex.: "Material prático"), mantendo a ordem. */
export function gruposDeApostila(lista: Apostila[]): [string, Apostila[]][] {
  const grupos = new Map<string, Apostila[]>()
  for (const a of lista) {
    const g = a.grupo ?? ''
    grupos.set(g, [...(grupos.get(g) ?? []), a])
  }
  return [...grupos.entries()].sort(([a], [b]) => (a === '' ? -1 : b === '' ? 1 : 0))
}
