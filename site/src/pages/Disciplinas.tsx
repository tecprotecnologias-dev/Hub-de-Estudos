import { useState } from 'react'
import { Link } from 'react-router-dom'
import { apostilas } from '../data/apostilas'
import { apresentacoes } from '../data/apresentacoes'
import { disciplinas } from '../data/disciplinas'
import { questoes } from '../data/questoes'
import CamposTurma from '../lib/CamposTurma'
import ComFiltrosAoLado from '../lib/ComFiltrosAoLado'
import { useDisciplinaVisivel } from '../lib/Protegida'
import {
  confereTurma,
  GRUPOS,
  grupoDe,
  gruposDoFiltro,
  nomeGrupo,
  partesDoGrupo,
  resumoApresentacao,
  TURMA_VAZIA,
} from '../lib/util'

// Lista de disciplinas por série (educação básica) ou por curso e período (Graduação). Quem
// vê mais de um grupo (professor e administração) filtra pelas caixas do cadastro: nível de
// ensino, curso (na Graduação) e ano ou período. O aluno vê só os seus grupos, sem filtros.
export default function Disciplinas() {
  const [turma, setTurma] = useState(TURMA_VAZIA)
  const visivel = useDisciplinaVisivel()
  const gruposDoPerfil = GRUPOS.filter((g) => disciplinas.some((d) => grupoDe(d) === g && visivel(d.id)))
  const visiveis = gruposDoPerfil.filter((g) => confereTurma(partesDoGrupo(g), turma))

  const cabecalho = (
    <section className="destaque">
      <h1>Disciplinas</h1>
      <p>Escolha sua disciplina para estudar pelas apostilas e praticar com simulados.</p>
    </section>
  )

  const lista = (
    <>
      {visiveis.length === 0 && <p className="vazio">Ainda não há disciplinas cadastradas para esta escolha.</p>}
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

  return (
    <>
      {gruposDoPerfil.length > 1 ? (
        <ComFiltrosAoLado
          filtros={<CamposTurma valor={turma} onChange={setTurma} grupos={gruposDoFiltro(gruposDoPerfil)} />}
        >
          {cabecalho}
          {lista}
        </ComFiltrosAoLado>
      ) : (
        <>
          {cabecalho}
          {lista}
        </>
      )}
    </>
  )
}
