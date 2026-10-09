import { apostilas } from '../data/apostilas'
import { questoes } from '../data/questoes'
import type { Apostila, ConteudoCapitulo } from '../data/tipos'

// Cada capítulo é carregado só quando o aluno abre, para o site continuar leve.
const arquivos = import.meta.glob<ConteudoCapitulo>('../data/capitulos/*.json', { import: 'default' })

export async function carregarCapitulo(id: string): Promise<ConteudoCapitulo | null> {
  const carregar = arquivos[`../data/capitulos/${id}.json`]
  return carregar ? carregar() : null
}

/** Capítulo de material complementar (cadastrado com grupo): fica fora do gerador de provas. */
export function ehComplementar(capituloId: string) {
  return !!apostilas.find((a) => a.id === capituloId)?.grupo
}

/** Banco do gerador de provas: só questões dos capítulos principais das disciplinas. */
export const questoesDaProva = questoes.filter((q) => !ehComplementar(q.capituloId))

/** Apostilas da disciplina, com os capítulos em ordem. */
export function apostilasDaDisciplina(disciplinaId: string): Apostila[] {
  // grupos na ordem do cadastro (capítulos principais primeiro), para "Anterior/Próximo" não misturar
  // o Módulo 1 com o Capítulo 1 de um livro complementar
  const lista = apostilas.filter((a) => a.disciplinaId === disciplinaId)
  const grupos = [...new Set(lista.map((a) => a.grupo ?? ''))].filter(Boolean)
  const ordemGrupo = (a: Apostila) => (a.grupo ? 1 + grupos.indexOf(a.grupo) : 0)
  // sem número: nos grupos complementares vale a ordem do cadastro (Apêndice A antes do B)
  return lista.sort(
    (a, b) =>
      ordemGrupo(a) - ordemGrupo(b) ||
      (a.capitulo ?? 999) - (b.capitulo ?? 999) ||
      (a.grupo ? apostilas.indexOf(a) - apostilas.indexOf(b) : a.titulo.localeCompare(b.titulo, 'pt-BR')),
  )
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
