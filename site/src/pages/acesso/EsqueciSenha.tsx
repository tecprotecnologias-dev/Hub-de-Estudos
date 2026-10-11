import { useState, type FormEvent } from 'react'
import { Link } from 'react-router-dom'
import { pedirNovaSenha } from '../../lib/auth'
import { authConfigurado } from '../../lib/supabase'
import { AvisoSemCadastro } from './AvisoSemCadastro'

export default function EsqueciSenha() {
  const [email, setEmail] = useState('')
  const [erro, setErro] = useState<string | null>(null)
  const [enviado, setEnviado] = useState(false)
  const [enviando, setEnviando] = useState(false)

  if (!authConfigurado) return <AvisoSemCadastro />

  async function enviar(e: FormEvent) {
    e.preventDefault()
    setEnviando(true)
    setErro(null)
    const falha = await pedirNovaSenha(email)
    setEnviando(false)
    if (falha) setErro(falha)
    else setEnviado(true)
  }

  if (enviado) {
    return (
      <section className="cartao-acesso">
        <h1>Verifique o seu e-mail</h1>
        <p>
          Se existir uma conta com <strong>{email.trim()}</strong>, você vai receber um link para criar uma nova senha.
        </p>
        <p className="dica">Não chegou em alguns minutos? Veja a caixa de spam.</p>
        <Link to="/entrar" className="botao">
          Voltar para Entrar
        </Link>
      </section>
    )
  }

  return (
    <section className="cartao-acesso">
      <h1>Esqueci minha senha</h1>
      <p className="dica">Informe o e-mail da sua conta. Vamos enviar um link para você criar uma nova senha.</p>
      <form onSubmit={enviar} className="formulario-acesso">
        <label>
          E-mail
          <input type="email" autoComplete="email" required value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        {erro && (
          <p className="erro-acesso" role="alert">
            {erro}
          </p>
        )}
        <button type="submit" disabled={enviando}>
          {enviando ? 'Enviando…' : 'Enviar link'}
        </button>
      </form>
      <p className="links-acesso">
        <Link to="/entrar">Voltar para Entrar</Link>
      </p>
    </section>
  )
}
