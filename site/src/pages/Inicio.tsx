import { useEffect } from 'react'
import { Link } from 'react-router-dom'
import { podeAcessar, useAuth } from '../lib/auth'
import { NIVEIS, type DadosNivel } from '../lib/niveis'

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

/** "1º ao 5º ano" ou, na Graduação, os tipos de curso */
function faixa(n: DadosNivel) {
  if (n.id === 'graduacao') return 'Bacharelado, Licenciatura e Tecnólogo'
  return `${n.etapas[0]}º ao ${n.etapas[n.etapas.length - 1]}º ano`
}

export default function Inicio() {
  const { perfil, sessao } = useAuth()
  // o Gerar prova é só para professores e administradores
  const caminhos = CAMINHOS.filter((c) => c.para !== '/gerar-prova' || podeAcessar(perfil, ['professor', 'admin']))

  // marca a página inicial: o cabeçalho fica branco sólido sobre a abertura escura
  useEffect(() => {
    document.body.classList.add('pagina-inicial')
    return () => document.body.classList.remove('pagina-inicial')
  }, [])

  return (
    <>
      <section className="hero">
        <div className="hero-interno">
          <div className="hero-texto">
            <h1 className="hero-titulo">Estudo organizado, do primeiro ano à graduação.</h1>
            <p className="hero-sub">
              Apostilas, exercícios com gabarito e simulados, separados por série, curso e período.
            </p>
            <div className="hero-acoes">
              {sessao ? (
                <Link to="/disciplinas" className="botao botao-latao">
                  Ver minhas disciplinas
                </Link>
              ) : (
                <>
                  <Link to="/criar-conta" className="botao botao-latao">
                    Criar conta
                  </Link>
                  <Link to="/entrar" className="botao botao-contorno">
                    Entrar
                  </Link>
                </>
              )}
            </div>
          </div>
          <dl className="hero-niveis" aria-label="Níveis de ensino atendidos">
            {NIVEIS.map((n) => (
              <div key={n.id}>
                <dt>{n.nome}</dt>
                <dd>{faixa(n)}</dd>
              </div>
            ))}
          </dl>
        </div>
      </section>

      <section className="secao-inicio" aria-labelledby="titulo-caminhos">
        <h2 id="titulo-caminhos" className="titulo-secao">
          Por onde começar
        </h2>
        <ul className="indice">
          {caminhos.map((c) => (
            <li key={c.titulo}>
              <Link to={c.para} className="indice-item">
                <span className="indice-titulo">{c.titulo}</span>
                <span className="indice-texto">{c.texto}</span>
                <span className="indice-acao">{c.acao}</span>
              </Link>
            </li>
          ))}
        </ul>
      </section>

      <section className="secao-inicio" aria-labelledby="titulo-como">
        <h2 id="titulo-como" className="titulo-secao">
          Como estudar aqui
        </h2>
        <ol className="passos">
          <li>
            <span className="passo-numero">1</span>
            <h3>Estude</h3>
            <p>Leia o capítulo da apostila, com exemplos explicados passo a passo.</p>
          </li>
          <li>
            <span className="passo-numero">2</span>
            <h3>Pratique</h3>
            <p>Resolva os exercícios e compare as suas respostas com o gabarito no fim da lista.</p>
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
