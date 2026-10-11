import { useState, type FormEvent } from 'react'
import { useNavigate } from 'react-router-dom'
import { emAnalise, NOMES_TIPO, traduzirErro, useAuth } from '../../lib/auth'
import { supabase } from '../../lib/supabase'

export default function MinhaConta() {
  const { perfil, recarregarPerfil, sair } = useAuth()
  const navegar = useNavigate()
  const [nome, setNome] = useState(perfil?.nome ?? '')
  const [mensagem, setMensagem] = useState<{ tipo: 'ok' | 'erro'; texto: string } | null>(null)
  const [salvando, setSalvando] = useState(false)

  if (!perfil || !supabase) return null
  const cliente = supabase

  async function salvarNome(e: FormEvent) {
    e.preventDefault()
    if (nome.trim().split(/\s+/).length < 2) {
      setMensagem({ tipo: 'erro', texto: 'Informe o nome completo (nome e sobrenome).' })
      return
    }
    setSalvando(true)
    const { error } = await cliente.from('perfis').update({ nome: nome.trim() }).eq('id', perfil!.id)
    setSalvando(false)
    if (error) setMensagem({ tipo: 'erro', texto: traduzirErro(error.message) })
    else {
      setMensagem({ tipo: 'ok', texto: 'Nome atualizado.' })
      await recarregarPerfil()
    }
  }

  async function excluirConta() {
    const ok = window.confirm(
      'Excluir a sua conta apaga o seu cadastro de forma definitiva. Você perderá o acesso ao site. Continuar?',
    )
    if (!ok) return
    const { error } = await cliente.rpc('excluir_minha_conta')
    if (error) {
      setMensagem({ tipo: 'erro', texto: traduzirErro(error.message) })
      return
    }
    await sair()
    navegar('/', { replace: true })
  }

  async function encerrar() {
    await sair()
    navegar('/', { replace: true })
  }

  return (
    <section className="cartao-acesso cartao-conta">
      <h1>Minha conta</h1>
      <dl className="dados-conta">
        {perfil.tipo === 'aluno' && !perfil.solicita_professor && (
          <>
            <div>
              <dt>Matrícula</dt>
              <dd>{perfil.matricula ?? '—'}</dd>
            </div>
            <div>
              <dt>Período</dt>
              <dd>{perfil.periodo ? `${perfil.periodo}º período` : '—'}</dd>
            </div>
          </>
        )}
        <div>
          <dt>E-mail</dt>
          <dd>{perfil.email}</dd>
        </div>
        <div>
          <dt>Perfil</dt>
          <dd>{emAnalise(perfil) ? 'Professor (cadastro em análise)' : NOMES_TIPO[perfil.tipo]}</dd>
        </div>
      </dl>
      {perfil.tipo === 'aluno' && !perfil.solicita_professor && (
        <p className="dica pequena">
          A matrícula e o período só podem ser alterados pela administração do site. Se o seu período mudou, peça a
          atualização.
        </p>
      )}

      <form onSubmit={salvarNome} className="formulario-acesso">
        <label>
          Nome completo
          <input value={nome} onChange={(e) => setNome(e.target.value)} />
        </label>
        <button type="submit" disabled={salvando || nome.trim() === perfil.nome}>
          {salvando ? 'Salvando…' : 'Salvar nome'}
        </button>
      </form>
      {mensagem && (
        <p className={mensagem.tipo === 'ok' ? 'ok-acesso' : 'erro-acesso'} role="status">
          {mensagem.texto}
        </p>
      )}

      <div className="acoes-conta">
        <button className="secundario" onClick={encerrar}>
          Sair da conta
        </button>
        <button className="perigo" onClick={excluirConta}>
          Excluir minha conta
        </button>
      </div>
    </section>
  )
}
