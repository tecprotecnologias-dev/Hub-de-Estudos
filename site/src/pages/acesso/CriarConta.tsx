import { useState, type FormEvent } from 'react'
import { Link, Navigate, useNavigate } from 'react-router-dom'
import { criarConta, useAuth } from '../../lib/auth'
import { authConfigurado } from '../../lib/supabase'
import { AvisoSemCadastro } from './AvisoSemCadastro'

const PERIODOS_CURSO = [1, 2, 3, 4, 5]
const MIN_SENHA = 8

export default function CriarConta() {
  const { sessao } = useAuth()
  const navegar = useNavigate()
  const [nome, setNome] = useState('')
  const [matricula, setMatricula] = useState('')
  const [periodo, setPeriodo] = useState('')
  const [email, setEmail] = useState('')
  const [senha, setSenha] = useState('')
  const [confirmar, setConfirmar] = useState('')
  const [aceite, setAceite] = useState(false)
  const [erro, setErro] = useState<string | null>(null)
  const [enviando, setEnviando] = useState(false)
  const [confirmarEmail, setConfirmarEmail] = useState(false)

  if (!authConfigurado) return <AvisoSemCadastro />
  if (sessao && !confirmarEmail) return <Navigate to="/" replace />

  if (confirmarEmail) {
    return (
      <section className="cartao-acesso">
        <h1>Confirme o seu e-mail</h1>
        <p>
          Enviamos uma mensagem para <strong>{email.trim()}</strong>. Abra o link que está nela para ativar a sua conta
          e depois entre com o seu e-mail e a sua senha.
        </p>
        <p className="dica">Não chegou? Veja a caixa de spam ou de promoções.</p>
        <Link to="/entrar" className="botao">
          Ir para Entrar
        </Link>
      </section>
    )
  }

  async function enviar(e: FormEvent) {
    e.preventDefault()
    setErro(null)
    if (nome.trim().split(/\s+/).length < 2) return setErro('Informe o seu nome completo (nome e sobrenome).')
    if (!matricula.trim()) return setErro('Informe a sua matrícula.')
    if (!periodo) return setErro('Escolha o período que você está cursando.')
    if (senha.length < MIN_SENHA) return setErro(`A senha precisa ter pelo menos ${MIN_SENHA} caracteres.`)
    if (senha !== confirmar) return setErro('As duas senhas não são iguais.')
    if (!aceite) return setErro('Para criar a conta, é preciso aceitar a Política de Privacidade.')
    setEnviando(true)
    const r = await criarConta({ nome, matricula, periodo: Number(periodo), email, senha })
    setEnviando(false)
    if (r.erro) setErro(r.erro)
    else if (r.precisaConfirmar) setConfirmarEmail(true)
    else navegar('/', { replace: true })
  }

  return (
    <section className="cartao-acesso">
      <h1>Criar conta</h1>
      <p className="dica">
        O seu período define as disciplinas que você acessa: as do seu período, as dos anteriores e as optativas.
      </p>
      <form onSubmit={enviar} className="formulario-acesso">
        <label>
          Nome completo
          <input autoComplete="name" required value={nome} onChange={(e) => setNome(e.target.value)} />
        </label>
        <div className="linha-campos">
          <label>
            Matrícula
            <input required value={matricula} onChange={(e) => setMatricula(e.target.value)} />
          </label>
          <label>
            Período
            <select required value={periodo} onChange={(e) => setPeriodo(e.target.value)}>
              <option value="">Escolha…</option>
              {PERIODOS_CURSO.map((p) => (
                <option key={p} value={p}>
                  {p}º período
                </option>
              ))}
            </select>
          </label>
        </div>
        <label>
          E-mail
          <input type="email" autoComplete="email" required value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <div className="linha-campos">
          <label>
            Senha
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
            Repita a senha
            <input
              type="password"
              autoComplete="new-password"
              required
              value={confirmar}
              onChange={(e) => setConfirmar(e.target.value)}
            />
          </label>
        </div>
        <p className="dica pequena">A senha precisa ter pelo menos {MIN_SENHA} caracteres.</p>
        <label className="inline aceite">
          <input type="checkbox" checked={aceite} onChange={(e) => setAceite(e.target.checked)} />
          <span>
            Li e aceito a{' '}
            <Link to="/privacidade" target="_blank">
              Política de Privacidade
            </Link>
            .
          </span>
        </label>
        {erro && (
          <p className="erro-acesso" role="alert">
            {erro}
          </p>
        )}
        <button type="submit" disabled={enviando}>
          {enviando ? 'Criando a conta…' : 'Criar conta'}
        </button>
      </form>
      <p className="links-acesso">
        <span>
          Já tem conta? <Link to="/entrar">Entrar</Link>
        </span>
      </p>
    </section>
  )
}
