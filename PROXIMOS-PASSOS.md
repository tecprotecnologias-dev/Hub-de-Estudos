# Próximos passos

Só o que **ainda falta fazer**. A data entre parênteses é o dia em que o item foi pedido.
Quando um item for concluído, ele sai da lista (o histórico fica no Git).

O site está em https://estudos.tecprotecnologias.com.br (Cloudflare) e se atualiza sozinho a cada envio para o GitHub.

## Conteúdo

- [ ] **Web II: revisão e complemento da apostila** (pedido em 20/10/2026). Roteiro da faculdade: `C:\Users\Neia\Downloads\Material_Didatico_Web_II.pdf`. A correção dos erros e o Módulo 3 já estão feitos.
  - [ ] **← retomar aqui.** Módulo 4: SSR/SSG/ISR/CSR, rotas dinâmicas, loading/error/not-found, useRouter/usePathname, Metadata (SEO)
  - [ ] Módulo 5: fetch com cache e revalidação, generateStaticParams, Server Actions e formulários
  - [ ] Decidir o Módulo 6 (Prisma, Route Handlers, NextAuth): curto, com remissão à Web III, ou completo
  - [ ] Decidir os exercícios do PDF: acrescentar aos que já existem (e levar ao simulado)
  - [ ] Enviar ao GitHub para entrar no site (as mudanças de 20/10/2026 ainda não foram enviadas)
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
- [ ] **Material complementar da Web II** (anotado em 20/10/2026): revisar o guia de Node.js, Express e MySQL (13 caps. e 2 apêndices), o guia de Git, o de Engenharia de Prompt e o infográfico do React.

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
- [ ] Opcional: transferir o projeto do Supabase para a organização da TecPro; o endereço e a chave não mudam (pedido em 18/10/2026).
- [ ] Opcional: desligar o site antigo no Netlify, que está parado desde 17/10/2026 (pedido em 18/10/2026).
