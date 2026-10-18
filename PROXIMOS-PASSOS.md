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
- [x] ~~Arrastar a pasta `site\dist` para o Netlify~~ — feito em 17/10/2026 às 22h48 (última publicação). **Os créditos do Netlify acabaram nessa noite:** o site continua no ar com essa versão, mas novas publicações estão pausadas. O que for feito depois (caps. da Web I em diante) só chega ao site com a mudança para o Cloudflare Pages (abaixo).
- [x] **Hospedagem trocada do Netlify para o Cloudflare** (18/10/2026): site no ar em https://estudos.tecprotecnologias.com.br, conta Cloudflare da TecPro, Worker `hubdeestudos`, publica sozinho a cada envio para o GitHub (repositório novo: https://github.com/tecprotecnologias-dev/Hub-de-Estudos). Build com Path `/site` e as variáveis `VITE_SUPABASE_URL` e `VITE_SUPABASE_ANON_KEY`. No Supabase (que continua em outra conta de e-mail), Site URL e Redirect URLs trocadas para o endereço novo. Os sites de venda usam checkout externo (Mercado Pago, Stripe, Hotmart): o site não recebe dados de cartão.
- [ ] Opcional: transferir o projeto do Supabase para a organização da TecPro (o endereço e a chave não mudam).
- [ ] Opcional: desligar o site antigo no Netlify.
- [ ] Revisar a Política de Privacidade.
- [ ] Testar o fluxo de aprovação de professor.

## Conteúdo
- [x] Web II: 50 questões objetivas no estilo de concurso (10 por módulo).
- [ ] **Web III — apostila "Desenvolvimento de APIs para a Web" (os 12 capítulos prontos em 17/10/2026)**
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
  - [x] Cap. 11 Testes de API
  - [x] Cap. 12 Segurança e deploy
  - [ ] **← retomar aqui.** Depois do cap. 12 (decidido em 17/10/2026): uma seção de exercícios no fim de cada um dos 12 capítulos da apostila e o simulado da Web III no site com **os mesmos exercícios, no mesmo capítulo**, mais as objetivas no estilo de concurso. Regra geral: todo exercício da apostila também está no simulado.
  - Arquivos: `apostilas/web-iii` (LaTeX e PDF). Para retomar, basta dizer ao Claude "vamos continuar a apostila da Web III": o passo a passo técnico está guardado na memória dele.
- [ ] **Web I — apostila "Desenvolvimento Web Front-End: HTML, CSS, JavaScript e TypeScript" (começada em 17/10/2026)**. Só a base do front-end, sem repetir a Web II (Node, React, Next) nem a Web III (APIs). Sem projeto acompanhando; exercícios e simulado depois dos 12 capítulos, como na Web III.
  - [x] Cap. 1 Como a Web funciona: navegador, servidor e HTTP
  - [x] Cap. 2 HTML: estrutura, semântica e acessibilidade
  - [ ] Cap. 3 Formulários e validação nativa
  - [ ] Cap. 4 CSS: cascata, seletores, box model e tipografia
  - [ ] Cap. 5 Layout com Flexbox e Grid
  - [ ] Cap. 6 Design responsivo e animações
  - [ ] Cap. 7 Bootstrap e Tailwind
  - [ ] Cap. 8 JavaScript: a linguagem
  - [ ] Cap. 9 JavaScript no navegador: DOM, eventos e armazenamento (com jQuery)
  - [ ] Cap. 10 Consumindo APIs no navegador: fetch, JSON e serviços externos
  - [ ] Cap. 11 TypeScript básico
  - [ ] Cap. 12 Git, GitHub e publicação no GitHub Pages
  - Arquivos: `apostilas/web-i`. Roteiro da faculdade: `C:\Users\Neia\Downloads\Material_Didatico_Web_I.pdf`.
- [ ] **Criar no site um módulo Projetos** (decidido em 17/10/2026, para depois): um módulo próprio, separado das apostilas, exercícios e simulados, com os projetos de todas as disciplinas, organizados por período. Os projetos dos materiais da faculdade (como o portfólio da Web I) ficam guardados para esse módulo, e não entram nas apostilas.
- [ ] Apostilas seguintes: Estrutura de Dados, Análise e Projeto de Sistemas, Cliente-Servidor, Dispositivos Móveis, Gestão de Banco de Dados.
