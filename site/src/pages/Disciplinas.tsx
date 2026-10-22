import { useState } from 'react'
import { Link } from 'react-router-dom'
import { apostilas } from '../data/apostilas'
import { apresentacoes } from '../data/apresentacoes'
import { disciplinas } from '../data/disciplinas'
import { questoes } from '../data/questoes'
import { useDisciplinaVisivel } from '../lib/Protegida'
import { GRUPOS, grupoDe, nomeGrupo, resumoApresentacao } from '../lib/util'

// Lista de disciplinas por período (Graduação) ou por nível (educação básica)
export default function Disciplinas() {
  const [grupo, setGrupo] = useState<string | null>(null)
  const visivel = useDisciplinaVisivel()
  const gruposDoPerfil = GRUPOS.filter((g) => disciplinas.some((d) => grupoDe(d) === g && visivel(d.id)))
  const visiveis = grupo === null ? gruposDoPerfil : [grupo]

  return (
    <>
      <section className="destaque">
        <h1>Disciplinas</h1>
        <p>Escolha sua disciplina para estudar pelas apostilas e praticar com simulados.</p>
      </section>

      <div className="abas" role="tablist">
        <button className={grupo === null ? 'aba ativa' : 'aba'} onClick={() => setGrupo(null)}>
          Todos
        </button>
        {gruposDoPerfil.map((g) => (
          <button key={g} className={grupo === g ? 'aba ativa' : 'aba'} onClick={() => setGrupo(g)}>
            {nomeGrupo(g)}
          </button>
        ))}
      </div>

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
