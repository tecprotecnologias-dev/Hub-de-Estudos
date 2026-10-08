import { Link, useParams } from 'react-router-dom'
import { apresentacoes } from '../data/apresentacoes'
import Apresentacao from '../lib/Apresentacao'
import { questoes } from '../data/questoes'
import { apostilasDaDisciplina } from '../lib/capitulos'
import { buscarDisciplina, nomePeriodo } from '../lib/util'

function Lista({ itens }: { itens: string[] }) {
  return (
    <ul>
      {itens.map((t, i) => (
        <li key={i}>{t}</li>
      ))}
    </ul>
  )
}

export default function PaginaDisciplina() {
  const { id = '' } = useParams()
  const d = buscarDisciplina(id)

  if (!d) {
    return (
      <>
        <h1>Disciplina não encontrada</h1>
        <Link to="/">Voltar para as disciplinas</Link>
      </>
    )
  }

  const minhasApostilas = apostilasDaDisciplina(d.id)
  // o texto da professora substitui "Objetivos" e "Habilidades" do plano de ensino
  const apresentacao = apresentacoes[d.id]
  const nQuestoes = questoes.filter((q) => q.disciplinaId === d.id).length

  return (
    <article className="disciplina">
      <Link to="/" className="voltar">
        Todas as disciplinas
      </Link>
      <p className="etiqueta">{nomePeriodo(d.periodo)}</p>
      <h1>{d.nome}</h1>

      {apresentacao && <Apresentacao texto={apresentacao} />}

      {/* os capítulos ficam só no menu Apostilas; aqui, um atalho já filtrado pela disciplina */}
      <div className="barra-acoes">
        {minhasApostilas.length > 0 && (
          <Link className="botao" to={`/apostilas?disciplina=${d.id}`}>
            Abrir a apostila
          </Link>
        )}
        {nQuestoes > 0 && (
          <Link className="botao secundario" to={`/simulado/${d.id}`}>
            Fazer simulado ({nQuestoes} questõ{nQuestoes > 1 ? 'es' : 'ão'})
          </Link>
        )}
        {minhasApostilas.length === 0 && nQuestoes === 0 && (
          <span className="dica">O material desta disciplina ainda está sendo publicado.</span>
        )}
      </div>

      {!apresentacao && d.objetivos.length > 0 && (
        <section>
          <h2>Objetivos</h2>
          <Lista itens={d.objetivos} />
        </section>
      )}

      {!apresentacao && d.habilidades.length > 0 && (
        <section>
          <h2>Habilidades e competências</h2>
          <Lista itens={d.habilidades} />
        </section>
      )}



      {!apresentacao && d.tecnologias.length > 0 && (
        <section>
          <h2>Tecnologias utilizadas</h2>
          <Lista itens={d.tecnologias} />
        </section>
      )}

      {(d.bibliografia.basica.length > 0 || d.bibliografia.complementar.length > 0) && (
        <section>
          <h2>Bibliografia</h2>
          {d.bibliografia.basica.length > 0 && (
            <>
              <h3>Básica</h3>
              <Lista itens={d.bibliografia.basica} />
            </>
          )}
          {d.bibliografia.complementar.length > 0 && (
            <>
              <h3>Complementar</h3>
              <Lista itens={d.bibliografia.complementar} />
            </>
          )}
        </section>
      )}
    </article>
  )
}
