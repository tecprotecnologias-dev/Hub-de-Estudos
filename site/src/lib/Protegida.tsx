import type { ReactNode } from 'react'
import { Link, Navigate, useLocation } from 'react-router-dom'
import { disciplinas } from '../data/disciplinas'
import { authConfigurado } from './supabase'
import { emAnalise, podeAcessar, podeVerDisciplina, useAuth, type TipoPerfil } from './auth'
import { CURSO_PADRAO, dadosNivel, NIVEL_PADRAO, nomeCurso, nomeEtapa } from './niveis'

// Portões das áreas restritas. Sem o Supabase configurado (site/.env.local), tudo passa:
// o site funciona aberto, como antes do cadastro.

function Carregando() {
  return <p className="dica">Carregando…</p>
}

/**
 * Só para quem está logado (e, se informado, de um destes tipos de perfil).
 * `liberarEmAnalise`: deixa passar o professor ainda não aprovado (usado em Minha conta).
 */
export function Protegida({
  tipos,
  liberarEmAnalise = false,
  children,
}: {
  tipos?: TipoPerfil[]
  liberarEmAnalise?: boolean
  children: ReactNode
}) {
  const { pronto, sessao, perfil } = useAuth()
  const local = useLocation()
  if (!authConfigurado) return <>{children}</>
  if (!pronto) return <Carregando />
  if (!sessao) return <Navigate to="/entrar" replace state={{ de: local.pathname }} />
  if (!perfil) return <Carregando />
  if (liberarEmAnalise && !tipos) return <>{children}</>
  if (emAnalise(perfil)) {
    return (
      <section className="aviso-acesso">
        <h1>Cadastro em análise</h1>
        <p>
          Recebemos o seu cadastro de professor. Assim que a administração do site aprovar, você terá acesso a todo o
          conteúdo e ao Gerar prova.
        </p>
        <Link to="/minha-conta" className="botao secundario">
          Minha conta
        </Link>
      </section>
    )
  }
  if (!podeAcessar(perfil, tipos)) {
    return (
      <section className="aviso-acesso">
        <h1>Área restrita</h1>
        <p>Esta área é só para {tipos?.includes('professor') ? 'professores' : 'administradores'}.</p>
        <Link to="/" className="botao">
          Voltar para o início
        </Link>
      </section>
    )
  }
  return <>{children}</>
}

/**
 * Conteúdo de uma disciplina: o aluno só vê as do seu nível e do ano/período atual (na
 * Graduação, do seu curso, mais as optativas dele).
 */
export function ProtegeDisciplina({ disciplinaId, children }: { disciplinaId: string; children: ReactNode }) {
  const { perfil, liberadas } = useAuth()
  const d = disciplinas.find((x) => x.id === disciplinaId)
  const outroNivel = !!d && (d.nivel ?? NIVEL_PADRAO) !== (perfil?.nivel ?? NIVEL_PADRAO)
  const outroCurso =
    !!d && !outroNivel && (d.nivel ?? NIVEL_PADRAO) === 'graduacao' && (d.curso ?? CURSO_PADRAO) !== (perfil?.curso ?? CURSO_PADRAO)
  return (
    <Protegida>
      {!d || podeVerDisciplina(perfil, d, liberadas) ? (
        children
      ) : (
        <section className="aviso-acesso">
          <h1>
            {outroNivel
              ? 'Disciplina de outro nível'
              : outroCurso
                ? 'Disciplina de outro curso'
                : (d.nivel ?? NIVEL_PADRAO) === 'graduacao'
                ? 'Disciplina de outro período'
                : 'Disciplina de outra série'}
          </h1>
          <p>
            {outroNivel
              ? `${d.nome} é do nível ${dadosNivel(d.nivel).nome}, e o seu cadastro é do nível ${dadosNivel(perfil?.nivel).nome}.`
              : outroCurso
                ? `${d.nome} é do curso ${nomeCurso(d.curso)}, e o seu cadastro é do curso ${nomeCurso(perfil?.curso)}.`
                : (d.nivel ?? NIVEL_PADRAO) === 'graduacao'
                ? `${d.nome} ${d.periodo === 0 ? 'é optativa' : `é do ${nomeEtapa(d.nivel, d.periodo)}`}. Você tem acesso às disciplinas do ${
                    perfil?.periodo ? nomeEtapa(perfil.nivel, perfil.periodo) : 'seu período'
                  }.`
                : `Esta disciplina é do ${nomeEtapa(d.nivel, d.periodo)}. Você tem acesso às disciplinas do ${
                    perfil?.periodo ? nomeEtapa(perfil.nivel, perfil.periodo) : 'seu ano'
                  }.`}
          </p>
          <p className="dica">
            {!outroNivel && !outroCurso && (d.nivel ?? NIVEL_PADRAO) === 'graduacao'
              ? 'Se você cursa esta disciplina, peça acesso no fim da página Disciplinas; a administração do site aprova o pedido.'
              : 'Se o seu nível, curso ou ano mudou, peça a atualização do cadastro à coordenação do site.'}
          </p>
          <Link to="/disciplinas" className="botao">
            Ver as minhas disciplinas
          </Link>
        </section>
      )}
    </Protegida>
  )
}

/** Filtro para listas: a disciplina aparece para este perfil? */
export function useDisciplinaVisivel() {
  const { perfil, liberadas } = useAuth()
  return (disciplinaId: string) => {
    const d = disciplinas.find((x) => x.id === disciplinaId)
    return !d || podeVerDisciplina(perfil, d, liberadas)
  }
}
