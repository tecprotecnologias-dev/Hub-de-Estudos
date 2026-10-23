import type { ReactNode } from 'react'

/**
 * Página com os filtros numa coluna à esquerda e o conteúdo no centro (prévia de
 * 23/10/2026). Em telas estreitas, os filtros voltam para cima do conteúdo. Sem filtros (o
 * aluno que só vê o seu grupo), mostra só o conteúdo.
 */
export default function ComFiltrosAoLado({ filtros, children }: { filtros?: ReactNode; children: ReactNode }) {
  if (!filtros) return <>{children}</>
  return (
    <div className="com-filtros-ao-lado">
      <aside className="painel-filtros" aria-label="Filtros">
        <h2>Filtrar</h2>
        <div className="filtros">{filtros}</div>
      </aside>
      <div className="conteudo-ao-lado">{children}</div>
    </div>
  )
}
