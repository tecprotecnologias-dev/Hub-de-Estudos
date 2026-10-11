import { useState, type ReactNode } from 'react'
import { Link } from 'react-router-dom'
import { apostilas } from '../data/apostilas'
import { apresentacoes } from '../data/apresentacoes'
import { disciplinas } from '../data/disciplinas'
import { questoes } from '../data/questoes'
import { nomePeriodo, PERIODOS, resumoApresentacao } from '../lib/util'

// Ícones de linha simples (24 × 24), na cor do texto do cartão
const icone = (caminho: ReactNode) => (
  <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" strokeWidth="1.8"
       strokeLinecap="round" strokeLinejoin="round">
    {caminho}
  </svg>
)

const CAMINHOS: { titulo: string; texto: string; acao: string; para?: string; cor: string; icone: ReactNode }[] = [
  {
    titulo: 'Apostilas',
    texto: 'Capítulos completos para ler no site ou imprimir, com exemplos, figuras e erros comuns.',
    acao: 'Abrir apostilas',
    para: '/apostilas',
    cor: 'roxo',
    icone: icone(
      <>
        <path d="M2 5.5C4.5 4.2 7.5 4.2 12 6v13c-4.5-1.8-7.5-1.8-10-.5z" />
        <path d="M22 5.5C19.5 4.2 16.5 4.2 12 6v13c4.5-1.8 7.5-1.8 10-.5z" />
      </>,
    ),
  },
  {
    titulo: 'Simulados',
    texto: 'Questões objetivas por capítulo, com cronômetro, nota e resolução comentada.',
    acao: 'Fazer um simulado',
    para: '/simulado',
    cor: 'azul',
    icone: icone(
      <>
        <path d="M9 11l3 3 8-8" />
        <path d="M20 12v6a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h9" />
      </>,
    ),
  },
  {
    titulo: 'Exercícios práticos',
    texto: 'Programe no seu computador, cole o código e confira com o gabarito no fim da lista.',
    acao: 'Praticar',
    para: '/simulado',
    cor: 'laranja',
    icone: icone(
      <>
        <path d="M8 8l-4 4 4 4" />
        <path d="M16 8l4 4-4 4" />
        <path d="M13.5 5l-3 14" />
      </>,
    ),
  },
  {
    titulo: 'Disciplinas',
    texto: 'Veja cada disciplina do curso, com objetivos, conteúdo e o material disponível.',
    acao: 'Ver disciplinas',
    cor: 'verde',
    icone: icone(
      <>
        <rect x="3" y="3" width="7" height="7" rx="1.5" />
        <rect x="14" y="3" width="7" height="7" rx="1.5" />
        <rect x="3" y="14" width="7" height="7" rx="1.5" />
        <rect x="14" y="14" width="7" height="7" rx="1.5" />
      </>,
    ),
  },
  {
    titulo: 'Dicas',
    texto: 'Novidades e dicas da área de tecnologia, comentadas para as disciplinas.',
    acao: 'Ler dicas',
    para: '/dicas',
    cor: 'rosa',
    icone: icone(
      <>
        <path d="M9 18h6" />
        <path d="M10 21h4" />
        <path d="M12 3a6 6 0 0 0-4 10.5c.8.8 1 1.6 1 2.5h6c0-.9.2-1.7 1-2.5A6 6 0 0 0 12 3z" />
      </>,
    ),
  },
  {
    titulo: 'Gerar prova',
    texto: 'Para professores: monte uma prova com as questões do site e imprima no modelo padrão.',
    acao: 'Montar prova',
    para: '/gerar-prova',
    cor: 'cinza',
    icone: icone(
      <>
        <path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z" />
        <path d="M14 3v5h5" />
        <path d="M9 13h6M9 17h4" />
      </>,
    ),
  },
]

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
            <Link to="/apostilas" className="hero-botao">
              Abrir as apostilas
            </Link>
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

      <section className="secao-inicio" aria-labelledby="titulo-caminhos">
        <p className="etiqueta">comece por aqui</p>
        <h2 id="titulo-caminhos" className="titulo-secao">
          Por onde você quer começar?
        </h2>
        <div className="caminhos">
          {CAMINHOS.map((c) => {
            const conteudo = (
              <>
                <span className={`caminho-icone caminho-${c.cor}`} aria-hidden="true">
                  {c.icone}
                </span>
                <h3>{c.titulo}</h3>
                <p>{c.texto}</p>
                <span className="caminho-acao">{c.acao} →</span>
              </>
            )
            return c.para ? (
              <Link key={c.titulo} to={c.para} className="caminho">
                {conteudo}
              </Link>
            ) : (
              <button
                key={c.titulo}
                className="caminho"
                onClick={() => document.getElementById('disciplinas')?.scrollIntoView({ behavior: 'smooth' })}
              >
                {conteudo}
              </button>
            )
          })}
        </div>
      </section>

      <section className="secao-inicio" aria-labelledby="titulo-como">
        <p className="etiqueta">como funciona</p>
        <h2 id="titulo-como" className="titulo-secao">
          Três passos para aprender de verdade
        </h2>
        <ol className="passos">
          <li>
            <span className="passo-numero">1</span>
            <h3>Estude</h3>
            <p>Leia o capítulo da apostila, com exemplos explicados e código que funciona.</p>
          </li>
          <li>
            <span className="passo-numero">2</span>
            <h3>Pratique</h3>
            <p>Resolva os exercícios práticos no seu computador e compare com o gabarito no fim.</p>
          </li>
          <li>
            <span className="passo-numero">3</span>
            <h3>Teste-se</h3>
            <p>Faça o simulado do capítulo, veja a sua nota e as resoluções comentadas.</p>
          </li>
        </ol>
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
