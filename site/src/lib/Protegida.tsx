import type { ReactNode } from 'react'
import { Link, Navigate, useLocation } from 'react-router-dom'
import { disciplinas } from '../data/disciplinas'
import { authConfigurado } from './supabase'
import { emAnalise, podeAcessar, podeVerDisciplina, useAuth, type TipoPerfil } from './auth'
import { dadosNivel, NIVEL_PADRAO, nomeEtapa } from './niveis'

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
 * Conteúdo de uma disciplina: o aluno só vê as do seu nível, do ano/período atual e dos
 * anteriores (e as optativas do seu nível).
 */
export function ProtegeDisciplina({ disciplinaId, children }: { disciplinaId: string; children: ReactNode }) {
  const { perfil } = useAuth()
  const d = disciplinas.find((x) => x.id === disciplinaId)
  const outroNivel = !!d && (d.nivel ?? NIVEL_PADRAO) !== (perfil?.nivel ?? NIVEL_PADRAO)
  return (
    <Protegida>
      {!d || podeVerDisciplina(perfil, d) ? (
        children
      ) : (
        <section className="aviso-acesso">
          <h1>{outroNivel ? 'Disciplina de outro nível' : 'Disciplina de outro período'}</h1>
          <p>
            {outroNivel
              ? `${d.nome} é do nível ${dadosNivel(d.nivel).nome}, e o seu cadastro é do nível ${dadosNivel(perfil?.nivel).nome}.`
              : `${d.nome} é do ${nomeEtapa(d.nivel, d.periodo)}. Você tem acesso às disciplinas até o ${
                  perfil?.periodo ? nomeEtapa(perfil.nivel, perfil.periodo) : 'seu ano ou período'
                }.`}
          </p>
          <p className="dica">Se o seu nível ou o seu ano mudou, peça a atualização do cadastro à coordenação do site.</p>
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
  const { perfil } = useAuth()
  return (disciplinaId: string) => {
    const d = disciplinas.find((x) => x.id === disciplinaId)
    return !d || podeVerDisciplina(perfil, d)
  }
}
