// Política de Privacidade (LGPD, Lei nº 13.709/2018). Texto em linguagem simples.
// Revise com quem for responsável legal pelo site antes de publicar.

export default function Privacidade() {
  return (
    <article className="texto-legal">
      <h1>Política de Privacidade</h1>
      <p className="dica">Última atualização: outubro de 2026.</p>

      <p>
        Esta política explica quais dados pessoais este site coleta no cadastro, para que eles são usados e quais são
        os seus direitos, de acordo com a Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018).
      </p>

      <h2>1. Quais dados coletamos</h2>
      <ul>
        <li>
          <strong>No cadastro:</strong> nome completo, matrícula, período do curso e e-mail.
        </li>
        <li>
          <strong>Senha:</strong> guardada de forma criptografada pelo serviço de autenticação. Ninguém da administração
          do site tem acesso à sua senha.
        </li>
        <li>
          <strong>Registros de acesso:</strong> data do cadastro e do último acesso, mantidos pelo serviço de
          autenticação por segurança.
        </li>
      </ul>
      <p>
        As respostas dos simulados, o histórico de notas e os códigos que você escreve nos exercícios práticos ficam
        guardados <strong>apenas no seu navegador</strong> e não são enviados para nós.
      </p>

      <h2>2. Para que usamos os dados</h2>
      <ul>
        <li>Identificar você e permitir o acesso ao conteúdo do site.</li>
        <li>Liberar as disciplinas de acordo com o seu período: as do seu período, as dos anteriores e as optativas.</li>
        <li>Enviar mensagens necessárias para a conta, como a confirmação do e-mail e o link para criar nova senha.</li>
      </ul>
      <p>Não usamos os seus dados para publicidade e não os vendemos a ninguém.</p>

      <h2>3. Base legal</h2>
      <p>
        O tratamento é feito com base no seu <strong>consentimento</strong>, dado ao aceitar esta política no
        cadastro, e na execução do serviço que você solicitou ao criar a conta.
      </p>

      <h2>4. Com quem compartilhamos</h2>
      <p>
        Os dados ficam armazenados no Supabase, serviço contratado para a autenticação e o banco de dados, que os trata
        apenas para prestar esse serviço. Não compartilhamos os seus dados com outras empresas, a não ser por
        obrigação legal ou ordem judicial.
      </p>

      <h2>5. Por quanto tempo guardamos</h2>
      <p>
        Enquanto a sua conta existir. Quando você exclui a conta, o seu cadastro é apagado. Registros técnicos de
        segurança podem ser mantidos pelo prazo exigido em lei.
      </p>

      <h2>6. Os seus direitos</h2>
      <ul>
        <li>
          <strong>Consultar os seus dados:</strong> na página Minha conta.
        </li>
        <li>
          <strong>Corrigir o nome:</strong> na página Minha conta. A matrícula e o período são corrigidos pela
          administração do site, a seu pedido.
        </li>
        <li>
          <strong>Excluir a conta e os dados:</strong> a qualquer momento, pelo botão Excluir minha conta, na página
          Minha conta.
        </li>
        <li>
          <strong>Revogar o consentimento:</strong> excluindo a conta.
        </li>
        <li>
          <strong>Tirar dúvidas ou fazer pedidos:</strong> pelos canais de contato indicados no rodapé do site.
        </li>
      </ul>

      <h2>7. Segurança</h2>
      <p>
        O acesso aos dados é protegido por regras no banco de dados: cada pessoa só vê o próprio cadastro, e só a
        administração do site vê a lista de cadastros. A comunicação com o site é criptografada (HTTPS).
      </p>

      <h2>8. Mudanças nesta política</h2>
      <p>
        Esta política pode ser atualizada. Quando houver mudanças importantes, avisaremos no site, e a data no início
        desta página será atualizada.
      </p>
    </article>
  )
}
