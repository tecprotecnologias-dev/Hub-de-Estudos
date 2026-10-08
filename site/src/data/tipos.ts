export type Nivel = 'facil' | 'medio' | 'dificil'

export interface Unidade {
  titulo: string
  topicos: string[]
}

export interface Disciplina {
  id: string
  /** 1 a 5; 0 = optativa */
  periodo: number
  nome: string
  objetivos: string[]
  habilidades: string[]
  unidades: Unidade[]
  tecnologias: string[]
  bibliografia: { basica: string[]; complementar: string[] }
}

export type ParteContexto =
  | { t: 'citacao'; texto: string; traducao?: string; fonte?: string }
  | { t: 'p'; texto: string }
  | { t: 'fonte'; texto: string }
  /** src relativo à pasta public, ex.: 'questoes/gestaoweb/gestaoweb-cap1-figura1.png' */
  | { t: 'imagem'; src: string; legenda?: string }

export type ParteResolucao = { t: 'p'; texto: string } | { t: 'codigo'; texto: string }

interface QuestaoBase {
  id: string
  /** id da disciplina (veja src/data/disciplinas.ts) */
  disciplinaId: string
  /** id do capítulo/módulo da apostila (veja src/data/apostilas.ts), ex.: 'engsoft-cap1' */
  capituloId: string
  nivel?: Nivel
  /** texto motivador: citação (com tradução, se for em outra língua) e a fonte */
  texto?: { citacao: string; traducao?: string; fonte?: string }
  /** caso aplicado (um parágrafo por item), mostrado antes do enunciado */
  caso?: string[]
  /** alternativa a texto + caso: partes na ordem do Word (citações, parágrafos, figuras) */
  contexto?: ParteContexto[]
  enunciado: string
}

export interface QuestaoObjetiva extends QuestaoBase {
  tipo: 'objetiva'
  alternativas: string[]
  /** índice da alternativa correta (0 = A, 1 = B, ...) */
  correta: number
  /** explicação mostrada depois que o aluno entrega */
  resolucao?: string
}

export interface QuestaoDiscursiva extends QuestaoBase {
  tipo: 'discursiva'
  /** itens a), b), c)... da questão */
  itens?: string[]
  /** exercício prático (feito no computador): sem campo de resposta nem linhas na prova impressa */
  pratica?: boolean
  /** resolução passo a passo, com trechos de código */
  resolucao?: ParteResolucao[]
  /** resposta esperada, mostrada quando o aluno clica em "Ver resposta esperada" */
  respostaEsperada?: string
  /** linhas para resposta na prova impressa (padrão: 6) */
  linhas?: number
}

export type Questao = QuestaoObjetiva | QuestaoDiscursiva

export interface Apostila {
  id: string
  titulo: string
  disciplinaId: string
  /** títulos das unidades do conteúdo programático que a apostila cobre */
  unidades?: string[]
  descricao: string
  /** número do capítulo, quando a apostila é dividida em capítulos */
  capitulo?: number
  /** agrupa capítulos complementares em uma seção à parte, ex.: "Material prático" */
  grupo?: string
  /** como a parte é chamada na apostila (padrão: "Capítulo"), ex.: "Módulo" */
  rotulo?: string
  /**
   * PDF dentro da pasta public (ex.: "apostilas/grafos.pdf").
   * Sem arquivo, o conteúdo é lido de src/data/capitulos/<id>.json.
   */
  arquivo?: string
}

export type Bloco =
  | { t: 'h2'; id: string; texto: string }
  | { t: 'h3'; texto: string }
  | { t: 'p'; html: string; estilo?: 'destaque' | 'nota' | 'debate' }
  | { t: 'lista'; numerada: boolean; itens: string[] }
  | { t: 'tabela'; cabecalho: string[]; linhas: string[][] }
  | { t: 'codigo'; texto: string }
  | { t: 'imagem'; src: string; alt: string; grande?: boolean }
  | { t: 'quadro'; tipo: 'exemplo' | 'atencao' | 'boa-pratica' | 'resposta' | 'nota'; titulo: string; blocos: Bloco[] }

export interface ConteudoCapitulo {
  numero: number | null
  titulo: string
  blocos: Bloco[]
}

export const NOMES_NIVEL: Record<Nivel, string> = {
  facil: 'Fácil',
  medio: 'Médio',
  dificil: 'Difícil',
}
