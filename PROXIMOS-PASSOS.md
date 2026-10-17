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

## Publicação
- [x] Site no ar no Netlify: https://hubdeestudos.netlify.app (16/10/2026), ligado ao Supabase.
- [x] No Supabase, Site URL e Redirect URLs com o endereço do Netlify.
- [ ] **Arrastar a pasta `site\dist` para o Netlify** para publicar o que foi feito depois (design novo já publicado; faltam os simulados da Web II e os capítulos 1 a 10 da Web III). Antes de arrastar, rodar `npm run build` dentro de `site`.
- [ ] (Opcional) Ligar o Netlify ao GitHub, para publicar sozinho a cada envio, sem arrastar pasta.
- [ ] Revisar a Política de Privacidade.
- [ ] Testar o fluxo de aprovação de professor.

## Conteúdo
- [x] Web II: 50 questões objetivas no estilo de concurso (10 por módulo).
- [ ] **Web III — apostila "Desenvolvimento de APIs para a Web" (caps. 1 a 10 prontos em 17/10/2026)**
  - [x] Cap. 1 APIs e Web Services
  - [x] Cap. 2 Design RESTful e métodos HTTP
  - [x] Cap. 3 Preparando o projeto
  - [x] Cap. 4 Roteamento e endpoints
  - [x] Cap. 5 JSON, XML e serialização
  - [x] Cap. 6 Validação com Zod
  - [x] Cap. 7 CRUD
  - [x] Cap. 8 Tratamento de erros e códigos HTTP
  - [x] Cap. 9 Autenticação com JWT
  - [x] Cap. 10 Documentação: Swagger/OpenAPI e Postman
  - [ ] **Cap. 11 Testes de API ← retomar aqui**
  - [ ] Cap. 12 Segurança e deploy
  - [ ] Depois da apostila: exercícios práticos e simulados da Web III
  - Arquivos: `apostilas/web-iii` (LaTeX e PDF). Para retomar, basta dizer ao Claude "vamos continuar a apostila da Web III": o passo a passo técnico está guardado na memória dele.
- [ ] Apostilas seguintes: Estrutura de Dados, Análise e Projeto de Sistemas, Cliente-Servidor, Dispositivos Móveis, Gestão de Banco de Dados, Web I.
