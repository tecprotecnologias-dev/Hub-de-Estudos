import { useEffect, useState } from 'react'
import { disciplinas } from '../data/disciplinas'
import { podeVerDisciplina, traduzirErro, useAuth } from './auth'
import { CURSO_PADRAO, NIVEL_PADRAO } from './niveis'
import { supabase } from './supabase'
import { grupoDe, nomeGrupo } from './util'

// Aluno da Graduação que cursa disciplina de outro período (dependência ou adiantamento):
// ele pede acesso aqui e a administração aprova na página Administração (pedido de
// 23/10/2026). Só disciplinas do próprio curso. A tabela é public.pedidos_disciplina.

export type SituacaoPedido = 'pendente' | 'aprovado' | 'recusado'

export interface PedidoDisciplina {
  id: number
  aluno_id: string
  disciplina_id: string
  situacao: SituacaoPedido
  criado_em: string
}

const NOMES_SITUACAO: Record<SituacaoPedido, string> = {
  pendente: 'Aguardando aprovação',
  aprovado: 'Liberada',
  recusado: 'Recusada',
}

export default function PedidosDisciplina() {
  const { perfil, recarregarPerfil } = useAuth()
  const [pedidos, setPedidos] = useState<PedidoDisciplina[]>([])
  const [escolhida, setEscolhida] = useState('')
  const [aviso, setAviso] = useState<{ tipo: 'ok' | 'erro'; texto: string } | null>(null)
  const [enviando, setEnviando] = useState(false)

  async function carregar() {
    if (!supabase || !perfil) return
    const { data } = await supabase
      .from('pedidos_disciplina')
      .select('*')
      .eq('aluno_id', perfil.id)
      .order('criado_em')
    setPedidos((data as PedidoDisciplina[] | null) ?? [])
  }

  useEffect(() => {
    carregar()
  }, [perfil?.id])

  if (!supabase || !perfil || perfil.tipo !== 'aluno' || (perfil.nivel ?? NIVEL_PADRAO) !== 'graduacao') return null
  const cliente = supabase

  // do mesmo curso, fora do período do aluno e ainda sem pedido
  const pedidas = new Set(pedidos.map((p) => p.disciplina_id))
  const candidatas = disciplinas.filter(
    (d) =>
      (d.nivel ?? NIVEL_PADRAO) === 'graduacao' &&
      (d.curso ?? CURSO_PADRAO) === (perfil.curso ?? CURSO_PADRAO) &&
      !podeVerDisciplina(perfil, d) &&
      !pedidas.has(d.id),
  )

  async function pedir() {
    if (!escolhida) return setAviso({ tipo: 'erro', texto: 'Escolha a disciplina que você cursa.' })
    setEnviando(true)
    const { error } = await cliente.from('pedidos_disciplina').insert({ aluno_id: perfil!.id, disciplina_id: escolhida })
    setEnviando(false)
    if (error) return setAviso({ tipo: 'erro', texto: traduzirErro(error.message) })
    setEscolhida('')
    setAviso({ tipo: 'ok', texto: 'Pedido enviado. A disciplina aparece aqui assim que a administração aprovar.' })
    await carregar()
  }

  async function apagar(p: PedidoDisciplina) {
    const { error } = await cliente.from('pedidos_disciplina').delete().eq('id', p.id)
    if (error) return setAviso({ tipo: 'erro', texto: traduzirErro(error.message) })
    setAviso(null)
    await carregar()
    if (p.situacao === 'aprovado') await recarregarPerfil()
  }

  const nome = (id: string) => disciplinas.find((d) => d.id === id)
  return (
    <section className="pedidos-disciplina" aria-labelledby="titulo-pedidos">
      <h2 id="titulo-pedidos">Cursa disciplina de outro período?</h2>
      <p className="dica">
        Escolha a disciplina e peça acesso. Depois que a administração aprovar, ela aparece na sua lista de disciplinas.
      </p>
      {candidatas.length > 0 && (
        <div className="pedir-disciplina">
          <label>
            Disciplina
            <select value={escolhida} onChange={(e) => setEscolhida(e.target.value)}>
              <option value="">Escolha…</option>
              {candidatas.map((d) => (
                <option key={d.id} value={d.id}>
                  {d.nome} ({nomeGrupo(grupoDe(d))})
                </option>
              ))}
            </select>
          </label>
          <button onClick={pedir} disabled={enviando}>
            {enviando ? 'Enviando…' : 'Pedir acesso'}
          </button>
        </div>
      )}
      {aviso && (
        <p className={aviso.tipo === 'ok' ? 'ok-acesso' : 'erro-acesso'} role="status">
          {aviso.texto}
        </p>
      )}
      {pedidos.length > 0 && (
        <ul className="lista-pedidos">
          {pedidos.map((p) => {
            const d = nome(p.disciplina_id)
            return (
              <li key={p.id}>
                <span>
                  <strong>{d?.nome ?? p.disciplina_id}</strong>
                  {d && <span className="dica"> {nomeGrupo(grupoDe(d))}</span>}
                </span>
                <span className={`situacao-pedido ${p.situacao}`}>{NOMES_SITUACAO[p.situacao]}</span>
                {p.situacao !== 'aprovado' && (
                  <button className="secundario" onClick={() => apagar(p)}>
                    {p.situacao === 'pendente' ? 'Cancelar pedido' : 'Apagar'}
                  </button>
                )}
              </li>
            )
          })}
        </ul>
      )}
    </section>
  )
}
