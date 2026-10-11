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

  const comApostila = disciplinas.filter((d) => apostilas.some((a) => a.disciplinaId === d.id)).length

  return (
    <>
      <section className="hero">
        <div className="hero-texto">
          <p className="hero-selo">estude · pratique · evolua</p>
          <p className="hero-titulo">
            Aprenda no seu ritmo.
            <br />
            <span>Pratique até dominar.</span>
          </p>
          <p className="hero-sub">
            Apostilas completas, exercícios com gabarito e simulados para cada capítulo, organizados pelas
            disciplinas do curso.
          </p>
          <div className="hero-acoes">
            <button
              className="hero-botao"
              onClick={() => document.getElementById('disciplinas')?.scrollIntoView({ behavior: 'smooth' })}
            >
              Explorar disciplinas
            </button>
            <Link to="/simulado" className="hero-botao hero-botao-claro">
              Fazer um simulado
            </Link>
          </div>
        </div>
        <ul className="hero-numeros" aria-label="O que há no site">
          <li>
            <strong>{apostilas.length}</strong>
            <span>capítulos de apostila</span>
          </li>
          <li>
            <strong>{questoes.length}</strong>
            <span>questões e exercícios</span>
          </li>
          <li>
            <strong>{comApostila}</strong>
            <span>disciplinas com material</span>
          </li>
        </ul>
        <div className="hero-codigo" aria-hidden="true">
          <span>{'</>'}</span>
          <span>{'{ }'}</span>
          <span>if</span>
          <span>for</span>
        </div>
      </section>

      <section className="destaque" id="disciplinas">
        <h1>Disciplinas</h1>
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
