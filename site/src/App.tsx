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
          <p className="rodape-credito">
            Desenvolvido por TecPro Tecnologias · <a href="tel:+5521983003074">(21) 98300-3074</a>
          </p>
        </div>
      </footer>
    </HashRouter>
  )
}
