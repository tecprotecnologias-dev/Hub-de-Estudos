import { Link } from 'react-router-dom'

/** Mostrado nas telas de acesso enquanto o Supabase não estiver configurado (site/.env.local). */
export function AvisoSemCadastro() {
  return (
    <section className="cartao-acesso">
      <h1>Cadastro ainda não ativado</h1>
      <p>
        O cadastro e o login ainda não foram configurados neste site. Por enquanto, todo o conteúdo está aberto.
      </p>
      <Link to="/" className="botao">
        Voltar para o início
      </Link>
    </section>
  )
}
