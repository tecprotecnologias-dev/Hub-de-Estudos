import { useEffect } from 'react'
import { Link } from 'react-router-dom'
import { podeAcessar, useAuth } from '../lib/auth'

const CAMINHOS: { titulo: string; texto: string; acao: string; para: string }[] = [
  {
    titulo: 'Disciplinas',
    texto: 'Veja cada disciplina do curso, com objetivos, conteúdo e o material disponível.',
    acao: 'Ver disciplinas',
    para: '/disciplinas',
  },
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
  const { perfil } = useAuth()
  // o Gerar prova é só para professores e administradores
  const caminhos = CAMINHOS.filter((c) => c.para !== '/gerar-prova' || podeAcessar(perfil, ['professor', 'admin']))

  // Só a página inicial tem o fundo roxo profundo; as páginas de estudo continuam claras.
  useEffect(() => {
    document.body.classList.add('pagina-inicial')
    return () => document.body.classList.remove('pagina-inicial')
  }, [])

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
        </div>
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
          {caminhos.map((c) => {
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
        <h2 id="titulo-como" className="titulo-secao">
          Três passos para aprender e sair na frente
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
