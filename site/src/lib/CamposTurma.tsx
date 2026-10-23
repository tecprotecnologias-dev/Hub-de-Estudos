import { CURSOS, cursosPorTipo, NIVEIS, nomeEtapa, rotuloEtapa, type DadosCurso, type Nivel } from './niveis'
import { partesDoGrupo, type FiltroTurma } from './util'

interface Props {
  valor: FiltroTurma
  onChange: (f: FiltroTurma) => void
  /** grupos que podem ser escolhidos (veja grupoDe); as caixas só mostram o que existe neles */
  grupos: string[]
}

/**
 * Caixas de filtro na mesma ordem do cadastro: Nível de ensino, Curso (só na Graduação) e
 * Ano/período. Vão dentro de um <div className="filtros">.
 */
export default function CamposTurma({ valor, onChange, grupos }: Props) {
  const partes = grupos.map(partesDoGrupo)
  const niveis = NIVEIS.filter((n) => partes.some((p) => p.nivel === n.id))
  const cursos = CURSOS.filter((c) => partes.some((p) => p.nivel === 'graduacao' && p.curso === c.id))
  const etapas = [
    ...new Set(
      partes
        .filter((p) => p.nivel === valor.nivel && (!valor.curso || p.curso === valor.curso))
        .map((p) => p.etapa),
    ),
  ]

  return (
    <>
      <label>
        Nível de ensino
        <select
          value={valor.nivel}
          // o curso e os anos/períodos mudam de um nível para outro
          onChange={(e) => onChange({ nivel: e.target.value as Nivel | '', curso: '', etapa: '' })}
        >
          <option value="">Todos</option>
          {niveis.map((n) => (
            <option key={n.id} value={n.id}>
              {n.nome}
            </option>
          ))}
        </select>
      </label>
      {valor.nivel === 'graduacao' && (
        <label>
          Curso
          <select value={valor.curso} onChange={(e) => onChange({ ...valor, curso: e.target.value, etapa: '' })}>
            <option value="">Todos</option>
            <OpcoesCursos cursos={cursos} />
          </select>
        </label>
      )}
      <label>
        {valor.nivel ? rotuloEtapa(valor.nivel) : 'Ano ou período'}
        <select value={valor.etapa} disabled={!valor.nivel} onChange={(e) => onChange({ ...valor, etapa: e.target.value })}>
          <option value="">{valor.nivel ? 'Todos' : 'Escolha o nível primeiro'}</option>
          {etapas.map((n) => (
            <option key={n} value={n}>
              {nomeEtapa(valor.nivel || null, n)}
            </option>
          ))}
        </select>
      </label>
    </>
  )
}

/** <option>s dos cursos, separados por tipo de graduação (Bacharelado, Licenciatura, Tecnólogo). */
export function OpcoesCursos({ cursos = CURSOS }: { cursos?: DadosCurso[] }) {
  return cursosPorTipo(cursos).map((t) => (
    <optgroup key={t.id} label={t.nome}>
      {t.cursos.map((c) => (
        <option key={c.id} value={c.id}>
          {c.nome}
        </option>
      ))}
    </optgroup>
  ))
}
