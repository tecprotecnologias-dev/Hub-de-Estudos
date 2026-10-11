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
    case 'codigo':
      return (
        <pre className="bloco-codigo">
          <code>{parte.texto}</code>
        </pre>
      )
    default:
      return <p className="caso">{parte.texto}</p>
  }
}

/** Linhas em branco para o aluno escrever a resposta na prova impressa. */
export function LinhasResposta({ quantidade }: { quantidade: number }) {
  return (
    <div className="linhas-resposta">
      {Array.from({ length: quantidade }, (_, i) => (
        <span key={i} />
      ))}
    </div>
  )
}

/**
 * Texto motivador, caso aplicado, enunciado e itens (a, b, c...) de uma questão.
 * Com `linhasPorItem`, cada item ganha suas linhas de resposta logo abaixo (prova impressa).
 */
export default function EnunciadoQuestao({ q, linhasPorItem }: { q: Questao; linhasPorItem?: number }) {
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
            <li key={i}>
              {it}
              {linhasPorItem ? <LinhasResposta quantidade={linhasPorItem} /> : null}
            </li>
          ))}
        </ul>
      )}
      {q.tipo === 'discursiva' && q.exemplos && q.exemplos.length > 0 && (
        <div className="tabela-rolavel">
          <table className="exemplos">
            <caption>Teste seu programa com estes exemplos</caption>
            <thead>
              <tr>
                <th>Você digita</th>
                <th>O programa mostra</th>
              </tr>
            </thead>
            <tbody>
              {q.exemplos.map((ex, i) => (
                <tr key={i}>
                  <td>
                    <code>{ex.entrada}</code>
                  </td>
                  <td>
                    <code>{ex.saida}</code>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
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
          <div key={i}>
            {p.linguagem && <p className="linguagem-codigo">{p.linguagem}</p>}
            <pre className="bloco-codigo">
              <code>{p.texto}</code>
            </pre>
          </div>
        ) : (
          <p key={i}>{p.texto}</p>
        ),
      )}
    </div>
  )
}
