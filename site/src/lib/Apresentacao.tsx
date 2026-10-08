import { Fragment, type ReactNode } from 'react'

/** **negrito** dentro de uma linha */
function inline(texto: string): ReactNode[] {
  return texto.split(/(\*\*[^*]+\*\*)/).map((parte, i) =>
    parte.startsWith('**') && parte.endsWith('**') ? <strong key={i}>{parte.slice(2, -2)}</strong> : <Fragment key={i}>{parte}</Fragment>,
  )
}

/** Mostra o texto de apresentação (formato descrito em src/data/apresentacoes.ts). */
export default function Apresentacao({ texto }: { texto: string }) {
  const blocos = texto.trim().split(/\n\s*\n/)
  return (
    <div className="apresentacao">
      {blocos.map((bloco, i) => {
        const linhas = bloco.trim().split('\n')
        if (bloco.startsWith('## ')) return <h2 key={i}>{bloco.slice(3).trim()}</h2>
        if (linhas.every((l) => l.startsWith('- ')))
          return (
            <ul key={i}>
              {linhas.map((l, j) => (
                <li key={j}>{inline(l.slice(2))}</li>
              ))}
            </ul>
          )
        if (linhas.every((l) => /^\d+\.\s/.test(l)))
          return (
            <ol key={i}>
              {linhas.map((l, j) => (
                <li key={j}>{inline(l.replace(/^\d+\.\s/, ''))}</li>
              ))}
            </ol>
          )
        return <p key={i}>{inline(bloco.replace(/\n/g, ' '))}</p>
      })}
    </div>
  )
}