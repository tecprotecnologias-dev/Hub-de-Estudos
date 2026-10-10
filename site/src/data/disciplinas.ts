import type { Disciplina } from './tipos'

// Gerado a partir dos planos de ensino. Período 0 = optativa.
export const disciplinas: Disciplina[] = [
  {
    "id": "algoritmos-e-linguagem-de-programacao-i",
    "periodo": 1,
    "nome": "Algoritmos e Linguagem de Programação I",
    "objetivos": [
      "Objetivos gerais",
      "Solucionar problemas do mundo real, fazendo uso das ferramentas de lógica, de algoritmos computacionais e do conhecimento de organização de computadores;",
      "Ler e escrever soluções algorítmicas complexas por meio do desenvolvimento de algoritmos e da prática em computador, utilizando o raciocínio lógico.",
      "Desenvolver algoritmos objetivos e eficientes;",
      "Propor solução de problemas computacionais, utilizando-se de lógicacomputacional;",
      "Aplicar pseudocódigo (portugol) no desenvolvimento da análise estruturada de umaaplicação;",
      "Identificar os paradigmas da lógicacomputacional;",
      "Classificar variáveis e explicar suasaplicações;",
      "Utilizar a linguagem C++ para implementar os algoritmosdesenvolvidos;",
      "Compreenderoparadigmadeorientaçãoporobjetoesuaaplicaçãoemprogramação;",
      "Compreender a linguagem Java e ambientes deprogramação."
    ],
    "habilidades": [
      "Interpretar problemas e retirar deles as informações necessárias para a solução a ser desenvolvida (levantamento de dados de entrada e saída e dos processamentos a serem realizados);",
      "Organizar a solução logicamente;",
      "Apresentar a solução de maneira adequada, conforme o padrão adotado para a representação dos algoritmos."
    ],
    "unidades": [
      {
        "titulo": "Algoritmos e Estruturas de Dados",
        "topicos": [
          "Conceitos básicos de algoritmos.",
          "Estruturas de dados como listas, pilhas, filas, árvores e grafos.",
          "Algoritmos de busca e ordenação.",
          "Algoritmos de recursão e backtracking."
        ]
      },
      {
        "titulo": "Linguagens de Programação",
        "topicos": [
          "Sintaxe e semântica de linguagens de programação.",
          "Variáveis, tipos de dados e operadores.",
          "Controle de fluxo (condicionais e loops).",
          "Funções e procedimentos.",
          "Manipulação de strings e vetores/matriz."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "fundamentos-de-sistemas-operacionais",
    "periodo": 1,
    "nome": "Fundamentos de Sistemas Operacionais",
    "objetivos": [
      "Ao término da disciplina o aluno deverá ser capaz de identificar, comparar e manipular os principais componentes de um sistema operacional, assim como entender a sua evolução e os aspectos relevantes para seu uso e aplicação adequada."
    ],
    "habilidades": [
      "Realizar avaliação dos aspectos de hardware referentes à arquitetura de computadores, destinando-se a obter a racionalização de investimentos feitos para as plataformas, com o máximo de desempenho.",
      "Ter conhecimentos de projeto lógico e físico da estrutura de informações organizacionais, visando à operacionalização de sistemas gerenciadores de bancos de dados e sua agregação a acervos em redes de computadores, incluindo projetos envolvendo a rede Internet como infraestrutura de difusão de informações;",
      "Gerenciar, manter e garantir a segurança dos sistemas de informação e da infraestrutura de Tecnologia da Informação de uma organização;",
      "Gerenciar o desempenho das aplicações e a escalabilidade dos sistemas de informação."
    ],
    "unidades": [
      {
        "titulo": "Conceitos Básicos de Sistemas Operacionais",
        "topicos": [
          "Definição e função de um sistema operacional.",
          "Gerenciamento de recursos: processos, memória, dispositivos de entrada/saída."
        ]
      },
      {
        "titulo": "Processos e Threads",
        "topicos": [
          "Conceito de processo e thread.",
          "Escalonamento de processos.",
          "Sincronização e comunicação entre processos/threads."
        ]
      },
      {
        "titulo": "Gerenciamento de Memória",
        "topicos": [
          "Modelos de alocação de memória.",
          "Paginação e segmentação.",
          "Memória virtual."
        ]
      },
      {
        "titulo": "Sistemas de Arquivos",
        "topicos": [
          "Hierarquia de sistemas de arquivos.",
          "Operações de entrada/saída em arquivos.",
          "Métodos de alocação de espaço em disco.",
          "Aplicabilidade Windows e Linux."
        ]
      },
      {
        "titulo": "Gerenciamento de Dispositivos",
        "topicos": [
          "Camadas de abstração de dispositivos.",
          "Filas de requisição de dispositivos.",
          "Drivers de dispositivos."
        ]
      },
      {
        "titulo": "Comandos e Interface de Linha de Comando",
        "topicos": [
          "Utilização de comandos em sistemas operacionais Unix/Linux ou Windows.",
          "Manipulação de arquivos e diretórios.",
          "Ferramentas de automatização de arquivos."
        ]
      },
      {
        "titulo": "Segurança e Proteção",
        "topicos": [
          "Controle de acesso e permissões.",
          "Mecanismos de autenticação.",
          "Políticas de segurança.",
          "Criptografia de disco."
        ]
      },
      {
        "titulo": "Virtualização e Contêineres",
        "topicos": [
          "Conceitos de virtualização.",
          "Uso de máquinas virtuais e contêineres.",
          "Estudos de casos: LINUX, WINDOWS, OPENVMS (PROXMOX), VMWARE/HYPER-V"
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "gestao-ambiental-e-responsabilidade-social",
    "periodo": 1,
    "nome": "Gestão Ambiental e Responsabilidade Social",
    "objetivos": [
      "Conhecer os principais parâmetros para avaliação da qualidade ambiental e os instrumentos necessários à gestão ambiental desenvolvendo uma visão crítica sobre o desenvolvimento sustentável empresarial. Proporcionar o conhecimento do desenvolvimento de um sistema de gestão ambiental empresarial. Compreender a aplicação da legislação ambiental. Conhecer a importância das Normas ambientais e da Certificação das empresas."
    ],
    "habilidades": [
      "Desenvolver o compromisso pessoal com a sustentabilidade e a responsabilidade social, empregando racionalmente os recursos disponíveis em sua atuação em sistemas de informação, compreendendo os impactos tecnológicos, econômicos, sociais e ambientais das atividades humanas."
    ],
    "unidades": [
      {
        "titulo": "Sustentabilidade e Tecnologia",
        "topicos": [
          "Como a tecnologia da informação pode contribuir para práticas sustentáveis.",
          "Uso de TI para monitoramento ambiental, eficiência energética, entre outros.",
          "Definições e Aplicabilidade de Green IT.",
          "O uso de Computação em Nuvem para sustentabilidade."
        ]
      },
      {
        "titulo": "Impacto Ambiental da Tecnologia",
        "topicos": [
          "Considerações sobre o ciclo de vida de produtos eletrônicos.",
          "E-waste (resíduos eletrônicos) e seu impacto no meio ambiente.",
          "SustainableCyclesProgramme (SCYCLE).",
          "O papel da ESG (Environmental, Social and Governance) na sustentabilidade."
        ]
      },
      {
        "titulo": "Ética e Responsabilidade Social na TI",
        "topicos": [
          "Papel da ética na tomada de decisões tecnológicas.",
          "Abordagens responsáveis no desenvolvimento de software e projetos de TI."
        ]
      },
      {
        "titulo": "Tecnologia e Inclusão Social",
        "topicos": [
          "Acesso à tecnologia em comunidades carentes.",
          "Uso de TI para promover a inclusão e a igualdade."
        ]
      },
      {
        "titulo": "Gestão de Dados Ambientais",
        "topicos": [
          "Coleta e análise de dados ambientais.",
          "Sistemas de informação geográfica (GIS) e mapeamento ambiental."
        ]
      },
      {
        "titulo": "Legislação Ambiental e Tecnologia",
        "topicos": [
          "Cumprimento de regulamentações ambientais na área de tecnologia."
        ]
      },
      {
        "titulo": "Economia Circular e Tecnologia",
        "topicos": [
          "Uso de tecnologia para promover a economia circular e o reaproveitamento de recursos."
        ]
      },
      {
        "titulo": "Projetos Sustentáveis e Tecnologia",
        "topicos": [
          "Desenvolvimento de projetos de TI com foco em sustentabilidade."
        ]
      },
      {
        "titulo": "Acesso à Informação Ambiental",
        "topicos": [
          "Uso de TI para disponibilizar informações ambientais ao público."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "ingles-instrumental",
    "periodo": 1,
    "nome": "Inglês Instrumental",
    "objetivos": [
      "Desenvolver no aluno capacidade de leitura e compreensão geral de textos em contextos técnicos da área de desenvolvimento web, assim como ampliar o conhecimento da Língua Inglesa e refletir de forma crítica-interpretativa."
    ],
    "habilidades": [],
    "unidades": [
      {
        "titulo": "Textos Técnicos",
        "topicos": [
          "Trechos de artigos acadêmicos sobre tecnologia.",
          "Documentações técnicas de software e sistemas.",
          "Textos relacionados ao desenvolvimento de software, programação, redes, segurança etc."
        ]
      },
      {
        "titulo": "Enunciados de Questões",
        "topicos": [
          "As questões poderiam apresentar enunciados em inglês para avaliar a compreensão do aluno."
        ]
      },
      {
        "titulo": "Termos e Vocabulário Técnico",
        "topicos": [
          "Reconhecimento de termos técnicos em inglês relacionados à área de sistemas de informação."
        ]
      },
      {
        "titulo": "Leitura e Interpretação",
        "topicos": [
          "Habilidades de leitura e interpretação de textos em inglês relacionados a temas tecnológicos."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "introducao-a-logica",
    "periodo": 1,
    "nome": "Introdução à Lógica",
    "objetivos": [
      "Desenvolver o raciocínio lógico-matemático na solução de argumentos lógicos, análise de sentenças dedutivas e operação com conjuntos, visando a aplicabilidade em sistemas de computação."
    ],
    "habilidades": [
      "O aluno ao cursar a disciplina será capaz de projetar, analisar, interpretar, resolver e validar soluções para problemas através do uso de metodologias e técnicas que envolvam elementos básicos de lógica; aplicar técnicas da lógica proposicional, de predicados e organização de conjuntos. Aplicar também a lógica como ferramenta para formalização e dedução de problemas relacionados à computação."
    ],
    "unidades": [
      {
        "titulo": "Introdução à Lógica",
        "topicos": [
          "Lógica de programação.",
          "Raciocínio lógico na criação e análise de algoritmos.",
          "Aplicação de operadores lógicos (AND, OR, NOT) na manipulação de dados."
        ]
      },
      {
        "titulo": "Programação e Linguagens de Programação",
        "topicos": [
          "Uso de estruturas condicionais (if/else) e loops.",
          "Avaliação de expressões booleanas.",
          "Compreensão de fluxo de controle."
        ]
      },
      {
        "titulo": "Resolução de Problemas",
        "topicos": [
          "Aplicação de pensamento lógico na resolução de desafios de programação.",
          "Decomposição de problemas complexos em partes menores."
        ]
      },
      {
        "titulo": "Álgebra Booleana",
        "topicos": [
          "Princípios da álgebra booleana.",
          "Uso de álgebra booleana em circuitos digitais e programação.",
          "Hardware para álgebra booleana."
        ]
      },
      {
        "titulo": "Lógica de Predicados",
        "topicos": [
          "Conceitos básicos de lógica de predicados.",
          "Uso em modelagem de problemas e linguagens de consulta."
        ]
      }
    ],
    "tecnologias": [
      "N/A"
    ]
  },
  {
    "id": "matematica-aplicada",
    "periodo": 1,
    "nome": "Matemática Aplicada",
    "objetivos": [
      "Demonstrar teoremas numéricos simples a partir dos mecanismos básicos de demonstração.",
      "Revisar conceitos de Relação e Função.",
      "Visualizar relações de recorrência como ferramenta para solucionar problemas computacionais.",
      "Entender as propriedades de números primos e sua aplicação em Computação.",
      "Revisar conceitos de Análise Combinatória.",
      "Estabelecer os fundamentos de Teoria de Grafos e suas aplicações no relacionamento de elementos."
    ],
    "habilidades": [
      "Operar e entender operações com Números Inteiros, e Aritmética Modular.",
      "Organizar e determinar possibilidades de processos combinatórios.",
      "Trabalhar com dados complexos."
    ],
    "unidades": [
      {
        "titulo": "Equações",
        "topicos": [
          "Conceitos básicos e tipos de equação.",
          "Equações: polinomiais, racionais, irracionais, exponencial e logarítmica."
        ]
      },
      {
        "titulo": "Álgebra Linear",
        "topicos": [
          "Vetores, grandeza vetorial, soma de vetores, multiplicação entre vetor e um escalar",
          "Matrizes, transposição e operações matriciais.",
          "Sistemas lineares.",
          "Transformações lineares."
        ]
      },
      {
        "titulo": "Cálculo Diferencial e Integral",
        "topicos": [
          "Conceitos básicos de cálculo.",
          "Limite, derivadas e integrais.",
          "Aplicações do cálculo em problemas de otimização e análise."
        ]
      },
      {
        "titulo": "Probabilidade e Estatística",
        "topicos": [
          "Conceitos de probabilidade.",
          "Distribuições de probabilidade (normal, binomial etc.).",
          "Estatísticas descritivas.",
          "Inferência estatística.",
          "Uso da Estatística na Ciência de Dados."
        ]
      },
      {
        "titulo": "Matemática Discreta",
        "topicos": [
          "Lógica proposicional e lógica de predicados.",
          "Teoria dos conjuntos.",
          "Combinatória e probabilidade discreta."
        ]
      },
      {
        "titulo": "Teoria dos Grafos",
        "topicos": [
          "Conceitos de grafos.",
          "Grafos direcionados e não direcionados.",
          "Aplicações de grafos na modelagem de redes."
        ]
      },
      {
        "titulo": "Teoria dos Números",
        "topicos": [
          "Propriedades de números inteiros.",
          "Aplicações em criptografia e segurança."
        ]
      },
      {
        "titulo": "Análise de Algoritmos",
        "topicos": [
          "Análise de complexidade de algoritmos.",
          "Notações Big O, Theta e Omega."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "organizacao-de-computadores",
    "periodo": 1,
    "nome": "Organização de Computadores",
    "objetivos": [
      "Entender o hardware de um sistema computacional. Entender o funcionamento dos vários módulos que compõem um sistema computacional. Desenvolver uma visão crítica sobre os requisitos de desempenho associados a um sistema computacional.",
      "Objetivo Específico",
      "Capacitar o aluno em relação à correta compreensão e aplicação/uso dos conceitos relacionados a arquitetura de computadores."
    ],
    "habilidades": [
      "Ao final da disciplina o aluno deverá ser capaz de:",
      "Fazer avaliação dos aspectos de hardware referentes à arquitetura de computadores, destinando-se a obter a racionalização de investimentos feitos para as plataformas, com o máximo de desempenho.",
      "Conhecer os conceitos fundamentais relacionados ao desenvolvimento e uso de arquiteturas;",
      "Conhecer as tecnologias e a organização envolvidas na implementação dos computadores e softwares."
    ],
    "unidades": [
      {
        "titulo": "Sistemas Numéricos",
        "topicos": [
          "Binário, Octal, Hexadecimal e Decimal.",
          "Transformações entre as bases."
        ]
      },
      {
        "titulo": "Arquitetura de Computadores",
        "topicos": [
          "Componentes básicos do computador (CPU, memória, dispositivos de entrada/saída).",
          "Arquiteturas de processadores (RISC, CISC).",
          "Hierarquia de memória."
        ]
      },
      {
        "titulo": "Organização de Memória",
        "topicos": [
          "Tipos de memória (RAM, ROM, cache, memória virtual).",
          "Endereçamento de memória."
        ]
      },
      {
        "titulo": "Sistemas de Entrada/Saída",
        "topicos": [
          "Interfaces de dispositivos (controladoras, barramentos).",
          "Tratamento de interrupções e DMA."
        ]
      },
      {
        "titulo": "Instruções e Linguagem de Máquina",
        "topicos": [
          "Ciclo de busca, decodificação e execução de instruções.",
          "Conjunto de instruções e codificação."
        ]
      },
      {
        "titulo": "Aritmética Computacional",
        "topicos": [
          "Representação de números em ponto flutuante e inteiros.",
          "Operações aritméticas em representações binárias."
        ]
      },
      {
        "titulo": "Arquitetura de Pipeline (possivelmente)",
        "topicos": [
          "Conceitos de pipeline.",
          "Estágios de execução de instruções."
        ]
      },
      {
        "titulo": "Arquitetura de Computadores Avançada (possivelmente)",
        "topicos": [
          "Processamento paralelo e distribuído.",
          "Arquiteturas multicore e manycore."
        ]
      },
      {
        "titulo": "Organização de Redes de Computadores (possivelmente)",
        "topicos": [
          "Estrutura de protocolos de rede.",
          "Encapsulamento de pacotes."
        ]
      },
      {
        "titulo": "Arquitetura de Servidores (possivelmente)",
        "topicos": [
          "Hardware para servidores: energia, rede,memória, discos, unidades externas, fitas, console de gerenciamento.",
          "RAID: definição, controladoras, tipos de RAID, combinação entre tipos RAID."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "algoritmos-e-linguagem-de-programacao-ii",
    "periodo": 2,
    "nome": "Algoritmos e Linguagem de Programação II",
    "objetivos": [
      "O aluno é capacitado para estudar e desenvolver novas tecnologias ligadas à computação e atuar na pesquisa científica e tecnológica; para atuar no mercado de trabalho a fim de projetar, desenvolver, implantar e gerenciar soluções envolvendo a tecnologia da computação para desafios da sociedade e empresas. Este profissional é formado para intervir na realidade, de forma empreendedora e criativa. Também pode seguir a carreira acadêmica através de mestrado e doutorado em computação."
    ],
    "habilidades": [
      "Construir software para informatização de sistemas avaliando sua qualidade técnica, testando o seu funcionamento, e validando seu atendimento às necessidades de eficácia, eficiência, efetividade e sustentabilidade desses sistemas.",
      "No decorrer da disciplina, o aluno deve ser capaz de:",
      "utilizar de forma correta (conforme a sintaxe da linguagem) as estruturas da linguagem (declaração de variáveis, condicionais, laços de repetição)",
      "conhecer as palavras reservadas e sua utilização",
      "trabalhar com tipos de dados primitivos (imutáveis) e tipos de dados por referência (mutáveis)",
      "desenvolver programas seguindo o formato de programação procedural",
      "compreender e utilizar a modularização de algoritmos através de funções ou métodos."
    ],
    "unidades": [
      {
        "titulo": "Testes e Depuração",
        "topicos": [
          "Práticas de testes de software.",
          "Identificação e correção de erros (depuração)."
        ]
      },
      {
        "titulo": "Programação Funcional",
        "topicos": [
          "Conceitos de programação funcional.",
          "Uso de funções de alta ordem e expressões lambda."
        ]
      },
      {
        "titulo": "Estruturas de Dados Avançadas",
        "topicos": [
          "Listas encadeadas.",
          "Pilhas e filas.",
          "Árvores (binárias, balanceadas, árvores de busca).",
          "Grafos."
        ]
      },
      {
        "titulo": "Algoritmos Avançados",
        "topicos": [
          "Algoritmos de busca (busca binária, busca em árvore).",
          "Algoritmos de ordenação (merge sort, quick sort, heapsort).",
          "Algoritmos de otimização (algoritmos gulosos, programação dinâmica)."
        ]
      },
      {
        "titulo": "Complexidade de Algoritmos",
        "topicos": [
          "Notação Big O e análise de complexidade.",
          "Análise de casos médio, melhor e pior."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "engenharia-de-software-e-da-usabilidade",
    "periodo": 2,
    "nome": "Engenharia de Software",
    "objetivos": [
      "Apresentar os conceitos fundamentais relacionados a Engenharia de Software e a usabilidade de sistemas baseados na WEB, assim como, desenvolver a capacidade do aluno na utilização de modelos e ferramentas no processo de desenvolvimento de software.",
      "Apresentar os conceitos básicos e características da engenharia de software e dos sistemas baseados na WEB;",
      "Desenvolver a compreensão das principais etapas no desenvolvimento de software;",
      "Desenvolver a capacidade de produzir e avaliar os projetos de interface de aplicações WEB."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto a:",
      "Definir engenharia de software e os principais fundamentos pertencentes a esta disciplina;",
      "Definir usabilidade de sistemas e os principais fundamentos pertencentes a esta disciplina;",
      "Descrever os processos de desenvolvimento e ciclo de vida de software;",
      "Utilizar modelos e ferramentas referentes ao processo de desenvolvimento de software e de Interfaces Homem-Computador;",
      "Analisar processos de desenvolvimento e manutenção de software de forma a identificar pontos de melhoria e implementar soluções;",
      "Planejar e organizar processos de desenvolvimento de software nas organizações."
    ],
    "unidades": [
      {
        "titulo": "Ciclo de Vida de Desenvolvimento de Software",
        "topicos": [
          "Modelos de desenvolvimento (cascata, incremental, ágil etc.).",
          "Fases do ciclo de vida (requisitos, análise, design, implementação, teste, implantação, manutenção)."
        ]
      },
      {
        "titulo": "Requisitos de Software",
        "topicos": [
          "Elicitação, análise e documentação de requisitos.",
          "Especificação funcional e não funcional."
        ]
      },
      {
        "titulo": "Arquitetura de Software",
        "topicos": [
          "Design de sistemas e componentes.",
          "Padrões arquiteturais, Modelo-Visão-Controle (MVC)",
          "Manutenção, modernização ou substituição de software."
        ]
      },
      {
        "titulo": "Programação Orientada a Objetos",
        "topicos": [
          "Conceitos de POO.",
          "Herança, polimorfismo, encapsulamento.",
          "Princípios SOLID."
        ]
      },
      {
        "titulo": "Testes de Software",
        "topicos": [
          "QA (Quality Assurance)",
          "Estratégias de testes (unitários, de integração, de sistema, de aceitação).",
          "Automação de testes."
        ]
      },
      {
        "titulo": "Qualidade de Software",
        "topicos": [
          "QC (Quality Control)",
          "Métricas de qualidade.",
          "Garantia de qualidade e controle de qualidade."
        ]
      },
      {
        "titulo": "Gestão da Configuração",
        "topicos": [
          "Parâmetros de configuração.",
          "Controle de versões e configurações.",
          "Auditoria de configuração, relatórios de status."
        ]
      },
      {
        "titulo": "Gestão de Projetos de Software",
        "topicos": [
          "Planejamento, execução e monitoramento de projetos de software.",
          "Uso de metodologias ágeis (Scrum, Kanban etc.)."
        ]
      },
      {
        "titulo": "Usabilidade e Experiência do Usuário (UX)",
        "topicos": [
          "Princípios de design de interface.",
          "Testes de usabilidade.",
          "Arquitetura da informação e design centrado no usuário."
        ]
      },
      {
        "titulo": "Engenharia de Requisitos",
        "topicos": [
          "Técnicas de elicitação e análise de requisitos.",
          "Especificação de requisitos."
        ]
      },
      {
        "titulo": "Interação Humano-Computador",
        "topicos": [
          "Conceitos de interação homem-computador.",
          "Design de interação e interfaces.",
          "Segurança para Desenvolvimento de Software",
          "Desenvolvimento, Operação e Segurança no Desenvolvimento de Software: DevOps e DevSecOps",
          "Segurança para aplicações Web: OWASP Top 10"
        ]
      }
    ],
    "tecnologias": [
      "N/A"
    ]
  },
  {
    "id": "estatistica-aplicada",
    "periodo": 2,
    "nome": "Estatística Aplicada",
    "objetivos": [
      "Introduzir as noções básicas de estatística com foco na de gestão;",
      "Capacitar o aluno para ler, interpretar e organizar dados em tabelas e gráficos;",
      "Desenvolver a capacidade de interpretação de dados estatísticos e análise crítica de informações divulgadas pelos meios de comunicação;",
      "Capacitar o aluno a calcular medidas estatísticas com o objetivo de avaliar as informações contidas em grande conjunto de dados."
    ],
    "habilidades": [
      "conhecimento das formas de catalogar, resumir e medir as variáveis de sua área de atuação e de organização e manipulação dos dados;",
      "domínio da linguagem técnica estatística, aliada à capacidade de adequação dessa linguagem à interação com profissionais das diversas áreas do conhecimento e à comunicação com a sociedade;",
      "saber produzir sínteses numéricas e gráficas dos dados, através da construção de índices, mapas e gráficos;",
      "saber usar os modelos básicos de análise estatística, de forma especial os modelos de associação entre uma variável resposta e um conjunto de variáveis explicativas."
    ],
    "unidades": [
      {
        "titulo": "Conceitos Básicos de Estatística",
        "topicos": [
          "População, amostra e variáveis.",
          "Tipos de dados (qualitativos e quantitativos)."
        ]
      },
      {
        "titulo": "Análise Descritiva de Dados",
        "topicos": [
          "Medidas de tendência central (média, mediana, moda).",
          "Medidas de dispersão (desvio padrão, variância, amplitude)."
        ]
      },
      {
        "titulo": "Distribuição de Probabilidade",
        "topicos": [
          "Distribuição normal.",
          "Distribuições discretas (binomial, Poisson)."
        ]
      },
      {
        "titulo": "Inferência Estatística",
        "topicos": [
          "Estimação de parâmetros populacionais.",
          "Testes de hipóteses."
        ]
      },
      {
        "titulo": "Análise de Regressão e Correlação",
        "topicos": [
          "Modelos de regressão linear.",
          "Coeficiente de correlação."
        ]
      },
      {
        "titulo": "Análise de Variância (ANOVA)",
        "topicos": [
          "Comparação de médias em diferentes grupos."
        ]
      },
      {
        "titulo": "Estatística Multivariada (possivelmente)",
        "topicos": [
          "Análise de componentes principais (PCA).",
          "Análise de cluster."
        ]
      },
      {
        "titulo": "Aplicação da Estatística em Experimentos e Pesquisas",
        "topicos": [
          "Planejamento de experimentos.",
          "Interpretação de resultados."
        ]
      },
      {
        "titulo": "Estatística Aplicada a Dados de Tecnologia",
        "topicos": [
          "Análise de dados de tecnologia da informação.",
          "Visualização de dados."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "fundamentos-de-estruturas-de-dados",
    "periodo": 2,
    "nome": "Fundamentos de Estruturas de Dados",
    "objetivos": [
      "Apresentar as principais estruturas de dados utilizadas no desenvolvimento de software;",
      "Descrever os conceitos necessários para a representação e manipulação de dados na memória interna do computador através das estruturas de dados.",
      "Demonstrar os algoritmos de operação associados às estruturas de dados apresentadas na disciplina."
    ],
    "habilidades": [
      "Ao final da disciplina o aluno estará apto a:",
      "Descrever as técnicas básicas de organização de dados em um computador sob a forma de estruturas de dados;",
      "Criar e manipular tipos abstratos de dados: listas, pilhas, filas e árvores;",
      "Desenvolver programas que façam uso das estruturas de dados apresentadas na disciplina."
    ],
    "unidades": [
      {
        "titulo": "Tipos de Dados e Abstração",
        "topicos": [
          "Diferentes tipos de dados (inteiros, ponto flutuante, caracteres etc.).",
          "Conceitos de abstração de dados."
        ]
      },
      {
        "titulo": "Estruturas de Dados Lineares",
        "topicos": [
          "Listas simplesmente encadeadas.",
          "Listas duplamente encadeadas.",
          "Pilhas e filas."
        ]
      },
      {
        "titulo": "Estruturas de Dados Não-Lineares",
        "topicos": [
          "Árvores (binárias, balanceadas, árvores de buscaetc.).",
          "Grafos."
        ]
      },
      {
        "titulo": "Tabelas Hash",
        "topicos": [
          "Conceito de tabelas hash.",
          "Funções de hash e resolução de colisões."
        ]
      },
      {
        "titulo": "Ordenação e Busca",
        "topicos": [
          "Algoritmos de ordenação (quicksort, mergesort etc.).",
          "Algoritmos de busca (busca binária, busca em árvore etc.)."
        ]
      },
      {
        "titulo": "Complexidade de Algoritmos",
        "topicos": [
          "Notação Big O e análise de complexidade.",
          "Análise de casos médio, melhor e pior."
        ]
      },
      {
        "titulo": "Aplicações Práticas",
        "topicos": [
          "Uso de estruturas de dados em problemas reais.",
          "Otimização de operações de busca e manipulação de dados."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "fundamentos-de-redes-de-computadores",
    "periodo": 2,
    "nome": "Fundamentos de Redes de Computadores",
    "objetivos": [
      "O aluno deverá ser capaz de entender a arquitetura básica de uma rede de computadores; o funcionamento do hardware utilizado em redes de computadores; as diferentes topologias de uma rede de computadores; entender os principais aspectos da arquitetura cliente/servidor; entender os padrões de cabeamento mais utilizados em redes de computadores; entender os protocolos de comunicação; entender os serviços especializados de comunicação de dados no Brasil."
    ],
    "habilidades": [
      "Avaliar a arquitetura física e lógica das redes de comunicação e de computadores para organização, utilizando conceitos dos modelos de referência, analisando a operação e desempenho de seus componentes, aplicando os conceitos de alta disponibilidade e balanceamento de carga, e utilizando máquinas virtuais e softwares de gerenciamento."
    ],
    "unidades": [
      {
        "titulo": "Conceitos Básicos de Redes",
        "topicos": [
          "Topologias de redes (estrela, anel, barramento etc.).",
          "Modelos de camadas (OSI e TCP/IP)."
        ]
      },
      {
        "titulo": "Meios de Transmissão",
        "topicos": [
          "Tipos de cabos (coaxial, fibra óptica, par trançado).",
          "Tecnologias de comunicação (Ethernet, Wi-Fi)."
        ]
      },
      {
        "titulo": "Protocolos de Rede",
        "topicos": [
          "Protocolos de transporte (TCP, UDP).",
          "Protocolos de aplicação (HTTP, FTP, SMTP etc.)."
        ]
      },
      {
        "titulo": "Endereçamento IP",
        "topicos": [
          "Endereços IPv4 e IPv6.",
          "Subrede e máscaras de rede."
        ]
      },
      {
        "titulo": "Roteamento e Switching",
        "topicos": [
          "Conceitos de roteamento.",
          "Switches e encaminhamento de pacotes.",
          "VLAN"
        ]
      },
      {
        "titulo": "Redes sem Fio",
        "topicos": [
          "Padrões de redes sem fio (Wi-Fi).",
          "Segurança em redes sem fio."
        ]
      },
      {
        "titulo": "Segurança de Redes",
        "topicos": [
          "A Segurança de Redes perante a Lei Geral de Proteção de Dados.",
          "Práticas e Ferramentas para prevenção, mitigação e repressão dos riscos cibernéticos.",
          "Tipos de ataques cibernéticos.",
          "Firewalls e prevenção de intrusões (IDS e IPS).",
          "VPN,Criptografia e autenticação.",
          "WAF (Web Application Firewall) para aplicações Web."
        ]
      },
      {
        "titulo": "Protocolos de Internet Avançados (possivelmente)",
        "topicos": [
          "DNS (Domain Name System).",
          "DHCP (Dynamic Host Configuration Protocol)."
        ]
      },
      {
        "titulo": "Redes de Longa Distância e Virtualização (possivelmente)",
        "topicos": [
          "Redes de longa distância (WANs).",
          "Virtualização de redes."
        ]
      },
      {
        "titulo": "Gerenciamento de Redes (possivelmente)",
        "topicos": [
          "Monitoramento e diagnóstico de problemas.",
          "Administração de redes."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "metodologia-da-pesquisa-cientifico-tecnologica",
    "periodo": 2,
    "nome": "Metodologia da Pesquisa Científico-Tecnológica",
    "objetivos": [
      "Promover a aquisição do conhecimento de métodos do estudo científico, levando o aluno a reconhecer a importância da pesquisa acadêmica.",
      "Preparar o aluno para a produção de conhecimentos de caráter científico-tecnológico e a apresentação dos mesmos.",
      "Aplicar as normas técnicas para construção e formatação de projetos de pesquisa e do trabalho de conclusão de curso."
    ],
    "habilidades": [
      "Analisar e elaborar textos técnico/científicos;",
      "Elaborar projetos de pesquisa;",
      "Planejar trabalhos de conclusão de curso;",
      "Atuar de forma ética e empreendedora em pesquisas e nas diversas áreas do conhecimento científico-tecnológico."
    ],
    "unidades": [
      {
        "titulo": "Métodos de Pesquisa",
        "topicos": [
          "Métodos quantitativos e qualitativos.",
          "Coleta de dados, análise e interpretação."
        ]
      },
      {
        "titulo": "Etapas da Pesquisa",
        "topicos": [
          "Formulação de problemas de pesquisa.",
          "Revisão bibliográfica.",
          "Definição de objetivos e hipóteses."
        ]
      },
      {
        "titulo": "Planejamento de Pesquisa",
        "topicos": [
          "Elaboração de um plano de pesquisa.",
          "Definição de amostra e população.",
          "Escolha de técnicas de coleta de dados."
        ]
      },
      {
        "titulo": "Instrumentos de Pesquisa",
        "topicos": [
          "Elaboração de questionários e entrevistas.",
          "Validação de instrumentos."
        ]
      },
      {
        "titulo": "Ética na Pesquisa",
        "topicos": [
          "Princípios éticos e respeito aos participantes.",
          "Consentimento informado."
        ]
      },
      {
        "titulo": "Análise de Dados",
        "topicos": [
          "Aplicação de técnicas estatísticas na análise de dados.",
          "Interpretação de resultados."
        ]
      },
      {
        "titulo": "Escrita Científica",
        "topicos": [
          "Estrutura de artigos científicos.",
          "Citação e referências bibliográficas."
        ]
      },
      {
        "titulo": "Pesquisa Científica em Tecnologia",
        "topicos": [
          "Adaptação dos métodos de pesquisa à área de tecnologia.",
          "Aplicação da pesquisa em projetos de desenvolvimento."
        ]
      },
      {
        "titulo": "Trabalhos Acadêmicos",
        "topicos": [
          "Elaboração de monografias, dissertações e teses."
        ]
      },
      {
        "titulo": "Metodologias Ágeis e Pesquisa em Desenvolvimento de Software",
        "topicos": [
          "Aplicação de metodologias ágeis na pesquisa.",
          "Pesquisa em práticas de desenvolvimento de software."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "modelagem-conceitual-de-dados",
    "periodo": 2,
    "nome": "Modelagem Conceitual de Dados",
    "objetivos": [
      "Apropriar-se de conhecimentos sobre modelagem de dados no contexto de desenvolvimento de sistemas."
    ],
    "habilidades": [
      "Capacidade de aplicar regras e procedimentos da modelagem conceitual de dados;",
      "Identificar as metodologias mais adequadas a diversas situações."
    ],
    "unidades": [
      {
        "titulo": "Conceitos Básicos de Modelagem de Dados",
        "topicos": [
          "Diferença entre dados e informações.",
          "Entidades, atributos e relacionamentos."
        ]
      },
      {
        "titulo": "Diagrama de Entidade-Relacionamento (DER)",
        "topicos": [
          "Notação e símbolos usados em diagramas DER.",
          "Identificação de entidades, atributos e relacionamentos."
        ]
      },
      {
        "titulo": "Cardinalidade e Participação",
        "topicos": [
          "Cardinalidade mínima e máxima em relacionamentos.",
          "Participação obrigatória e opcional."
        ]
      },
      {
        "titulo": "Modelagem de Atributos",
        "topicos": [
          "Tipos de atributos (simples, compostos, multivalorados, derivados).",
          "Normalização de atributos."
        ]
      },
      {
        "titulo": "Chaves Primárias e Estrangeiras",
        "topicos": [
          "Identificação de chaves primárias.",
          "Uso de chaves estrangeiras para estabelecer relacionamentos."
        ]
      },
      {
        "titulo": "Modelagem de Herança",
        "topicos": [
          "Representação de herança e generalização/especialização.",
          "Tabelas de herança."
        ]
      },
      {
        "titulo": "Modelagem de Relacionamentos Complexos",
        "topicos": [
          "Relacionamentos ternários e n-ários.",
          "Entidades associativas."
        ]
      },
      {
        "titulo": "Normalização de Dados",
        "topicos": [
          "Primeira, segunda e terceira formas normais.",
          "Processo de normalização de um esquema de banco de dados."
        ]
      },
      {
        "titulo": "Técnicas de Modelagem e Ferramentas",
        "topicos": [
          "Uso de ferramentas de modelagem.",
          "Técnicas para transformar requisitos em modelos conceituais."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "programacao-e-design-para-web-i",
    "periodo": 2,
    "nome": "Programação e Design para Web I",
    "objetivos": [
      "Apresentar ao aluno a fundamentação teórico-prática do desenvolvimento de aplicativos Web."
    ],
    "habilidades": [],
    "unidades": [
      {
        "titulo": "Desenvolvimento Web Front-End",
        "topicos": [
          "Linguagens de marcação (HTML).",
          "Folhas de estilo (CSS) e design responsivo.",
          "JavaScript e interatividade no navegador."
        ]
      },
      {
        "titulo": "Frameworks e Bibliotecas",
        "topicos": [
          "Uso de bibliotecas como jQuery, Bootstrap etc.",
          "Frameworks front-end como Angular, React, Vue.js."
        ]
      },
      {
        "titulo": "Desenvolvimento Web Back-End",
        "topicos": [
          "Linguagens de programação para o servidor (como PHP, Python, Ruby, Node.js).",
          "Interação com bancos de dados (SQL, NoSQL)."
        ]
      },
      {
        "titulo": "APIs e Integrações",
        "topicos": [
          "Consumo e criação de APIs.",
          "Integração com serviços externos."
        ]
      },
      {
        "titulo": "Arquitetura de Aplicações Web",
        "topicos": [
          "MVC (Model-View-Controller) e arquiteturas relacionadas.",
          "Separar a lógica de negócios da interface."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "analise-e-projeto-de-sistemas",
    "periodo": 3,
    "nome": "Análise e Projeto de Sistemas",
    "objetivos": [
      "Apresentar os conceitos fundamentais relacionados à análise e projeto de sistemas, capacitando o aluno a construir os modelos adequados ao desenvolvimento de um sistema de informação.",
      "Apresentar os conceitos básicos e características da análise e projeto de sistemas de informação;",
      "Desenvolver a compreensão das etapas e ferramentas aplicadas a modelagem de sistemas;",
      "Aprofundar o conhecimento do aluno na Linguagem Unificada de Modelagem (UML), a fim de desenvolver sua capacidade de aplicá-la na produção de modelos de sistemas de informação."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto a:",
      "Definir Análise e Projeto de Sistemas e os principais fundamentos pertencentes a esta disciplina;",
      "Descrever o processo de modelagem de sistemas de informação;",
      "Utilizar as ferramentas adequadas ao processo de modelagem de sistemas de informação;",
      "Analisar situações do mundo real de forma a criar modelos de sistemas de informação apropriados a organização observada;",
      "Planejar e organizar os processos de modelagem de sistemas de informação em organizações e projetos de desenvolvimento de software."
    ],
    "unidades": [
      {
        "titulo": "Diagramas UML (Unified Modeling Language)",
        "topicos": [
          "Uso de diagramas de casos de uso, classes, sequência etc.",
          "Documentação para casos de uso.",
          "Modelagem de sistemas."
        ]
      },
      {
        "titulo": "Arquitetura de Sistemas",
        "topicos": [
          "Design de sistemas e componentes.",
          "Padrões arquiteturais."
        ]
      },
      {
        "titulo": "Design de Interfaces de Usuário",
        "topicos": [
          "Princípios de design de interface.",
          "Prototipagem e wireframes."
        ]
      },
      {
        "titulo": "Modelagem de Dados e Banco de Dados",
        "topicos": [
          "Diagramas de entidade-relacionamento.",
          "Normalização de dados."
        ]
      },
      {
        "titulo": "Padrões de Projeto (Design Patterns)",
        "topicos": [
          "Padrões de projeto comuns e sua aplicação.",
          "Reutilização de soluções."
        ]
      },
      {
        "titulo": "Gestão de Projetos de Sistemas",
        "topicos": [
          "Planejamento, execução e monitoramento de projetos de sistemas.",
          "Uso de metodologias ágeis (Scrum, Kanban etc.)."
        ]
      },
      {
        "titulo": "Documentação e Manutenção de Sistemas",
        "topicos": [
          "Documento de visão",
          "Criação de manuais de usuário.",
          "Atualizações e manutenção de sistemas."
        ]
      }
    ],
    "tecnologias": [
      "N/A"
    ]
  },
  {
    "id": "gestao-de-processos",
    "periodo": 3,
    "nome": "Gestão de Processos",
    "objetivos": [
      "Compreender o desenvolvimento de atividades de processos gerenciais.",
      "Desenvolvimento de capacidade analítica de processo e mapeamento de resultados.",
      "Propiciar análise crítica e capacidade de correção de processos.",
      "Multiplicidade de ações entre pessoas, tecnologia, informação e governança como forma de melhorar os resultados corporativos."
    ],
    "habilidades": [
      "Definição sobre o que são processos de negócios.",
      "Compreensão da dinâmica e envergadura dos processos em métodos de gestão de atividades rotineiras.",
      "Capacidade de analisar e responder aos problemas que podem ocorrer no processo de gestão de uma empresa.",
      "Desenvolvimento de ações que estimulem o perfil gerencial.",
      "Leitura e resumo de trabalhos acadêmicos como forma de desenvolver a capacidade científica e crítica."
    ],
    "unidades": [
      {
        "titulo": "Conceitos de Gestão de Processos",
        "topicos": [
          "Definição de processos e sua importância para as organizações.",
          "Relação entre processos e objetivos organizacionais."
        ]
      },
      {
        "titulo": "Mapeamento e Modelagem de Processos",
        "topicos": [
          "Técnicas para identificar e representar processos.",
          "Diagramas de fluxo de processos, BPMN etc.",
          "Uso de IA com BPMN para processos",
          "BPO (Business Process Optimization)"
        ]
      },
      {
        "titulo": "Análise e Melhoria de Processos",
        "topicos": [
          "Identificação de gargalos e ineficiências.",
          "Estratégias para otimizar processos.",
          "O Processo 5W2H para processos."
        ]
      },
      {
        "titulo": "Automação de Processos",
        "topicos": [
          "Uso de tecnologia para automatizar fluxos de trabalho.",
          "Integração com sistemas de TI.",
          "Uso de Bots em RPA (Robotic Process Automation)"
        ]
      },
      {
        "titulo": "Padronização e Documentação de Processos",
        "topicos": [
          "Documentação de procedimentos e políticas.",
          "Manuais de processos e normas."
        ]
      },
      {
        "titulo": "Monitoramento e Métricas de Processos",
        "topicos": [
          "Definição de indicadores de desempenho.",
          "Acompanhamento e medição de processos."
        ]
      },
      {
        "titulo": "Gestão da Mudança e Transformação Digital",
        "topicos": [
          "Lidar com resistência à mudança.",
          "Incorporar tecnologia na transformação dos processos.",
          "Criação de base de conhecimento em TI."
        ]
      },
      {
        "titulo": "Abordagens Ágeis na Gestão de Processos",
        "topicos": [
          "Aplicação de métodos ágeis na gestão de processos.",
          "Adaptação de processos em ambientes dinâmicos."
        ]
      },
      {
        "titulo": "Lean e Seis Sigma",
        "topicos": [
          "Princípios do Lean e Seis Sigma na otimização de processos.",
          "Redução de desperdícios e melhoria contínua."
        ]
      },
      {
        "titulo": "Gestão de Processos de TI",
        "topicos": [
          "Processos relacionados à entrega e manutenção de sistemas de informação.",
          "Alinhamento de processos de TI com objetivos de negócios."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "gestao-de-projeto-de-banco-de-dados",
    "periodo": 3,
    "nome": "Gestão de Projeto de Banco de Dados",
    "objetivos": [
      "Ministrar ao aluno os fundamentos referentes a projeto e operação de Banco de Dados relacional, assim como, introduzir os conceitos de base dados para sistemas de apoio a decisão e aplicativos web.",
      "Desenvolver a capacidade para a construção de projetos de banco de dados;",
      "Instruir quanto as operações de atualização e consulta a banco de dados;",
      "Apresentar os conceitos referentes a banco de dados para sistemas de apoio a decisão e aplicativos web."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto a:",
      "Nomear os principais conceitosreferentes a projeto e operação de banco de dados;",
      "Descrever o processo de construção do projeto de banco de dados;",
      "Utilizar a linguagem SQL na consulta e manutenção de bancos de dados;",
      "Analisar projetos de banco de dados de forma a identificar pontos de otimização e implementar soluções;",
      "Propor e desenvolver projetos de banco de dados para atendimento de sistemas de informação e aplicativos web."
    ],
    "unidades": [
      {
        "titulo": "Ciclo de Vida de Projetos de Banco de Dados",
        "topicos": [
          "Fases de planejamento, análise, design, implementação, teste e manutenção."
        ]
      },
      {
        "titulo": "Modelagem de Dados",
        "topicos": [
          "Diagramas de entidade-relacionamento (DER).",
          "Normalização de dados."
        ]
      },
      {
        "titulo": "Requisitos do Banco de Dados",
        "topicos": [
          "Coleta e análise de requisitos de dados.",
          "Definição de escopo e metas do projeto de banco de dados."
        ]
      },
      {
        "titulo": "Projeto Físico de Banco de Dados",
        "topicos": [
          "Decisões de implementação e otimização de desempenho.",
          "Escolha de índices, partições etc."
        ]
      },
      {
        "titulo": "Administração de Banco de Dados",
        "topicos": [
          "Instalação e configuração de sistemas de gerenciamento de banco de dados (SGBD).",
          "Backup, recuperação e manutenção."
        ]
      },
      {
        "titulo": "Segurança de Dados",
        "topicos": [
          "Proteção contra ameaças internas e externas.",
          "Autenticação e autorização."
        ]
      },
      {
        "titulo": "Gerenciamento de Mudanças e Manutenção",
        "topicos": [
          "Atualizações, migrações e evolução do banco de dados.",
          "Controle de versão e documentação."
        ]
      },
      {
        "titulo": "Gerenciamento de Projetos",
        "topicos": [
          "Definição de escopo e cronograma.",
          "Acompanhamento de progresso e riscos."
        ]
      },
      {
        "titulo": "Integração com Sistemas",
        "topicos": [
          "Integração de bancos de dados com sistemas de informação.",
          "Interface com APIs e serviços."
        ]
      },
      {
        "titulo": "Grandes bases de Dados",
        "topicos": [
          "Processo de ETL (Extract, Transform e Load) para grandes bases de Dados.",
          "Data Warehouse e OLAP.",
          "Data Lake.",
          "IA e BigData."
        ]
      }
    ],
    "tecnologias": [
      "Banco de Dados: SqLite;",
      "Interface Gráfica com Banco de Dados: DB Browser for SQLite."
    ]
  },
  {
    "id": "gestao-de-projetos-inovadores",
    "periodo": 3,
    "nome": "Gestão de Projetos Inovadores",
    "objetivos": [
      "Apresentar os conceitos fundamentais relacionados ao Gerenciamento de Projetos tradicional e ágil, assim como, desenvolver a capacidade do aluno na utilização de metodologias, boas práticas e ferramentas no gerenciamento de projetos de desenvolvimento de software.",
      "Apresentar os conceitos fundamentais e características do Gerenciamento de Projetos tradicional e ágil;",
      "Desenvolver a compreensão dos principais processos do gerenciamento de projetos tradicional e ágil;",
      "Desenvolver a capacidade de gerenciar projetos de desenvolvimento de software."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto a:",
      "Definir Gerenciamento de Projetos e os principais fundamentos pertencentes a esta disciplina;",
      "Descrever os processos de Gerenciamento de Projetos tradicionais e ágeis;",
      "Utilizar boas práticas, metodologias e ferramentas referentes ao processo de Gerenciamento de Projetos;",
      "Analisar processos de Gerenciamento de Projetos de software de forma a identificar pontos de melhoria e implementar soluções;",
      "Planejar, organizar e gerir projetos de desenvolvimento de software nas organizações."
    ],
    "unidades": [
      {
        "titulo": "Inovação e Criatividade em Projetos",
        "topicos": [
          "Compreensão dos conceitos de inovação e criatividade.",
          "Identificação de oportunidades de inovação."
        ]
      },
      {
        "titulo": "Geração de Ideias e Seleção de Projetos",
        "topicos": [
          "Métodos para gerar ideias inovadoras.",
          "Critérios de seleção de projetos inovadores."
        ]
      },
      {
        "titulo": "Análise de Viabilidade",
        "topicos": [
          "Avaliação técnica, econômica e estratégica de projetos inovadores.",
          "Riscos associados à inovação."
        ]
      },
      {
        "titulo": "Design Thinking e Métodos Ágeis",
        "topicos": [
          "Aplicação de metodologias ágeis e de design thinking.",
          "Ciclo de vida iterativo e colaborativo."
        ]
      },
      {
        "titulo": "Gestão de Equipes Multidisciplinares",
        "topicos": [
          "Colaboração entre diferentes especialidades.",
          "Liderança de equipes inovadoras."
        ]
      },
      {
        "titulo": "Prototipagem e Experimentação",
        "topicos": [
          "Criação de protótipos para testar ideias inovadoras.",
          "Aprendizado com experimentação."
        ]
      },
      {
        "titulo": "Estratégias de Implementação",
        "topicos": [
          "Planejamento da implementação de projetos inovadores.",
          "Gerenciamento de mudanças organizacionais."
        ]
      },
      {
        "titulo": "Propriedade Intelectual e Patentes",
        "topicos": [
          "Proteção legal de ideias e inovações.",
          "Aspectos éticos e legais da propriedade intelectual.",
          "Blockchain para proteção de patentes."
        ]
      },
      {
        "titulo": "Métricas de Sucesso em Inovação",
        "topicos": [
          "Definição e avaliação de métricas de sucesso.",
          "Medição do impacto da inovação."
        ]
      }
    ],
    "tecnologias": [
      "n/a"
    ]
  },
  {
    "id": "midias-digitais",
    "periodo": 3,
    "nome": "Mídias Digitais",
    "objetivos": [
      "Contextualizar o desenvolvimento da digitalização;",
      "Conhecer os conceitos, termos inerentes e utilização de novas mídias;",
      "Compreender a Cibercultura e a comunicação realizada através da internet;",
      "Capacitar o aluno para identificar a melhor ferramenta que possa otimizar as rotinas produtivas das organizações;",
      "Identificar as ações digitais criativas e potenciais de interações nas mídias sociais;"
    ],
    "habilidades": [
      "Conhecimento sobre os conceitos e ferramentas de marketing e de gestão de mídias digitais;",
      "Domínio na gestão das ferramentas de marketing online e off line.",
      "Processo de interação comunicacional;",
      "Visão estratégica sobre a inserção das organizações nas redes sociais e mídias digitais;"
    ],
    "unidades": [
      {
        "titulo": "Conceitos de Mídias Digitais",
        "topicos": [
          "Definição de mídias digitais e sua importância.",
          "Evolução das mídias tradicionais para digitais."
        ]
      },
      {
        "titulo": "Design e Composição de Conteúdo",
        "topicos": [
          "Princípios de design visual para mídias digitais.",
          "Uso de cores, tipografia, layout etc."
        ]
      },
      {
        "titulo": "Produção de Conteúdo Multimídia",
        "topicos": [
          "Criação de imagens, vídeos, áudios e animações.",
          "Edição e pós-produção."
        ]
      },
      {
        "titulo": "Plataformas e Redes Sociais",
        "topicos": [
          "Estratégias de publicação em plataformas digitais.",
          "Interação em redes sociais."
        ]
      },
      {
        "titulo": "Marketing Digital",
        "topicos": [
          "Técnicas de marketing online.",
          "Publicidade digital e análise de métricas."
        ]
      },
      {
        "titulo": "User Experience (UX) em Mídias Digitais",
        "topicos": [
          "Design centrado no usuário.",
          "Melhoria da experiência do usuário em plataformas digitais."
        ]
      },
      {
        "titulo": "Conteúdo Interativo e Gamificação",
        "topicos": [
          "Desenvolvimento de conteúdo interativo.",
          "Uso de elementos de gamificação."
        ]
      },
      {
        "titulo": "Estratégias de Engajamento e Audiência",
        "topicos": [
          "Estratégias para envolver e manter a audiência.",
          "Análise de métricas de engajamento."
        ]
      },
      {
        "titulo": "Direitos Autorais e Propriedade Intelectual",
        "topicos": [
          "Aspectos legais do uso de conteúdo digital.",
          "Respeito aos direitos autorais."
        ]
      },
      {
        "titulo": "Tendências em Mídias Digitais",
        "topicos": [
          "Novas tecnologias e formatos de conteúdo digital.",
          "Realidade virtual, realidade aumentada etc."
        ]
      }
    ],
    "tecnologias": [
      "Plataformas sociais de conteúdo; Software de automação de Marketing RD; Ferramentas Google. Aplicativos mobiles e plataformas de mídias."
    ]
  },
  {
    "id": "programacao-e-design-para-web-ii",
    "periodo": 3,
    "nome": "Programação e Design para Web II",
    "objetivos": [
      "Apresentar ao aluno a fundamentação teórico-práticado desenvolvimento avançado de aplicativos Web."
    ],
    "habilidades": [],
    "unidades": [
      {
        "titulo": "Segurança em Aplicações Web",
        "topicos": [
          "Prevenção de ataques (injeção SQL, cross-site scripting etc.).",
          "Autenticação e autorização."
        ]
      },
      {
        "titulo": "Design de Interface para Web",
        "topicos": [
          "Princípios de design para a web.",
          "Criação de layouts e elementos visuais."
        ]
      },
      {
        "titulo": "User Experience (UX) e Usabilidade",
        "topicos": [
          "Melhorar a experiência do usuário.",
          "Testes de usabilidade e prototipagem."
        ]
      },
      {
        "titulo": "Tecnologias Emergentes",
        "topicos": [
          "Progressive Web Apps (PWAs).",
          "Aplicações web em tempo real."
        ]
      },
      {
        "titulo": "Desenvolvimento Mobile",
        "topicos": [
          "Adaptação de aplicações web para dispositivos móveis.",
          "Uso de frameworks mobile."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "projeto-de-extensao-i",
    "periodo": 3,
    "nome": "Projeto de Extensão I",
    "objetivos": [
      "Facilitar o estabelecimento de relações entre temas e conteúdos ao longo do curso;",
      "Fomentar a capacidade de planejamento do discente com vistas à resolução do problema elaborado;",
      "Estimular o uso de metodologia científica e de pesquisa como forma de resolução de problemas;",
      "Facilitar a construção coletiva do conhecimento e a interdisciplinaridade;",
      "Dar condições para a aprendizagem autônoma do educando no exercício de pesquisa, organização e sistematização de novas informações;",
      "Facilitar as trocas entre docente e discente pela via de orientações individuais e coletivas;",
      "Fomentar a elaboração de relatórios parciais e finais conforme normas de apresentação e escrita científicas;",
      "Fomentar o acesso à comunidade local pela via do mapeamento de suas demandas;",
      "Analisar o objeto de estudo e elaborar possíveis soluções ou novas propostas com vistas às demandas locais;"
    ],
    "habilidades": [
      "Capacidade de aplicação de conceitos e teorias apreendidos de maneira integrada em sala de aula;",
      "Confrontar teorias estudadas com práticas profissionais em ambientes reais ou simulados;",
      "Aperfeiçoamento discente por meio da solução de problemas sociais e ambientais;",
      "Elaboração e exposição de um trabalho científico;",
      "Reconhecer e delimitar problemas e identificar oportunidades;"
    ],
    "unidades": [
      {
        "titulo": "Módulo I - Apresentação da estrutura da disciplina",
        "topicos": [
          "Conceitos de prática extensionista;",
          "Metodologias para elaboração e operacionalização de projetos, instrumental teórico-prático para a pesquisa, coleta, sistematização, e análise dos dados;",
          "Tipos de prática extensionista : programas, projetos (vinculados ou não a programas), cursos, eventos ou prestação de serviços ou produtos;",
          "Estudos de casos de práticas extensionistas exitosas;",
          "Formação dos grupos de trabalho."
        ]
      },
      {
        "titulo": "Módulo II - Abordagem teórica dos objetivos de desenvolvimento sustentável",
        "topicos": [
          "Os ODS e as práticas extensionistas sustentáveis",
          "Exemplos e casos reais"
        ]
      },
      {
        "titulo": "Módulo III – O projeto extensionista na prática",
        "topicos": [
          "A escolha do local a ser encontrado a Dor a ser solucionada",
          "O instrumento extensionista e suas fases"
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "etica-e-cidadania",
    "periodo": 3,
    "nome": "Ética e Cidadania",
    "objetivos": [
      "Debater a Ética, a Moral e a Cidadania na sociedade contemporânea;",
      "Provocar uma reflexão sobre Ética e Responsabilidade Social;",
      "Discutir a Ética e a postura do profissional no mundo do trabalho;",
      "Contextualizar a importância da Ética nas mídias sociais;",
      "Relacionar Ética, Moral e confiabilidade no mundo tecnológico."
    ],
    "habilidades": [
      "Exercício reflexivo e constante da cidadania e da ética na vida em sociedade;",
      "Estabelecimento de uma postura profissional ética no mundo do trabalho;",
      "Desenvolvimento da responsabilidade social no ambiente digital;",
      "Valorização e exercício do comportamento éticono mundo tecnológico."
    ],
    "unidades": [
      {
        "titulo": "Ética Profissional na Tecnologia",
        "topicos": [
          "Códigos de ética profissional na área de tecnologia da informação.",
          "Responsabilidade ética na tomada de decisões tecnológicas."
        ]
      },
      {
        "titulo": "Privacidade e Proteção de Dados",
        "topicos": [
          "Importância da privacidade e confidencialidade dos dados.",
          "Conformidade com regulamentações de proteção de dados.",
          "LGPD",
          "Marco Civil da Internet"
        ]
      },
      {
        "titulo": "Responsabilidade Social na Tecnologia",
        "topicos": [
          "Contribuição da tecnologia para o bem-estar social.",
          "Uso de tecnologia em iniciativas de responsabilidade social."
        ]
      },
      {
        "titulo": "Acesso Universal à Tecnologia",
        "topicos": [
          "Equidade no acesso à tecnologia e à informação.",
          "Digitalização e inclusão digital."
        ]
      },
      {
        "titulo": "Impactos Sociais da Tecnologia",
        "topicos": [
          "Reflexão sobre os efeitos sociais da automação, inteligência artificial etc.",
          "Impacto das redes sociais e da desinformação."
        ]
      },
      {
        "titulo": "Ética no Desenvolvimento de Software",
        "topicos": [
          "Questões éticas no design de sistemas e aplicações.",
          "Considerações de bias e justiça em algoritmos."
        ]
      },
      {
        "titulo": "Ética na Coleta e Uso de Dados",
        "topicos": [
          "Questões éticas na coleta, armazenamento e análise de dados.",
          "Consentimento informado."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "empreendedorismo-digital",
    "periodo": 4,
    "nome": "Empreendedorismo Digital",
    "objetivos": [
      "Identificar e propor alternativas para atender às demandas de informação visando a possibilidade de empreender de modo inovador e sustentável, sobretudo no meio digital e interativo.",
      "Fomentar a criação de negócios inovadores nesse meio.",
      "Fornecer bases para a capacitação na gestão de modelos de negócios da área, sistemas, aplicações, produtos e serviços.",
      "Trabalha o papel do empreendedor na composição e gerenciamento de equipes e fomentar a implementação de negócios digitais, identificando oportunidade de novos negócios."
    ],
    "habilidades": [
      "Conhecimento sobre os conceitos e ferramentas de marketing e de gestão de mídias digitais;",
      "Domínio na gestão das ferramentas de marketing online e off line.",
      "Processo de identificação de oportunidade de negócios e aplicar idéias inovadoras;",
      "Visão estratégica sobre a inserção das organizações nas redes sociais e mídias digitais;",
      "Conhecimentos básicos para empreender, gerenciar, divulgar e negociar;",
      "Desenvolver habilidades empreendedoras, demonstrando os caminhos para novos negócios e eficientes."
    ],
    "unidades": [
      {
        "titulo": "Fundamentos de Empreendedorismo",
        "topicos": [
          "Conceitos básicos de empreendedorismo.",
          "Identificação de oportunidades de negócios."
        ]
      },
      {
        "titulo": "Modelos de Negócios Digitais",
        "topicos": [
          "Tipos de modelos de negócios online.",
          "Estratégias de monetização."
        ]
      },
      {
        "titulo": "Validação de Ideias e Prototipagem",
        "topicos": [
          "Processo de validação de ideias de negócios digitais.",
          "Criação de protótipos e MVP (Minimum Viable Product).",
          "Modelo Canva de negócio."
        ]
      },
      {
        "titulo": "Estratégias de Marketing e Vendas",
        "topicos": [
          "Uso de marketing digital para atrair clientes.",
          "Técnicas de venda online."
        ]
      },
      {
        "titulo": "Plataformas de E-commerce e Marketplaces",
        "topicos": [
          "Criação e gestão de lojas virtuais.",
          "Venda em marketplaces online."
        ]
      },
      {
        "titulo": "Gestão Financeira e Aspectos Legais",
        "topicos": [
          "Finanças para empreendedores digitais.",
          "Aspectos legais de negócios online."
        ]
      },
      {
        "titulo": "Inovação e Disrupção Digital",
        "topicos": [
          "Uso da tecnologia para criar inovações disruptivas.",
          "Adaptação a mudanças tecnológicas."
        ]
      },
      {
        "titulo": "Gestão de Riscos e Estratégias de Crescimento",
        "topicos": [
          "Identificação e mitigação de riscos no empreendedorismo digital.",
          "Estratégias de crescimento escalável."
        ]
      },
      {
        "titulo": "Pitch e Captação de Investimentos",
        "topicos": [
          "Preparação de pitches para investidores.",
          "Processo de captação de investimentos."
        ]
      },
      {
        "titulo": "Tendências em Empreendedorismo Digital",
        "topicos": [
          "Novas tecnologias e oportunidades de negócios.",
          "Ecossistemas de startups e inovação."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "gestao-de-sistemas-digitais-na-web",
    "periodo": 4,
    "nome": "Gestão de Sistemas Digitais na Web",
    "objetivos": [
      "Apresentar os conceitos fundamentais relacionados a desenvolvimento e administração de sistemas baseados na WEB, assim como, desenvolver a capacidade do aluno na utilização de modelos e ferramentas no processo de desenvolvimento e administração de softwares desta modalidade.",
      "Apresentar os conceitos básicos e características da engenharia de software direcionada aos sistemas baseados na WEB;",
      "Desenvolver a compreensão das principais etapas no desenvolvimento e administração de Webapp;",
      "Desenvolver a capacidade de conduzir os processos de modelagem, construção, implantação e administração de aplicações Web."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto a:",
      "Definir Gestão de Sistemas Web e os principais fundamentos pertencentes a esta disciplina;",
      "Descrever os processos de desenvolvimento e administração dos aplicativos Web;",
      "Utilizar modelos e ferramentas referentes ao processo de desenvolvimento e administração de Webapp;",
      "Analisar processos de desenvolvimento e administração de Webapp de forma a identificar pontos de melhoria e implementar soluções;",
      "Planejar e organizar processos de desenvolvimento e administração de Webapp nas organizações."
    ],
    "unidades": [
      {
        "titulo": "Arquitetura de Sistemas na Web",
        "topicos": [
          "Arquiteturas cliente-servidor e distribuídas.",
          "Uso de APIs e microsserviços.",
          "Cloud Computing para Sistemas Web",
          "IAAS, PAAS, SAAS, BAAS",
          "Estrutura On-Premise x Cloud"
        ]
      },
      {
        "titulo": "Desenvolvimento de Aplicações Web",
        "topicos": [
          "Frameworks e linguagens de programação para a web.",
          "Princípios de design responsivo."
        ]
      },
      {
        "titulo": "Gerenciamento de Conteúdo Web",
        "topicos": [
          "Sistemas de gerenciamento de conteúdo (CMS).",
          "Criação e manutenção de sites."
        ]
      },
      {
        "titulo": "Segurança em Sistemas Web",
        "topicos": [
          "Proteção contra ameaças online (injeção SQL, XSSetc.).",
          "Autenticação, autorização e criptografia."
        ]
      },
      {
        "titulo": "Integração de Sistemas na Web",
        "topicos": [
          "Integração com APIs de terceiros.",
          "Uso de Web Services e RESTful APIs."
        ]
      },
      {
        "titulo": "Monitoramento e Análise de Desempenho",
        "topicos": [
          "Ferramentas de monitoramento de desempenho.",
          "Otimização de velocidade e escalabilidade."
        ]
      },
      {
        "titulo": "Gestão de Projetos de Desenvolvimento Web",
        "topicos": [
          "Planejamento, execução e acompanhamento de projetos.",
          "Uso de metodologias ágeis (Scrum, Kanban etc.)."
        ]
      },
      {
        "titulo": "Tecnologias Emergentes na Web",
        "topicos": [
          "Uso de WebRTC, Progressive Web Apps (PWAs) etc.",
          "Tendências em desenvolvimento web."
        ]
      }
    ],
    "tecnologias": [
      "N/A"
    ]
  },
  {
    "id": "programacao-cliente-servidor",
    "periodo": 4,
    "nome": "Programação Cliente Servidor",
    "objetivos": [
      "Apresentar ao aluno a fundamentação teórico-práticano desenvolvimento na arquitetura cliente/servidor."
    ],
    "habilidades": [],
    "unidades": [
      {
        "titulo": "Arquitetura Cliente-Servidor",
        "topicos": [
          "Conceitos fundamentais de arquitetura cliente-servidor.",
          "Distribuição de responsabilidades entre cliente e servidor."
        ]
      },
      {
        "titulo": "Comunicação entre Cliente e Servidor",
        "topicos": [
          "Protocolos de comunicação, como HTTP, WebSocket etc.",
          "Uso de APIs e chamadas assíncronas."
        ]
      },
      {
        "titulo": "Desenvolvimento de Aplicações Web",
        "topicos": [
          "Linguagens de marcação (HTML) e folhas de estilo (CSS).",
          "Integração de linguagens de programação do lado do servidor (como PHP, Python etc.)."
        ]
      },
      {
        "titulo": "Frameworks de Desenvolvimento Web",
        "topicos": [
          "Utilização de frameworks como Express.js, Django, Ruby onRails etc.",
          "Facilitação do desenvolvimento cliente-servidor."
        ]
      },
      {
        "titulo": "Banco de Dados e Persistência",
        "topicos": [
          "Interação com bancos de dados a partir do servidor.",
          "Consultas SQL e operações CRUD."
        ]
      },
      {
        "titulo": "Segurança em Aplicações Cliente-Servidor",
        "topicos": [
          "Proteção contra ameaças DDoS, injeção SQL e cross-site scripting.",
          "Implementação de autenticação e autorização."
        ]
      },
      {
        "titulo": "Autenticação e Sessões",
        "topicos": [
          "Gerenciamento de autenticação de usuários.",
          "Uso de cookies e tokens."
        ]
      },
      {
        "titulo": "Desenvolvimento de APIs",
        "topicos": [
          "Criação de APIs para comunicação entre sistemas.",
          "Princípios RESTful e melhores práticas."
        ]
      },
      {
        "titulo": "Tecnologias Emergentes",
        "topicos": [
          "Uso de WebSockets para comunicação em tempo real.",
          "Aplicações de Progressive Web Apps (PWAs)."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "programacao-para-dispositivos-moveis",
    "periodo": 4,
    "nome": "Programação para Dispositivos Móveis",
    "objetivos": [
      "Apresentar ao aluno a fundamentação teórico-práticano desenvolvimento de aplicativos para dispositivos móveis."
    ],
    "habilidades": [],
    "unidades": [
      {
        "titulo": "Desenvolvimento de Aplicativos Móveis",
        "topicos": [
          "Linguagens de programação e tecnologias usadas no desenvolvimento móvel.",
          "Diferenças entre desenvolvimento para iOS e Android."
        ]
      },
      {
        "titulo": "Interfaces de Usuário Móveis",
        "topicos": [
          "Princípios de design de interface para dispositivos móveis.",
          "Uso de componentes nativos e customizados."
        ]
      },
      {
        "titulo": "Gerenciamento de Layout e Componentes",
        "topicos": [
          "Criação de layouts responsivos e adaptáveis.",
          "Uso de componentes de interface, como botões, listas etc."
        ]
      },
      {
        "titulo": "Interação com Dispositivos",
        "topicos": [
          "Acesso a recursos do dispositivo, como câmera, GPS etc.",
          "Uso de sensores e recursos de hardware."
        ]
      },
      {
        "titulo": "Persistência de Dados Móveis",
        "topicos": [
          "Armazenamento local de dados em aplicativos móveis.",
          "Uso de bancos de dados e armazenamento em nuvem."
        ]
      },
      {
        "titulo": "Desenvolvimento Multiplataforma",
        "topicos": [
          "Uso de ferramentas que permitem desenvolver para várias plataformas.",
          "Vantagens e desvantagens da abordagem multiplataforma."
        ]
      },
      {
        "titulo": "Testes e Depuração em Dispositivos Móveis",
        "topicos": [
          "Técnicas de teste de aplicativos em dispositivos reais e emuladores.",
          "Identificação e correção de erros."
        ]
      },
      {
        "titulo": "Segurança e Privacidade em Apps Móveis",
        "topicos": [
          "Proteção de dados pessoais e informações sensíveis.",
          "Melhores práticas de segurança."
        ]
      },
      {
        "titulo": "Publicação e Distribuição de Apps",
        "topicos": [
          "Processo de publicação em lojas de aplicativos (App Store, Google Play etc.).",
          "Considerações sobre termos de uso e diretrizes."
        ]
      },
      {
        "titulo": "Tendências em Desenvolvimento Móvel",
        "topicos": [
          "Uso de realidade aumentada, machine learning etc., em aplicativos móveis.",
          "Adaptação a novas tecnologias e dispositivos."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "projeto-integrador-i",
    "periodo": 4,
    "nome": "Projeto Integrador I",
    "objetivos": [
      "Orientar o aluno na concepção e desenvolvimento de um produto tecnológico inovador a partir da observação de ambientes e identificação de problemas até a prototipação da solução."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto aconceber e desenvolver protótipos de soluções tecnológicas inovadoras."
    ],
    "unidades": [
      {
        "titulo": "I - Propostas de Soluções Tecnológicas Inovadoras",
        "topicos": [
          "Compreender os conceitos de inovação e sua aplicação em soluções tecnológicas.",
          "Identificar problemas ou oportunidades que podem ser abordados com soluções inovadoras.",
          "Desenvolver habilidades de pesquisa e brainstorming para gerar ideias criativas.",
          "Introdução à Inovação e Tecnologia",
          "Identificação de Problemas e Oportunidades",
          "Metodologias de Geração de Ideias",
          "Brainstorming e Seleção de Ideias"
        ]
      },
      {
        "titulo": "II: Construção de Modelo Ambiental de Soluções Tecnológicas",
        "topicos": [
          "Analisar o contexto ambiental em que as soluções tecnológicas serão implantadas.",
          "Considerar os impactos sociais, econômicos e ambientais das soluções propostas.",
          "Integrar princípios de sustentabilidade no processo de desenvolvimento tecnológico.",
          "Análise do Contexto Ambiental e Social",
          "Avaliação de Impactos Socioambientais",
          "Sustentabilidade e Desenvolvimento Tecnológico",
          "Apresentação do Modelo Ambiental"
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "projeto-de-extensao-ii",
    "periodo": 4,
    "nome": "Projeto de Extensão II",
    "objetivos": [
      "Facilitar o estabelecimento de relações entre temas e conteúdos ao longo do curso;",
      "Fomentar a capacidade de planejamento do discente com vistas à resolução do problema elaborado;",
      "Estimular o uso de metodologia científica e de pesquisa como forma de resolução de problemas;",
      "Facilitar a construção coletiva do conhecimento e a interdisciplinaridade;",
      "Dar condições para a aprendizagem autônoma do educando no exercício de pesquisa, organização e sistematização de novas informações;",
      "Facilitar as trocas entre docente e discente pela via de orientações individuais e coletivas;",
      "Fomentar a elaboração de relatórios parciais e finais conforme normas de apresentação e escrita científicas;",
      "Fomentar o acesso à comunidade local pela via do mapeamento de suas demandas;",
      "Analisar o objeto de estudo e elaborar possíveis soluções ou novas propostas com vistas às demandas locais;"
    ],
    "habilidades": [
      "Capacidade de aplicação de conceitos e teorias apreendidos de maneira integrada em sala de aula;",
      "Confrontar teorias estudadas com práticas profissionais em ambientes reais ou simulados;",
      "Aperfeiçoamento discente por meio da solução de problemas sociais e ambientais;",
      "Elaboração e exposição de um trabalho científico;",
      "Reconhecer e delimitar problemas e identificar oportunidades;"
    ],
    "unidades": [
      {
        "titulo": "Módulo I - Apresentação da estrutura da disciplina",
        "topicos": [
          "Conceitos de prática extensionista;",
          "Metodologias para elaboração e operacionalização de projetos, instrumental teórico-prático para a pesquisa, coleta, sistematização, e análise dos dados;",
          "Tipos de prática extensionista : programas, projetos (vinculados ou não a programas), cursos, eventos ou prestação de serviços ou produtos;",
          "Estudos de casos de práticas extensionistas exitosas;",
          "Formação dos grupos de trabalho."
        ]
      },
      {
        "titulo": "Módulo II - BUSINESS MODEL CANVAS",
        "topicos": [
          "Ideação e protótipos;",
          "Os 9 elementos;",
          "O Quadro do Modelo de Negócios;",
          "Construção do quadro;",
          "Aplicação do Modelo CANVAS no projeto extensionista desenvolvido."
        ]
      },
      {
        "titulo": "Módulo III – O projeto extensionista na prática",
        "topicos": [
          "A escolha do local a ser encontrado a Dor a ser solucionada",
          "O instrumento extensionista e suas fases"
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "governanca-de-ti",
    "periodo": 5,
    "nome": "Governança de TI",
    "objetivos": [
      "Propiciar uma visão sobre Governança de TI, Gestão de Serviços de TI e o uso de melhores práticas com o framework COBIT e ITIL."
    ],
    "habilidades": [
      "Compreender as bases teóricas sobre governança de TI",
      "Conhecer os principais modelos e padrões de Governança de TI.",
      "Compreender o alinhamento estratégico entre os objetivos de negócio ea TI."
    ],
    "unidades": [
      {
        "titulo": "Conceitos e Princípios de Governança de TI",
        "topicos": [
          "Definições de governança de TI e sua importância.",
          "Princípios de alinhamento estratégico e entrega de valor."
        ]
      },
      {
        "titulo": "Estruturas de Governança de TI",
        "topicos": [
          "Frameworks de governança de TI, como COBIT, ITIL, ISO/IEC 38500 etc.",
          "Modelos de referência e melhores práticas."
        ]
      },
      {
        "titulo": "Planejamento Estratégico de TI",
        "topicos": [
          "Integração da estratégia de TI com a estratégia global da organização.",
          "Definição de metas, objetivos e indicadores de desempenho."
        ]
      },
      {
        "titulo": "Gestão de Riscos de TI",
        "topicos": [
          "Identificação e avaliação de riscos de TI.",
          "Desenvolvimento de planos de mitigação de riscos."
        ]
      },
      {
        "titulo": "Gerenciamento de Projetos de TI",
        "topicos": [
          "Metodologias de gerenciamento de projetos (ex: PMBOK, Scrum).",
          "Avaliação de viabilidade, cronogramas e recursos."
        ]
      },
      {
        "titulo": "Avaliação de Desempenho e Monitoramento",
        "topicos": [
          "Indicadores-chave de desempenho (KPIs) em TI.",
          "Monitoramento contínuo de processos e serviços de TI."
        ]
      },
      {
        "titulo": "Políticas e Processos de TI",
        "topicos": [
          "Desenvolvimento e implementação de políticas de TI.",
          "Documentação de processos e procedimentos."
        ]
      },
      {
        "titulo": "Compliance e Conformidade",
        "topicos": [
          "Cumprimento de regulamentações e padrões de segurança.",
          "Auditorias e certificações relacionadas a TI."
        ]
      },
      {
        "titulo": "Gestão de Fornecedores de TI",
        "topicos": [
          "Seleção, contratação e monitoramento de fornecedores de serviços e produtos de TI.",
          "Acordos de nível de serviço (SLAs) e contratos."
        ]
      },
      {
        "titulo": "Cultura e Ética em Governança de TI",
        "topicos": [
          "Promoção de uma cultura organizacional alinhada à governança de TI.",
          "Aspectos éticos relacionados ao uso de recursos de TI."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "legislacao-em-negocios-digitais",
    "periodo": 5,
    "nome": "Legislação em Negócios Digitais",
    "objetivos": [
      "Capacitar os alunos para análise de questões jurídicas referente a tecnologia. Fornecer os conceitos básicos jurídicos e familiarizar os discentes com os termos técnicos. Despertar uma visão crítica do direito tecnológico. Preparar o profissional tecnológico para analisar a utilização da informática e suas consequências jurídicas."
    ],
    "habilidades": [
      "Despertar a visão crítica, investigativa, ética e empreendedora com capacidade de atuação nos ambientes virtuais. Desenvolver competência analítica, possibilitando implantação e gerenciamento de contratos, modelação de ambientes seguros seguindo as normas técnicas e protegendo dados e informações confidenciais. Habilitar para criação de projetos e soluções de questões administrativas e negócios nos ambientes de E-Commerce."
    ],
    "unidades": [
      {
        "titulo": "Legislação de Proteção de Dados Pessoais",
        "topicos": [
          "Compreensão das leis de proteção de dados, como a GDPR na Europa e a LGPD no Brasil.",
          "Responsabilidades das empresas em relação à coleta, armazenamento e uso de dados pessoais."
        ]
      },
      {
        "titulo": "Propriedade Intelectual e Direitos Autorais",
        "topicos": [
          "Conhecimento das leis de direitos autorais e patentes em contexto digital.",
          "Uso legal de conteúdo protegido por direitos autorais."
        ]
      },
      {
        "titulo": "Comércio Eletrônico e Contratos Online",
        "topicos": [
          "Regulamentações de comércio eletrônico e contratos digitais.",
          "Validade e execução de contratos assinados eletronicamente."
        ]
      },
      {
        "titulo": "Responsabilidade Digital e Crimes Cibernéticos",
        "topicos": [
          "Entendimento das responsabilidades legais em casos de crimes cibernéticos.",
          "Implicações legais de violações de segurança e vazamentos de dados."
        ]
      },
      {
        "titulo": "Regulamentação de Marketing Digital",
        "topicos": [
          "Restrições e regulamentações relacionadas a publicidade online.",
          "Consentimento e privacidade em campanhas de marketing."
        ]
      },
      {
        "titulo": "Aspectos Legais de Startups e Empreendedorismo Digital",
        "topicos": [
          "Legislação para startups, como captação de investimentos e propriedade intelectual.",
          "Desafios legais na criação e crescimento de empresas digitais."
        ]
      },
      {
        "titulo": "Legislação Internacional em Negócios Digitais",
        "topicos": [
          "Entendimento das leis internacionais que afetam transações e atividades digitais.",
          "Conflitos legais em jurisdições diferentes."
        ]
      },
      {
        "titulo": "Proteção ao Consumidor em Negócios Digitais",
        "topicos": [
          "Regulamentações para garantir os direitos do consumidor online.",
          "Direito de arrependimento, devoluções e reembolsos."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "programacao-e-design-para-web-iii",
    "periodo": 5,
    "nome": "Programação e Design para Web III",
    "objetivos": [
      "Apresentar ao aluno a fundamentação teórico-prática do desenvolvimento avançado de aplicativos Web."
    ],
    "habilidades": [],
    "unidades": [
      {
        "titulo": "Construção de API – Back-End",
        "topicos": []
      },
      {
        "titulo": "Introdução a APIs e Web Services",
        "topicos": [
          "Conceitos básicos de APIs e serviços web.",
          "Tipos de serviços, como SOAP, REST, GraphQL, entre outros."
        ]
      },
      {
        "titulo": "Design de API e Boas Práticas",
        "topicos": [
          "Princípios de design RESTful (Representational State Transfer).",
          "Uso adequado de métodos HTTP (GET, POST, PUT, DELETE)."
        ]
      },
      {
        "titulo": "Roteamento e Endpoints",
        "topicos": [
          "Definição de rotas e endpoints em uma API.",
          "Mapeamento de URLs para funções específicas."
        ]
      },
      {
        "titulo": "Autenticação e Autorização",
        "topicos": [
          "Implementação de autenticação e autorização em APIs.",
          "Uso de tokens, como JWT (JSON Web Tokens)."
        ]
      },
      {
        "titulo": "Formatos de Dados e Serialização",
        "topicos": [
          "Uso de formatos de dados como JSON e XML.",
          "Serialização e desserialização de dados."
        ]
      },
      {
        "titulo": "Manipulação de Recursos",
        "topicos": [
          "Criação, leitura, atualização e exclusão de recursos.",
          "Uso de verbos HTTP correspondentes (POST, GET, PUT, DELETE)."
        ]
      },
      {
        "titulo": "Tratamento de Erros e Códigos de Resposta",
        "topicos": [
          "Tratamento de erros e códigos de resposta HTTP.",
          "Respostas adequadas para diferentes cenários."
        ]
      },
      {
        "titulo": "Documentação de API",
        "topicos": [
          "Importância da documentação clara e completa.",
          "Uso de ferramentas como Swagger ou Postman."
        ]
      },
      {
        "titulo": "Testes de API",
        "topicos": [
          "Testes unitários e de integração para APIs.",
          "Uso de bibliotecas de teste, como Jest ou Postman."
        ]
      },
      {
        "titulo": "Segurança em APIs",
        "topicos": [
          "Proteção contra-ataques, como injeção, cross-site scripting, etc.",
          "Considerações de segurança ao projetar APIs."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "projeto-integrador-ii",
    "periodo": 5,
    "nome": "Projeto Integrador II",
    "objetivos": [
      "Orientar o aluno no planejamento de negócio de uma solução tecnológica inovadora e no desenvolvimento do Mínimo Produto Viável."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto a desenvolver o plano de negócio e o mínimo produto viável (MVP) de soluções tecnológicas inovadoras."
    ],
    "unidades": [
      {
        "titulo": "I: Monetização e Orçamento Preliminar de Soluções Tecnológicas",
        "topicos": [
          "Explorar estratégias de monetização para soluções tecnológicas.",
          "Desenvolver um orçamento preliminar que considere custos e receitas.",
          "Compreender a relação entre viabilidade financeira e inovação.",
          "Estratégias de Monetização",
          "Estimativa de Custos e Receitas",
          "Análise de Viabilidade Financeira",
          "Apresentação do Orçamento Preliminar"
        ]
      },
      {
        "titulo": "II: Avaliação de Propostas Tecnológicas",
        "topicos": [
          "Aprender métodos de avaliação de propostas tecnológicas.",
          "Identificar critérios de sucesso e métricas relevantes.",
          "Realizar análises de risco e benefício para tomada de decisões.",
          "Métodos de Avaliação de Propostas",
          "Definição de Critérios de Avaliação",
          "Análise de Riscos e Benefícios",
          "Apresentação da Avaliação"
        ]
      },
      {
        "titulo": "III: Modelo Relacional de Dados e Prototipação de Soluções Tecnológicas",
        "topicos": [
          "Criar um modelo relacional de dados para suportar as soluções propostas.",
          "Desenvolver protótipos funcionais das soluções tecnológicas.",
          "Realizar testes e iterações nos protótipos para refinamento.",
          "Conceitos de Modelagem de Dados Relacionais",
          "Criação do Modelo Relacional",
          "Desenvolvimento de Protótipos Funcionais",
          "Testes e Iterações de Protótipos"
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "qualidade-e-testes-de-software",
    "periodo": 5,
    "nome": "Qualidade e Testes de Software",
    "objetivos": [
      "Apresentar os conceitos fundamentais relacionados à qualidade de software, assim como, desenvolver a capacidade do aluno na utilização de modelos e ferramentas no processo de garantia da qualidade de software.",
      "Apresentar o histórico, conceitos básicos e características da qualidade de software;",
      "Desenvolver a compreensão dos principais modelos de maturidade na garantia da qualidade de software;",
      "Desenvolver a capacidade de planejamento e execução do processo de garantia da qualidade de software."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto a:",
      "Definir qualidade de software e os principais fundamentos pertencentes a esta disciplina;",
      "Descrever o processo de garantia da qualidade de software durante o ciclo de vida do software;",
      "Utilizar modelos e ferramentas referentes ao processo de garantia da qualidade de software em organizações e projetos de desenvolvimento de software;",
      "Analisar processos de garantia da qualidade de software de forma a identificar pontos de melhoria e implementar soluções;",
      "Planejar e organizar processos de garantia de software em organizações e projetos de desenvolvimento de software."
    ],
    "unidades": [
      {
        "titulo": "Conceitos Básicos de Qualidade de Software",
        "topicos": [
          "Definições de qualidade de software e sua importância.",
          "Fatores que afetam a qualidade do software."
        ]
      },
      {
        "titulo": "Modelos de Qualidade de Software",
        "topicos": [
          "Modelos de qualidade, como o Modelo de Qualidade ISO/IEC 9126.",
          "Características de qualidade, como funcionalidade, confiabilidade, usabilidade etc."
        ]
      },
      {
        "titulo": "Modelos de Maturidade do Software",
        "topicos": [
          "CMM e CMMI.",
          "MPS.BR."
        ]
      },
      {
        "titulo": "Testes de Software",
        "topicos": [
          "Importância dos testes na garantia da qualidade.",
          "Tipos de testes, como testes unitários, de integração, de sistema e de aceitação.",
          "Caixa Branca, Caixa preta, teste alfa."
        ]
      },
      {
        "titulo": "Estratégias de Teste",
        "topicos": [
          "Planejamento de estratégias de teste.",
          "Uso de técnicas de testes como teste caixa-preta e caixa-branca."
        ]
      },
      {
        "titulo": "Automação de Testes",
        "topicos": [
          "Vantagens da automação de testes.",
          "Ferramentas de automação, como Selenium, JUnit, TestNG etc."
        ]
      },
      {
        "titulo": "Testes de Regressão",
        "topicos": [
          "Testes para garantir que novas funcionalidades não impactem as existentes.",
          "Automação de testes de regressão."
        ]
      },
      {
        "titulo": "Testes de Performance e Carga",
        "topicos": [
          "Avaliação do desempenho e escalabilidade do software.",
          "Testes de estresse e carga."
        ]
      },
      {
        "titulo": "Testes de Segurança",
        "topicos": [
          "Identificação e prevenção de vulnerabilidades.",
          "Testes de penetração e avaliação de segurança.",
          "OWASP ZAP e Top 10"
        ]
      },
      {
        "titulo": "Gerenciamento de Defeitos e Relatórios",
        "topicos": [
          "Identificação, registro e acompanhamento de defeitos.",
          "Uso de ferramentas de gerenciamento de defeitos."
        ]
      },
      {
        "titulo": "Melhores Práticas de Teste e Garantia de Qualidade",
        "topicos": [
          "Padrões e boas práticas de teste.",
          "Integração contínua e práticas ágeis de desenvolvimento."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "seguranca-em-sistemas-computacionais",
    "periodo": 5,
    "nome": "Segurança em Sistemas Computacionais",
    "objetivos": [
      "Propiciar uma visão sobre Segurança da Informação, técnicas e os principais mecanimos de defesa utilizados."
    ],
    "habilidades": [
      "Desenvolver noções e habilidades básicas sobre questões envolvendo Segurança da Informação e sua aplicabilidade."
    ],
    "unidades": [
      {
        "titulo": "Princípios de Segurança da Informação",
        "topicos": [
          "Conceitos de confidencialidade, integridade e disponibilidade.",
          "Triângulo de segurança e modelo CIA (Confidentiality, Integrity, Availability)."
        ]
      },
      {
        "titulo": "Criptografia e Criptografia de Dados",
        "topicos": [
          "Princípios de criptografia simétrica e assimétrica.",
          "Uso de criptografia para proteger dados confidenciais."
        ]
      },
      {
        "titulo": "Autenticação e Controle de Acesso",
        "topicos": [
          "Métodos de autenticação, como senhas, autenticação de dois fatores, etc.",
          "Gerenciamento de permissões e controle de acesso a recursos."
        ]
      },
      {
        "titulo": "Firewalls e Detecção de Intrusões",
        "topicos": [
          "Uso de firewalls para proteger redes.",
          "Detecção e prevenção de intrusões."
        ]
      },
      {
        "titulo": "Vulnerabilidades e Ataques",
        "topicos": [
          "Tipos de ameaças, como malware, phishing, engenharia social etc.",
          "Exploração de vulnerabilidades em sistemas."
        ]
      },
      {
        "titulo": "Segurança de Redes e Protocolos",
        "topicos": [
          "Segurança em redes sem fio e redes cabeadas.",
          "Uso de protocolos seguros (por exemplo, HTTPS)."
        ]
      },
      {
        "titulo": "Gestão de Riscos de Segurança",
        "topicos": [
          "Identificação e avaliação de riscos de segurança.",
          "Desenvolvimento de planos de mitigação."
        ]
      },
      {
        "titulo": "Políticas de Segurança e Conformidade",
        "topicos": [
          "Criação e implementação de políticas de segurança.",
          "Conformidade com regulamentações (GDPR x LGPD)."
        ]
      },
      {
        "titulo": "Segurança em Aplicações e Desenvolvimento Seguro",
        "topicos": [
          "Práticas de desenvolvimento seguro de software.",
          "Teste de segurança de aplicações."
        ]
      },
      {
        "titulo": "Aspectos Éticos e Legais em Segurança",
        "topicos": [
          "Ética no uso de informações e tecnologias de segurança.",
          "Aspectos legais da invasão de sistemas."
        ]
      }
    ],
    "tecnologias": []
  },
  {
    "id": "arquitetura-da-informacao-wireframe",
    "periodo": 0,
    "nome": "Arquitetura da Informação - Wireframe",
    "objetivos": [
      "Apresentar os conceitos fundamentais relacionados a Arquitetura da Informação e sua aplicação na construção de interfaces de aplicativos Web e Móveis.",
      "Apresentar os conceitos básicos e características da Arquitetura da Informação aplicada ao desenvolvimento Web e Móvel;",
      "Desenvolver a compreensão dos principais fundamentos do design de aplicativos Web e Móveis;",
      "Desenvolver a capacidade de produzir projetos de interfaces de aplicativos Web e Móveis, utilizando wireframes."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto a:",
      "Definir Arquitetura de Software utilizada no desenvolvimento de aplicativos Web e Móveis e os principais fundamentos pertencentes a esta disciplina;",
      "Descrever os fundamentos do design e de navegação de aplicativos Web e Móveis;",
      "Utilizar conceitos e ferramentas na construção de Wireframes para o desenvolvimento de aplicativos Web e Móveis;",
      "Analisar processos de desenvolvimento e manutenção de aplicativos Web e Móveis com a aplicação de Wireframes, de forma a identificar pontos de melhoria e implementar soluções;",
      "Planejar e organizar processos de desenvolvimento de aplicativos Web e Móveis, utilizando Wireframes."
    ],
    "unidades": [
      {
        "titulo": "Introdução à Arquitetura da Informação",
        "topicos": [
          "Definição de arquitetura da informação e sua importância.",
          "Relação entre arquitetura da informação e experiência do usuário."
        ]
      },
      {
        "titulo": "Organização de Conteúdo",
        "topicos": [
          "Hierarquização e categorização de informações.",
          "Estruturação de menus, navegação e taxonomia."
        ]
      },
      {
        "titulo": "Princípios de Usabilidade e Acessibilidade",
        "topicos": [
          "Práticas para tornar interfaces mais usáveis.",
          "Considerações para acessibilidade a usuários com deficiências."
        ]
      },
      {
        "titulo": "Mapeamento de Fluxos de Usuário",
        "topicos": [
          "Definição de jornadas e fluxos de usuários.",
          "Identificação de pontos de interação e decisão."
        ]
      },
      {
        "titulo": "Wireframe e Prototipação",
        "topicos": [
          "Criação de wireframes como representações visuais de interfaces.",
          "Uso de ferramentas para prototipação de baixa e alta fidelidade."
        ]
      },
      {
        "titulo": "Layout Responsivo e Design Adaptativo",
        "topicos": [
          "Adaptação de interfaces para diferentes dispositivos.",
          "Práticas de design responsivo e breakpoints."
        ]
      },
      {
        "titulo": "Testes de Usabilidade em Wireframes",
        "topicos": [
          "Aplicação de testes de usabilidade em protótipos.",
          "Identificação de problemas de interação e fluxo."
        ]
      },
      {
        "titulo": "Diretrizes de Design e Padrões Visuais",
        "topicos": [
          "Uso de padrões de design, como Material Design ou Bootstrap.",
          "Coerência visual e consistência na interface."
        ]
      },
      {
        "titulo": "Feedback e Iterações de Design",
        "topicos": [
          "Coleta de feedback e iterações em protótipos.",
          "Aperfeiçoamento da usabilidade e experiência do usuário."
        ]
      },
      {
        "titulo": "Integração com Desenvolvimento",
        "topicos": [
          "Interface entre designers e desenvolvedores.",
          "Entrega de recursos para implementação."
        ]
      }
    ],
    "tecnologias": [
      "Ferramentas Wireframe para Design Mobile e Web: Moqups; Wireframe; Pencilevolus; Wirify; WireframeSketcher."
    ]
  },
  {
    "id": "computacao-grafica-para-multimidia",
    "periodo": 0,
    "nome": "Computação Gráfica para Multimídia",
    "objetivos": [
      "Conhecer os principais fatos e a evolução das artes gráficas, seus principais processos e desenvolver o interesse e a curiosidade por esta área.",
      "Identificar os métodos de produção gráfica utilizados no mercado editorial.",
      "Desenvolver a crítica em relação aos diversos movimentos que influenciam as artes gráficas.",
      "Praticar a editoração eletrônica.",
      "Analisar os estilos de Projetos Gráficos aplicados à linha editorial de publicações impressas.",
      "Exercitar elementos gráficos na composição de impressos.",
      "Produzir uma publicação experimental."
    ],
    "habilidades": [
      "Geração de produtos a partir dos conhecimentos adquiridos e divulgação dos mesmos;",
      "Formulação e execução de políticas institucionais;",
      "Elaboração, coordenação, execução e avaliação de planos, programas e projetos;",
      "Desenvolvimento e utilização de novas tecnologias;",
      "Práticas profissionais voltadas para assegurar um núcleo básico de competências que permitam a atuação profissional e a inserção do graduado em diferentes contextos institucionais e sociais, de forma articulada com profissionais de áreas afins."
    ],
    "unidades": [
      {
        "titulo": "Introdução à Computação Gráfica",
        "topicos": [
          "Conceitos básicos de computação gráfica.",
          "Componentes e processos envolvidos na geração de imagens digitais."
        ]
      },
      {
        "titulo": "Modelagem 3D e Renderização",
        "topicos": [
          "Técnicas de modelagem tridimensional.",
          "Processos de iluminação, sombreamento e renderização."
        ]
      },
      {
        "titulo": "Gráficos Vetoriais e Rasterização",
        "topicos": [
          "Diferenças entre gráficos vetoriais e gráficos rasterizados.",
          "Algoritmos de rasterização para desenho de linhas e preenchimento de áreas."
        ]
      },
      {
        "titulo": "Animação e Interatividade",
        "topicos": [
          "Princípios de animação em ambientes digitais.",
          "Técnicas de animação de objetos, personagens e cenas."
        ]
      },
      {
        "titulo": "Edição de Imagens e Ferramentas (possivelmente)",
        "topicos": [
          "Uso de software de edição de imagens, como Photoshop, GIMP etc.",
          "Manipulação de imagens, retoque e tratamento."
        ]
      },
      {
        "titulo": "Realidade Virtual e Aumentada",
        "topicos": [
          "Conceitos de realidade virtual e realidade aumentada.",
          "Desenvolvimento de experiências interativas imersivas."
        ]
      },
      {
        "titulo": "Multimídia e Integração",
        "topicos": [
          "Combinação de elementos gráficos, áudio e vídeo.",
          "Criação de apresentações multimídia interativas."
        ]
      },
      {
        "titulo": "Técnicas de Compressão de Imagem",
        "topicos": [
          "Algoritmos de compressão de imagem.",
          "Formatos de imagem otimizados para web e dispositivos móveis."
        ]
      },
      {
        "titulo": "Aplicações de Jogos e Entretenimento",
        "topicos": [
          "Princípios de design de jogos.",
          "Desenvolvimento de elementos gráficos para jogos."
        ]
      },
      {
        "titulo": "Gráficos Web e Design Responsivo",
        "topicos": [
          "Uso de gráficos em design web.",
          "Adaptação de elementos gráficos para diferentes dispositivos."
        ]
      }
    ],
    "tecnologias": [
      "N/A"
    ]
  },
  {
    "id": "gestao-de-servicos",
    "periodo": 0,
    "nome": "Gestão de Serviços",
    "objetivos": [
      "Ministrar ao aluno os fundamentos da gestão de serviços,capacitando-o a compreender a estrutura de uma empresa de prestação de serviços sob o aspecto teórico e prático."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto a:",
      "Nomear os principais conceitos referentes a gestão de serviços;",
      "Descrever as principais atividades da gestão de serviços;",
      "Analisar estruturas organizacionais de prestação de serviços de forma a identificar pontos de otimização e implementar soluções;",
      "Propor e desenvolver projetos de prestação de serviços."
    ],
    "unidades": [
      {
        "titulo": "Introdução à Gestão de Serviços",
        "topicos": [
          "Conceitos básicos de gestão de serviços.",
          "Papel da TI na prestação de serviços."
        ]
      },
      {
        "titulo": "ITIL (Information Technology Infrastructure Library)",
        "topicos": [
          "Visão geral do framework ITIL.",
          "Processos como gerenciamento de incidentes, problemas, mudanças, entre outros."
        ]
      },
      {
        "titulo": "Processos de Atendimento e Suporte (Service Desk)",
        "topicos": [
          "Funções e responsabilidades do Service Desk.",
          "Técnicas de atendimento ao cliente e resolução de problemas."
        ]
      },
      {
        "titulo": "Gestão de Níveis de Serviço (SLA)",
        "topicos": [
          "Definição de acordos de nível de serviço.",
          "Monitoramento e cumprimento de SLAs."
        ]
      },
      {
        "titulo": "Gerenciamento de Incidentes e Problemas",
        "topicos": [
          "Identificação, registro e resolução de incidentes.",
          "Investigação e solução de problemas recorrentes."
        ]
      },
      {
        "titulo": "Gerenciamento de Mudanças e Versionamento",
        "topicos": [
          "Processo de gerenciamento de mudanças.",
          "Controle de versões de software e documentação."
        ]
      },
      {
        "titulo": "Gestão de Configuração e Ativos (CMDB)",
        "topicos": [
          "Manutenção do registro de configuração.",
          "Controle de ativos de TI."
        ]
      },
      {
        "titulo": "Gerenciamento de Capacidade e Disponibilidade",
        "topicos": [
          "Planejamento e dimensionamento de recursos de TI.",
          "Garantia de disponibilidade de serviços."
        ]
      },
      {
        "titulo": "Segurança da Informação e Gestão de Riscos",
        "topicos": [
          "Considerações de segurança na gestão de serviços.",
          "Avaliação e mitigação de riscos de segurança."
        ]
      }
    ],
    "tecnologias": [
      "N/A"
    ]
  },
  {
    "id": "inteligencia-artificial",
    "periodo": 0,
    "nome": "Inteligência Artificial",
    "objetivos": [
      "Apresentar os conceitos fundamentais relacionados a Arquitetura da Informação e sua aplicação na construção de interfaces de aplicativos Web e Móveis.",
      "Introduzir os alunos aos conceitos, terminologias e fundamentos da Inteligência Artificial.",
      "Familiarizar os alunos com técnicas de aprendizado de máquina, algoritmos de classificação, regressão e agrupamento.",
      "Apresentar os conceitos de redes neurais artificiais e deep learning, permitindo que os alunos compreendam como essas arquiteturas podem ser usadas para resolver problemas complexos, como reconhecimento de padrões e processamento de imagens.",
      "Capacitar os alunos a avaliarem de forma crítica as soluções de IA disponíveis, considerando suas limitações, vantagens e desafios, e escolhendo abordagens adequadas para problemas específicos."
    ],
    "habilidades": [
      "O aluno deverá, ao final da disciplina, estar apto a:",
      "Compreender os princípios subjacentes da Inteligência Artificial e suas aplicações em diversas áreas.",
      "Utilizar algoritmos de aprendizado de máquina para resolver problemas de classificação, regressão e agrupamento.",
      "Realizar análise exploratória de dados, tratamento de valores ausentes e normalização de dados antes de aplicar técnicas de IA.",
      "Desenvolver soluções que envolvam análise de texto, criação de modelos de linguagem e construção de chatbots.",
      "Comunicar de maneira clara e eficaz os resultados das análises e projetos de IA para públicos técnicos e não técnicos."
    ],
    "unidades": [
      {
        "titulo": "Introdução à Inteligência Artificial",
        "topicos": [
          "Definição e conceitos fundamentais da Inteligência Artificial.",
          "História e evolução da IA."
        ]
      },
      {
        "titulo": "Aprendizado de Máquina (Machine Learning)",
        "topicos": [
          "Tipos de aprendizado de máquina: supervisionado, não supervisionado e reforçado.",
          "Algoritmos de aprendizado, como regressão linear, árvores de decisão, redes neurais etc."
        ]
      },
      {
        "titulo": "Processamento de Linguagem Natural (NLP)",
        "topicos": [
          "Processamento e análise de textos e linguagem natural.",
          "Aplicações de NLP, como chatbots e análise de sentimento."
        ]
      },
      {
        "titulo": "Visão Computacional",
        "topicos": [
          "Processamento de imagens e detecção de padrões.",
          "Reconhecimento de objetos, faces e cenas."
        ]
      },
      {
        "titulo": "IA e Ética",
        "topicos": [
          "Considerações éticas na aplicação de IA.",
          "Viés e responsabilidade algorítmica."
        ]
      },
      {
        "titulo": "IA em Sistemas Inteligentes",
        "topicos": [
          "Sistemas autônomos e agentes inteligentes.",
          "IA aplicada a jogos, robótica e automação."
        ]
      },
      {
        "titulo": "Deep Learning e Redes Neurais",
        "topicos": [
          "Exploração de arquiteturas de redes neurais profundas.",
          "Treinamento de redes neurais convolucionais e recorrentes."
        ]
      },
      {
        "titulo": "Tendências Futuras em IA",
        "topicos": [
          "Exploração de avanços emergentes em IA.",
          "IA quântica, IA explicável, IA em saúde, entre outros."
        ]
      }
    ],
    "tecnologias": [
      "Ferramentas de IA online: Chat GPT, Bard, outros."
    ]
  }
]
