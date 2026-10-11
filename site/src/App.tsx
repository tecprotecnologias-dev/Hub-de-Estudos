import { HashRouter, NavLink, Route, Routes } from 'react-router-dom'
import Inicio from './pages/Inicio'
import Disciplinas from './pages/Disciplinas'
import PaginaDisciplina from './pages/PaginaDisciplina'
import Apostilas from './pages/Apostilas'
import LeituraCapitulo from './pages/LeituraCapitulo'
import Simulado from './pages/Simulado'
import Atualidades from './pages/Atualidades'
import GerarProva from './pages/GerarProva'

export default function App() {
  return (
    <HashRouter>
      <header className="topo no-print">
        <div className="topo-conteudo">
          <NavLink to="/" className="marca">
            <img src={`${import.meta.env.BASE_URL}marca/hub-logo-branco.svg`} alt="" />
            <span>Hub de Estudos</span>
          </NavLink>
          <nav>
            <NavLink to="/disciplinas">Disciplinas</NavLink>
            <NavLink to="/apostilas">Apostilas</NavLink>
            <NavLink to="/simulado">Simulados</NavLink>
            <NavLink to="/dicas">Dicas</NavLink>
            <NavLink to="/gerar-prova">Gerar prova</NavLink>
          </nav>
        </div>
      </header>
      <main className="conteudo">
        <Routes>
          <Route path="/" element={<Inicio />} />
          <Route path="/disciplinas" element={<Disciplinas />} />
          <Route path="/disciplina/:id" element={<PaginaDisciplina />} />
          <Route path="/apostilas" element={<Apostilas />} />
          <Route path="/apostila/:id" element={<LeituraCapitulo />} />
          <Route path="/simulado" element={<Simulado />} />
          <Route path="/simulado/:disciplinaId" element={<Simulado />} />
          <Route path="/simulado/:disciplinaId/:capituloId/:tipo" element={<Simulado />} />
          <Route path="/dicas" element={<Atualidades />} />
          <Route path="/dicas/:id" element={<Atualidades />} />
          {/* endereços antigos, de quando a aba se chamava Atualidades */}
          <Route path="/atualidades" element={<Atualidades />} />
          <Route path="/atualidades/:id" element={<Atualidades />} />
          <Route path="/gerar-prova" element={<GerarProva />} />
        </Routes>
      </main>
      <footer className="rodape no-print">
        <div className="rodape-conteudo">
          <nav className="rodape-links" aria-label="Rodapé">
            <NavLink to="/disciplinas">Disciplinas</NavLink>
            <NavLink to="/apostilas">Apostilas</NavLink>
            <NavLink to="/simulado">Simulados</NavLink>
            <NavLink to="/dicas">Dicas</NavLink>
            <NavLink to="/gerar-prova">Gerar prova</NavLink>
          </nav>
          <div className="rodape-redes">
            <a href="https://www.instagram.com/tecpro_tecnologias/" target="_blank" rel="noreferrer">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="1.8"
                   aria-hidden="true">
                <rect x="3" y="3" width="18" height="18" rx="5" />
                <circle cx="12" cy="12" r="4" />
                <circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none" />
              </svg>
              Instagram
            </a>
            <a href="https://www.facebook.com/profile.php?id=61575373685541" target="_blank" rel="noreferrer">
              <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">
                <path d="M13.5 21v-7.5H16l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.5V4.4c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.4H8v3h2.6V21z" />
              </svg>
              Facebook
            </a>
          </div>
          <p className="rodape-credito">Desenvolvido por TecPro Tecnologias</p>
        </div>
      </footer>
    </HashRouter>
  )
}
