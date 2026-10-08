import { Link, useParams } from 'react-router-dom'
import { atualidades } from '../data/atualidades'
import Apresentacao from '../lib/Apresentacao'
import { nomeDisciplina } from '../lib/util'

const ordenadas = [...atualidades].sort((a, b) => b.data.localeCompare(a.data))

export default function Atualidades() {
  const { id } = useParams()

  if (id) {
    const item = atualidades.find((a) => a.id === id)
    if (!item) {
      return (
        <>
          <h1>Publicação não encontrada</h1>
          <Link to="/dicas">Voltar para Dicas</Link>
        </>
      )
    }
    return (
      <article className="atualidade">
        <Link to="/dicas" className="voltar">
          Dicas
        </Link>
        {item.disciplinaId && <p className="etiqueta">{nomeDisciplina(item.disciplinaId)}</p>}
        <h1>{item.titulo}</h1>
        <Apresentacao texto={item.texto} />
        {item.fonte && (
          <p className="fonte">
            Fonte:{' '}
            <a href={item.fonte} target="_blank" rel="noreferrer">
              {item.fonte}
            </a>
          </p>
        )}
      </article>
    )
  }

  return (
    <>
      <h1>Dicas</h1>
      <p className="dica">Dicas e novidades da área de tecnologia comentadas para as nossas disciplinas.</p>
      {ordenadas.length === 0 ? (
        <p className="vazio">Em breve, as primeiras publicações.</p>
      ) : (
        <div className="lista-atualidades">
          {ordenadas.map((a) => (
            <Link key={a.id} to={`/dicas/${a.id}`} className="cartao">
              {a.disciplinaId && <span className="etiqueta">{nomeDisciplina(a.disciplinaId)}</span>}
              <h3>{a.titulo}</h3>
              <p>{a.resumo}</p>
            </Link>
          ))}
        </div>
      )}
    </>
  )
}
