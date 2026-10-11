import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from 'react'
import type { Session } from '@supabase/supabase-js'
import { authConfigurado, enderecoDoSite, supabase } from './supabase'

// Quem está logado e com que perfil. Os dados do perfil vêm da tabela public.perfis
// (supabase/esquema.sql); o login em si é do Supabase Auth, só com e-mail e senha
// (sem Google: todo aluno passa pelo formulário e informa o período).

export type TipoPerfil = 'aluno' | 'professor' | 'admin'

export interface Perfil {
  id: string
  nome: string
  matricula: string | null
  email: string
  tipo: TipoPerfil
  /** período do curso (1 a 5), informado no cadastro; só o administrador muda */
  periodo: number | null
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
  const [recuperandoSenha, setRecuperandoSenha] = useState(false)

  const buscarPerfil = useCallback(async (s: Session | null) => {
    if (!supabase || !s) {
      setPerfil(null)
      return
    }
    const { data } = await supabase.from('perfis').select('*').eq('id', s.user.id).maybeSingle()
    setPerfil((data as Perfil | null) ?? null)
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
    setSessao(null)
  }, [])

  return (
    <Contexto.Provider value={{ pronto, sessao, perfil, recuperandoSenha, recarregarPerfil, sair }}>
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
  if (!perfil) return false
  return !tipos || tipos.includes(perfil.tipo)
}

/**
 * O perfil pode ver uma disciplina deste período? (periodo 0 = optativa)
 * Aluno: o próprio período e os anteriores, mais as optativas. Professor e administrador: tudo.
 */
export function podeVerPeriodo(perfil: Perfil | null, periodoDisciplina: number): boolean {
  if (!authConfigurado) return true
  if (!perfil) return false
  if (perfil.tipo !== 'aluno') return true
  if (periodoDisciplina === 0) return true
  return perfil.periodo != null && periodoDisciplina <= perfil.periodo
}

// Ações de login, usadas pelas telas de acesso -------------------------------------

export async function entrarComSenha(email: string, senha: string) {
  const { error } = await supabase!.auth.signInWithPassword({ email: email.trim(), password: senha })
  return error ? traduzirErro(error.message) : null
}

export interface DadosCadastro {
  nome: string
  matricula: string
  periodo: number
  email: string
  senha: string
}

export async function criarConta({ nome, matricula, periodo, email, senha }: DadosCadastro) {
  const { data: emUso, error: erroBusca } = await supabase!.rpc('matricula_em_uso', { m: matricula.trim() })
  if (erroBusca) return { erro: traduzirErro(erroBusca.message), precisaConfirmar: false }
  if (emUso) {
    return {
      erro: 'Esta matrícula já tem uma conta. Se for a sua, entre com o seu e-mail ou recupere a senha.',
      precisaConfirmar: false,
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
        periodo: String(periodo),
        aceite_privacidade: 'true',
      },
    },
  })
  if (error) return { erro: traduzirErro(error.message), precisaConfirmar: false }
  // sem sessão: o projeto exige confirmar o e-mail antes do primeiro acesso
  return { erro: null, precisaConfirmar: !data.session }
}

export async function pedirNovaSenha(email: string) {
  const { error } = await supabase!.auth.resetPasswordForEmail(email.trim(), { redirectTo: enderecoDoSite() })
  return error ? traduzirErro(error.message) : null
}

export async function definirNovaSenha(senha: string) {
  const { error } = await supabase!.auth.updateUser({ password: senha })
  return error ? traduzirErro(error.message) : null
}
