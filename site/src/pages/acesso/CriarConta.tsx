import { useState, type FormEvent } from 'react'
import { Link, Navigate, useNavigate } from 'react-router-dom'
import { criarConta, criarContaProfessor, normalizarTelefone, useAuth } from '../../lib/auth'
import { authConfigurado } from '../../lib/supabase'
import { AvisoSemCadastro } from './AvisoSemCadastro'

const PERIODOS_CURSO = [1, 2, 3, 4, 5]
const MIN_SENHA = 8

type Tipo = 'aluno' | 'professor'

// Duas abas: o aluno informa nome, e-mail e período (que define as disciplinas liberadas);
// o professor informa nome e e-mail, e o cadastro fica em análise até a administração
// aprovar. Matrícula e celular aparecem no formulário, mas são opcionais (pedido de
// 22/10/2026). Ninguém se cadastra como administrador.
export default function CriarConta() {
  const { sessao } = useAuth()
  const navegar = useNavigate()
  const [tipo, setTipo] = useState<Tipo>('aluno')
  const [nome, setNome] = useState('')
  const [matricula, setMatricula] = useState('')
  const [periodo, setPeriodo] = useState('')
  const [email, setEmail] = useState('')
  const [telefone, setTelefone] = useState('')
  const [senha, setSenha] = useState('')
  const [confirmar, setConfirmar] = useState('')
  const [aceite, setAceite] = useState(false)
  const [erro, setErro] = useState<string | null>(null)
  const [enviando, setEnviando] = useState(false)
  const [concluido, setConcluido] = useState<{ precisaConfirmar: boolean } | null>(null)

  if (!authConfigurado) return <AvisoSemCadastro />
  if (sessao && !concluido) return <Navigate to="/" replace />

  if (concluido) {
    return (
      <section className="cartao-acesso">
        <h1>{concluido.precisaConfirmar ? 'Confirme o seu e-mail' : 'Conta criada'}</h1>
        {concluido.precisaConfirmar && (
          <>
            <p>
              Enviamos uma mensagem para <strong>{email.trim()}</strong>. Abra o link que está nela para ativar a sua
              conta e depois entre com o seu e-mail e a sua senha.
            </p>
            <p className="dica">Não chegou? Veja a caixa de spam ou de promoções.</p>
          </>
        )}
        {tipo === 'professor' && (
          <p>
            O seu cadastro de professor será analisado pela administração do site. Depois da aprovação, você terá
            acesso a todo o conteúdo e ao Gerar prova.
          </p>
        )}
        <Link to={concluido.precisaConfirmar ? '/entrar' : '/'} className="botao">
          {concluido.precisaConfirmar ? 'Ir para Entrar' : 'Ir para o início'}
        </Link>
      </section>
    )
  }

  async function enviar(e: FormEvent) {
    e.preventDefault()
    setErro(null)
    if (nome.trim().split(/\s+/).length < 2) return setErro('Informe o seu nome completo (nome e sobrenome).')
    if (tipo === 'aluno' && !periodo) return setErro('Escolha o período que você está cursando.')
    // celular opcional: em branco, segue sem ele; preenchido, precisa ser válido
    const celular = telefone.trim() ? normalizarTelefone(telefone) : null
    if (telefone.trim() && !celular)
      return setErro('Confira o celular: informe com DDD, por exemplo (21) 99999-8888, ou deixe em branco.')
    if (senha.length < MIN_SENHA) return setErro(`A senha precisa ter pelo menos ${MIN_SENHA} caracteres.`)
    if (senha !== confirmar) return setErro('As duas senhas não são iguais.')
    if (!aceite) return setErro('Para criar a conta, é preciso aceitar a Política de Privacidade.')
    setEnviando(true)
    const r =
      tipo === 'aluno'
        ? await criarConta({ nome, matricula, periodo: Number(periodo), email, telefone: celular, senha })
        : await criarContaProfessor({ nome, email, telefone: celular, senha })
    setEnviando(false)
    if (r.erro) setErro(r.erro)
    else if (r.precisaConfirmar || tipo === 'professor') setConcluido({ precisaConfirmar: r.precisaConfirmar })
    else navegar('/', { replace: true })
  }

  function trocarTipo(t: Tipo) {
    setTipo(t)
    setErro(null)
  }

  return (
    <section className="cartao-acesso">
      <h1>Criar conta</h1>
      <div className="abas-acesso" role="tablist" aria-label="Tipo de cadastro">
        <button
          type="button"
          role="tab"
          aria-selected={tipo === 'aluno'}
          className={tipo === 'aluno' ? 'ativa' : ''}
          onClick={() => trocarTipo('aluno')}
        >
          Sou aluno
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={tipo === 'professor'}
          className={tipo === 'professor' ? 'ativa' : ''}
          onClick={() => trocarTipo('professor')}
        >
          Sou professor
        </button>
      </div>
      <p className="dica">
        {tipo === 'aluno'
          ? 'O seu período define as disciplinas que você acessa: as do seu período, as dos anteriores e as optativas.'
          : 'O cadastro de professor é analisado pela administração do site antes de liberar o acesso.'}
      </p>
      <form onSubmit={enviar} className="formulario-acesso">
        <label>
          Nome completo
          <input autoComplete="name" required value={nome} onChange={(e) => setNome(e.target.value)} />
        </label>
        <label>
          E-mail
          <input type="email" autoComplete="email" required value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        {tipo === 'aluno' && (
          <div className="linha-campos">
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
            <label>
              Matrícula (opcional)
              <input value={matricula} onChange={(e) => setMatricula(e.target.value)} />
            </label>
          </div>
        )}
        <label>
          Celular (WhatsApp), opcional
          <input
            type="tel"
            inputMode="tel"
            autoComplete="tel-national"
            placeholder="(21) 99999-8888"
            value={telefone}
            onChange={(e) => setTelefone(e.target.value)}
          />
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
          {enviando ? 'Criando a conta…' : tipo === 'aluno' ? 'Criar conta de aluno' : 'Pedir cadastro de professor'}
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
