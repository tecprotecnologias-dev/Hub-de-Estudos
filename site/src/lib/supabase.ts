import { createClient, type SupabaseClient } from '@supabase/supabase-js'

// Configuração do Supabase (cadastro e login). Os dois valores ficam em site/.env.local,
// que não vai para o GitHub (veja site/.env.example). A chave "anon" é pública por
// natureza: quem protege os dados são as regras do banco (supabase/esquema.sql).
//
// Sem a configuração, o site funciona aberto, como antes do cadastro existir.
const url = import.meta.env.VITE_SUPABASE_URL as string | undefined
const chave = import.meta.env.VITE_SUPABASE_ANON_KEY as string | undefined

export const authConfigurado = Boolean(url && chave)

export const supabase: SupabaseClient | null = authConfigurado
  ? createClient(url!, chave!, {
      auth: {
        // PKCE: os links dos e-mails (confirmação, nova senha) chegam como ?code=..., o que convive
        // bem com o HashRouter (#/rota) do site
        flowType: 'pkce',
        detectSessionInUrl: true,
        persistSession: true,
      },
    })
  : null

/** Endereço do site para onde os links dos e-mails do Supabase levam a pessoa de volta. */
export function enderecoDoSite() {
  return window.location.origin + window.location.pathname
}
