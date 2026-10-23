import { useState, type FormEvent } from 'react'
import { useNavigate } from 'react-router-dom'
import { emAnalise, formatarTelefone, NOMES_TIPO, normalizarTelefone, traduzirErro, useAuth } from '../../lib/auth'
import { supabase } from '../../lib/supabase'
import { dadosNivel, NIVEL_PADRAO, nomeCurso, nomeEtapa, rotuloEtapa, TIPOS_GRADUACAO, CURSO_PADRAO, tipoDoCurso } from '../../lib/niveis'

export default function MinhaConta() {
  const { perfil, recarregarPerfil, sair } = useAuth()
  const navegar = useNavigate()
  const [nome, setNome] = useState(perfil?.nome ?? '')
  const [telefone, setTelefone] = useState(perfil?.telefone ? formatarTelefone(perfil.telefone) : '')
  const [mensagem, setMensagem] = useState<{ tipo: 'ok' | 'erro'; texto: string } | null>(null)
  const [salvando, setSalvando] = useState(false)

  if (!perfil || !supabase) return null
  const cliente = supabase

  // o celular é opcional: vazio vira null; preenchido, precisa ser válido
  const semCelular = telefone.trim() === ''
  const celular = semCelular ? null : normalizarTelefone(telefone)
  const semMudanca = nome.trim() === perfil.nome && celular === (perfil.telefone ?? null)

  async function salvarDados(e: FormEvent) {
    e.preventDefault()
    if (nome.trim().split(/\s+/).length < 2) {
      setMensagem({ tipo: 'erro', texto: 'Informe o nome completo (nome e sobrenome).' })
      return
    }
    if (!semCelular && !celular) {
      setMensagem({ tipo: 'erro', texto: 'Confira o celular: informe com DDD, por exemplo (21) 99999-8888, ou deixe em branco.' })
      return
    }
    setSalvando(true)
    const { error } = await cliente
      .from('perfis')
      .update({ nome: nome.trim(), telefone: celular })
      .eq('id', perfil!.id)
    setSalvando(false)
    if (error) setMensagem({ tipo: 'erro', texto: traduzirErro(error.message) })
    else {
      setMensagem({ tipo: 'ok', texto: 'Dados atualizados.' })
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
            {perfil.matricula && (
              <div>
                <dt>Matrícula</dt>
                <dd>{perfil.matricula}</dd>
              </div>
            )}
            <div>
              <dt>Nível de ensino</dt>
              <dd>{dadosNivel(perfil.nivel).nome}</dd>
            </div>
            {(perfil.nivel ?? NIVEL_PADRAO) === 'graduacao' && (
              <>
                <div>
                  <dt>Tipo de graduação</dt>
                  <dd>{TIPOS_GRADUACAO.find((t) => t.id === tipoDoCurso(perfil.curso ?? CURSO_PADRAO))?.nome ?? '—'}</dd>
                </div>
                <div>
                  <dt>Curso</dt>
                  <dd>{nomeCurso(perfil.curso)}</dd>
                </div>
              </>
            )}
            <div>
              <dt>{rotuloEtapa(perfil.nivel)}</dt>
              <dd>{perfil.periodo ? nomeEtapa(perfil.nivel, perfil.periodo) : '—'}</dd>
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
          A matrícula, o nível, o curso e o ano ou período só podem ser alterados pela administração do site. Se algum deles
          mudou, peça a atualização.
        </p>
      )}

      <form onSubmit={salvarDados} className="formulario-acesso">
        <label>
          Nome completo
          <input value={nome} onChange={(e) => setNome(e.target.value)} />
        </label>
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
        <button type="submit" disabled={salvando || semMudanca}>
          {salvando ? 'Salvando…' : 'Salvar'}
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
