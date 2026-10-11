import { useState, type FormEvent } from 'react'
import { Link, Navigate, useLocation, useNavigate } from 'react-router-dom'
import { entrarComSenha, useAuth } from '../../lib/auth'
import { authConfigurado } from '../../lib/supabase'
import { AvisoSemCadastro } from './AvisoSemCadastro'

export default function Entrar() {
  const { sessao } = useAuth()
  const navegar = useNavigate()
  const local = useLocation()
  const destino = (local.state as { de?: string } | null)?.de ?? '/'
  const [email, setEmail] = useState('')
  const [senha, setSenha] = useState('')
  const [erro, setErro] = useState<string | null>(null)
  const [enviando, setEnviando] = useState(false)

  if (!authConfigurado) return <AvisoSemCadastro />
  if (sessao) return <Navigate to={destino} replace />

  async function enviar(e: FormEvent) {
    e.preventDefault()
    setEnviando(true)
    setErro(null)
    const falha = await entrarComSenha(email, senha)
    setEnviando(false)
    if (falha) setErro(falha)
    else navegar(destino, { replace: true })
  }

  return (
    <section className="cartao-acesso">
      <h1>Entrar</h1>
      <p className="dica">Use o e-mail e a senha que você cadastrou.</p>
      <form onSubmit={enviar} className="formulario-acesso">
        <label>
          E-mail
          <input type="email" autoComplete="email" required value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <label>
          Senha
          <input
            type="password"
            autoComplete="current-password"
            required
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
          />
        </label>
        {erro && (
          <p className="erro-acesso" role="alert">
            {erro}
          </p>
        )}
        <button type="submit" disabled={enviando}>
          {enviando ? 'Entrando…' : 'Entrar'}
        </button>
      </form>
      <p className="links-acesso">
        <Link to="/esqueci-senha">Esqueci minha senha</Link>
        <span>
          Ainda não tem conta? <Link to="/criar-conta">Criar conta</Link>
        </span>
      </p>
    </section>
  )
}
