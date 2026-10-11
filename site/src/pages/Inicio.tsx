import { Link } from 'react-router-dom'
import { apostilas } from '../data/apostilas'
import { disciplinas } from '../data/disciplinas'
import { questoes } from '../data/questoes'

const CAMINHOS: { titulo: string; texto: string; acao: string; para: string }[] = [
  {
    titulo: 'Apostilas',
    texto: 'Capítulos completos para ler no site ou imprimir, com exemplos, figuras e erros comuns.',
    acao: 'Abrir apostilas',
    para: '/apostilas',
  },
  {
    titulo: 'Simulados',
    texto: 'Questões objetivas por capítulo, com cronômetro, nota e resolução comentada.',
    acao: 'Fazer um simulado',
    para: '/simulado',
  },
  {
    titulo: 'Exercícios práticos',
    texto: 'Programe no seu computador, cole o código e confira com o gabarito no fim da lista.',
    acao: 'Praticar',
    para: '/simulado',
  },
  {
    titulo: 'Disciplinas',
    texto: 'Veja cada disciplina do curso, com objetivos, conteúdo e o material disponível.',
    acao: 'Ver disciplinas',
    para: '/disciplinas',
  },
  {
    titulo: 'Dicas',
    texto: 'Novidades e dicas da área de tecnologia, comentadas para as disciplinas.',
    acao: 'Ler dicas',
    para: '/dicas',
  },
  {
    titulo: 'Gerar prova',
    texto: 'Para professores: monte uma prova com as questões do site e imprima no modelo padrão.',
    acao: 'Montar prova',
    para: '/gerar-prova',
  },
]

export default function Inicio() {
  const comApostila = disciplinas.filter((d) => apostilas.some((a) => a.disciplinaId === d.id)).length

  return (
    <>
      <section className="hero">
        <div className="hero-texto">
          <h1 className="hero-titulo">
            Aprenda no seu ritmo.
            <br />
            <span>Pratique até dominar.</span>
          </h1>
          <p className="hero-sub">Apostilas completas, exercícios com gabarito e simulados.</p>
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
        <h2 id="titulo-caminhos" className="titulo-secao">
          Por onde você quer começar?
        </h2>
        <div className="caminhos">
          {CAMINHOS.map((c) => {
            const conteudo = (
              <>
                <h3>{c.titulo}</h3>
                <p>{c.texto}</p>
                <span className="caminho-acao">{c.acao} →</span>
              </>
            )
            return (
              <Link key={c.titulo} to={c.para} className="caminho">
                {conteudo}
              </Link>
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
    </>
  )
}
