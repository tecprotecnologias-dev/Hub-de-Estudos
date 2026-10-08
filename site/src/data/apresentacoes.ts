// Texto inicial (apresentação) de cada disciplina, escrito pela professora.
// A chave é o id da disciplina (veja src/data/disciplinas.ts).
//
// Formato simples:
//   - parágrafos separados por uma linha em branco
//   - "## Título" para um subtítulo
//   - "- item" para lista com marcador; "1. item" para lista numerada
//   - **texto** para negrito
// O primeiro parágrafo também aparece, resumido, no cartão da tela inicial.
// Quando a disciplina tem apresentação, as seções antigas "Objetivos" e
// "Habilidades e competências" (do plano de ensino) deixam de aparecer.
export const apresentacoes: Record<string, string> = {
  'engenharia-de-software-e-da-usabilidade': `A apostila de Engenharia de Software e Usabilidade Web foi estruturada para capacitar estudantes e profissionais no planejamento, desenvolvimento, avaliação e manutenção de sistemas modernos, com foco especial na qualidade, na segurança e na experiência do usuário em aplicações web.

Com uma abordagem prática e alinhada ao mercado, este material orienta você desde o levantamento inicial de requisitos e padrões arquiteturais até o design centrado no usuário, testes automatizados e práticas avançadas de DevSecOps.

## O que você vai aprender?

O conteúdo abrange as principais etapas do ciclo de vida de desenvolvimento e as melhores práticas de Engenharia de Software e Interação Humano-Computador:

- **Ciclos de Vida e Metodologias:** Estudo de modelos de desenvolvimento (Cascata, Incremental, Ágil) e a aplicação prática de frameworks como Scrum e Kanban na gestão de projetos.
- **Arquitetura e Orientação a Objetos:** Projeto de sistemas e componentes, padrões arquiteturais (MVC), aplicação dos princípios SOLID e conceitos essenciais de POO (Herança, Polimorfismo e Encapsulamento).
- **Qualidade e Testes de Software:** Diferenças entre Quality Assurance (QA) e Quality Control (QC), estratégias de testes (unitários, integração, sistema e aceitação), automação e métricas de qualidade.
- **Usabilidade, UX e IHC:** Fundamentos de Interação Humano-Computador, arquitetura da informação, design centrado no usuário e metodologias para condução e avaliação de testes de usabilidade em interfaces Web.
- **Gestão de Configuração e Mudanças:** Controle de versão, parâmetros de configuração, auditorias e relatórios de status para manter a integridade dos projetos.
- **Segurança na Web e DevSecOps:** Integração contínua entre Desenvolvimento, Operações e Segurança, prevenindo vulnerabilidades críticas com base nas diretrizes do OWASP Top 10.

## Habilidades Desenvolvidas

Ao dominar o conteúdo deste material, você estará preparado para:

1. **Modelar e Planejar Projetos:** Escolher a metodologia e arquitetura mais adequadas para o contexto e as metas da organização.
2. **Especificar e Garantir Qualidade:** Levantar requisitos funcionais e não funcionais com precisão, aplicando técnicas modernas de teste e controle de qualidade.
3. **Projetar Interfaces Eficientes:** Criar e avaliar telas e fluxos focados na usabilidade, garantindo uma experiência de uso intuitiva e acessível nas aplicações Web.
4. **Analisar e Otimizar Processos:** Identificar gargalos em projetos existentes, propondo melhorias em arquitetura, código, manutenção e segurança.

## Para quem é este material?

Esta apostila é ideal para estudantes de Engenharia de Software, Ciência da Computação, Análise e Desenvolvimento de Sistemas, Sistemas de Informação, além de desenvolvedores, analistas de requisitos e designers de UX/UI que buscam consolidar conhecimentos teóricos e práticos no desenvolvimento de software de alta qualidade.`,

  'programacao-e-design-para-web-ii': `## O que você vai aprender?

Você vai percorrer o caminho completo do desenvolvimento web moderno com JavaScript: começa entendendo o Node.js e o ecossistema NPM, a base que roda por trás de praticamente todo projeto web atual. Em seguida, entra no React, aprendendo a construir interfaces a partir de componentes e props, e depois avança para hooks e estado, dando vida e interatividade a essas interfaces. Com essa base, você passa para o Next.js, um framework que organiza rotas, páginas e navegação de forma estruturada através do App Router. Por fim, você aprende a diferença entre Server e Client Components — entendendo onde cada parte do seu código roda e por quê, uma das decisões mais importantes em aplicações Next.js modernas.

## Habilidades Desenvolvidas

- Uso do Node.js e gerenciamento de pacotes com NPM
- Construção de interfaces com componentes React e props
- Gerenciamento de estado e uso de hooks (useState, useEffect, entre outros)
- Roteamento baseado em pastas com o App Router do Next.js
- Criação de layouts compartilhados e navegação entre páginas
- Distinção entre Server Components e Client Components, e quando usar cada um
- Organização de projetos full-stack baseados em React/Next.js

## Para quem é este material?

Para alunos de Programação e Design para Web II que estão construindo, do zero, a base necessária para desenvolver aplicações web modernas com React e Next.js — desde o ambiente de execução (Node.js) até a montagem de páginas reais com rotas e navegação. É indicado tanto para quem está começando no desenvolvimento front-end orientado a componentes quanto para quem já conhece HTML/CSS/JavaScript básico e quer dar o próximo passo rumo a frameworks profissionais.`,
}
