// Publicações da aba "Dicas" (antes chamada "Atualidades").
//
// Cada publicação:
//   id         identificador único, sem espaços (vira o endereço: #/dicas/<id>)
//   titulo     título da publicação
//   data       data no formato AAAA-MM-DD (não aparece no site; só ordena a lista, mais recentes primeiro)
//   resumo     uma ou duas frases para o cartão da lista
//   texto      texto completo, no mesmo formato das apresentações:
//                parágrafos separados por linha em branco, "## Subtítulo",
//                "- item" (lista), "1. item" (lista numerada), **negrito**
//   fonte      (opcional) link para a notícia ou documento original
//   disciplinaId (opcional) disciplina da dica, mostrada no cartão e na publicação (id de src/data/disciplinas.ts)
export interface Atualidade {
  id: string
  titulo: string
  data: string
  resumo: string
  texto: string
  fonte?: string
  disciplinaId?: string
}

export const atualidades: Atualidade[] = [
  {
    id: 'profissoes-futuras-com-ia',
    titulo: 'Profissões Futuras com IA',
    data: '2026-10-07',
    disciplinaId: 'programacao-e-design-para-web-ii',
    resumo:
      'O seu setor deixará de criar apenas softwares abstratos na tela e passará a construir códigos que ganham corpo, movem-se e interagem com o mundo físico. Conheça as profissões que vão dominar a robótica e o que estudar.',
    texto: `O seu setor deixará de criar apenas softwares abstratos na tela e passará a construir códigos que ganham corpo, movem-se e interagem com o mundo físico.

As profissões de tecnologia que vão dominar o mercado de robótica no futuro próximo incluem:

## Engenharia de Software e Dados

- **Engenheiro de Software para Sistemas Embarcados:** Profissional que desenvolve sistemas operacionais de tempo real (RTOS) e códigos otimizados para chips e microcontroladores que comandam o "corpo" dos robôs.
- **Engenheiro de Visão Computacional:** Especialista em fazer o robô "enxergar" e entender o ambiente. Envolve criar algoritmos de reconhecimento de objetos, profundidade, mapeamento 3D (como LiDAR e SLAM) e rastreamento facial.
- **Arquiteto de Dados para Robótica:** Os robôs geram terabytes de informações por segundo através de seus sensores. Esse profissional projeta a infraestrutura na nuvem (ou Edge Computing) para processar e armazenar esses dados com baixa latência.

## Infraestrutura e Segurança

- **Especialista em Cibersegurança Robótica:** Um robô hackeado pode causar danos físicos reais. Este profissional blinda os sistemas de comunicação do robô contra invasões, sequestros de dados (ransomware) e interceptação de comandos.
- **Engenheiro de Redes e Computação de Borda (Edge Computing):** Garante que os robôs tomem decisões milissegundos mais rápidas processando dados localmente ou através de redes 5G/6G, mantendo uma conexão ultraestável.

## Inteligência Artificial Aplicada

- **Engenheiro de Aprendizado por Reforço (Reinforcement Learning):** Cria modelos de IA onde o robô aprende a executar tarefas complexas (como andar em terrenos acidentados ou pegar objetos frágeis) por meio de tentativa e erro em ambientes simulados.
- **Desenvolvedor de Gêmeos Digitais (Digital Twins):** Cria réplicas virtuais exatas de robôs e fábricas inteiras no computador para testar atualizações de código e simular falhas antes de enviar o software para o robô real.

## O que estudar

Desenvolvimento de software e algoritmos para robótica; aos poucos, migre para a lógica de sistemas em tempo real, inteligência artificial e manipulação de dados de sensores.

Aqui está a trilha de aprendizado essencial que você pode começar a estudar:

**1. Linguagens de Programação Dominantes**

- **C++ (O Coração da Robótica):** É a linguagem mais importante. Os robôs precisam de respostas em milissegundos e controle direto de memória, coisas que o C++ faz com máxima eficiência.
- **Python (A Porta de Entrada e IA):** Fundamental para o desenvolvimento de inteligência artificial, visão computacional e prototipagem rápida. É ideal para começar por ter uma sintaxe amigável.

**2. Frameworks e Ferramentas Padrão do Mercado**

- **ROS (Robot Operating System):** Conheça o ROS 2. Ele não é um sistema operacional tradicional, mas um ecossistema de ferramentas e bibliotecas que serve como o padrão global para programar robôs. Saber ROS é o maior diferencial de um programador de robótica hoje.
- **OpenCV:** A biblioteca mais famosa do mundo para Visão Computacional. Com ela, você aprende a programar códigos que reconhecem formas, cores, rostos e objetos em uma câmera.

**3. Fundamentos Matemáticos e Lógicos**

- **Álgebra Linear e Matrizes:** Essencial para a computação gráfica e robótica. Os robôs se movem em um espaço 3D usando eixos cartesianos (X, Y, Z), e transformações de matrizes são usadas para calcular a rotação e a posição de braços mecânicos ou rodas.
- **Estrutura de Dados e Algoritmos de Busca:** Conceitos de grafos e algoritmos de caminho mínimo (como A* ou Dijkstra), que são a base para fazer robôs autônomos navegarem por labirintos ou desviarem de obstáculos.

**4. Inteligência Artificial Aplicada**

- **Machine Learning e Redes Neurais:** Entender como treinar modelos simples de IA. Ferramentas como TensorFlow ou PyTorch são usadas para que os robôs tomem decisões baseadas em padrões anteriores.

## Como começar na prática (mesmo sem robôs físicos)?

Você não precisa de robôs caros para aprender isso. Você pode usar simuladores virtuais:

- **Webots ou Gazebo:** Simuladores de robótica gratuitos e de código aberto onde você escreve o código em Python ou C++ e veem o robô virtual se mover na tela obedecendo às leis da física.
- **Arduino / ESP32 com simuladores (como Wokwi ou Tinkercad):** Permitem criar lógica de código para ler sensores virtuais e acionar motores sem gastar nada.

## Competências de nível universitário

Projetos ou recomendações de estudo focando nas seguintes competências de nível universitário:

**1. Arquitetura de Software e Middleware**

- **ROS 2 (Robot Operating System) Avançado:** Na faculdade, o ROS 2 é obrigatório. É preciso aprender sobre comunicação por tópicos, serviços e ações (Nodes, Publishers, Subscribers). É o ecossistema que rege desde robôs industriais até os carros autônomos.
- **Sistemas Operacionais de Tempo Real (RTOS):** Diferente do Windows ou Linux comum, robôs usam sistemas como o FreeRTOS ou VxWorks. O código precisa garantir que um comando de parada seja executado instantaneamente, sem travar ou "esperar" outros processos.

**2. Visão Computacional e IA Profunda (Deep Learning)**

- **Redes Neurais Convolucionais (CNNs):** Aprenda a usar frameworks como PyTorch ou TensorFlow para processamento de imagens em tempo real (detecção e segmentação de objetos usando modelos como o YOLO).
- **SLAM (Simultaneous Localization and Mapping):** Algoritmos que permitem ao robô construir o mapa de um ambiente desconhecido e, ao mesmo tempo, descobrir onde ele está dentro desse mapa (usando dados de câmeras e sensores LiDAR).

**3. Computação de Borda (Edge AI) e Otimização**

- **Programação Eficiente em C++:** Na faculdade, gerenciar memória (ponteiros, concorrência, multithreading) de forma manual é crucial, pois os robôs operam com recursos de hardware limitados.
- **Deploy em Hardware de Borda:** Aprender a compilar e rodar modelos de código em placas de processamento embarcado de alta performance, como a linha NVIDIA Jetson (Nano, Orin) ou Raspberry Pi 5.

**4. Matemática de Engenharia Aplicada**

- **Cinemática Direta e Inversa:** Aplicação de matrizes e trigonometria avançada para calcular: "Se eu mover os motores X e Y nesta intensidade, onde a mão do robô vai parar no espaço 3D?" (Cinemática Direta) e o inverso disso.

## Sugestão de Projetos Práticos

Em vez de projetos web tradicionais (como criar um e-commerce ou um app de banco), desafie-se com:

1. **Simulação Completa de Navegação:** Criar um ambiente virtual no simulador Gazebo ou Webots, programar um robô virtual em ROS 2 (utilizando Python ou C++) para mapear uma sala e encontrar a saída de forma 100% autônoma.
2. **Braço Robótico Virtual com Visão:** Integrar a biblioteca OpenCV para fazer uma câmera reconhecer um objeto de uma cor específica na mesa e enviar coordenadas via código para um braço robótico (simulado ou físico) pegar o objeto.`,
  },
  {
    id: 'react-e-robotica',
    titulo: 'React e Robótica: a Web no Controle do Mundo Físico',
    data: '2026-10-07',
    disciplinaId: 'programacao-e-design-para-web-ii',
    resumo:
      'A Web e a Robótica estão se fundindo de forma acelerada: painéis de controle, teleoperação e monitoramento de robôs já são feitos em React. Veja como levar o React para o mundo físico.',
    texto: `Os cursos de desenvolvimento para internet historicamente focam em desenvolvimento Web tradicional (como o React), mas o mercado está expandindo as fronteiras da Web. A boa notícia é que a Web e a Robótica estão se fundindo de forma muito acelerada!

Hoje, as interfaces de controle de robôs, os painéis de teleoperação (controlar robôs à distância) e os sistemas de monitoramento de frotas autônomas são feitos em React e tecnologias web.

Você não precisa abandonar o React. Em vez de criar mais um e-commerce ou uma rede social em React, que tal criar um Dashboard de Controle Robótico?

Como usar o React e se preparar para o futuro da robótica e sistemas inteligentes:

## 1. Conecte o React ao Mundo Físico (WebSockets e MQTT)

Robôs enviam dados em tempo real (posição, bateria, velocidade). O desenvolvimento Web tradicional foca em requisições HTTP normais (que atualizam a página ou esperam uma resposta).

- **O que aprender:** Conectar o React a protocolos de tempo real como WebSockets ou MQTT (muito usado em Internet das Coisas - IoT e Robótica).
- **Ideia de Projeto:** Criar uma página em React com um velocímetro e um gráfico de linha que recebe "dados simulados de sensores de um robô" em tempo real.

## 2. Interfaces de Teleoperação (Controlar Robôs pelo Navegador)

Muitas empresas controlam frotas de robôs ou drones através de uma página web usando tecnologias como WebRTC (para streaming de vídeo de baixa latência da câmera do robô).

- **O que aprender:** Como capturar eventos do teclado, mouse ou até de um controle de videogame (Gamepad API do navegador) dentro do React para enviar comandos.
- **Ideia de Projeto:** Criar um joystick virtual na tela com React. Quando o usuário clica nas setas, a interface dispara um comando no console simulando o movimento de um robô.

## 3. Visualização 3D no Navegador (React Three Fiber / Three.js)

Os operadores de robôs precisam ver onde a máquina está em um mapa 3D direto pelo navegador. O uso de gráficos 3D na web explodiu.

- **O que aprender:** React Three Fiber (R3F), uma biblioteca que permite renderizar cenários e objetos 3D usando componentes React.
- **Ideia de Projeto:** Em vez de uma página plana, crie uma página web onde um modelo 3D simples de um robô (pode ser um cubo ou um carrinho básico) se move na tela quando o usuário altera os inputs nos componentes React.

## 4. Conheça o Web-ROS (roslibjs)

Existe uma biblioteca JavaScript oficial chamada roslibjs que permite conectar uma página web feita em React diretamente ao ROS 2 (o sistema dos robôs citado na dica "Profissões Futuras com IA").

- Se um robô está rodando ROS 2 em uma fábrica, ele pode jogar os dados direto para o seu painel em React. Isso é o estado da arte no mercado atual de frotas autônomas.

## Projeto: CyberFleet Dashboard

Aqui está o escopo de um projeto completo focado em React e Web Robótica. O nome do projeto é **"CyberFleet: Dashboard de Teleoperação e Monitoramento de Robôs"**.

Construa uma aplicação web que simula o painel de controle que um operador usaria em uma central para monitorar e controlar um robô à distância.

**Objetivo do Projeto**

Desenvolver uma interface web SPA (Single Page Application) utilizando React que simule o recebimento de dados de telemetria em tempo real de um robô autônomo e permita o envio de comandos de movimentação.

**Estrutura e Componentes que você deve criar**

O projeto deve ser dividido em componentes reutilizáveis no React:

1. **Sidebar (Menu Lateral):** Para alternar entre diferentes robôs da frota (Ex: "Robô Alfa", "Robô Beta").
2. **TelemetryGrid (Painel de Status):** Uma grade de cards mostrando dados dinâmicos (detalhados abaixo).
3. **ControlPad (Mesa de Comando):** Um componente com botões direcionais (Seta para Cima, Baixo, Esquerda, Direita, e botão de Parada de Emergência).
4. **LiveCamera (Simulador de Visão Computacional):** Uma área da tela que simula a câmera do robô.

Os cards do TelemetryGrid devem mostrar:

- **Nível da Bateria:** com mudança de cor: verde se > 50%, vermelho se < 20%.
- **Velocidade Atual:** em m/s.
- **Temperatura do Motor:** com alerta visual se estiver muito alta.
- **Status de Conexão:** Online / Offline.

**Como simular o tempo real em JavaScript?**

A simulação pode ser feita localmente, no próprio código: um useEffect com setInterval altera o estado do componente de tempos em tempos (por exemplo, a bateria cai 1% a cada 2 segundos) e o React atualiza a tela automaticamente. Depois, essa simulação pode ser trocada por dados reais recebidos via WebSockets ou MQTT.`,
  },
]
