import type { Apostila } from './tipos'

// Dois tipos de apostila:
//
// 1. Capítulo lido dentro do site: converta para src/data/capitulos/<id>.json e cadastre aqui
//    com o mesmo id e o número do capítulo. Há um conversor para cada modelo de arquivo:
//      - Word com títulos em fonte/cor manual (Legislação): ferramentas/converter_capitulo.py
//      - Word com estilos de título e caixas em tabela (Qualidade): ferramentas/converter_word_estilos.py
//      - LaTeX (.tex): ferramentas/converter_latex.py
//    Todos tiram resumo, estudo de caso e exercícios, e recusam conteúdo com o nome da instituição.
//
// 2. PDF: copie o arquivo para public/apostilas e informe "arquivo: 'apostilas/nome.pdf'".
export const apostilas: Apostila[] = [
  // Legislação em Negócios Digitais
  {
    id: 'legislacao-cap1',
    capitulo: 1,
    titulo: 'Legislação de Proteção de Dados Pessoais',
    disciplinaId: 'legislacao-em-negocios-digitais',
    unidades: ['Legislação de Proteção de Dados Pessoais'],
    descricao:
      'LGPD e GDPR: dados pessoais e sensíveis, princípios e bases legais, responsabilidades das empresas, direitos dos titulares e sanções da ANPD.',
  },
  {
    id: 'legislacao-cap2',
    capitulo: 2,
    titulo: 'Propriedade Intelectual e Direitos Autorais',
    disciplinaId: 'legislacao-em-negocios-digitais',
    unidades: ['Propriedade Intelectual e Direitos Autorais'],
    descricao:
      'Ramos da propriedade intelectual, direitos autorais no ambiente digital, patentes de software, marcas, licenças abertas e pirataria.',
  },
  {
    id: 'legislacao-cap3',
    capitulo: 3,
    titulo: 'Comércio Eletrônico e Contratos Online',
    disciplinaId: 'legislacao-em-negocios-digitais',
    unidades: ['Comércio Eletrônico e Contratos Online'],
    descricao:
      'E-commerce no Brasil, Decreto 7.962/2013 e CDC, obrigações de lojas e marketplaces, pagamentos digitais, contratos e assinatura eletrônica.',
  },
  {
    id: 'legislacao-cap4',
    capitulo: 4,
    titulo: 'Responsabilidade Digital e Crimes Cibernéticos',
    disciplinaId: 'legislacao-em-negocios-digitais',
    unidades: ['Responsabilidade Digital e Crimes Cibernéticos'],
    descricao:
      'Marco Civil da Internet, crimes cibernéticos na lei brasileira, golpes digitais, responsabilidade das plataformas, vazamentos e resposta a incidentes.',
  },
  {
    id: 'legislacao-cap5',
    capitulo: 5,
    titulo: 'Regulamentação de Marketing Digital',
    disciplinaId: 'legislacao-em-negocios-digitais',
    unidades: ['Regulamentação de Marketing Digital'],
    descricao:
      'Publicidade enganosa e abusiva, influenciadores e o CONAR, publicidade segmentada, consentimento, e-mail marketing e públicos vulneráveis.',
  },
  {
    id: 'legislacao-cap6',
    capitulo: 6,
    titulo: 'Aspectos Legais de Startups e Empreendedorismo Digital',
    disciplinaId: 'legislacao-em-negocios-digitais',
    unidades: ['Aspectos Legais de Startups e Empreendedorismo Digital'],
    descricao:
      'Marco Legal das Startups, estruturas jurídicas, captação de investimentos, investidor-anjo, propriedade intelectual, contratos e compliance.',
  },
  {
    id: 'legislacao-cap7',
    capitulo: 7,
    titulo: 'Legislação Internacional em Negócios Digitais',
    disciplinaId: 'legislacao-em-negocios-digitais',
    unidades: ['Legislação Internacional em Negócios Digitais'],
    descricao:
      'Soberania digital, marcos legais internacionais, dados pessoais e tributação no plano global, comércio na OMC e conflitos de jurisdição.',
  },
  {
    id: 'legislacao-cap8',
    capitulo: 8,
    titulo: 'Proteção ao Consumidor em Negócios Digitais',
    disciplinaId: 'legislacao-em-negocios-digitais',
    unidades: ['Proteção ao Consumidor em Negócios Digitais'],
    descricao:
      'Direitos do consumidor online, direito de arrependimento, devoluções, reembolsos e garantias, práticas abusivas e resolução de conflitos.',
  },
  {
    // links das leis na íntegra; página em src/data/capitulos/legislacao-leis.json
    id: 'legislacao-leis',
    rotulo: 'Links',
    grupo: 'Material complementar',
    titulo: 'Textos da LGPD e do GDPR',
    disciplinaId: 'legislacao-em-negocios-digitais',
    descricao: 'Links para ler a LGPD (Lei nº 13.709/2018) e o GDPR, o regulamento europeu de proteção de dados.',
  },

  // Qualidade e Testes de Software
  // Capítulos 1 a 11: ferramentas/converter_word_estilos.py (um capítulo por unidade)
  // Capítulos 12 e 13: ferramentas/converter_latex.py <tex> <json> 12|13 (antigos capítulos 8 e 9;
  // depois da conversão, as referências "Capítulo 7/8" no texto foram atualizadas para 11/12)
  {
    id: 'qualidade-cap1',
    capitulo: 1,
    titulo: 'Conceitos Básicos de Qualidade de Software',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Conceitos Básicos de Qualidade de Software'],
    descricao:
      'Definições clássicas de qualidade, qualidade de produto, processo e uso, fatores internos e externos, modelo de McCall e Custo da Qualidade.',
  },
  {
    id: 'qualidade-cap2',
    capitulo: 2,
    titulo: 'Modelos de Qualidade de Software',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Modelos de Qualidade de Software'],
    descricao:
      'A ISO/IEC 9126 e suas seis características, da funcionalidade à portabilidade, e a evolução para a ISO/IEC 25010 (SQuaRE).',
  },
  {
    id: 'qualidade-cap3',
    capitulo: 3,
    titulo: 'Modelos de Maturidade do Software',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Modelos de Maturidade do Software'],
    descricao: 'CMM, CMMI e MPS.BR: níveis de maturidade, áreas de processo, comparativo e aplicação prática.',
  },
  {
    id: 'qualidade-cap4',
    capitulo: 4,
    titulo: 'Testes de Software',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Testes de Software'],
    descricao:
      'Níveis de teste (unitário, integração, sistema e aceitação), técnicas de caixa branca e caixa preta, e testes alfa e beta.',
  },
  {
    id: 'qualidade-cap5',
    capitulo: 5,
    titulo: 'Estratégias de Teste',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Estratégias de Teste'],
    descricao:
      'Planejamento da estratégia em 7 passos, análise de risco, plano de teste (IEEE 829) e combinação de técnicas em contextos ágeis.',
  },
  {
    id: 'qualidade-cap6',
    capitulo: 6,
    titulo: 'Automação de Testes',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Automação de Testes'],
    descricao:
      'Vantagens e limites da automação, ROI, quando automatizar, Selenium, JUnit, TestNG e outras ferramentas como Cypress e Playwright.',
  },
  {
    id: 'qualidade-cap7',
    capitulo: 7,
    titulo: 'Testes de Regressão',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Testes de Regressão'],
    descricao:
      'Quando fazer regressão, estratégias de seleção de casos, automação da suíte, regressão em CI/CD e manutenção da suíte.',
  },
  {
    id: 'qualidade-cap8',
    capitulo: 8,
    titulo: 'Testes de Performance e Carga',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Testes de Performance e Carga'],
    descricao:
      'Desempenho e escalabilidade, métricas e percentis, testes de carga, estresse, pico e resistência, e ferramentas de performance.',
  },
  {
    id: 'qualidade-cap9',
    capitulo: 9,
    titulo: 'Testes de Segurança',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Testes de Segurança'],
    descricao:
      'Conceitos de segurança, prevenção de vulnerabilidades, testes de penetração, OWASP ZAP e OWASP Top 10.',
  },
  {
    id: 'qualidade-cap10',
    capitulo: 10,
    titulo: 'Gerenciamento de Defeitos e Relatórios',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Gerenciamento de Defeitos e Relatórios'],
    descricao:
      'Terminologia de defeitos, severidade e prioridade, como escrever um bom bug report, ciclo de vida, métricas e ferramentas.',
  },
  {
    id: 'qualidade-cap11',
    capitulo: 11,
    titulo: 'Melhores Práticas de Teste e Garantia de Qualidade',
    disciplinaId: 'qualidade-e-testes-de-software',
    unidades: ['Melhores Práticas de Teste e Garantia de Qualidade'],
    descricao:
      'Fundamentos de QA, normas de qualidade, boas práticas de teste, CI/CD, práticas ágeis e melhoria contínua de processos.',
  },
  {
    id: 'qualidade-cap12',
    capitulo: 12,
    grupo: 'Material prático',
    titulo: 'Projeto Final',
    disciplinaId: 'qualidade-e-testes-de-software',
    descricao:
      'A aplicação TaskFlow: testes unitários, de integração e E2E, performance com k6, pipeline de CI/CD e rubrica de avaliação.',
  },
  {
    id: 'qualidade-cap13',
    capitulo: 13,
    grupo: 'Material prático',
    titulo: 'Testes Práticos com Postman',
    disciplinaId: 'qualidade-e-testes-de-software',
    descricao: 'O que é uma API, métodos HTTP, collections, primeiros testes no Postman e como rodar tudo de uma vez.',
  },

  // Engenharia de Software
  // Capítulos 1 e 4 a 12: Apostila_Completa.tex, separada com ferramentas/separar_latex.py e
  // convertida com ferramentas/converter_latex.py.
  // Capítulos 2 e 3: a versão nova (31/08) só existe em PDF -> ferramentas/converter_pdf_latex.py
  // (cap. 2 com --trocar para remover uma referência institucional de uma tabela,
  // juntar "Manutenibilidade" e quebrar a linha antes de RF03).
  {
    id: 'engsoft-cap1',
    capitulo: 1,
    titulo: 'Ciclo de Vida de Desenvolvimento de Software',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Ciclo de Vida de Desenvolvimento de Software'],
    descricao: 'Modelos de desenvolvimento (cascata, incremental, espiral, ágil), fases do ciclo de vida e comparativo entre os modelos.',
  },
  {
    id: 'engsoft-cap2',
    capitulo: 2,
    titulo: 'Requisitos de Software',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Requisitos de Software'],
    descricao: 'Técnicas de elicitação, histórias de usuário, critérios de qualidade, MoSCoW, documentação e requisitos funcionais e não funcionais.',
  },
  {
    id: 'engsoft-cap3',
    capitulo: 3,
    titulo: 'Arquitetura de Software',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Arquitetura de Software'],
    descricao: 'Design de sistemas e componentes, princípios SOLID, padrões arquiteturais e MVC, manutenção, modernização e substituição.',
  },
  {
    id: 'engsoft-cap4',
    capitulo: 4,
    titulo: 'Programação Orientada a Objetos (POO)',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Programação Orientada a Objetos'],
    descricao: 'Classes e objetos, os quatro pilares da POO, herança, polimorfismo e abstração em profundidade, e princípios SOLID.',
  },
  {
    id: 'engsoft-cap5',
    capitulo: 5,
    titulo: 'Testes de Software',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Testes de Software'],
    descricao: 'Conceitos de QA, caixa branca, preta e cinza, níveis de teste e pirâmide, automação de testes e CI/CD.',
  },
  {
    id: 'engsoft-cap6',
    capitulo: 6,
    titulo: 'Qualidade de Software',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Qualidade de Software'],
    descricao: 'Controle de qualidade, QA vs. QC, métricas de produto e processo, CMMI e MPS.BR, custo da qualidade e DevOps.',
  },
  {
    id: 'engsoft-cap7',
    capitulo: 7,
    titulo: 'Gestão da Configuração de Software',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Gestão da Configuração'],
    descricao: 'Itens de configuração, controle de versões com Git, estratégias de branching, auditoria e controle de mudanças.',
  },
  {
    id: 'engsoft-cap8',
    capitulo: 8,
    titulo: 'Gestão de Projetos de Software',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Gestão de Projetos de Software'],
    descricao: 'Planejamento, execução e monitoramento de projetos, Scrum, Kanban e comparativo entre os dois.',
  },
  {
    id: 'engsoft-cap9',
    capitulo: 9,
    titulo: 'Usabilidade e Experiência do Usuário (UX)',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Usabilidade e Experiência do Usuário (UX)'],
    descricao: 'UI vs. UX, as dez heurísticas de Nielsen, Gestalt e leis cognitivas, testes de usabilidade e design centrado no usuário.',
  },
  {
    id: 'engsoft-cap10',
    capitulo: 10,
    titulo: 'Engenharia de Requisitos',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Engenharia de Requisitos'],
    descricao: 'Técnicas de elicitação, análise e priorização, especificação (ERS/SRS), critérios de aceitação e requisitos em contextos ágeis.',
  },
  {
    id: 'engsoft-cap11',
    capitulo: 11,
    titulo: 'Interação Humano-Computador (IHC)',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    unidades: ['Interação Humano-Computador'],
    descricao: 'Modelo de interação e affordances, paradigmas (CLI, GUI, toque, voz, AR/VR), design de interação, acessibilidade (WCAG) e avaliação.',
  },
  {
    id: 'engsoft-cap12',
    capitulo: 12,
    grupo: 'Material complementar',
    titulo: 'Segurança para Desenvolvimento de Software',
    disciplinaId: 'engenharia-de-software-e-da-usabilidade',
    descricao: 'DevOps e DevSecOps, ferramentas de segurança no pipeline, modelagem de ameaças com STRIDE e OWASP Top 10.',
  },

  // Gestão de Sistemas Digitais na Web
  // Fonte: 02- APOSTILAS/LATEX/Capitulo*.tex (mesma versão dos PDFs de 11/08), ferramentas/converter_latex.py.
  // O capítulo 2 (Cloud) não tem unidade própria no plano: ligado à unidade de Arquitetura.
  {
    id: 'gestaoweb-cap1',
    capitulo: 1,
    titulo: 'Arquitetura de Software e Web',
    disciplinaId: 'gestao-de-sistemas-digitais-na-web',
    unidades: ['Arquitetura de Sistemas na Web'],
    descricao:
      'Evolução das arquiteturas, protocolos, cliente-servidor, URL e HTTP, HTML/CSS/JavaScript, W3C, hipertexto e arquiteturas distribuídas com APIs.',
  },
  {
    id: 'gestaoweb-cap2',
    capitulo: 2,
    titulo: 'Cloud Computing para Sistemas Web',
    disciplinaId: 'gestao-de-sistemas-digitais-na-web',
    unidades: ['Arquitetura de Sistemas na Web'],
    descricao:
      'Computação em nuvem, tipos de implantação, IaaS, PaaS, SaaS e BaaS, principais provedores, on-premises × cloud e migração para a nuvem.',
  },
  {
    id: 'gestaoweb-cap3',
    capitulo: 3,
    titulo: 'Desenvolvimento de Aplicações Web',
    disciplinaId: 'gestao-de-sistemas-digitais-na-web',
    unidades: ['Desenvolvimento de Aplicações Web'],
    descricao:
      'Frontend × backend, sites estáticos e dinâmicos, JavaScript e TypeScript, bancos SQL e NoSQL, frameworks e design responsivo.',
  },
  {
    id: 'gestaoweb-cap4',
    capitulo: 4,
    titulo: 'Gerenciamento de Conteúdo Web',
    disciplinaId: 'gestao-de-sistemas-digitais-na-web',
    unidades: ['Gerenciamento de Conteúdo Web'],
    descricao: 'O que é um CMS, mercado e tendências, WordPress, Joomla, Drupal e outros, workflow de aprovações, SEO e ROI.',
  },
  {
    id: 'gestaoweb-cap5',
    capitulo: 5,
    titulo: 'Segurança em Sistemas Web',
    disciplinaId: 'gestao-de-sistemas-digitais-na-web',
    unidades: ['Segurança em Sistemas Web'],
    descricao:
      'Tríade CIA, princípios de segurança, SQL Injection, XSS, CSRF, ransomware, DDoS e phishing, ferramentas, boas práticas, LGPD e GDPR.',
  },
  {
    id: 'gestaoweb-cap6',
    capitulo: 6,
    titulo: 'Integração de Sistemas na Web',
    disciplinaId: 'gestao-de-sistemas-digitais-na-web',
    unidades: ['Integração de Sistemas na Web'],
    descricao:
      'Integração ponto a ponto, via middleware e por eventos, APIs de terceiros e autenticação, SOAP × REST e princípios RESTful.',
  },
  {
    id: 'gestaoweb-cap7',
    capitulo: 7,
    titulo: 'Monitoramento e Análise de Desempenho',
    disciplinaId: 'gestao-de-sistemas-digitais-na-web',
    unidades: ['Monitoramento e Análise de Desempenho'],
    descricao:
      'Core Web Vitals, métricas de backend, ferramentas de monitoramento, otimizações, escalabilidade, testes de carga, SLI, SLO e error budget.',
  },
  {
    id: 'gestaoweb-cap8',
    capitulo: 8,
    titulo: 'Gestão de Projetos de Desenvolvimento Web',
    disciplinaId: 'gestao-de-sistemas-digitais-na-web',
    unidades: ['Gestão de Projetos de Desenvolvimento Web'],
    descricao:
      'Os 7 passos para gerenciar um projeto: termo de abertura, EAP e requisitos, cronograma, comunicação, riscos, controle e encerramento.',
  },
  {
    id: 'gestaoweb-cap9',
    capitulo: 9,
    titulo: 'Tecnologias Emergentes na Web',
    disciplinaId: 'gestao-de-sistemas-digitais-na-web',
    unidades: ['Tecnologias Emergentes na Web'],
    descricao:
      'Ciclo de vida das tecnologias, WebRTC, PWAs, WebAssembly, Web Components, Jamstack, serverless, edge computing e IA no frontend.',
  },

  // Algoritmos e Linguagem de Programação I — "Algoritmos e Programação: Lógica, Portugol e C++" (TecPro)
  // Texto próprio, escrito a partir da ementa (Portugol + C++; Java só na orientação a objetos).
  // Fonte: apostilas/algoritmos-i/capitulos/capitulo-NN.tex (raiz do repositório), convertida com
  // ferramentas/converter_latex.py; o código é testado com apostilas/algoritmos-i/testar_codigo.py
  {
    id: 'alg1-cap1',
    capitulo: 1,
    titulo: 'Lógica, algoritmos e o computador',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Algoritmos e Estruturas de Dados'],
    descricao:
      'Proposições e tabela-verdade, o que é um algoritmo, a arquitetura de Von Neumann, do problema ao algoritmo, fluxogramas, Portugol, teste de mesa e o primeiro programa em C++.',
  },
  {
    id: 'alg1-cap2',
    capitulo: 2,
    titulo: 'Linguagens de programação',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Linguagens de Programação'],
    descricao:
      'Níveis de linguagem, sintaxe e semântica, compilação e interpretação, ambiente de programação, a estrutura de um programa em C++, saída com cout, entrada com cin e como ler as mensagens de erro.',
  },
  {
    id: 'alg1-cap3',
    capitulo: 3,
    titulo: 'Variáveis, tipos e operadores',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Linguagens de Programação'],
    descricao:
      'Variáveis e constantes, tipos de dados e seus limites, operadores aritméticos, divisão inteira e resto, conversões de tipo, operadores relacionais e lógicos, precedência e funções matemáticas.',
  },
  {
    id: 'alg1-cap4',
    capitulo: 4,
    titulo: 'Estruturas de decisão',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Linguagens de Programação'],
    descricao:
      'Decisão simples e composta, decisões encadeadas e aninhadas, escolha múltipla com switch, operador ternário, ano bissexto e as armadilhas que o compilador aceita.',
  },
  {
    id: 'alg1-cap5',
    capitulo: 5,
    titulo: 'Estruturas de repetição',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Linguagens de Programação'],
    descricao:
      'Laços while, do-while e for, sentinela, contadores e acumuladores, maior e menor valor, break e continue, laços aninhados, laço infinito e números primos.',
  },
  {
    id: 'alg1-cap6',
    capitulo: 6,
    titulo: 'Funções e procedimentos',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Linguagens de Programação'],
    descricao:
      'Modularização, funções e procedimentos em Portugol e C++, parâmetros e retorno, pilha de chamadas, escopo, passagem por valor e por referência, protótipos, valores padrão e sobrecarga.',
  },
  {
    id: 'alg1-cap7',
    capitulo: 7,
    titulo: 'Vetores e matrizes',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Algoritmos e Estruturas de Dados'],
    descricao:
      'Vetores e matrizes em Portugol e C++, índices e limites, contagem por categoria, maior elemento, inversão, vetores em funções, jogo da velha e o vector da biblioteca padrão.',
  },
  {
    id: 'alg1-cap8',
    capitulo: 8,
    titulo: 'Caracteres e strings',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Algoritmos e Estruturas de Dados'],
    descricao:
      'Tabela ASCII, o tipo string em C++ e caractere em Portugol, leitura com getline, find, substr e conversões, palíndromos, acentos em UTF-8, strings no estilo C e a cifra de César.',
  },
  {
    id: 'alg1-cap9',
    capitulo: 9,
    titulo: 'Recursão e backtracking',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Algoritmos e Estruturas de Dados'],
    descricao:
      'Caso base e caso recursivo, a pilha de chamadas, fatorial, MDC de Euclides, Fibonacci e memoização, recursão ou laço, Torres de Hanói, permutações e o problema das oito rainhas.',
  },
  {
    id: 'alg1-cap10',
    capitulo: 10,
    titulo: 'Busca e ordenação',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Algoritmos e Estruturas de Dados'],
    descricao:
      'Busca sequencial e binária, noção de complexidade, ordenação por seleção, bolha e inserção, comparação experimental, sort e binary_search da biblioteca e a classificação de uma turma com vetores paralelos.',
  },
  {
    id: 'alg1-cap11',
    capitulo: 11,
    titulo: 'Introdução às estruturas de dados',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Algoritmos e Estruturas de Dados'],
    descricao:
      'Registros (struct) e vetores de registros, tipos abstratos de dados, pilha, fila circular, ponteiros e memória dinâmica, lista encadeada, as estruturas da biblioteca e a verificação de parênteses balanceados.',
  },
  {
    id: 'alg1-cap12',
    capitulo: 12,
    titulo: 'Introdução à orientação a objetos',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-i',
    unidades: ['Algoritmos e Estruturas de Dados'],
    descricao:
      'Classes e objetos, construtores, encapsulamento, herança e polimorfismo em C++; o Java e a JVM, instalação do JDK e da IDE, do C++ para o Java, classes e herança em Java e um sistema de biblioteca.',
  },

  // Algoritmos e Linguagem de Programação II — "Algoritmos e Estruturas de Dados" (TecPro)
  // Texto próprio, escrito a partir da ementa (temas dos slides de EDA usados só como roteiro).
  // Fonte: apostilas/algoritmos-ii/capitulos/capitulo-NN.tex (raiz do repositório), convertida com
  // ferramentas/converter_latex.py; o código é testado com apostilas/algoritmos-ii/testar_codigo.py
  {
    id: 'alg2-cap1',
    capitulo: 1,
    titulo: 'Fundamentos de C++ para Estruturas de Dados',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Passagem de parâmetros por valor e por referência, ponteiros, memória dinâmica com new e delete, structs, classes e templates, com comparações em Python.',
  },
  {
    // gráfico: apostilas/algoritmos-ii/imagens/capitulo-02_crescimento.tex (pgfplots) -> public/apostilas/alg2
    id: 'alg2-cap2',
    capitulo: 2,
    titulo: 'Complexidade de Algoritmos',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Análise experimental e de complexidade, melhor, pior e caso médio, notação Big O, as principais classes de complexidade, análise de código passo a passo e complexidade de espaço.',
  },
  {
    // figuras: apostilas/algoritmos-ii/imagens/capitulo-03_*.tex (TikZ, estilo-nos.tex)
    id: 'alg2-cap3',
    capitulo: 3,
    titulo: 'Listas Encadeadas',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Tipo abstrato de dados, nós e ponteiros, inserção, busca e remoção passo a passo, listas simples, duplas e circulares, e quando usar vetor ou lista.',
  },
  {
    id: 'alg2-cap4',
    capitulo: 4,
    titulo: 'Pilhas e Filas',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'LIFO e FIFO, pilha e fila genéricas com nós encadeados, parênteses balanceados, notação pós-fixa, fila circular em vetor e as versões prontas do C++ e do Python.',
  },
  {
    id: 'alg2-cap5',
    capitulo: 5,
    titulo: 'Árvores',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Terminologia, árvores binárias, percursos (pré-ordem, em ordem, pós-ordem e em largura), árvore binária de busca com inserção, busca e remoção, árvores degeneradas e árvores AVL com rotações.',
  },
  {
    id: 'alg2-cap6',
    capitulo: 6,
    titulo: 'Grafos',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Vértices e arestas, matriz e lista de adjacência, busca em largura e em profundidade, componentes conexos, ordenação topológica, caminho mínimo com Dijkstra e árvore geradora mínima com Prim.',
  },
  {
    id: 'alg2-cap7',
    capitulo: 7,
    titulo: 'Busca',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Busca sequencial com sentinela, busca binária iterativa e recursiva, primeira ocorrência e ponto de inserção, busca binária na resposta, funções de busca da biblioteca padrão e quando vale a pena ordenar.',
  },
  {
    id: 'alg2-cap8',
    capitulo: 8,
    titulo: 'Ordenação',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Estabilidade e ordenação no lugar; bubble sort, selection sort e insertion sort; merge sort e quicksort com dividir para conquistar; heap, heapsort e fila de prioridade; o limite de n log n e a ordenação da biblioteca padrão.',
  },
  {
    id: 'alg2-cap9',
    capitulo: 9,
    titulo: 'Algoritmos gulosos e programação dinâmica',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Escolha gulosa e quando ela falha; troco e seleção de atividades; algoritmo de Kruskal com conjuntos disjuntos (union-find); programação dinâmica com memorização e tabulação; Fibonacci, troco mínimo e problema da mochila.',
  },
  {
    id: 'alg2-cap10',
    capitulo: 10,
    titulo: 'Programação funcional',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Estilo imperativo e funcional; funções puras, efeitos colaterais e imutabilidade; lambdas e function; capturas por valor e por referência e closures; mapear, filtrar e reduzir com a biblioteca padrão; composição de funções.',
  },
  {
    id: 'alg2-cap11',
    capitulo: 11,
    titulo: 'Testes e depuração',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Tipos de erro; asserções com pré-condições e pós-condições; testes unitários, faixas de valores e fronteiras; tabela de casos e testes de regressão; testes com dados gerados e oráculo; roteiro de depuração, cerr, gdb e sintomas comuns.',
  },
  {
    id: 'alg2-apa',
    rotulo: 'Apêndice A',
    grupo: 'Material complementar',
    titulo: 'Tabelas hash',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Funções hash para números e textos, colisões, encadeamento separado com redimensionamento, endereçamento aberto com sondagem linear, unordered_map e unordered_set.',
  },
  {
    id: 'alg2-apb',
    rotulo: 'Apêndice B',
    grupo: 'Material complementar',
    titulo: 'Arquivos',
    disciplinaId: 'algoritmos-e-linguagem-de-programacao-ii',
    descricao:
      'Fluxos de arquivo, leitura e gravação de texto, arquivos CSV, arquivos binários com registros de tamanho fixo, acesso direto com seekg e índices.',
  },

  // Programação e Design para Web II (apostila em módulos)
  // Fonte: 02- APOSTILAS/Módulo 5/LATEX/modulos/modulo-0N.tex (24/08), convertida com
  //   ferramentas/converter_latex.py --imagens <pasta> apostilas/web2
  //     --sem-secao "O Projeto do Curso" --sem-secao "Continuando o Projeto" --sem-secao "Etapa"
  // para ficar igual à versão de 12/09 (APOSTILAS NOVAS), que tirou o projeto do curso e as
  // resoluções dos exercícios. O Projeto Portfólio não entra no site (decisão da professora).
  // O Módulo 4 recebe as mudanças de 12/09 e perde as frases que citam o projeto com
  //   ferramentas/ajustar_web2_modulo4.py
  // A figura public/apostilas/web2/fluxograma-nodejs.png foi recortada para tirar um rodapé
  // institucional; ao reconverter, não sobrescreva esse arquivo.
  // Os módulos não seguem as unidades do plano de ensino, por isso não têm "unidades".
  {
    id: 'web2-cap1',
    capitulo: 1,
    rotulo: 'Módulo',
    titulo: 'Node.js e Ecossistema NPM',
    disciplinaId: 'programacao-e-design-para-web-ii',
    descricao:
      'O que é Node.js, npm e package.json, CommonJS vs ES Modules, servidor HTTP nativo, variáveis de ambiente e argumentos de linha de comando.',
  },
  {
    id: 'web2-cap2',
    capitulo: 2,
    rotulo: 'Módulo',
    titulo: 'React: Componentes e Props',
    disciplinaId: 'programacao-e-design-para-web-ii',
    descricao:
      'O que é React, JSX, criação do projeto, componentes, props e children, renderização condicional, listas e a prop key.',
  },
  {
    id: 'web2-cap3',
    capitulo: 3,
    rotulo: 'Módulo',
    titulo: 'React: Hooks e Estado',
    disciplinaId: 'programacao-e-design-para-web-ii',
    descricao:
      'Estado com useState, atualização correta, formulários controlados, estado como objeto, useEffect e o array de dependências.',
  },
  {
    id: 'web2-cap4',
    capitulo: 4,
    rotulo: 'Módulo',
    titulo: 'Next.js: App Router e Roteamento',
    disciplinaId: 'programacao-e-design-para-web-ii',
    descricao:
      'O que é Next.js, App Router vs Pages Router, criação do projeto, estrutura de pastas, rotas por arquivos, o componente Link e layouts.',
  },
  {
    id: 'web2-cap5',
    capitulo: 5,
    rotulo: 'Módulo',
    titulo: 'Server e Client Components',
    disciplinaId: 'programacao-e-design-para-web-ii',
    descricao:
      'Por que Server Components existem, a diretiva "use client", como misturar os dois tipos e como decidir entre server e client.',
  },
  {
    // COMANDOS GITHUB.docx, convertido com ferramentas/converter_word_comandos.py
    //   --remover-primeiro "Bem, nós iremos repassar" (parágrafo repetido fora do lugar)
    //   e --trocar para corrigir digitação nos títulos (bransh, CHECOUT, GIR, hitórico, seu commits)
    id: 'web2-git',
    rotulo: 'Guia',
    grupo: 'Material complementar',
    titulo: 'Git e GitHub: Comandos Essenciais',
    disciplinaId: 'programacao-e-design-para-web-ii',
    descricao:
      'Instalação e configuração no Windows, criação do repositório, add, commit, reset, branch, merge, stash, tag, fetch, pull, push e outros comandos.',
  },
  {
    // "Como funciona o react.png" (infográfico da professora), com o rodapé do nome recortado, publicado em
    // public/apostilas/web2/como-o-react-funciona.png; página em src/data/capitulos/web2-react.json
    id: 'web2-react',
    rotulo: 'Infográfico',
    grupo: 'Material complementar',
    titulo: 'Como o React Funciona',
    disciplinaId: 'programacao-e-design-para-web-ii',
    descricao:
      'Infográfico do ciclo de renderização: componente, JSX, Virtual DOM, setState e o diffing que atualiza só o que mudou no DOM real.',
  },
  {
    // "técnicas da engenharia de prompt.docx" (pasta INTELIGENCIA ARTIFICIAL): os 5 passos e o exemplo do Word;
    // os frameworks (RTF, CTF, GRADE, PECRA, ROSES, SPARK, CREATE) reescritos em texto com exemplos de web, no
    // lugar das capturas de tela do vídeo; infográfico em public/apostilas/web2/engenharia-de-prompt-rtf.png;
    // página em src/data/capitulos/web2-prompt.json
    id: 'web2-prompt',
    rotulo: 'Guia',
    grupo: 'Material complementar',
    titulo: 'Técnicas de Engenharia de Prompt',
    disciplinaId: 'programacao-e-design-para-web-ii',
    descricao:
      'Como escrever bons pedidos para ferramentas de IA: os 5 passos de um prompt e os frameworks RTF, CTF, GRADE, PECRA, ROSES, SPARK e CREATE, com exemplos de desenvolvimento web.',
  },

  // Livro "Node.js, Express e MySQL — Guia Completo para Desenvolvimento de APIs Modernas" (TecPro)
  // Fonte: Guia NODES.js/LIVRO A5/livro-completo-A5 (LaTeX), convertido com ferramentas/converter_livro_node.py
  // (capítulo 10 junta os arquivos 10a a 10d; sem as seções de Estudo de Caso e Resumo Visual)
  // Depois de converter, tire a assinatura "TecPro Tecnologia" do fim do capítulo 13: no site, a
  // TecPro só aparece no rodapé.
  ...[
    ['Introdução ao Node.js', 'O que é o Node.js, por que foi criado, o que é um runtime, arquitetura, vantagens, limitações e o que é uma API.'],
    ['Preparando o Ambiente de Desenvolvimento Node.js', 'Instalação do Node.js e do VS Code, o primeiro projeto, package.json, package-lock.json, node_modules e o primeiro programa.'],
    ['JavaScript Moderno para Node.js', 'let e const, funções, arrow functions, template strings, destructuring e módulos.'],
    ['Programação Assíncrona no Node.js', 'Síncrono e assíncrono, Event Loop, Call Stack, callbacks, callback hell, Promises e async/await.'],
    ['NPM e Gerenciamento de Pacotes', 'O que é o NPM, pacotes, dependências de produção e desenvolvimento, atualização, remoção e scripts.'],
    ['MySQL: Fundamentos e Linguagem SQL', 'Banco relacional, tipos de dados, CREATE TABLE, chaves, constraints, INSERT, SELECT, WHERE, GROUP BY, JOIN e índices.'],
    ['Preparando o Ambiente para a API', 'A BibliotecaAPI, o que é uma API REST, cliente e servidor, métodos HTTP, Postman e a estrutura do projeto.'],
    ['Conectando o Node.js ao MySQL com mysql2', 'Pool de conexões, consultas, INSERT, UPDATE e DELETE, prepared statements contra SQL Injection e as camadas Model e Service.'],
    ['Construindo a Primeira API REST', 'Express, o primeiro servidor, rotas, Express Router, controllers, req.body, req.params e req.query, middlewares e tratamento de erros.'],
    ['CRUD Completo da BibliotecaAPI', 'Modelagem e tabelas do sistema, Create, Read, Update e Delete, empréstimos, validação com express-validator, paginação e filtros.'],
    ['Autenticação com JWT', 'Hash de senhas com bcrypt, login, JSON Web Token, middleware de autenticação e controle de perfis.'],
    ['Qualidade e Boas Práticas', 'Arquitetura em camadas, respostas padronizadas, logs, introdução aos testes automatizados, variáveis de ambiente e checklist.'],
    ['Projeto Integrador', 'A BibliotecaAPI completa: estrutura de pastas, todos os endpoints, consumo com HTML e fetch(), como rodar do zero e como levar ao portfólio.'],
  ].map(
    ([titulo, descricao], i): Apostila => ({
      id: `web2-node-cap${i + 1}`,
      capitulo: i + 1,
      grupo: 'Material complementar: Node.js, Express e MySQL',
      titulo,
      disciplinaId: 'programacao-e-design-para-web-ii',
      descricao,
    }),
  ),
  {
    id: 'web2-node-apa',
    rotulo: 'Apêndice A',
    grupo: 'Material complementar: Node.js, Express e MySQL',
    titulo: 'Referência Rápida',
    disciplinaId: 'programacao-e-design-para-web-ii',
    descricao: 'Os comandos SQL, npm, mysql2, métodos e status HTTP, JavaScript moderno e autenticação mais usados no livro, para consulta.',
  },
  {
    id: 'web2-node-apb',
    rotulo: 'Apêndice B',
    grupo: 'Material complementar: Node.js, Express e MySQL',
    titulo: 'Guia de Arquivos e Pacotes da BibliotecaAPI',
    disciplinaId: 'programacao-e-design-para-web-ii',
    descricao: 'Para que serve cada arquivo e pasta do projeto, o fluxo de uma requisição, os pacotes usados e o que nunca fazer.',
  },

  // Programação e Design para Web III — "Desenvolvimento de APIs para a Web: REST, Next.js, Prisma e
  // segurança" (TecPro). Texto próprio, escrito a partir da ementa; o material da faculdade (projeto
  // TaskFlow) serviu só de roteiro e virou o projeto que atravessa a apostila.
  // Fonte: apostilas/web-iii/capitulos/capitulo-NN.tex (raiz do repositório), convertida com
  //   ferramentas/converter_latex.py <tex> src/data/capitulos/web3-capN.json --imagens public/apostilas/web3 apostilas/web3
  {
    id: 'web3-cap1',
    capitulo: 1,
    titulo: 'APIs e Web Services',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Introdução a APIs e Web Services'],
    descricao:
      'O que é uma API, cliente e servidor, o protocolo HTTP, a anatomia de uma URL, SOAP, REST, GraphQL, gRPC, WebSocket e webhooks, e a primeira consulta a uma API pública.',
  },
  {
    id: 'web3-cap2',
    capitulo: 2,
    titulo: 'Design RESTful e métodos HTTP',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Design de API e Boas Práticas'],
    descricao:
      'Recursos e representações, as restrições do REST, boas URLs, métodos seguros e idempotentes, PUT e PATCH, códigos de status, paginação, versionamento, HATEOAS e o projeto da API do TaskFlow.',
  },
  {
    id: 'web3-cap3',
    capitulo: 3,
    titulo: 'Preparando o projeto',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Construção de API – Back-End'],
    descricao:
      'O projeto Next.js só de API, o PostgreSQL na nuvem com o NeonDB, o Prisma 7 (esquema, migrações e cliente), dados de teste com seed, o Prisma Studio e a primeira rota.',
  },
  {
    id: 'web3-cap4',
    capitulo: 4,
    titulo: 'Roteamento e endpoints',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Roteamento e Endpoints'],
    descricao:
      'Route Handlers do Next.js, como ler parâmetros, cabeçalhos e corpo, montar respostas, segmentos dinâmicos, o que o Next.js faz sozinho (HEAD, OPTIONS, 405) e como testar com curl e REST Client.',
  },
  {
    id: 'web3-cap5',
    capitulo: 5,
    titulo: 'JSON, XML e serialização',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Formatos de Dados e Serialização'],
    descricao:
      'Serializar e desserializar, os tipos do JSON e o que ele perde, datas em ISO 8601 e fusos, nomes de campos, os campos públicos da API (DTO), XML, negociação de conteúdo e por que desserializar não é validar.',
  },
  {
    id: 'web3-cap6',
    capitulo: 6,
    titulo: 'Validação com Zod',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Formatos de Dados e Serialização', 'Segurança em APIs'],
    descricao:
      'Por que validar no servidor, esquemas do Zod 4, parse e safeParse, mensagens de erro por campo, os esquemas de criação e edição do TaskFlow, atribuição em massa e a validação da query string.',
  },
  {
    id: 'web3-cap7',
    capitulo: 7,
    titulo: 'CRUD: manipulação de recursos',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Manipulação de Recursos'],
    descricao:
      'CRUD, métodos HTTP e funções do Prisma, a camada de serviço, edição com PATCH e o erro P2025, listagem com filtros, busca, ordenação e paginação, transações e controle de concorrência.',
  },
  {
    id: 'web3-cap8',
    capitulo: 8,
    titulo: 'Erros e códigos HTTP',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Tratamento de Erros e Códigos de Resposta'],
    descricao:
      'Como escolher o código de status (400, 401, 403, 404, 405, 409, 422, 500), o formato Problem Details da RFC 9457, um tratador central de erros, o 500 seguro e rastreável, 404 em JSON e a leitura dos erros no cliente.',
  },
  {
    id: 'web3-cap9',
    capitulo: 9,
    titulo: 'Autenticação com JWT',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Autenticação e Autorização', 'Segurança em APIs'],
    descricao:
      'Autenticação e autorização, senhas com bcrypt (hash, salt e custo), sessão ou token, a anatomia de um JWT, a chave secreta, cadastro e login com a biblioteca jose, o ataque de temporização, o cabeçalho Authorization: Bearer e o 401 com WWW-Authenticate.',
  },
  {
    id: 'web3-cap10',
    capitulo: 10,
    titulo: 'Documentação: OpenAPI, Swagger e Postman',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Documentação de API', 'Testes de API'],
    descricao:
      'O que uma boa documentação precisa ter, a Especificação OpenAPI 3.1, design-first e code-first, esquemas gerados a partir do Zod, o Swagger UI com Try it out e Authorize, a validação com o Redocly e o Postman: importação, variáveis, scripts, testes, Collection Runner e Newman.',
  },
  {
    id: 'web3-cap11',
    capitulo: 11,
    titulo: 'Testes de API',
    disciplinaId: 'programacao-e-design-para-web-iii',
    unidades: ['Testes de API'],
    descricao:
      'Por que testar automaticamente, testes de unidade, integração e ponta a ponta, o Vitest (e o Jest), um banco só para os testes, describe, it e expect, espiões, relógio falso, mocks, testes das rotas sem o servidor, teste de contrato com o OpenAPI e cobertura.',
  },
]
