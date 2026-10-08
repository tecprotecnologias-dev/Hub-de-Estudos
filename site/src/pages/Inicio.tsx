import { useState } from 'react'
import { Link } from 'react-router-dom'
import { apostilas } from '../data/apostilas'
import { apresentacoes } from '../data/apresentacoes'
import { disciplinas } from '../data/disciplinas'
import { questoes } from '../data/questoes'
import { nomePeriodo, PERIODOS, resumoApresentacao } from '../lib/util'

export default function Inicio() {
  const [periodo, setPeriodo] = useState<number | null>(null)
  const visiveis = periodo === null ? PERIODOS : [periodo]

  return (
    <>
      <section className="destaque">
        <h1>Sala de estudos</h1>
        <p>Escolha sua disciplina para estudar pelas apostilas e praticar com simulados.</p>
      </section>

      <div className="abas" role="tablist">
        <button className={periodo === null ? 'aba ativa' : 'aba'} onClick={() => setPeriodo(null)}>
          Todos
        </button>
        {PERIODOS.map((p) => (
          <button key={p} className={periodo === p ? 'aba ativa' : 'aba'} onClick={() => setPeriodo(p)}>
            {nomePeriodo(p)}
          </button>
        ))}
      </div>

      {visiveis.map((p) => (
        <section key={p} className="bloco-periodo">
          <h2>{nomePeriodo(p)}</h2>
          <div className="cartoes">
            {disciplinas
              .filter((d) => d.periodo === p)
              .map((d) => {
                const nq = questoes.filter((q) => q.disciplinaId === d.id).length
                const na = apostilas.filter((a) => a.disciplinaId === d.id).length
                return (
                  <Link key={d.id} to={`/disciplina/${d.id}`} className="cartao">
                    <h3>{d.nome}</h3>
                    {apresentacoes[d.id] && (
                      <p className="resumo-apresentacao">{resumoApresentacao(apresentacoes[d.id])}</p>
                    )}
                    <span className="ver-mais">{na > 0 ? 'Ver apostila' : 'Ver disciplina'}</span>
                    {(nq > 0 || na > 0) && (
                      <p className="contagens">
                        {na > 0 && <span>{na} apostila{na > 1 && 's'}</span>}
                        {nq > 0 && <span>{nq} questõ{nq > 1 ? 'es' : 'ão'}</span>}
                      </p>
                    )}
                  </Link>
                )
              })}
          </div>
        </section>
      ))}
    </>
  )
}
