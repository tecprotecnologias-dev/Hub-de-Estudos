import { disciplinas } from '../data/disciplinas'
import { apostilasDaDisciplina, questoesDaProva, rotuloApostila } from './capitulos'
import { buscarDisciplina, GRUPOS, grupoDe, nomeGrupo, type Filtro } from './util'

interface Props {
  valor: Filtro
  onChange: (f: Filtro) => void
}

const contar = (pred: (q: (typeof questoesDaProva)[number]) => boolean) => questoesDaProva.filter(pred).length

/** Filtros do banco de questões (usado no gerador de provas). */
export default function Filtros({ valor, onChange }: Props) {
  const daTurma = disciplinas.filter(
    (d) => (!valor.periodo || grupoDe(d) === valor.periodo) && apostilasDaDisciplina(d.id).length > 0,
  )
  const disciplina = buscarDisciplina(valor.disciplinaId)
  // só os capítulos da disciplina: material complementar não entra nas provas
  const capitulos = disciplina ? apostilasDaDisciplina(disciplina.id).filter((a) => !a.grupo) : []

  return (
    <div className="filtros">
      <label>
        Período ou nível
        <select
          value={valor.periodo}
          onChange={(e) => onChange({ ...valor, periodo: e.target.value, disciplinaId: '', capituloId: '' })}
        >
          <option value="">Todos</option>
          {GRUPOS.map((p) => (
            <option key={p} value={p}>
              {nomeGrupo(p)}
            </option>
          ))}
        </select>
      </label>
      <label className="largo">
        Disciplina
        <select value={valor.disciplinaId} onChange={(e) => onChange({ ...valor, disciplinaId: e.target.value, capituloId: '' })}>
          <option value="">Todas</option>
          {daTurma.map((d) => (
            <option key={d.id} value={d.id}>
              {d.nome} ({contar((q) => q.disciplinaId === d.id)})
            </option>
          ))}
        </select>
      </label>
      <label className="largo">
        Capítulo
        <select value={valor.capituloId} disabled={!disciplina} onChange={(e) => onChange({ ...valor, capituloId: e.target.value })}>
          <option value="">{disciplina ? 'Todos' : 'Escolha a disciplina'}</option>
          {capitulos.map((a) => (
            <option key={a.id} value={a.id}>
              {rotuloApostila(a)} – {a.titulo} ({contar((q) => q.capituloId === a.id)})
            </option>
          ))}
        </select>
      </label>
      <label>
        Tipo
        <select value={valor.tipo} onChange={(e) => onChange({ ...valor, tipo: e.target.value })}>
          <option value="">Todas</option>
          <option value="objetiva">Objetivas</option>
          <option value="discursiva">Discursivas</option>
        </select>
      </label>
    </div>
  )
}
