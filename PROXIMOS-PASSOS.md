# Próximos passos

Só o que **ainda falta fazer**. A data entre parênteses é o dia em que o item foi pedido.
Quando um item for concluído, ele sai da lista (o histórico fica no Git).

O site está em https://estudos.tecprotecnologias.com.br (Cloudflare) e se atualiza sozinho a cada envio para o GitHub.

## Conteúdo

- [ ] **Horários das aulas no pedido de disciplina de outro período** (pedido em 23/10/2026). **A confirmar: ela ainda está analisando; não começar sem o ok dela.** Cadastrar os horários das aulas de cada disciplina (dia da semana e hora) e, no pedido de acesso a disciplina de outro período, mostrar ao aluno só as que **não batem com o horário** das disciplinas do período em que ele está matriculado. Ex.: aluno do 2º período com Estatística às 19h não pode pedir outra disciplina no mesmo dia e horário. Hoje a administração confere isso em outro sistema antes de aprovar. Precisa dos quadros de horário de cada período.
  - Outro caso em análise (pedido em 23/10/2026): o aluno se matricula no seu período e **escolhe quais disciplinas quer cursar**: as do período dele e, além delas, outras que estejam disponíveis, sempre com a regra de dia e horário (e os pré-requisitos). Entender com ela antes de fazer.
- [ ] **Disciplinas dos outros cursos da Graduação** (pedido em 23/10/2026). Só Sistemas para Internet tem disciplinas; os outros 17 cursos (Bacharelado e Licenciatura até o 10º período, Tecnólogo até o 5º) aparecem nos filtros, mas sem cartões. Duas opções: ela manda a grade de cada curso, ou o Claude monta uma grade provisória com as disciplinas mais comuns (começando por um curso para ela conferir). Cada disciplina leva `curso` (id em `CURSOS`, `src/lib/niveis.ts`). Para cada curso, pedir também a **matriz com os pré-requisitos** (vão em `src/data/prerequisitos.ts`) e **em que período ficam as optativas** (`PERIODO_DAS_OPTATIVAS`, `src/lib/niveis.ts`); sem isso, o aluno pode pedir qualquer disciplina e vê as optativas em todos os períodos.

- [ ] **Web III: exercícios e simulado** (pedido em 17/10/2026). Os 12 capítulos estão prontos. Falta uma seção de exercícios no fim de cada capítulo e o simulado da Web III no site com **os mesmos exercícios, no mesmo capítulo**, mais as objetivas no estilo de concurso. Regra geral: todo exercício da apostila também está no simulado.
  - Arquivos: `apostilas/web-iii` (LaTeX e PDF). Para retomar, basta dizer ao Claude "vamos continuar a apostila da Web III".
- [ ] **Web I: apostila "Desenvolvimento Web Front-End: HTML, CSS, JavaScript e TypeScript"** (pedido em 17/10/2026). Os caps. 1 e 2 estão prontos. Só a base do front-end, sem repetir a Web II nem a Web III, e sem projeto acompanhando; exercícios e simulado depois dos 12 capítulos.
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
- [ ] **Módulo Projetos no site** (pedido em 17/10/2026): um módulo próprio, separado das apostilas, exercícios e simulados, com os projetos de todas as disciplinas, organizados por período. Os projetos dos materiais da faculdade (o portfólio da Web I, o projeto final da Web II) ficam guardados para esse módulo.
- [ ] **Apostilas seguintes** (pedido em 17/10/2026): Estrutura de Dados, Análise e Projeto de Sistemas, Cliente-Servidor, Dispositivos Móveis, Gestão de Banco de Dados.
- [ ] **Livro de Node.js, Express e MySQL: deixar pronto para publicar** (pedido em 20/10/2026). Guia prático, direto, sem enrolação. Já corrigido e atualizado (Node 24, MySQL 9.7). Falta:
  - Já testado (20/10/2026): no MySQL 9.7, as 6 tabelas e o cadastro inicial do cap. 10 foram criados sem erro; a BibliotecaAPI inteira foi montada com o código de cada capítulo.
  - [ ] **← retomar aqui.** Rodar o roteiro de 25 verificações (passo 7 do cap. 13: login certo e errado, token, permissões de leitor e admin, cadastro e validação, PATCH contra o ataque, empréstimo, devolução e novo empréstimo, usuários sem a senha, página HTML). Basta dizer "continua".
  - [ ] Corrigir no livro o que o teste já mostrou (guia prático, direto; só código e avisos curtos onde o leitor travaria):
    1. Código que o livro usa e não mostra: a busca do usuário por e-mail (login); o registro das rotas no `app.js` (`/login`, `/autores`, `/emprestimos`...); o Service e o Controller da listagem paginada e do PATCH; o Controller e a rota da devolução; os scripts finais do `package.json` (`dev`, `start`, `test`).
    2. Senha do seed: o passo 5 do cap. 13 manda gerar hashes reais com bcrypt, mas não mostra como (falta um comando de uma linha).
    3. Formato da listagem: com a paginação, os livros vêm em `dados.data`, mas o teste do cap. 12 e a página do cap. 13 esperam a lista direto em `dados` (a página quebraria).
    4. Segurança no empréstimo: o `usuario_id` vem do corpo da requisição, e um leitor consegue registrar empréstimo em nome de outro; usar `req.usuario.id` (do token).
    5. Senha com `#` no `.env`: sem aspas, o dotenv corta o que vem depois do `#` e a conexão falha com "Access denied"; um aviso de uma linha.
  - [ ] Revisar os serviços citados (Railway sem plano gratuito, Thunder Client pago) e o MySQL Workbench com o MySQL 9.7.
  - [ ] Levar as correções do site de volta para o LaTeX do livro (pasta Guia NODES.js), antes de publicar.

## Segurança dos dados e do site (antes de liberar para os alunos)

### Feito pela dona das contas (pedido em 12/10/2026)
- [ ] Verificação em duas etapas (2FA) no GitHub, no Supabase, no Cloudflare e no e-mail usado neles.
- [ ] Senhas fortes e diferentes em cada serviço, guardadas num gerenciador de senhas (ex.: Bitwarden).
- [ ] Apagar o projeto antigo do Supabase (região Oregon, `pgrzoobsbdtpmmxzqcfj`).
- [ ] Nunca compartilhar nem colocar no GitHub a chave secreta (service_role/secret) nem a senha do banco.

### Feito no código / na configuração (pedido em 12/10/2026)
- [ ] Serviço de e-mail próprio (Brevo ou Resend) no Supabase e religar **Confirm email**.
- [ ] CAPTCHA (Cloudflare Turnstile) no cadastro, no login e no "esqueci minha senha".
- [ ] Senha mais forte: exigir letras e números (no site e no Supabase).
- [ ] Cópia de segurança semanal dos cadastros (script que baixa a tabela `perfis`); avaliar o plano Pro do Supabase (cópias diárias) quando houver muitos alunos.
- [ ] Cabeçalhos de segurança no Cloudflare (CSP, X-Frame-Options, etc.).
- [ ] Rodar o **Security Advisor** do Supabase e corrigir o que ele apontar.

### Logo depois (pedido em 12/10/2026)
- [ ] 2FA dentro do site para a conta de administradora.
- [ ] Alertas do GitHub (Dependabot) para bibliotecas com falha conhecida.
- [ ] **Etapa 2:** mover apostilas, questões e gabaritos para o banco, liberados só para quem está logado e no período certo.

### Sempre (pedido em 12/10/2026)
- [ ] Revisar a lista de cadastros de vez em quando, procurando contas estranhas.
- [ ] Roteiro de incidente (LGPD): o que fazer e quem avisar (alunos e ANPD) se houver vazamento.

## Código "escondido" do Inspecionar (pedido em 12/10/2026)

O navegador precisa baixar o código do site para mostrá-lo, então **não existe forma de esconder 100%** o que roda na tela. Bloquear o botão direito ou o F12 não funciona: qualquer pessoa contorna. O código já vai minificado e sem *source maps*. O que ainda dá para fazer:

- [ ] Ofuscar o JavaScript no build (ex.: `vite-plugin-javascript-obfuscator`): deixa o código muito difícil de ler, mas não impossível.
- [ ] A proteção de verdade é a **Etapa 2** acima: o que for importante (gabaritos, apostilas) fica no servidor e só é entregue a quem tem permissão. O que não é enviado ao navegador não aparece no Inspecionar.
- [ ] Manter o repositório do GitHub privado (o código-fonte original fica só lá).

## Site e contas

- [ ] Revisar a Política de Privacidade (pedido em 12/10/2026).
- [ ] Testar o fluxo de aprovação de professor (pedido em 12/10/2026).
- [ ] Opcional: desligar o site antigo no Netlify, que está parado desde 17/10/2026 (pedido em 18/10/2026).
