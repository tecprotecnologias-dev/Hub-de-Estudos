import { useState } from 'react'
import { Link } from 'react-router-dom'
import { apostilas } from '../data/apostilas'
import { apresentacoes } from '../data/apresentacoes'
import { disciplinas } from '../data/disciplinas'
import { questoes } from '../data/questoes'
import { useDisciplinaVisivel } from '../lib/Protegida'
import { NIVEIS, nomeEtapa, rotuloEtapa, type Nivel } from '../lib/niveis'
import { GRUPOS, grupoDe, nomeGrupo, partesDoGrupo, resumoApresentacao } from '../lib/util'

// Lista de disciplinas por série (educação básica) ou por período (Graduação). Quem vê mais
// de um grupo (professor e administração) filtra por duas caixas, como no cadastro: o nível
// de ensino e, dentro dele, o ano ou período. O aluno vê só os seus grupos, sem filtros.
export default function Disciplinas() {
  const [nivel, setNivel] = useState<Nivel | ''>('')
  const [etapa, setEtapa] = useState('')
  const visivel = useDisciplinaVisivel()
  const gruposDoPerfil = GRUPOS.filter((g) => disciplinas.some((d) => grupoDe(d) === g && visivel(d.id)))

  const niveisDisponiveis = NIVEIS.filter((n) => gruposDoPerfil.some((g) => partesDoGrupo(g).nivel === n.id))
  const etapasDoNivel = nivel
    ? gruposDoPerfil.map(partesDoGrupo).filter((p) => p.nivel === nivel).map((p) => p.etapa)
    : []
  const visiveis = gruposDoPerfil.filter((g) => {
    const p = partesDoGrupo(g)
    return (!nivel || p.nivel === nivel) && (!etapa || String(p.etapa) === etapa)
  })

  return (
    <>
      <section className="destaque">
        <h1>Disciplinas</h1>
        <p>Escolha sua disciplina para estudar pelas apostilas e praticar com simulados.</p>
      </section>

      {gruposDoPerfil.length > 1 && (
        <div className="filtros">
          <label>
            Nível de ensino
            <select
              value={nivel}
              onChange={(e) => {
                setNivel(e.target.value as Nivel | '')
                setEtapa('') // os anos/períodos mudam de um nível para outro
              }}
            >
              <option value="">Todos</option>
              {niveisDisponiveis.map((n) => (
                <option key={n.id} value={n.id}>
                  {n.nome}
                </option>
              ))}
            </select>
          </label>
          <label>
            {nivel ? rotuloEtapa(nivel) : 'Ano ou período'}
            <select value={etapa} disabled={!nivel} onChange={(e) => setEtapa(e.target.value)}>
              <option value="">{nivel ? 'Todos' : 'Escolha o nível primeiro'}</option>
              {etapasDoNivel.map((n) => (
                <option key={n} value={n}>
                  {nomeEtapa(nivel || null, n)}
                </option>
              ))}
            </select>
          </label>
        </div>
      )}

      {visiveis.map((g) => (
        <section key={g} className="bloco-periodo">
          <h2>{nomeGrupo(g)}</h2>
          <div className="cartoes">
            {disciplinas
              .filter((d) => grupoDe(d) === g && visivel(d.id))
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
