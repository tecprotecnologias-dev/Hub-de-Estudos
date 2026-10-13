# Próximos passos

Lista do que está combinado para fazer depois. Marque `[x]` quando concluir.

## Segurança dos dados e do site (antes de liberar para os alunos)

### Feito pela dona das contas
- [ ] Verificação em duas etapas (2FA) no GitHub, no Supabase, na Vercel e no e-mail usado neles.
- [ ] Senhas fortes e diferentes em cada serviço, guardadas num gerenciador de senhas (ex.: Bitwarden).
- [ ] Apagar o projeto antigo do Supabase (região Oregon, `pgrzoobsbdtpmmxzqcfj`).
- [ ] Nunca compartilhar nem colocar no GitHub a chave secreta (service_role/secret) nem a senha do banco.

### Feito no código / na configuração
- [ ] Serviço de e-mail próprio (Brevo ou Resend) no Supabase e religar **Confirm email**.
- [ ] CAPTCHA (Cloudflare Turnstile) no cadastro, no login e no "esqueci minha senha".
- [ ] Senha mais forte: exigir letras e números (no site e no Supabase).
- [ ] Cópia de segurança semanal dos cadastros (script que baixa a tabela `perfis`); avaliar o plano Pro do Supabase (cópias diárias) quando houver muitos alunos.
- [ ] Cabeçalhos de segurança na Vercel (`vercel.json`: CSP, X-Frame-Options, etc.).
- [ ] Rodar o **Security Advisor** do Supabase e corrigir o que ele apontar.

### Logo depois
- [ ] 2FA dentro do site para a conta de administradora.
- [ ] Alertas do GitHub (Dependabot) para bibliotecas com falha conhecida.
- [ ] **Etapa 2:** mover apostilas, questões e gabaritos para o banco, liberados só para quem está logado e no período certo.

### Sempre
- [ ] Revisar a lista de cadastros de vez em quando, procurando contas estranhas.
- [ ] Roteiro de incidente (LGPD): o que fazer e quem avisar (alunos e ANPD) se houver vazamento.

## Código "escondido" do Inspecionar

O navegador precisa baixar o código do site para mostrá-lo, então **não existe forma de esconder 100%** o que roda na tela. Bloquear o botão direito ou o F12 não funciona: qualquer pessoa contorna. O que dá para fazer:

- [x] Código de produção minificado e sem *source maps* (já é o padrão do build: o Inspecionar mostra só um código compactado, sem os arquivos originais).
- [ ] Ofuscar o JavaScript no build (ex.: `vite-plugin-javascript-obfuscator`): deixa o código muito difícil de ler, mas não impossível.
- [ ] A proteção de verdade é a **Etapa 2** acima: o que for importante (gabaritos, apostilas) fica no servidor e só é entregue a quem tem permissão. O que não é enviado ao navegador não aparece no Inspecionar.
- [ ] Manter o repositório do GitHub privado (o código-fonte original fica só lá).

## Publicação (depois das apostilas)
- [ ] Publicar na Vercel com as variáveis `VITE_SUPABASE_URL` e `VITE_SUPABASE_ANON_KEY`.
- [ ] No Supabase, trocar Site URL e Redirect URLs para o domínio da Vercel.
- [ ] Revisar a Política de Privacidade.
- [ ] Testar o fluxo de aprovação de professor.

## Conteúdo
- [ ] Apostilas seguintes: Estrutura de Dados, Análise e Projeto de Sistemas, Cliente-Servidor, Dispositivos Móveis, Gestão de Banco de Dados, Web I, Web III.
