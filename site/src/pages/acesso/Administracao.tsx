import { useEffect, useMemo, useState } from 'react'
import { formatarTelefone, NOMES_TIPO, traduzirErro, useAuth, type Perfil, type TipoPerfil } from '../../lib/auth'
import { supabase } from '../../lib/supabase'
import CamposTurma from '../../lib/CamposTurma'
import type { PedidoDisciplina } from '../../lib/PedidosDisciplina'
import { disciplinas } from '../../data/disciplinas'
import { confereTurma, grupoDe, nomeGrupo, TODOS_GRUPOS, TURMA_VAZIA } from '../../lib/util'
import {
  CURSO_PADRAO,
  cursosPorTipo,
  dadosNivel,
  etapasDe,
  NIVEIS,
  NIVEL_PADRAO,
  nomeCurso,
  type Nivel,
} from '../../lib/niveis'

// Área da administradora: ver os cadastros, mudar o perfil (aluno, professor,
// administrador), o nível de ensino, o curso (Graduação) e o ano/período de cada pessoa, e avançar o ano/período
// de vários alunos de uma vez. As regras do banco garantem que só um administrador consegue.

const TIPOS: TipoPerfil[] = ['aluno', 'professor', 'admin']

/** Aluno de verdade (o professor em análise também é 'aluno' no banco, mas não estuda aqui). */
const ehAluno = (p: Perfil) => p.tipo === 'aluno' && !p.solicita_professor

export default function Administracao() {
  const { perfil: eu } = useAuth()
  const [pessoas, setPessoas] = useState<Perfil[]>([])
  const [carregando, setCarregando] = useState(true)
  const [busca, setBusca] = useState('')
  const [filtroTipo, setFiltroTipo] = useState('')
  const [turma, setTurma] = useState(TURMA_VAZIA)
  const [marcados, setMarcados] = useState<Set<string>>(new Set())
  const [aviso, setAviso] = useState<{ tipo: 'ok' | 'erro'; texto: string } | null>(null)
  // pedidos de alunos da Graduação para disciplinas de outros períodos
  const [pedidos, setPedidos] = useState<PedidoDisciplina[]>([])

  async function carregar() {
    if (!supabase) return
    setCarregando(true)
    const [{ data, error }, { data: dadosPedidos }] = await Promise.all([
      supabase.from('perfis').select('*').order('nome'),
      supabase.from('pedidos_disciplina').select('*').order('criado_em'),
    ])
    setCarregando(false)
    if (error) setAviso({ tipo: 'erro', texto: traduzirErro(error.message) })
    else setPessoas((data as Perfil[]) ?? [])
    setPedidos((dadosPedidos as PedidoDisciplina[] | null) ?? [])
  }

  async function decidir(p: PedidoDisciplina, situacao: 'aprovado' | 'recusado' | null) {
    if (!supabase) return
    // null = retirar uma disciplina já liberada (apaga o pedido)
    const { error } =
      situacao == null
        ? await supabase.from('pedidos_disciplina').delete().eq('id', p.id)
        : await supabase
            .from('pedidos_disciplina')
            .update({ situacao, decidido_em: new Date().toISOString() })
            .eq('id', p.id)
    if (error) return setAviso({ tipo: 'erro', texto: traduzirErro(error.message) })
    setPedidos((ps) =>
      situacao == null ? ps.filter((x) => x.id !== p.id) : ps.map((x) => (x.id === p.id ? { ...x, situacao } : x)),
    )
    setAviso({
      tipo: 'ok',
      texto:
        situacao === 'aprovado'
          ? 'Disciplina liberada.'
          : situacao === 'recusado'
            ? 'Pedido recusado.'
            : 'Acesso retirado.',
    })
  }

  const nomeDaPessoa = (id: string) => pessoas.find((x) => x.id === id)
  const descreverDisciplina = (id: string) => {
    const d = disciplinas.find((x) => x.id === id)
    return d ? `${d.nome} (${nomeGrupo(grupoDe(d))})` : id
  }
  const pedidosPendentes = pedidos.filter((p) => p.situacao === 'pendente')
  const pedidosAprovados = pedidos.filter((p) => p.situacao === 'aprovado')

  useEffect(() => {
    carregar()
  }, [])

  const lista = useMemo(() => {
    const t = busca.trim().toLowerCase()
    return pessoas.filter(
      (p) =>
        (!t ||
          `${p.nome} ${p.matricula ?? ''} ${p.email} ${p.telefone ?? ''} ${p.curso ? nomeCurso(p.curso) : ''}`
            .toLowerCase()
            .includes(t)) &&
        (!filtroTipo || p.tipo === filtroTipo) &&
        // quem não tem nível (professor, administrador) só aparece com o nível em "Todos"
        (!turma.nivel ||
          (!!p.nivel &&
            confereTurma(
              {
                nivel: p.nivel,
                curso: p.nivel === 'graduacao' ? (p.curso ?? CURSO_PADRAO) : null,
                etapa: p.periodo ?? -1,
              },
              turma,
            ))),
    )
  }, [pessoas, busca, filtroTipo, turma])

  async function atualizar(
    id: string,
    campos: Partial<Pick<Perfil, 'tipo' | 'nivel' | 'curso' | 'periodo' | 'solicita_professor'>>,
  ) {
    if (!supabase) return
    const { error } = await supabase.from('perfis').update(campos).eq('id', id)
    if (error) {
      setAviso({ tipo: 'erro', texto: traduzirErro(error.message) })
      return
    }
    setPessoas((ps) => ps.map((p) => (p.id === id ? { ...p, ...campos } : p)))
    setAviso({ tipo: 'ok', texto: 'Alteração salva.' })
  }

  async function avancarPeriodo() {
    if (!supabase) return
    // só avança quem ainda não está no último ano/período do seu nível
    const ultimo = (p: Perfil) => Math.max(...etapasDe(p.nivel, p.curso))
    const alvos = pessoas.filter((p) => marcados.has(p.id) && p.tipo === 'aluno' && p.periodo && p.periodo < ultimo(p))
    if (alvos.length === 0) {
      setAviso({ tipo: 'erro', texto: 'Marque alunos que ainda não estão no último ano ou período do seu nível.' })
      return
    }
    if (!window.confirm(`Avançar ${alvos.length} aluno(s) para o ano ou período seguinte?`)) return
    for (const p of alvos) {
      const { error } = await supabase
        .from('perfis')
        .update({ periodo: p.periodo! + 1 })
        .eq('id', p.id)
      if (error) {
        setAviso({ tipo: 'erro', texto: `Erro ao atualizar ${p.nome}: ${traduzirErro(error.message)}` })
        await carregar()
        return
      }
    }
    setMarcados(new Set())
    await carregar()
    setAviso({ tipo: 'ok', texto: `${alvos.length} aluno(s) avançado(s) de ano ou período.` })
  }

  const todosMarcados = lista.length > 0 && lista.every((p) => marcados.has(p.id))

  function marcarTodos() {
    setMarcados(todosMarcados ? new Set() : new Set(lista.map((p) => p.id)))
  }

  function marcar(id: string) {
    setMarcados((m) => {
      const n = new Set(m)
      if (n.has(id)) n.delete(id)
      else n.add(id)
      return n
    })
  }

  const contagem = (tipo: TipoPerfil) => pessoas.filter((p) => p.tipo === tipo).length
  const pendentes = pessoas.filter((p) => p.tipo === 'aluno' && p.solicita_professor)

  async function aprovar(p: Perfil) {
    await atualizar(p.id, { tipo: 'professor', solicita_professor: false })
  }

  async function recusar(p: Perfil) {
    const ok = window.confirm(
      `Recusar o cadastro de professor de ${p.nome}? A conta continua existindo, mas sem acesso de professor. ` +
        'Para apagá-la, use o painel do Supabase (Authentication > Users).',
    )
    if (ok) await atualizar(p.id, { solicita_professor: false })
  }

  return (
    <>
      <h1>Administração</h1>
      <p className="dica">
        {pessoas.length} cadastro(s): {contagem('aluno')} aluno(s), {contagem('professor')} professor(es) e{' '}
        {contagem('admin')} administrador(es).
      </p>

      {pendentes.length > 0 && (
        <section className="pendentes">
          <h2>Professores aguardando aprovação ({pendentes.length})</h2>
          <ul>
            {pendentes.map((p) => (
              <li key={p.id}>
                <div>
                  <strong>{p.nome}</strong>
                  <span className="dica">
                    {p.email} · {formatarTelefone(p.telefone)} · pedido em{' '}
                    {new Date(p.criado_em).toLocaleDateString('pt-BR')}
                  </span>
                </div>
                <div className="botoes-pendente">
                  <button onClick={() => aprovar(p)}>Aprovar como professor</button>
                  <button className="perigo" onClick={() => recusar(p)}>
                    Recusar
                  </button>
                </div>
              </li>
            ))}
          </ul>
        </section>
      )}

      {pedidosPendentes.length > 0 && (
        <section className="pendentes">
          <h2>Pedidos de disciplinas de outros períodos ({pedidosPendentes.length})</h2>
          <ul>
            {pedidosPendentes.map((p) => {
              const aluno = nomeDaPessoa(p.aluno_id)
              return (
                <li key={p.id}>
                  <div className="pedido-admin">
                    <span>
                      <strong>{aluno?.nome ?? 'Aluno não encontrado'}</strong>
                      {aluno && <span className="dica"> ({aluno.email})</span>}
                    </span>
                    <span className="dica">
                      Está no {aluno?.periodo ? `${aluno.periodo}º período` : 'período não informado'}
                      {aluno?.curso ? ` de ${nomeCurso(aluno.curso)}` : ''}. Pedido em{' '}
                      {new Date(p.criado_em).toLocaleDateString('pt-BR')}.
                    </span>
                    <span>
                      Pede acesso a: <strong>{descreverDisciplina(p.disciplina_id)}</strong>
                    </span>
                  </div>
                  <div className="botoes-pendente">
                    <button onClick={() => decidir(p, 'aprovado')}>Aprovar</button>
                    <button className="perigo" onClick={() => decidir(p, 'recusado')}>
                      Recusar
                    </button>
                  </div>
                </li>
              )
            })}
          </ul>
        </section>
      )}

      {pedidosAprovados.length > 0 && (
        <details className="liberadas-admin">
          <summary>Disciplinas de outros períodos já liberadas ({pedidosAprovados.length})</summary>
          <ul>
            {pedidosAprovados.map((p) => (
              <li key={p.id}>
                <span>
                  <strong>{nomeDaPessoa(p.aluno_id)?.nome ?? 'Aluno não encontrado'}</strong>
                  <span className="dica"> ({nomeDaPessoa(p.aluno_id)?.email})</span>:{' '}
                  {descreverDisciplina(p.disciplina_id)}
                </span>
                <button
                  className="secundario"
                  onClick={() => window.confirm('Retirar o acesso a esta disciplina?') && decidir(p, null)}
                >
                  Retirar
                </button>
              </li>
            ))}
          </ul>
        </details>
      )}

      <div className="filtros">
        <label>
          Buscar
          <input value={busca} onChange={(e) => setBusca(e.target.value)} placeholder="Nome, matrícula ou e-mail" />
        </label>
        <label>
          Perfil
          <select value={filtroTipo} onChange={(e) => setFiltroTipo(e.target.value)}>
            <option value="">Todos</option>
            {TIPOS.map((t) => (
              <option key={t} value={t}>
                {NOMES_TIPO[t]}
              </option>
            ))}
          </select>
        </label>
        {/* as optativas não são um período: o aluno não fica nelas */}
        <CamposTurma valor={turma} onChange={setTurma} grupos={TODOS_GRUPOS.filter((g) => !g.endsWith(':0'))} />
      </div>

      <div className="barra-acoes">
        <button onClick={avancarPeriodo} disabled={marcados.size === 0}>
          Avançar ano/período dos marcados ({marcados.size})
        </button>
        <span className="dica pequena">
          Use no começo do semestre ou do ano letivo: cada aluno marcado sobe um ano ou período, até o último do seu
          nível.
        </span>
      </div>

      {aviso && (
        <p className={aviso.tipo === 'ok' ? 'ok-acesso' : 'erro-acesso'} role="status">
          {aviso.texto}
        </p>
      )}

      {carregando ? (
        <p className="dica">Carregando…</p>
      ) : (
        <div className="tabela-rolavel">
          <table className="tabela-admin">
            <thead>
              <tr>
                <th>
                  <input type="checkbox" aria-label="Marcar todos" checked={todosMarcados} onChange={marcarTodos} />
                </th>
                <th>Nome</th>
                <th>Matrícula</th>
                <th>E-mail</th>
                <th>Celular</th>
                <th>Nível</th>
                <th>Curso</th>
                <th>Ano/período</th>
                <th>Perfil</th>
                <th>Cadastro</th>
              </tr>
            </thead>
            <tbody>
              {lista.map((p) => (
                <tr key={p.id}>
                  <td>
                    <input
                      type="checkbox"
                      aria-label={`Marcar ${p.nome}`}
                      checked={marcados.has(p.id)}
                      onChange={() => marcar(p.id)}
                    />
                  </td>
                  <td>
                    {p.nome}
                    {p.tipo === 'aluno' && p.solicita_professor && <span className="selo-pendente">em análise</span>}
                  </td>
                  <td>{p.matricula ?? '—'}</td>
                  <td>{p.email}</td>
                  <td>
                    {p.telefone ? (
                      <a
                        href={`https://wa.me/${p.telefone}`}
                        target="_blank"
                        rel="noreferrer"
                        title="Abrir no WhatsApp"
                      >
                        {formatarTelefone(p.telefone)}
                      </a>
                    ) : (
                      '—'
                    )}
                  </td>
                  {/* nível, curso e ano/período só existem para aluno (professor e administrador: —) */}
                  <td>
                    {ehAluno(p) ? (
                      <select
                        aria-label={`Nível de ${p.nome}`}
                        value={p.nivel ?? NIVEL_PADRAO}
                        onChange={(e) => {
                          const novo = e.target.value as Nivel
                          // ao trocar de nível, o ano/período passa para o primeiro do novo nível; o
                          // curso só existe na Graduação
                          atualizar(p.id, {
                            nivel: novo,
                            curso: novo === 'graduacao' ? (p.curso ?? CURSO_PADRAO) : null,
                            periodo: p.periodo == null ? null : dadosNivel(novo).etapas[0],
                          })
                        }}
                      >
                        {NIVEIS.map((n) => (
                          <option key={n.id} value={n.id}>
                            {n.nome}
                          </option>
                        ))}
                      </select>
                    ) : (
                      '—'
                    )}
                  </td>
                  <td>
                    {ehAluno(p) && (p.nivel ?? NIVEL_PADRAO) === 'graduacao' ? (
                      <select
                        aria-label={`Curso de ${p.nome}`}
                        value={p.curso ?? CURSO_PADRAO}
                        onChange={(e) => {
                          // de um Bacharelado (até o 10º) para um Tecnólogo (até o 5º), o período
                          // passa a ser o último do curso novo
                          const novo = e.target.value
                          const ultimoNovo = Math.max(...etapasDe('graduacao', novo))
                          atualizar(p.id, {
                            curso: novo,
                            periodo: p.periodo != null && p.periodo > ultimoNovo ? ultimoNovo : p.periodo,
                          })
                        }}
                      >
                        {cursosPorTipo().map((t) => (
                          <optgroup key={t.id} label={t.nome}>
                            {t.cursos.map((c) => (
                              <option key={c.id} value={c.id}>
                                {c.nome}
                              </option>
                            ))}
                          </optgroup>
                        ))}
                      </select>
                    ) : (
                      '—'
                    )}
                  </td>
                  <td>
                    {ehAluno(p) ? (
                      <select
                        aria-label={`Ano ou período de ${p.nome}`}
                        value={p.periodo ?? ''}
                        onChange={(e) => atualizar(p.id, { periodo: e.target.value ? Number(e.target.value) : null })}
                      >
                        <option value="">—</option>
                        {etapasDe(p.nivel, p.curso).map((n) => (
                          <option key={n} value={n}>
                            {n}º
                          </option>
                        ))}
                      </select>
                    ) : (
                      '—'
                    )}
                  </td>
                  <td>
                    <select
                      aria-label={`Perfil de ${p.nome}`}
                      value={p.tipo}
                      disabled={p.id === eu?.id}
                      title={p.id === eu?.id ? 'Você não pode mudar o seu próprio perfil' : undefined}
                      onChange={(e) => atualizar(p.id, { tipo: e.target.value as TipoPerfil })}
                    >
                      {TIPOS.map((t) => (
                        <option key={t} value={t}>
                          {NOMES_TIPO[t]}
                        </option>
                      ))}
                    </select>
                  </td>
                  <td>{new Date(p.criado_em).toLocaleDateString('pt-BR')}</td>
                </tr>
              ))}
            </tbody>
          </table>
          {lista.length === 0 && <p className="vazio">Nenhum cadastro encontrado.</p>}
        </div>
      )}
    </>
  )
}
