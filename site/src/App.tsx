import { useEffect } from 'react'
import { HashRouter, NavLink, Route, Routes, useLocation, useNavigate, useParams } from 'react-router-dom'
import Inicio from './pages/Inicio'
import Disciplinas from './pages/Disciplinas'
import PaginaDisciplina from './pages/PaginaDisciplina'
import Apostilas from './pages/Apostilas'
import LeituraCapitulo from './pages/LeituraCapitulo'
import Simulado from './pages/Simulado'
import Atualidades from './pages/Atualidades'
import GerarProva from './pages/GerarProva'
import Entrar from './pages/acesso/Entrar'
import CriarConta from './pages/acesso/CriarConta'
import EsqueciSenha from './pages/acesso/EsqueciSenha'
import RedefinirSenha from './pages/acesso/RedefinirSenha'
import MinhaConta from './pages/acesso/MinhaConta'
import Administracao from './pages/acesso/Administracao'
import Privacidade from './pages/acesso/Privacidade'
import { apostilas } from './data/apostilas'
import { AuthProvider, podeAcessar, useAuth } from './lib/auth'
import { ProtegeDisciplina, Protegida } from './lib/Protegida'
import { authConfigurado } from './lib/supabase'

// Rotas com disciplina: o portão confere o período do aluno ---------------------------

function RotaDisciplina() {
  const { id = '' } = useParams()
  return (
    <ProtegeDisciplina disciplinaId={id}>
      <PaginaDisciplina />
    </ProtegeDisciplina>
  )
}

function RotaApostila() {
  const { id = '' } = useParams()
  const disciplinaId = apostilas.find((a) => a.id === id)?.disciplinaId ?? ''
  return (
    <ProtegeDisciplina disciplinaId={disciplinaId}>
      <LeituraCapitulo />
    </ProtegeDisciplina>
  )
}

function RotaSimulado() {
  const { disciplinaId } = useParams()
  if (!disciplinaId) {
    return (
      <Protegida>
        <Simulado />
      </Protegida>
    )
  }
  return (
    <ProtegeDisciplina disciplinaId={disciplinaId}>
      <Simulado />
    </ProtegeDisciplina>
  )
}

/** Quem chega pelo link de "esqueci minha senha" vai direto para a tela de nova senha. */
function DesvioRecuperacao() {
  const { recuperandoSenha } = useAuth()
  const navegar = useNavigate()
  const local = useLocation()
  useEffect(() => {
    if (recuperandoSenha && local.pathname !== '/redefinir-senha') navegar('/redefinir-senha', { replace: true })
  }, [recuperandoSenha, local.pathname, navegar])
  return null
}

function Cabecalho() {
  const { sessao, perfil } = useAuth()
  const professor = podeAcessar(perfil, ['professor', 'admin'])
  const admin = authConfigurado && perfil?.tipo === 'admin'
  return (
    <header className="topo no-print">
      <div className="topo-conteudo">
        <NavLink to="/" className="marca">
          <img src={`${import.meta.env.BASE_URL}marca/hub-logo.svg`} alt="" />
          <span>Hub de Estudos</span>
        </NavLink>
        <nav>
          <NavLink to="/disciplinas">Disciplinas</NavLink>
          <NavLink to="/apostilas">Apostilas</NavLink>
          <NavLink to="/simulado">Simulados</NavLink>
          <NavLink to="/dicas">Dicas</NavLink>
          {(!authConfigurado || professor) && <NavLink to="/gerar-prova">Gerar prova</NavLink>}
          {admin && <NavLink to="/admin">Administração</NavLink>}
          {authConfigurado &&
            (sessao ? (
              <NavLink to="/minha-conta" className="link-conta" title="Minha conta">
                {perfil ? perfil.nome.split(' ')[0] : 'Minha conta'}
              </NavLink>
            ) : (
              <NavLink to="/entrar" className="botao-entrar">
                Entrar
              </NavLink>
            ))}
        </nav>
      </div>
    </header>
  )
}

export default function App() {
  return (
    <AuthProvider>
      <HashRouter>
        <DesvioRecuperacao />
        <Cabecalho />
        <main className="conteudo">
          <Routes>
            {/* abertas: a vitrine, as telas de acesso e a política de privacidade */}
            <Route path="/" element={<Inicio />} />
            <Route path="/entrar" element={<Entrar />} />
            <Route path="/criar-conta" element={<CriarConta />} />
            <Route path="/esqueci-senha" element={<EsqueciSenha />} />
            <Route path="/redefinir-senha" element={<RedefinirSenha />} />
            <Route path="/privacidade" element={<Privacidade />} />

            {/* só para quem tem conta (e, nas disciplinas, conforme o período do aluno) */}
            <Route path="/disciplinas" element={<Protegida><Disciplinas /></Protegida>} />
            <Route path="/disciplina/:id" element={<RotaDisciplina />} />
            <Route path="/apostilas" element={<Protegida><Apostilas /></Protegida>} />
            <Route path="/apostila/:id" element={<RotaApostila />} />
            <Route path="/simulado" element={<RotaSimulado />} />
            <Route path="/simulado/:disciplinaId" element={<RotaSimulado />} />
            <Route path="/simulado/:disciplinaId/:capituloId/:tipo" element={<RotaSimulado />} />
            <Route path="/dicas" element={<Protegida><Atualidades /></Protegida>} />
            <Route path="/dicas/:id" element={<Protegida><Atualidades /></Protegida>} />
            {/* endereços antigos, de quando a aba se chamava Atualidades */}
            <Route path="/atualidades" element={<Protegida><Atualidades /></Protegida>} />
            <Route path="/atualidades/:id" element={<Protegida><Atualidades /></Protegida>} />
            <Route path="/minha-conta" element={<Protegida liberarEmAnalise><MinhaConta /></Protegida>} />

            {/* só professores e administradores */}
            <Route path="/gerar-prova" element={<Protegida tipos={['professor', 'admin']}><GerarProva /></Protegida>} />
            <Route path="/admin" element={<Protegida tipos={['admin']}><Administracao /></Protegida>} />
          </Routes>
        </main>
        <footer className="rodape no-print">
          <div className="rodape-conteudo">
            <div className="rodape-redes">
              <a href="https://www.instagram.com/tecpro_tecnologias/" target="_blank" rel="noreferrer" aria-label="Instagram" title="Instagram">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" strokeWidth="1.8"
                     aria-hidden="true">
                  <rect x="3" y="3" width="18" height="18" rx="5" />
                  <circle cx="12" cy="12" r="4" />
                  <circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none" />
                </svg>
              </a>
              <a href="https://www.facebook.com/profile.php?id=61575373685541" target="_blank" rel="noreferrer" aria-label="Facebook" title="Facebook">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true">
                  <path d="M13.5 21v-7.5H16l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.5V4.4c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.4H8v3h2.6V21z" />
                </svg>
              </a>
            </div>
            <p className="rodape-credito">
              Todos os direitos reservados.
              <br />
              Desenvolvido por TecPro Tecnologias
              {authConfigurado && (
                <>
                  <br />
                  <NavLink to="/privacidade">Política de privacidade</NavLink>
                </>
              )}
            </p>
          </div>
        </footer>
      </HashRouter>
    </AuthProvider>
  )
}
