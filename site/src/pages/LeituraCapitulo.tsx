import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { apostilas } from '../data/apostilas'
import type { Bloco, ConteudoCapitulo } from '../data/tipos'
import { apostilasDaDisciplina, carregarCapitulo, rotuloApostila } from '../lib/capitulos'
import { nomeDisciplina } from '../lib/util'

const html = (h: string) => ({ __html: h })

function Blocos({ blocos }: { blocos: Bloco[] }) {
  return (
    <>
      {blocos.map((b, i) => (
        <BlocoView key={i} b={b} />
      ))}
    </>
  )
}

function BlocoView({ b }: { b: Bloco }) {
  switch (b.t) {
    case 'h2':
      return <h2 id={b.id}>{b.texto}</h2>
    case 'h3':
      return <h3>{b.texto}</h3>
    case 'p':
      return <p className={b.estilo} dangerouslySetInnerHTML={html(b.html)} />
    case 'lista': {
      const Tag = b.numerada ? 'ol' : 'ul'
      return (
        <Tag className={b.numerada ? 'lista-numerada' : undefined}>
          {b.itens.map((it, i) => (
            <li key={i} dangerouslySetInnerHTML={html(it)} />
          ))}
        </Tag>
      )
    }
    case 'tabela':
      return (
        <div className="tabela-rolagem">
          <table>
            {b.cabecalho.length > 0 && (
              <thead>
                <tr>
                  {b.cabecalho.map((c, i) => (
                    <th key={i} dangerouslySetInnerHTML={html(c)} />
                  ))}
                </tr>
              </thead>
            )}
            <tbody>
              {b.linhas.map((l, i) => (
                <tr key={i}>
                  {l.map((c, j) => (
                    <td key={j} dangerouslySetInnerHTML={html(c)} />
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )
    case 'codigo':
      return (
        <pre className="bloco-codigo">
          <code>{b.texto}</code>
        </pre>
      )
    case 'imagem':
      return (
        <figure className={b.grande ? 'figura figura-grande' : 'figura'}>
          {b.grande ? (
            <a href={import.meta.env.BASE_URL + b.src.replace(/^\//, '')} target="_blank" rel="noreferrer">
              <img src={import.meta.env.BASE_URL + b.src.replace(/^\//, '')} alt={b.alt} loading="lazy" />
              <figcaption className="dica">Clique na imagem para abrir em tamanho original e ampliar.</figcaption>
            </a>
          ) : (
            <img src={import.meta.env.BASE_URL + b.src.replace(/^\//, '')} alt={b.alt} loading="lazy" />
          )}
        </figure>
      )
    case 'quadro':
      if (b.tipo === 'resposta') {
        return (
          <details className="quadro quadro-resposta">
            <summary>Ver resposta comentada</summary>
            <Blocos blocos={b.blocos} />
          </details>
        )
      }
      return (
        <aside className={`quadro quadro-${b.tipo}`}>
          <p className="quadro-titulo">{b.titulo}</p>
          <Blocos blocos={b.blocos} />
        </aside>
      )
  }
}

export default function LeituraCapitulo() {
  const { id = '' } = useParams()
  const apostila = apostilas.find((a) => a.id === id)
  // no celular o sumário começa fechado
  const [sumarioAberto] = useState(() => window.matchMedia('(min-width: 801px)').matches)
  const [carregado, setCarregado] = useState<{ id: string; conteudo: ConteudoCapitulo | null } | null>(null)
  // undefined enquanto o capítulo pedido ainda está carregando
  const conteudo = carregado?.id === id ? carregado.conteudo : undefined

  useEffect(() => {
    let ativo = true
    carregarCapitulo(id).then((c) => ativo && setCarregado({ id, conteudo: c }))
    window.scrollTo(0, 0)
    return () => {
      ativo = false
    }
  }, [id])

  if (!apostila || conteudo === null) {
    return (
      <>
        <h1>Capítulo não encontrado</h1>
        <Link to="/apostilas">Voltar para as apostilas</Link>
      </>
    )
  }

  const irmaos = apostilasDaDisciplina(apostila.disciplinaId).filter((a) => !a.arquivo)
  const pos = irmaos.findIndex((a) => a.id === id)
  const anterior = irmaos[pos - 1]
  const proximo = irmaos[pos + 1]
  const secoes = conteudo?.blocos.filter((b): b is Extract<Bloco, { t: 'h2' }> => b.t === 'h2') ?? []

  return (
    <div className="leitura">
      <aside className="sumario no-print">
        <Link to={`/apostilas?disciplina=${apostila.disciplinaId}`} className="voltar">
          Apostilas de {nomeDisciplina(apostila.disciplinaId)}
        </Link>
        <details open={sumarioAberto} hidden={secoes.length === 0}>
          <summary className="sumario-titulo">Neste {(apostila.rotulo ?? 'Capítulo').toLowerCase()}</summary>
          <ol>
          {secoes.map((s) => (
            <li key={s.id}>
              <a
                href={`#${s.id}`}
                onClick={(e) => {
                  e.preventDefault()
                  document.getElementById(s.id)?.scrollIntoView({ behavior: 'smooth' })
                }}
              >
                {s.texto}
              </a>
            </li>
          ))}
          </ol>
        </details>
      </aside>

      <article className="capitulo">
        <header className="capitulo-cabecalho">
          <p className="etiqueta">
            {nomeDisciplina(apostila.disciplinaId)} · {rotuloApostila(apostila)}
          </p>
          <h1>{apostila.titulo}</h1>
          <button className="secundario no-print" onClick={() => window.print()}>
            Imprimir / salvar PDF
          </button>
        </header>

        {conteudo === undefined ? <p className="dica">Carregando...</p> : <Blocos blocos={conteudo.blocos} />}

        <nav className="navegacao-capitulos no-print">
          {anterior ? (
            <Link to={`/apostila/${anterior.id}`} className="botao secundario">
              Anterior: {rotuloApostila(anterior)}
            </Link>
          ) : (
            <span />
          )}
          {proximo && (
            <Link to={`/apostila/${proximo.id}`} className="botao">
              Próximo: {rotuloApostila(proximo)}
            </Link>
          )}
        </nav>
      </article>
    </div>
  )
}
