import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from 'react'
import type { Session } from '@supabase/supabase-js'
import { authConfigurado, enderecoDoSite, supabase } from './supabase'
import { CURSO_PADRAO, NIVEL_PADRAO, PERIODO_DAS_OPTATIVAS, type Nivel } from './niveis'

// Quem está logado e com que perfil. Os dados do perfil vêm da tabela public.perfis
// (supabase/esquema.sql); o login em si é do Supabase Auth, só com e-mail e senha
// (sem Google: todo aluno passa pelo formulário e informa o período).

export type TipoPerfil = 'aluno' | 'professor' | 'admin'

export interface Perfil {
  id: string
  nome: string
  matricula: string | null
  email: string
  /** celular com DDI e DDD, só dígitos (ex.: 5521999998888); contas antigas podem não ter */
  telefone: string | null
  tipo: TipoPerfil
  /** nível de ensino do aluno; contas antigas, sem nível, são da Graduação */
  nivel: Nivel | null
  /** curso do aluno da Graduação (veja CURSOS em niveis.ts); vazio nos outros níveis */
  curso: string | null
  /** ano ou período dentro do nível, informado no cadastro; só o administrador muda */
  periodo: number | null
  /** cadastro de professor aguardando a aprovação do administrador */
  solicita_professor: boolean
  aceite_privacidade_em: string | null
  criado_em: string
}

export const NOMES_TIPO: Record<TipoPerfil, string> = {
  aluno: 'Aluno',
  professor: 'Professor',
  admin: 'Administrador',
}

interface ContextoAuth {
  /** false enquanto ainda não se sabe se há alguém logado */
  pronto: boolean
  sessao: Session | null
  perfil: Perfil | null
  /** disciplinas de outros períodos liberadas pela administração para este aluno (ids) */
  liberadas: Set<string>
  /** a pessoa chegou pelo link de "esqueci minha senha" e precisa escolher uma nova */
  recuperandoSenha: boolean
  recarregarPerfil: () => Promise<void>
  sair: () => Promise<void>
}

const Contexto = createContext<ContextoAuth | null>(null)

/** Traduz as mensagens de erro mais comuns do Supabase. */
export function traduzirErro(mensagem: string): string {
  const m = mensagem.toLowerCase()
  if (m.includes('invalid login credentials')) return 'E-mail ou senha incorretos.'
  if (m.includes('email not confirmed')) return 'Confirme o seu e-mail antes de entrar: procure a mensagem que enviamos.'
  if (m.includes('user already registered')) return 'Já existe uma conta com este e-mail. Tente entrar ou recuperar a senha.'
  // a matrícula é única: se duas contas tentarem a mesma ao mesmo tempo, o banco recusa a segunda
  if (m.includes('database error saving new user')) return 'Esta matrícula já tem uma conta. Se for a sua, entre ou recupere a senha.'
  if (m.includes('password should be at least')) return 'A senha precisa ter pelo menos 8 caracteres.'
  if (m.includes('rate limit') || m.includes('too many')) return 'Muitas tentativas seguidas. Espere alguns minutos e tente de novo.'
  if (m.includes('unable to validate email') || m.includes('invalid email')) return 'Este e-mail não parece válido.'
  if (m.includes('same as the old')) return 'A nova senha precisa ser diferente da anterior.'
  if (m.includes('failed to fetch') || m.includes('network')) return 'Sem conexão com o servidor. Verifique a internet e tente de novo.'
  return mensagem
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [pronto, setPronto] = useState(!authConfigurado)
  const [sessao, setSessao] = useState<Session | null>(null)
  const [perfil, setPerfil] = useState<Perfil | null>(null)
  const [liberadas, setLiberadas] = useState<Set<string>>(new Set())
  const [recuperandoSenha, setRecuperandoSenha] = useState(false)

  const buscarPerfil = useCallback(async (s: Session | null) => {
    if (!supabase || !s) {
      setPerfil(null)
      setLiberadas(new Set())
      return
    }
    const [{ data }, { data: pedidos }] = await Promise.all([
      supabase.from('perfis').select('*').eq('id', s.user.id).maybeSingle(),
      // pedidos aprovados de disciplinas de outros períodos (sem a tabela ainda, vem vazio)
      supabase.from('pedidos_disciplina').select('disciplina_id').eq('aluno_id', s.user.id).eq('situacao', 'aprovado'),
    ])
    setPerfil((data as Perfil | null) ?? null)
    setLiberadas(new Set(((pedidos as { disciplina_id: string }[] | null) ?? []).map((p) => p.disciplina_id)))
  }, [])

  useEffect(() => {
    if (!supabase) return
    let ativo = true
    supabase.auth.getSession().then(async ({ data }) => {
      if (!ativo) return
      setSessao(data.session)
      await buscarPerfil(data.session)
      if (ativo) setPronto(true)
    })
    const { data: inscricao } = supabase.auth.onAuthStateChange((evento, s) => {
      setSessao(s)
      if (evento === 'PASSWORD_RECOVERY') setRecuperandoSenha(true)
      if (evento === 'SIGNED_OUT') setRecuperandoSenha(false)
      // fora do callback: o Supabase recomenda não aguardar outra chamada aqui dentro
      setTimeout(() => buscarPerfil(s), 0)
    })
    return () => {
      ativo = false
      inscricao.subscription.unsubscribe()
    }
  }, [buscarPerfil])

  const recarregarPerfil = useCallback(() => buscarPerfil(sessao), [buscarPerfil, sessao])

  const sair = useCallback(async () => {
    await supabase?.auth.signOut()
    setPerfil(null)
    setLiberadas(new Set())
    setSessao(null)
  }, [])

  return (
    <Contexto.Provider value={{ pronto, sessao, perfil, liberadas, recuperandoSenha, recarregarPerfil, sair }}>
      {children}
    </Contexto.Provider>
  )
}

export function useAuth(): ContextoAuth {
  const c = useContext(Contexto)
  if (!c) throw new Error('useAuth precisa estar dentro de <AuthProvider>')
  return c
}

/** O perfil pode usar áreas restritas a esses tipos? Sem cadastro configurado, tudo é liberado. */
export function podeAcessar(perfil: Perfil | null, tipos?: TipoPerfil[]): boolean {
  if (!authConfigurado) return true
  if (!perfil || emAnalise(perfil)) return false
  return !tipos || tipos.includes(perfil.tipo)
}

/**
 * O perfil pode ver esta disciplina? (periodo 0 = optativa)
 * Aluno da Graduação: do seu curso, somente o período atual (desde 23/10/2026: nem os
 * períodos anteriores nem os seguintes); as optativas, no período em que a matriz as coloca
 * (PERIODO_DAS_OPTATIVAS).
 * Aluno da educação básica (Fundamental I e II, Médio): somente a sua série.
 * Aluno da Graduação: também as de outros períodos que a administração liberou (`liberadas`).
 * Professor e administrador: tudo.
 */
export function podeVerDisciplina(
  perfil: Perfil | null,
  d: { id?: string; periodo: number; nivel?: Nivel; curso?: string },
  liberadas?: Set<string>,
): boolean {
  if (!authConfigurado) return true
  if (!perfil || emAnalise(perfil)) return false
  if (perfil.tipo !== 'aluno') return true
  if (d.id && liberadas?.has(d.id)) return true
  const nivel = perfil.nivel ?? NIVEL_PADRAO
  if ((d.nivel ?? NIVEL_PADRAO) !== nivel) return false
  if (perfil.periodo == null) return false
  if (nivel !== 'graduacao') return d.periodo === perfil.periodo
  if ((d.curso ?? CURSO_PADRAO) !== (perfil.curso ?? CURSO_PADRAO)) return false
  if (d.periodo === 0) {
    const periodoOptativas = PERIODO_DAS_OPTATIVAS[d.curso ?? CURSO_PADRAO]
    return periodoOptativas == null || periodoOptativas === perfil.periodo
  }
  return d.periodo === perfil.periodo
}

// Ações de login, usadas pelas telas de acesso -------------------------------------

export async function entrarComSenha(email: string, senha: string) {
  const { error } = await supabase!.auth.signInWithPassword({ email: email.trim(), password: senha })
  return error ? traduzirErro(error.message) : null
}

export interface DadosCadastro {
  nome: string
  /** opcional: em branco, a conta é criada sem matrícula */
  matricula: string
  nivel: Nivel
  /** curso, só na Graduação (null nos outros níveis) */
  curso: string | null
  /** ano ou período dentro do nível */
  periodo: number
  email: string
  /** opcional: null quando o celular não foi informado */
  telefone: string | null
  senha: string
}

/**
 * Celular brasileiro digitado em qualquer formato -> só dígitos com o DDI 55
 * (ex.: "(21) 99999-8888" -> "5521999998888"), o formato que o WhatsApp usa.
 * Devolve null se não for um número com DDD válido.
 */
export function normalizarTelefone(texto: string): string | null {
  let d = texto.replace(/\D/g, '')
  if (d.length === 13 && d.startsWith('55')) d = d.slice(2)
  if (d.length === 12 && d.startsWith('55')) d = d.slice(2)
  if (d.length !== 10 && d.length !== 11) return null
  if (d[0] === '0' || d[1] === '0') return null
  return '55' + d
}

/** "5521999998888" -> "(21) 99999-8888" */
export function formatarTelefone(telefone: string | null): string {
  if (!telefone) return '—'
  const d = telefone.startsWith('55') ? telefone.slice(2) : telefone
  if (d.length < 10) return telefone
  return `(${d.slice(0, 2)}) ${d.slice(2, -4)}-${d.slice(-4)}`
}

/** Cadastro pela aba "Sou aluno": nome, e-mail, período e senha; matrícula e celular são opcionais. */
export async function criarConta({ nome, matricula, nivel, curso, periodo, email, telefone, senha }: DadosCadastro) {
  // a matrícula continua única, mas só é conferida quando foi preenchida
  if (matricula.trim()) {
    const { data: emUso, error: erroBusca } = await supabase!.rpc('matricula_em_uso', { m: matricula.trim() })
    if (erroBusca) return { erro: traduzirErro(erroBusca.message), precisaConfirmar: false }
    if (emUso) {
      return {
        erro: 'Esta matrícula já tem uma conta. Se for a sua, entre com o seu e-mail ou recupere a senha.',
        precisaConfirmar: false,
      }
    }
  }
  const { data, error } = await supabase!.auth.signUp({
    email: email.trim(),
    password: senha,
    options: {
      emailRedirectTo: enderecoDoSite(),
      data: {
        nome: nome.trim(),
        matricula: matricula.trim(),
        nivel,
        curso: curso ?? '',
        periodo: String(periodo),
        telefone: telefone ?? '',
        aceite_privacidade: 'true',
      },
    },
  })
  if (error) return { erro: traduzirErro(error.message), precisaConfirmar: false }
  // sem sessão: o projeto exige confirmar o e-mail antes do primeiro acesso
  return { erro: null, precisaConfirmar: !data.session }
}

/** Cadastro pela aba "Sou professor": só nome, e-mail e senha; fica em análise até a aprovação. */
export async function criarContaProfessor({
  nome,
  email,
  telefone,
  senha,
}: Pick<DadosCadastro, 'nome' | 'email' | 'telefone' | 'senha'>) {
  const { data, error } = await supabase!.auth.signUp({
    email: email.trim(),
    password: senha,
    options: {
      emailRedirectTo: enderecoDoSite(),
      data: { nome: nome.trim(), telefone: telefone ?? '', professor: 'true', aceite_privacidade: 'true' },
    },
  })
  if (error) return { erro: traduzirErro(error.message), precisaConfirmar: false }
  return { erro: null, precisaConfirmar: !data.session }
}

/** Cadastro de professor que ainda não foi aprovado: não acessa o conteúdo. */
export function emAnalise(perfil: Perfil | null): boolean {
  return !!perfil && perfil.tipo === 'aluno' && perfil.solicita_professor
}

export async function pedirNovaSenha(email: string) {
  const { error } = await supabase!.auth.resetPasswordForEmail(email.trim(), { redirectTo: enderecoDoSite() })
  return error ? traduzirErro(error.message) : null
}

export async function definirNovaSenha(senha: string) {
  const { error } = await supabase!.auth.updateUser({ password: senha })
  return error ? traduzirErro(error.message) : null
}
