import { HashRouter, NavLink, Route, Routes } from 'react-router-dom'
import Inicio from './pages/Inicio'
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
            <img src={`${import.meta.env.BASE_URL}marca/tecpro-logo.png`} alt="TecPro Tecnologias" />
          </NavLink>
          <nav>
            <NavLink to="/" end>
              Disciplinas
            </NavLink>
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
    </HashRouter>
  )
}
