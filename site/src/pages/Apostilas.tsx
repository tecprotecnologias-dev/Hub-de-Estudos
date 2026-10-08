import { useState } from 'react'
import { Link, useSearchParams } from 'react-router-dom'
import { apostilas } from '../data/apostilas'
import { disciplinas } from '../data/disciplinas'
import type { Apostila } from '../data/tipos'
import { apostilasDaDisciplina, gruposDeApostila, rotuloApostila } from '../lib/capitulos'
import { buscarDisciplina, nomePeriodo, PERIODOS } from '../lib/util'

const url = (a: Apostila) => import.meta.env.BASE_URL + (a.arquivo ?? '')

export default function Apostilas() {
  // vindo da página da disciplina: /apostilas?disciplina=<id> já abre filtrado
  const [params] = useSearchParams()
  const inicial = buscarDisciplina(params.get('disciplina') ?? '')
  const [periodo, setPeriodo] = useState(inicial ? String(inicial.periodo) : '')
  const [disciplinaId, setDisciplinaId] = useState(inicial?.id ?? '')
  const [busca, setBusca] = useState('')
  const [aberta, setAberta] = useState<Apostila | null>(null)

  const termo = busca.trim().toLowerCase()
  const confere = (a: Apostila) =>
    !termo || (a.titulo + ' ' + a.descricao + ' ' + (a.unidades ?? []).join(' ')).toLowerCase().includes(termo)

  // disciplinas com apostila, na ordem de período e nome, respeitando os filtros
  const comApostila = disciplinas.filter(
    (d) =>
      (!periodo || String(d.periodo) === periodo) &&
      (!disciplinaId || d.id === disciplinaId) &&
      apostilasDaDisciplina(d.id).some(confere),
  )

  if (aberta) {
    return (
      <>
        <div className="barra-acoes">
          <button onClick={() => setAberta(null)}>Voltar</button>
          <a className="botao secundario" href={url(aberta)} target="_blank" rel="noreferrer">
            Abrir em nova aba / baixar
          </a>
        </div>
        <h1>{aberta.titulo}</h1>
        <iframe className="leitor-pdf" src={url(aberta)} title={aberta.titulo} />
      </>
    )
  }

  return (
    <>
      <h1>Apostilas</h1>
      <div className="filtros">
        <label>
          Buscar
          <input value={busca} onChange={(e) => setBusca(e.target.value)} placeholder="Título ou assunto" />
        </label>
        <label>
          Período
          <select
            value={periodo}
            onChange={(e) => {
              setPeriodo(e.target.value)
              setDisciplinaId('')
            }}
          >
            <option value="">Todos</option>
            {PERIODOS.map((p) => (
              <option key={p} value={p}>
                {nomePeriodo(p)}
              </option>
            ))}
          </select>
        </label>
        <label className="largo">
          Disciplina
          <select value={disciplinaId} onChange={(e) => setDisciplinaId(e.target.value)}>
            <option value="">Todas</option>
            {disciplinas
              .filter((d) => (!periodo || String(d.periodo) === periodo) && apostilasDaDisciplina(d.id).length > 0)
              .map((d) => (
                <option key={d.id} value={d.id}>
                  {d.nome}
                </option>
              ))}
          </select>
        </label>
      </div>

      {apostilas.length === 0 ? (
        <p className="vazio">As apostilas ainda estão sendo publicadas.</p>
      ) : (
        comApostila.length === 0 && <p className="vazio">Nenhuma apostila encontrada.</p>
      )}

      {comApostila.map((d) => (
        <section key={d.id} className="bloco-apostila">
          <h2>
            <Link to={`/disciplina/${d.id}`}>{d.nome}</Link>
            <span className="etiqueta">{nomePeriodo(d.periodo)}</span>
          </h2>
          {gruposDeApostila(apostilasDaDisciplina(d.id).filter(confere)).map(([grupo, itens]) => (
            <div key={grupo || 'principal'}>
              {grupo && <h3 className="grupo-apostila">{grupo}</h3>}
              <div className="cartoes">
                {itens.map((a) => {
                  const corpo = (
                    <>
                      <span className="etiqueta">{rotuloApostila(a)}</span>
                      <h3>{a.titulo}</h3>
                      <p>{a.descricao}</p>
                    </>
                  )
                  return a.arquivo ? (
                    <button key={a.id} className="cartao" onClick={() => setAberta(a)}>
                      {corpo}
                    </button>
                  ) : (
                    <Link key={a.id} className="cartao" to={`/apostila/${a.id}`}>
                      {corpo}
                    </Link>
                  )
                })}
              </div>
            </div>
          ))}
        </section>
      ))}
    </>
  )
}
