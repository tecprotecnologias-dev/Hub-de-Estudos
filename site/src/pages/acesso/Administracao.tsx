import { useEffect, useMemo, useState } from 'react'
import { formatarTelefone, NOMES_TIPO, traduzirErro, useAuth, type Perfil, type TipoPerfil } from '../../lib/auth'
import { supabase } from '../../lib/supabase'
import CamposTurma from '../../lib/CamposTurma'
import ComFiltrosAoLado from '../../lib/ComFiltrosAoLado'
import type { PedidoDisciplina } from '../../lib/PedidosDisciplina'
import { disciplinas } from '../../data/disciplinas'
import { confereTurma, grupoDe, nomeGrupo, TODOS_GRUPOS, TURMA_VAZIA } from '../../lib/util'
import {
  CURSO_PADRAO,
  dadosNivel,
  NIVEL_PADRAO,
  nomeCurso,
  nomeEtapa,
} from '../../lib/niveis'

// Área da administradora: ver os cadastros, mudar o perfil (aluno, professor, administrador),
// aprovar professores e os pedidos de disciplinas de outros períodos. O nível, o curso e o
// período do aluno só aparecem: o cadastro é definitivo e, se algo mudar, o aluno exclui a
// conta e cria outra (pedido de 23/10/2026). As regras do banco garantem que só um
// administrador muda os perfis.

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
    // filtros à esquerda e a página mais larga que as outras: a tabela tem muitas colunas
    <ComFiltrosAoLado
      largo
      filtros={
        <>
          <label>
            Buscar
            <input value={busca} onChange={(e) => setBusca(e.target.value)} placeholder="Nome, matrícula ou e-mail" />
          </label>
          <label>
            Perfil
            <select
              value={filtroTipo}
              onChange={(e) => {
                setFiltroTipo(e.target.value)
                // professor e administrador não têm nível, curso nem período
                if (e.target.value && e.target.value !== 'aluno') setTurma(TURMA_VAZIA)
              }}
            >
              <option value="">Todos</option>
              {TIPOS.map((t) => (
                <option key={t} value={t}>
                  {NOMES_TIPO[t]}
                </option>
              ))}
            </select>
          </label>
          {/* as optativas não são um período: o aluno não fica nelas */}
          {(!filtroTipo || filtroTipo === 'aluno') && (
            <CamposTurma valor={turma} onChange={setTurma} grupos={TODOS_GRUPOS.filter((g) => !g.endsWith(':0'))} />
          )}
        </>
      }
    >
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
                <th>Pessoa</th>
                <th>Nível, curso e período</th>
                <th>Perfil</th>
                <th>Cadastro</th>
              </tr>
            </thead>
            <tbody>
              {lista.map((p) => (
                <tr key={p.id}>
                  {/* nome, e-mail, matrícula e celular numa coluna só, para a tabela caber ao lado dos filtros */}
                  <td className="celula-pessoa">
                    <strong>{p.nome}</strong>
                    {p.tipo === 'aluno' && p.solicita_professor && <span className="selo-pendente">em análise</span>}
                    <span className="dica">{p.email}</span>
                    {p.matricula && <span className="dica">Matrícula {p.matricula}</span>}
                    {p.telefone && (
                      <a
                        className="dica"
                        href={`https://wa.me/${p.telefone}`}
                        target="_blank"
                        rel="noreferrer"
                        title="Abrir no WhatsApp"
                      >
                        {formatarTelefone(p.telefone)}
                      </a>
                    )}
                  </td>
                  {/* o cadastro do aluno é definitivo (pedido de 23/10/2026): nível, curso e período só
                      aparecem; se algo mudar, o aluno exclui a conta e cria outra */}
                  <td>
                    {ehAluno(p) ? (
                      <div className="celula-turma">
                        <span className="nivel-fixo">{dadosNivel(p.nivel).nome}</span>
                        {(p.nivel ?? NIVEL_PADRAO) === 'graduacao' && <span>{nomeCurso(p.curso)}</span>}
                        <span>{p.periodo ? nomeEtapa(p.nivel, p.periodo) : '—'}</span>
                      </div>
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
    </ComFiltrosAoLado>
  )
}
