import {
  CURSOS,
  NIVEIS,
  nomeEtapa,
  rotuloEtapa,
  TIPOS_GRADUACAO,
  tipoDoCurso,
  type Nivel,
  type TipoGraduacao,
} from './niveis'
import { partesDoGrupo, type FiltroTurma } from './util'

interface Props {
  valor: FiltroTurma
  onChange: (f: FiltroTurma) => void
  /** grupos que podem ser escolhidos (veja grupoDe); as caixas só mostram o que existe neles */
  grupos: string[]
}

/**
 * Caixas de filtro na mesma ordem do cadastro: Nível de ensino, Tipo de graduação e Curso
 * (só na Graduação) e Ano/período. Vão dentro de um <div className="filtros">. Uma caixa
 * que teria uma opção só não aparece (o aluno, que só tem o seu nível e o seu curso, vê só
 * o Ano/período).
 */
export default function CamposTurma({ valor, onChange, grupos }: Props) {
  const partes = grupos.map(partesDoGrupo)
  const niveis = NIVEIS.filter((n) => partes.some((p) => p.nivel === n.id))
  const cursosComGrupo = CURSOS.filter((c) => partes.some((p) => p.nivel === 'graduacao' && p.curso === c.id))
  const tipos = TIPOS_GRADUACAO.filter((t) => cursosComGrupo.some((c) => c.tipo === t.id))
  const cursos = cursosComGrupo.filter((c) => !valor.tipo || c.tipo === valor.tipo)
  // com um nível só, ele já vale como escolhido (a caixa nem aparece)
  const nivel = valor.nivel || (niveis.length === 1 ? niveis[0].id : '')
  const etapas = [
    ...new Set(
      partes
        .filter(
          (p) =>
            p.nivel === nivel &&
            (!valor.tipo || tipoDoCurso(p.curso) === valor.tipo) &&
            (!valor.curso || p.curso === valor.curso),
        )
        .map((p) => p.etapa),
    ),
  ]

  return (
    <>
      {niveis.length > 1 && (
        <label>
          Nível de ensino
          <select
            value={valor.nivel}
            // o tipo, o curso e os anos/períodos mudam de um nível para outro
            onChange={(e) => onChange({ nivel: e.target.value as Nivel | '', tipo: '', curso: '', etapa: '' })}
          >
            <option value="">Todos</option>
            {niveis.map((n) => (
              <option key={n.id} value={n.id}>
                {n.nome}
              </option>
            ))}
          </select>
        </label>
      )}
      {nivel === 'graduacao' && (
        <>
          {tipos.length > 1 && (
            <label>
              Tipo de graduação
              <select
                value={valor.tipo}
                onChange={(e) =>
                  onChange({ ...valor, tipo: e.target.value as TipoGraduacao | '', curso: '', etapa: '' })
                }
              >
                <option value="">Todos</option>
                {tipos.map((t) => (
                  <option key={t.id} value={t.id}>
                    {t.nome}
                  </option>
                ))}
              </select>
            </label>
          )}
          {cursos.length > 1 && (
            <label>
              Curso
              <select value={valor.curso} onChange={(e) => onChange({ ...valor, curso: e.target.value, etapa: '' })}>
                <option value="">Todos</option>
                {cursos.map((c) => (
                  <option key={c.id} value={c.id}>
                    {c.nome}
                  </option>
                ))}
              </select>
            </label>
          )}
        </>
      )}
      <label>
        {nivel ? rotuloEtapa(nivel) : 'Ano ou período'}
        <select value={valor.etapa} disabled={!nivel} onChange={(e) => onChange({ ...valor, etapa: e.target.value })}>
          <option value="">{nivel ? 'Todos' : 'Escolha o nível primeiro'}</option>
          {etapas.map((n) => (
            <option key={n} value={n}>
              {nomeEtapa(nivel || null, n)}
            </option>
          ))}
        </select>
      </label>
    </>
  )
}
