import { useState, type FormEvent } from 'react'
import { Link, Navigate } from 'react-router-dom'
import { definirNovaSenha, useAuth } from '../../lib/auth'
import { authConfigurado } from '../../lib/supabase'
import { AvisoSemCadastro } from './AvisoSemCadastro'

const MIN_SENHA = 8

// Aberta pelo link do e-mail de "esqueci minha senha": o Supabase já fez o login
// temporário, e a pessoa escolhe a nova senha.
export default function RedefinirSenha() {
  const { pronto, sessao } = useAuth()
  const [senha, setSenha] = useState('')
  const [confirmar, setConfirmar] = useState('')
  const [erro, setErro] = useState<string | null>(null)
  const [feito, setFeito] = useState(false)
  const [enviando, setEnviando] = useState(false)

  if (!authConfigurado) return <AvisoSemCadastro />
  if (!pronto) return <p className="dica">Carregando…</p>
  if (!sessao && !feito) return <Navigate to="/esqueci-senha" replace />

  async function enviar(e: FormEvent) {
    e.preventDefault()
    setErro(null)
    if (senha.length < MIN_SENHA) return setErro(`A senha precisa ter pelo menos ${MIN_SENHA} caracteres.`)
    if (senha !== confirmar) return setErro('As duas senhas não são iguais.')
    setEnviando(true)
    const falha = await definirNovaSenha(senha)
    setEnviando(false)
    if (falha) setErro(falha)
    else setFeito(true)
  }

  if (feito) {
    return (
      <section className="cartao-acesso">
        <h1>Senha alterada</h1>
        <p>Pronto! A sua nova senha já está valendo.</p>
        <Link to="/" className="botao">
          Ir para o início
        </Link>
      </section>
    )
  }

  return (
    <section className="cartao-acesso">
      <h1>Criar nova senha</h1>
      <form onSubmit={enviar} className="formulario-acesso">
        <label>
          Nova senha
          <input
            type="password"
            autoComplete="new-password"
            required
            minLength={MIN_SENHA}
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
          />
        </label>
        <label>
          Repita a nova senha
          <input
            type="password"
            autoComplete="new-password"
            required
            value={confirmar}
            onChange={(e) => setConfirmar(e.target.value)}
          />
        </label>
        {erro && (
          <p className="erro-acesso" role="alert">
            {erro}
          </p>
        )}
        <button type="submit" disabled={enviando}>
          {enviando ? 'Salvando…' : 'Salvar nova senha'}
        </button>
      </form>
    </section>
  )
}
