import type { ParteContexto, ParteResolucao, Questao } from '../data/tipos'

function Parte({ parte }: { parte: ParteContexto }) {
  switch (parte.t) {
    case 'citacao':
      return (
        <figure className="texto-motivador">
          <blockquote>{parte.texto}</blockquote>
          {parte.traducao && <p className="traducao">{parte.traducao}</p>}
          {parte.fonte && <figcaption>{parte.fonte}</figcaption>}
        </figure>
      )
    case 'fonte':
      return <p className="fonte-questao">{parte.texto}</p>
    case 'imagem':
      return (
        <figure className="figura-questao">
          <img src={`${import.meta.env.BASE_URL}${parte.src}`} alt={parte.legenda ?? ''} loading="lazy" />
          {parte.legenda && <figcaption>{parte.legenda}</figcaption>}
        </figure>
      )
    default:
      return <p className="caso">{parte.texto}</p>
  }
}

/** Texto motivador, caso aplicado, enunciado e itens (a, b, c...) de uma questão. */
export default function EnunciadoQuestao({ q }: { q: Questao }) {
  return (
    <>
      {q.texto && (
        <figure className="texto-motivador">
          <blockquote>{q.texto.citacao}</blockquote>
          {q.texto.traducao && <p className="traducao">{q.texto.traducao}</p>}
          {q.texto.fonte && <figcaption>{q.texto.fonte}</figcaption>}
        </figure>
      )}
      {q.contexto?.map((parte, i) => (
        <Parte key={i} parte={parte} />
      ))}
      {q.caso?.map((p, i) => (
        <p key={i} className="caso">
          {p}
        </p>
      ))}
      <p className="enunciado">{q.enunciado}</p>
      {q.tipo === 'discursiva' && q.itens && q.itens.length > 0 && (
        <ul className="itens-discursiva">
          {q.itens.map((it, i) => (
            <li key={i}>{it}</li>
          ))}
        </ul>
      )}
    </>
  )
}

/** Resolução passo a passo de um exercício prático. */
export function Resolucao({ partes }: { partes: ParteResolucao[] }) {
  return (
    <div className="resolucao">
      {partes.map((p, i) =>
        p.t === 'codigo' ? (
          <pre key={i} className="bloco-codigo">
            <code>{p.texto}</code>
          </pre>
        ) : (
          <p key={i}>{p.texto}</p>
        ),
      )}
    </div>
  )
}
