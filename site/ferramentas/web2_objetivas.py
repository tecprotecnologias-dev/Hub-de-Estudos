"""
Questões objetivas de Programação e Design para Web II (módulos 1 a 5), no estilo de
concursos públicos e exames nacionais: situação-problema, afirmativas I/II/III,
asserção-razão, "assinale a incorreta" e leitura de código, sempre com 5 alternativas.

A primeira alternativa de cada questão é a certa; o site embaralha a ordem, por isso a
resolução nunca cita letras. Uso (dentro de site/):

    python ferramentas/web2_objetivas.py

Grava em src/data/questoes/web2.json, trocando só as objetivas (os exercícios práticos
ficam como estão).
"""

import json
import sys
from pathlib import Path

DISCIPLINA = 'programacao-e-design-para-web-ii'
ARQUIVO = Path(__file__).resolve().parent.parent / 'src' / 'data' / 'questoes' / 'web2.json'
PROIBIDAS = ['faeterj', 'faetec', 'enade', 'barra mansa']

ASSERCAO = [
    'As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.',
    'As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.',
    'A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.',
    'A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.',
    'As asserções I e II são proposições falsas.',
]

COMBINACOES = {
    'I': 'I, apenas.',
    'II': 'II, apenas.',
    'III': 'III, apenas.',
    'I,II': 'I e II, apenas.',
    'I,III': 'I e III, apenas.',
    'II,III': 'II e III, apenas.',
    'I,II,III': 'I, II e III.',
}

questoes = []


def _base(cap, nivel, enunciado, contexto=None, caso=None):
    q = {
        'id': f'web2-cap{cap}-o{sum(1 for x in questoes if x["capituloId"] == f"web2-cap{cap}") + 1}',
        'disciplinaId': DISCIPLINA,
        'capituloId': f'web2-cap{cap}',
        'tipo': 'objetiva',
        'nivel': nivel,
    }
    if contexto:
        q['contexto'] = contexto
    if caso:
        q['caso'] = caso
    q['enunciado'] = enunciado
    return q


def p(texto):
    return {'t': 'p', 'texto': texto}


def codigo(texto):
    return {'t': 'codigo', 'texto': texto.strip('\n')}


def multipla(cap, nivel, enunciado, certa, erradas, resolucao, contexto=None, caso=None):
    q = _base(cap, nivel, enunciado, contexto, caso)
    q['alternativas'] = [certa, *erradas]
    q['correta'] = 0
    q['resolucao'] = resolucao
    questoes.append(q)


def afirmativas(cap, nivel, itens, resolucao, contexto=None, intro='Avalie as afirmativas a seguir.'):
    """itens: lista de (texto, verdadeira). A resposta é o conjunto das verdadeiras."""
    romanos = ['I', 'II', 'III']
    caso = [intro] + [f'{romanos[i]}. {t}' for i, (t, _) in enumerate(itens)]
    certa_chave = ','.join(romanos[i] for i, (_, v) in enumerate(itens) if v)
    ordem = ['I', 'II', 'III', 'I,II', 'I,III', 'II,III', 'I,II,III']
    outras = [k for k in ordem if k != certa_chave]
    # quatro distratoras: as combinações "vizinhas" da certa primeiro, depois as demais
    vizinhas = [k for k in outras if set(k.split(',')) & set(certa_chave.split(','))]
    distratoras = (vizinhas + [k for k in outras if k not in vizinhas])[:4]
    q = _base(cap, nivel, 'É correto o que se afirma em', contexto, caso)
    q['alternativas'] = [COMBINACOES[certa_chave]] + [COMBINACOES[k] for k in distratoras]
    q['correta'] = 0
    q['resolucao'] = resolucao
    questoes.append(q)


def assercao(cap, nivel, i, ii, resposta, resolucao, contexto=None):
    """resposta: índice em ASSERCAO (0 = I e II verdadeiras e II justifica I ...)."""
    caso = ['Avalie as asserções a seguir e a relação proposta entre elas.', f'I. {i}', 'PORQUE', f'II. {ii}']
    q = _base(cap, nivel, 'A respeito dessas asserções, assinale a opção correta.', contexto, caso)
    q['alternativas'] = [ASSERCAO[resposta]] + [a for k, a in enumerate(ASSERCAO) if k != resposta]
    q['correta'] = 0
    q['resolucao'] = resolucao
    questoes.append(q)


# =====================================================================================
# Módulo 1: Node.js e Ecossistema NPM
# =====================================================================================

multipla(
    1, 'facil',
    'Sobre o Node.js, assinale a alternativa correta.',
    'É um ambiente de execução (runtime) que roda JavaScript fora do navegador, com o motor V8, e dá acesso a arquivos, rede, processos e variáveis de ambiente.',
    [
        'É um compilador que transforma todo o código JavaScript em um arquivo executável separado antes de rodá-lo.',
        'É um framework de interfaces que leva o DOM e o objeto window para o servidor.',
        'É uma linguagem de programação diferente do JavaScript, criada especificamente para servidores.',
        'É um navegador sem interface gráfica, usado apenas para executar testes automatizados.',
    ],
    'O Node.js é um runtime: lê e executa o arquivo .js na hora, sem gerar executável, usando o mesmo motor V8 do Chrome. '
    'Ele não tem DOM nem window; em troca, oferece APIs de sistema (fs, path, http, process.env). A linguagem continua sendo JavaScript.',
    contexto=[p('Em uma reunião de planejamento, uma equipe de desenvolvimento discute se deve instalar o Node.js nas máquinas, '
                'já que o projeto será uma aplicação web com React e não terá, a princípio, um servidor próprio.')],
)

multipla(
    1, 'facil',
    'Após o comando npm install -D typescript, o pacote é registrado no package.json na seção',
    'devDependencies, pois é necessário apenas durante o desenvolvimento.',
    [
        'dependencies, pois todo pacote instalado pelo npm vai para produção.',
        'scripts, pois o TypeScript passa a ser executado por npm run.',
        'globalDependencies, pois a opção -D instala o pacote para todo o sistema.',
        'peerDependencies, pois o TypeScript depende da versão do Node.js instalada.',
    ],
    'A opção -D (ou --save-dev) grava o pacote em devDependencies: ferramentas usadas só no desenvolvimento, como TypeScript, ESLint e tipos @types. '
    'Pacotes sem -D vão para dependencies, e a instalação global usa a opção -g, que não grava nada no package.json do projeto.',
)

multipla(
    1, 'facil',
    'Sobre o package.json, o package-lock.json e os scripts do npm, assinale a alternativa INCORRETA.',
    'O package-lock.json deve ser editado manualmente sempre que for preciso trocar a versão de uma dependência.',
    [
        'O package.json descreve o projeto, lista as dependências e define os scripts que podem ser executados.',
        'O comando npm start executa o script "start" sem precisar da palavra run.',
        'O comando npm run build executa o script "build" definido no package.json.',
        'O package-lock.json é gerado pelo npm para garantir que todos instalem exatamente as mesmas versões.',
    ],
    'O package-lock.json nunca deve ser editado à mão: ele é gerado automaticamente pelo npm para tornar as instalações reproduzíveis. '
    'Para trocar a versão de uma dependência, usa-se o npm (npm install pacote@versão), que atualiza os dois arquivos. As demais afirmações estão corretas.',
)

multipla(
    1, 'medio',
    'Se o usuário executar node tasks.js add "Estudar Node.js", o que será exibido no terminal?',
    '2 Estudar Node.js',
    ['4 Estudar Node.js', '2 add', '3 tasks.js', '4 add'],
    'process.argv traz, nas posições 0 e 1, o caminho do executável do Node e o caminho do script; os argumentos reais começam na posição 2. '
    'Com slice(2), args fica ["add", "Estudar Node.js"]: o tamanho é 2 e args[1] é o texto "Estudar Node.js".',
    contexto=[
        p('Considere o arquivo tasks.js a seguir.'),
        codigo('''
const args = process.argv.slice(2);
console.log(args.length, args[1]);
'''),
    ],
)

afirmativas(
    1, 'medio',
    [
        ('O arquivo .env deve ser enviado ao repositório Git, para que toda a equipe use as mesmas senhas e chaves.', False),
        ('Em um projeto Next.js, variáveis com o prefixo NEXT_PUBLIC_ ficam visíveis no navegador e, por isso, não devem guardar chaves secretas.', True),
        ('Em um projeto Next.js, variáveis sem o prefixo NEXT_PUBLIC_ ficam disponíveis apenas no servidor.', True),
    ],
    'I é falsa: o .env guarda segredos e deve constar do .gitignore; se for para o Git, as senhas ficam expostas. '
    'II é verdadeira: o prefixo NEXT_PUBLIC_ faz a variável ser embutida no código enviado ao navegador. '
    'III é verdadeira: sem o prefixo, a variável só é lida no servidor, o lugar certo para senhas e tokens.',
    contexto=[p('Uma desenvolvedora está configurando as variáveis de ambiente de uma aplicação que acessa um banco de dados '
                'e consome uma API pública. Ela precisa decidir o que fica no arquivo .env e como cada variável será exposta.')],
)

multipla(
    1, 'medio',
    'Qual alternativa reescreve corretamente esse módulo e essa importação no formato ES Modules?',
    'No utils.js: export { somar, PI }; e, no outro arquivo: import { somar, PI } from "./utils.js";',
    [
        'No utils.js: module.export = { somar, PI }; e, no outro arquivo: import { somar, PI } = require("./utils.js");',
        'No utils.js: exports.default = { somar, PI }; e, no outro arquivo: const { somar, PI } = import("./utils.js");',
        'No utils.js: export require { somar, PI }; e, no outro arquivo: import require("./utils.js");',
        'No utils.js: module.exports = { somar, PI }; e, no outro arquivo: import * from "./utils.js";',
    ],
    'Em ES Modules, a exportação nomeada usa export (export { somar, PI } ou export antes de cada declaração) '
    'e a importação usa import { ... } from "...". No Node.js, o caminho de um arquivo do próprio projeto leva a extensão (./utils.js). '
    'require e module.exports pertencem ao CommonJS, e import * exige um nome (import * as Utils from ...).',
    contexto=[
        p('Um projeto antigo em CommonJS tem o módulo e a importação abaixo, e será migrado para ES Modules.'),
        codigo('''
// utils.js
function somar(a, b) { return a + b; }
const PI = 3.14159;
module.exports = { somar, PI };

// app.js
const { somar, PI } = require("./utils");
'''),
    ],
)

assercao(
    1, 'medio',
    'Em um arquivo escrito como ES Module, usar diretamente a variável __dirname provoca erro.',
    'Em ES Modules, __dirname não é criada automaticamente; o equivalente é obtido a partir de import.meta.url, com fileURLToPath e dirname.',
    0,
    'As duas asserções são verdadeiras, e a II explica a I: __dirname e __filename só existem no CommonJS. '
    'Em ES Modules, obtém-se o mesmo valor com const __dirname = dirname(fileURLToPath(import.meta.url)).',
)

multipla(
    1, 'dificil',
    'Existe o arquivo public/logo.svg. Ao receber uma requisição GET para /logo.svg, o servidor responde com',
    'status 200 e Content-Type application/octet-stream, porque a extensão .svg não está no objeto MIME.',
    [
        'status 404, porque a extensão .svg não está no objeto MIME.',
        'status 200 e Content-Type image/svg+xml, identificado automaticamente pelo readFile.',
        'status 200 e Content-Type text/html, porque o servidor devolve o index.html.',
        'status 500, porque o readFile não consegue ler arquivos de imagem.',
    ],
    'O arquivo existe, então readFile lê o conteúdo e o bloco try segue com status 200. Como MIME[".svg"] é undefined, '
    'o operador || usa o valor padrão "application/octet-stream". O 404 só acontece quando readFile lança erro (arquivo inexistente), '
    'e o index.html só é usado para a URL "/".',
    contexto=[
        p('Considere o servidor HTTP abaixo, feito apenas com os módulos nativos do Node.js.'),
        codigo('''
const MIME = {
  ".html": "text/html",
  ".css": "text/css",
  ".js": "application/javascript",
  ".png": "image/png",
};

const server = createServer(async (req, res) => {
  const url = req.url === "/" ? "/index.html" : req.url;
  const filePath = join(process.cwd(), "public", url);
  try {
    const content = await readFile(filePath);
    const mime = MIME[extname(filePath)] || "application/octet-stream";
    res.writeHead(200, { "Content-Type": mime });
    res.end(content);
  } catch {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("404 -- Arquivo nao encontrado");
  }
});
'''),
    ],
)

assercao(
    1, 'dificil',
    'O Node.js consegue atender centenas de conexões simultâneas usando uma única thread principal.',
    'O Node.js cria uma nova thread do sistema operacional para cada requisição recebida, como fazem os servidores tradicionais.',
    2,
    'A I é verdadeira: o Node.js usa um modelo assíncrono e não bloqueante, com o Event Loop, e atende muitas conexões com uma única thread principal. '
    'A II é falsa: criar uma thread por requisição é justamente o modelo tradicional (como o do Apache) que o Node.js evita.',
)

multipla(
    1, 'dificil',
    'Na primeira vez que o programa é usado, ainda não existe o arquivo tarefas.json. O que acontece ao executar node tasks.js list?',
    'Nada é exibido e o programa termina normalmente, sem criar o arquivo tarefas.json.',
    [
        'O programa é interrompido com um erro de arquivo não encontrado (ENOENT).',
        'O programa cria um arquivo tarefas.json vazio e não exibe nada.',
        'O programa exibe a mensagem de uso "Uso: node tasks.js ...".',
        'O programa exibe "Tarefa undefined nao encontrada."',
    ],
    'O readFile lança erro porque o arquivo não existe, mas o catch de carregarTarefas devolve uma lista vazia. '
    'Com o comando "list", o forEach percorre uma lista vazia e não imprime nada. Só os comandos "add" e "done" chamam salvarTarefas, '
    'então o arquivo também não é criado.',
    contexto=[
        p('Considere este trecho de uma ferramenta de linha de comando que guarda tarefas em um arquivo JSON.'),
        codigo('''
async function carregarTarefas() {
  try {
    const conteudo = await readFile("tarefas.json", "utf-8");
    return JSON.parse(conteudo);
  } catch {
    return [];
  }
}

async function main() {
  const [comando, valor] = process.argv.slice(2);
  const tarefas = await carregarTarefas();
  if (comando === "add") {
    tarefas.push({ id: tarefas.length + 1, texto: valor, feita: false });
    await salvarTarefas(tarefas);
  } else if (comando === "list") {
    tarefas.forEach(t => console.log(`${t.id} - ${t.texto}`));
  } else {
    console.log("Uso: node tasks.js [add | list | done]");
  }
}
'''),
    ],
)

# =====================================================================================
# Módulo 2: React: Componentes e Props
# =====================================================================================

multipla(
    2, 'facil',
    'Sobre o React, assinale a alternativa correta.',
    'É uma biblioteca JavaScript focada em construir interfaces, sem roteamento, busca de dados ou banco de dados embutidos.',
    [
        'É um framework completo, com roteamento, acesso a banco de dados e servidor embutidos.',
        'É uma linguagem que substitui o JavaScript na construção de interfaces.',
        'É um servidor web que entrega páginas HTML prontas ao navegador.',
        'É uma ferramenta de build, usada no lugar do Vite para empacotar o projeto.',
    ],
    'O React é uma biblioteca escrita em JavaScript e focada em uma coisa: renderizar a interface de forma eficiente e previsível. '
    'Roteamento, renderização no servidor e rotas de API ficam a cargo de frameworks construídos sobre ele, como o Next.js.',
)

multipla(
    2, 'facil',
    'Sobre as diferenças entre JSX e HTML, assinale a alternativa INCORRETA.',
    'No JSX, o atributo class é usado normalmente para aplicar classes CSS, exatamente como no HTML.',
    [
        'No JSX, o atributo for do rótulo é escrito como htmlFor.',
        'No JSX, os eventos são escritos em camelCase, como onClick.',
        'No JSX, toda tag precisa ser fechada, como em <br />.',
        'No JSX, valores JavaScript são inseridos entre chaves, como em {nome}.',
    ],
    'Como class é palavra reservada do JavaScript, o JSX usa className. Pelo mesmo motivo, for vira htmlFor. '
    'As demais afirmações descrevem corretamente o JSX.',
)

multipla(
    2, 'facil',
    'Por que o nome de um componente React deve começar com letra maiúscula?',
    'Porque é assim que o React diferencia um componente, como <Botao />, de uma tag HTML comum, como <button>.',
    [
        'Porque o TypeScript não compila funções com nome em letra minúscula.',
        'Porque é apenas uma convenção de estilo, sem nenhum efeito no funcionamento.',
        'Porque só funções com inicial maiúscula podem ser exportadas com export default.',
        'Porque o Vite ignora os arquivos cujo nome começa com letra minúscula.',
    ],
    'Ao encontrar <botao />, o React entende que é uma tag HTML; ao encontrar <Botao />, chama a função Botao. '
    'Por isso a inicial maiúscula não é só estilo: muda o que o React faz.',
)

multipla(
    2, 'medio',
    'Ao renderizar <Carrinho quantidade={0} />, o que aparece na tela?',
    'O número 0.',
    ['Nada.', 'O texto "Itens: 0".', 'O texto "false".', 'Uma mensagem de erro do React.'],
    'O operador && devolve o primeiro valor "falso" que encontra. Com quantidade igual a 0, a expressão vale 0, e o React '
    'mostra números na tela, mesmo o zero (só false, null e undefined não aparecem). A forma segura é quantidade > 0 && ...',
    contexto=[
        p('Considere o componente abaixo.'),
        codigo('''
function Carrinho({ quantidade }: { quantidade: number }) {
  return (
    <div>
      {quantidade && <p>Itens: {quantidade}</p>}
    </div>
  );
}
'''),
    ],
)

afirmativas(
    2, 'medio',
    [
        ('As props são somente leitura: o componente filho não deve alterar os valores que recebeu.', True),
        ('O conteúdo colocado entre as tags de abertura e de fechamento de um componente chega a ele pela prop children.', True),
        ('Na interface CardProps, o ponto de interrogação em footer?: React.ReactNode torna essa prop obrigatória.', False),
    ],
    'I e II são verdadeiras. III é falsa: o ? torna a prop opcional; o componente funciona com ou sem ela. '
    'Se um valor precisa mudar com o tempo, ele deve ser estado (useState), e não uma prop alterada pelo filho.',
    contexto=[
        p('Considere o componente Card abaixo.'),
        codigo('''
interface CardProps {
  titulo: string;
  children: React.ReactNode;
  footer?: React.ReactNode;
}

function Card({ titulo, children, footer }: CardProps) {
  return (
    <div className="card">
      <h3>{titulo}</h3>
      <div>{children}</div>
      {footer && <div className="rodape">{footer}</div>}
    </div>
  );
}
'''),
    ],
)

assercao(
    2, 'medio',
    'Em uma lista que pode ser reordenada, filtrada ou ter itens removidos, recomenda-se usar como key um identificador estável, como o id vindo do banco de dados, e não o índice do array.',
    'A key ajuda o React a identificar qual item mudou, foi adicionado ou foi removido durante a reconciliação.',
    0,
    'As duas são verdadeiras, e a II justifica a I. Se a key for o índice, ao remover ou reordenar itens os índices mudam, '
    'e o React passa a confundir um item com outro. Um id estável mantém cada item reconhecível entre as renderizações.',
)

multipla(
    2, 'medio',
    'Qual trecho JSX exibe corretamente "Maior de idade" ou "Menor de idade", conforme o valor de idade?',
    '<p>{idade >= 18 ? "Maior de idade" : "Menor de idade"}</p>',
    [
        '<p>{if (idade >= 18) "Maior de idade" else "Menor de idade"}</p>',
        '<p>{switch (idade >= 18) { case true: "Maior de idade" }}</p>',
        '<p>if (idade >= 18) {"Maior de idade"} else {"Menor de idade"}</p>',
        '<p>{for (idade >= 18) "Maior de idade"}</p>',
    ],
    'Dentro das chaves do JSX só cabem expressões, ou seja, algo que produz um valor. if, switch e for são comandos e não podem ficar ali. '
    'O operador ternário é uma expressão; por isso é a forma usada no JSX. Fora das chaves, o texto "if (...)" seria exibido literalmente.',
)

multipla(
    2, 'dificil',
    'Sobre a forma como o React atualiza a tela quando os dados mudam, assinale a alternativa correta.',
    'O React gera uma nova árvore no Virtual DOM, compara-a com a anterior (reconciliação) e altera no DOM real apenas os nós que mudaram.',
    [
        'O React apaga e recria todo o DOM real a cada mudança, o que garante que a tela fique sempre correta.',
        'O Virtual DOM é uma cópia da página guardada no servidor, que envia o HTML atualizado a cada mudança.',
        'O React altera o DOM real diretamente, sem comparação, assim que uma variável comum do componente muda.',
        'A reconciliação é a junção do código de vários componentes em um único arquivo durante o build.',
    ],
    'O Virtual DOM é uma cópia leve da árvore de elementos, mantida em memória no navegador. Quando o estado muda, o React '
    'monta a nova árvore, compara-a com a anterior e aplica no DOM real só as diferenças. Mudar uma variável comum não avisa o React de nada.',
)

multipla(
    2, 'dificil',
    'Ao escrever <Botao texto="Ok" variante="azul" />, o que acontece?',
    'O TypeScript aponta um erro antes da execução, porque "azul" não faz parte dos valores aceitos por variante.',
    [
        'O botão é exibido com o estilo padrão, porque valores desconhecidos são ignorados.',
        'O erro só aparece no navegador, quando o usuário clicar no botão.',
        'O TypeScript converte "azul" para "primary", o primeiro valor da lista.',
        'O código é aceito, porque "azul" é uma string, e variante espera uma string.',
    ],
    'O tipo "primary" | "secondary" | "danger" é uma união de valores literais: só essas três strings são aceitas. '
    'O TypeScript verifica isso no editor e na compilação, antes de o código rodar, e não converte valores automaticamente.',
    contexto=[
        p('Considere a definição do componente Botao, escrito em TypeScript.'),
        codigo('''
interface BotaoProps {
  texto: string;
  variante: "primary" | "secondary" | "danger";
}

function Botao({ texto, variante }: BotaoProps) {
  return <button className={`btn btn-${variante}`}>{texto}</button>;
}
'''),
    ],
)

afirmativas(
    2, 'dificil',
    [
        ('O arquivo src/main.tsx é o ponto de entrada: ele monta o React na página.', True),
        ('O arquivo index.html é a página HTML na qual o React é injetado.', True),
        ('O template react-ts configura o projeto com TypeScript desde o início.', True),
    ],
    'As três estão corretas. O index.html é a página que o navegador abre; o main.tsx é o ponto de entrada que monta o componente App '
    'dentro dela; e o template react-ts já traz o TypeScript configurado, permitindo tipar props e funções.',
    contexto=[
        p('Um projeto foi criado com o comando a seguir.'),
        codigo('$ npm create vite@latest meu-app -- --template react-ts'),
    ],
    intro='Sobre a estrutura do projeto criado, avalie as afirmativas a seguir.',
)

# =====================================================================================
# Módulo 3: React: Hooks e Estado
# =====================================================================================

multipla(
    3, 'facil',
    'Qual alternativa diferencia corretamente props e estado em um componente React?',
    'Props vêm do componente pai e são somente leitura; estado é um valor guardado e controlado pelo próprio componente, que pode mudar.',
    [
        'Props são criadas com useState; estado é recebido do componente pai.',
        'Props e estado são a mesma coisa, com nomes diferentes conforme a versão do React.',
        'Estado é somente leitura; props podem ser alteradas livremente pelo componente filho.',
        'Props só existem em componentes de classe; estado só existe em componentes de função.',
    ],
    'Props são como uma carta recebida pronta: vêm de fora e o filho não as altera. Estado é como um caderno de anotações: '
    'vive dentro do componente, só ele muda, e a mudança faz a tela ser redesenhada.',
)

multipla(
    3, 'facil',
    'O que a chamada useState(0) devolve?',
    'Um array com dois itens: o valor atual do estado e a função que o atualiza.',
    [
        'Apenas o valor inicial do estado, o número 0.',
        'Um objeto com as propriedades value e set.',
        'Uma Promise, que é resolvida quando o estado muda.',
        'Uma função que reinicia o componente com o valor 0.',
    ],
    'useState recebe o valor inicial e devolve [valor, função]. Por isso se escreve const [contagem, setContagem] = useState(0): '
    'contagem é o valor atual, e setContagem atualiza o estado e manda o React redesenhar a tela.',
)

multipla(
    3, 'facil',
    'Sobre Hooks e estado no React, assinale a alternativa INCORRETA.',
    'Alterar diretamente a variável de estado, como em contagem = contagem + 1, faz o React redesenhar o componente.',
    [
        'Todo Hook do React começa com o prefixo use.',
        'Chamar a função setter faz o React executar a função do componente de novo, com o novo valor.',
        'O useEffect é usado para efeitos colaterais, como mudar o título da aba do navegador.',
        'Um useEffect com o array de dependências vazio roda uma vez, quando o componente aparece na tela.',
    ],
    'Mudar a variável diretamente não avisa o React de nada, e a tela não muda. Só a função setter (setContagem, setNome...) dispara '
    'uma nova renderização. As demais afirmações estão corretas.',
)

multipla(
    3, 'medio',
    'Com o estado inicial abaixo, qual é o valor de dados depois de atualizarCampo("email", "novo@x.com")?',
    '{ email: "novo@x.com" }',
    [
        '{ nome: "Ana", email: "novo@x.com", mensagem: "" }',
        '{ nome: "Ana", email: "ana@x.com", mensagem: "" }',
        '{ nome: "Ana", email: "novo@x.com" }',
        'O React lança um erro, porque a propriedade nome deixou de existir.',
    ],
    'O setter substitui o estado inteiro pelo objeto recebido; o React não mistura objetos automaticamente. '
    'Como falta o spread, nome e mensagem se perdem. O certo é setDados({ ...dados, [campo]: valor }), que copia os campos e troca só o que mudou.',
    contexto=[
        p('Considere o trecho de um formulário controlado.'),
        codigo('''
const [dados, setDados] = useState({
  nome: "Ana",
  email: "ana@x.com",
  mensagem: "",
});

function atualizarCampo(campo, valor) {
  setDados({ [campo]: valor });
}
'''),
    ],
)

multipla(
    3, 'medio',
    'O estado contagem começa em 0. Depois de um clique no botão, qual valor aparece na tela?',
    '1',
    ['3', '0', '2', 'O React lança um erro por chamar o setter três vezes seguidas.'],
    'As três chamadas usam o mesmo valor de contagem daquela renderização (0), então cada uma pede setContagem(0 + 1). '
    'O resultado é 1. Para somar 3, é preciso a forma com função: setContagem((valorAtual) => valorAtual + 1), que recebe sempre o valor mais atualizado.',
    contexto=[
        p('Considere o componente abaixo.'),
        codigo('''
function Contador() {
  const [contagem, setContagem] = useState(0);

  function somarTres() {
    setContagem(contagem + 1);
    setContagem(contagem + 1);
    setContagem(contagem + 1);
  }

  return <button onClick={somarTres}>{contagem}</button>;
}
'''),
    ],
)

multipla(
    3, 'medio',
    'Um componente precisa buscar a lista de produtos de uma API apenas uma vez, quando aparece na tela pela primeira vez. Qual é a forma adequada?',
    'useEffect(() => { buscarProdutos(); }, []);',
    [
        'useEffect(() => { buscarProdutos(); });',
        'useEffect(() => { buscarProdutos(); }, [produtos]); com setProdutos chamado dentro de buscarProdutos.',
        'Chamar buscarProdutos() diretamente no corpo do componente, antes do return.',
        'const [produtos] = useState(buscarProdutos);',
    ],
    'O array de dependências vazio faz o efeito rodar só uma vez, quando o componente aparece. Sem array, o efeito roda depois de toda renderização. '
    'Com [produtos] e a atualização de produtos dentro do efeito, ele dispara de novo a cada busca, em repetição sem fim. '
    'Chamar a busca no corpo do componente a repete em toda renderização.',
)

assercao(
    3, 'medio',
    'Em um input controlado, o valor exibido no campo vem do estado do React, ligado à propriedade value.',
    'A cada digitação, o evento onChange atualiza o estado com e.target.value, e o React redesenha o campo com o novo valor.',
    0,
    'As duas são verdadeiras, e a II explica a I. É o ciclo do formulário controlado: o estado define o value, a digitação dispara o onChange, '
    'o onChange atualiza o estado, e o novo estado volta ao value. Assim, quem manda no conteúdo do campo é sempre o React.',
)

multipla(
    3, 'dificil',
    'O que acontece quando o componente acima aparece na tela?',
    'O efeito entra em repetição sem fim: ele altera itens, que está no array de dependências, e isso dispara o efeito de novo.',
    [
        'O efeito roda uma única vez e itens fica com um elemento.',
        'O efeito roda duas vezes e para, porque o React limita as repetições.',
        'O React lança um erro, porque não é permitido chamar o setter dentro de um useEffect.',
        'Nada acontece, porque itens começa vazio e o efeito não é executado.',
    ],
    'Na primeira renderização o efeito roda e cria um novo array. Como itens mudou e está no array de dependências, o efeito roda de novo, '
    'muda itens de novo, e assim por diante. Chamar o setter dentro de um efeito é permitido; o problema é a dependência alterada pelo próprio efeito.',
    contexto=[
        codigo('''
function Lista() {
  const [itens, setItens] = useState<string[]>([]);

  useEffect(() => {
    setItens([...itens, "novo item"]);
  }, [itens]);

  return <p>{itens.length} itens</p>;
}
'''),
    ],
)

afirmativas(
    3, 'dificil',
    [
        ('Um useEffect sem o array de dependências roda apenas uma vez, quando o componente aparece na tela.', False),
        ('Um useEffect com o array [contagem] roda quando o componente aparece e, depois, toda vez que contagem mudar.', True),
        ('Quando o novo valor depende do anterior, setContagem((valorAtual) => valorAtual + 1) é mais seguro do que setContagem(contagem + 1).', True),
    ],
    'I é falsa: sem array, o efeito roda depois de TODA renderização; quem roda uma vez só é o efeito com array vazio []. '
    'II é verdadeira: o efeito roda na primeira vez e sempre que uma dependência muda. '
    'III é verdadeira: a forma com função recebe o valor mais atualizado, mesmo com várias chamadas seguidas.',
    intro='Sobre os Hooks useEffect e useState, avalie as afirmativas a seguir.',
)

assercao(
    3, 'dificil',
    'Um Hook como useState pode ser chamado dentro de um if, desde que a condição seja verdadeira na primeira renderização.',
    'O React identifica cada Hook pela ordem em que ele é chamado em cada renderização do componente.',
    3,
    'A I é falsa: Hooks devem ser chamados sempre no nível mais alto do componente, nunca dentro de if, laços ou funções internas. '
    'A II é verdadeira e é justamente o motivo da regra: se a condição mudar, a ordem das chamadas muda, e o React associa o estado ao Hook errado.',
)

# =====================================================================================
# Módulo 4: Next.js: App Router e Roteamento
# =====================================================================================

multipla(
    4, 'facil',
    'Qual alternativa descreve corretamente a relação entre Next.js e React?',
    'O Next.js é um framework construído sobre o React que acrescenta roteamento por arquivos, renderização no servidor e rotas de API.',
    [
        'O Next.js substitui o React; componentes, props e Hooks deixam de ser usados.',
        'O Next.js é uma biblioteca de gerenciamento de estado que substitui o useState.',
        'O Next.js é um banco de dados para aplicações React.',
        'O Next.js é a versão antiga do React, anterior aos Hooks.',
    ],
    'Tudo o que se aprende de React continua valendo no Next.js. Ele acrescenta o que o React sozinho não tem: estrutura de projeto, '
    'roteamento baseado em pastas, renderização no servidor, API Routes e otimização de imagens, fontes e SEO.',
)

multipla(
    4, 'facil',
    'Em um projeto com App Router, o arquivo app/sobre/page.tsx corresponde a qual endereço?',
    '/sobre',
    ['/app/sobre', '/sobre/page', '/page/sobre', 'Nenhum, até que a rota seja registrada em um arquivo de configuração.'],
    'No App Router, cada pasta dentro de app/ vira um trecho da URL, e o arquivo page.tsx é o que aparece naquela rota. '
    'A pasta app não entra no endereço, o nome page também não, e não existe arquivo de configuração de rotas.',
)

multipla(
    4, 'facil',
    'Sobre o App Router e o Pages Router do Next.js, assinale a alternativa INCORRETA.',
    'No App Router, todo componente é Client Component por padrão e só vira Server Component com uma diretiva.',
    [
        'O App Router usa a pasta app/ e é o padrão dos projetos novos desde a versão 13.4.',
        'O App Router permite layouts aninhados, com um layout.tsx em cada pasta de rota.',
        'O Pages Router usa a pasta pages/ e um layout único definido em _app.js.',
        'No Pages Router não existem Server Components: o código de todos os componentes vai para o navegador.',
    ],
    'No App Router, todo componente dentro de app/ é Server Component por padrão; só vira Client Component com a diretiva "use client". '
    'É no Pages Router que o código de todos os componentes vai para o navegador. As demais afirmações estão corretas.',
)

multipla(
    4, 'medio',
    'Qual endereço passa a exibir essa página?',
    '/blog/projetos',
    ['/projetos', '/blog', 'Os dois endereços, /projetos e /blog/projetos.', 'Nenhum: o Next.js mostra um erro de rota duplicada.'],
    'A estrutura de pastas define a URL: como projetos/ ficou dentro de blog/, o endereço vira /blog/projetos. '
    'Para ter /projetos, a pasta precisa ficar diretamente dentro de app/, ao lado de blog/.',
    contexto=[p('Ao criar a página de projetos do portfólio, um estudante criou por engano a pasta projetos dentro da pasta blog, '
                'ficando com o arquivo app/blog/projetos/page.tsx.')],
)

multipla(
    4, 'medio',
    'O que acontece ao acessar o endereço /contato?',
    'A rota não é reconhecida, porque o App Router só transforma em página o arquivo chamado page (page.tsx, page.jsx ou page.js).',
    [
        'A página é exibida normalmente, porque index.tsx é o nome padrão de página em qualquer ferramenta.',
        'O Next.js renomeia automaticamente o arquivo para page.tsx na primeira execução.',
        'A página só é exibida depois de registrada em um arquivo de rotas.',
        'A página funciona apenas no servidor de produção, depois do npm run build.',
    ],
    'No App Router, só uma pasta com um arquivo chamado literalmente page vira URL. Nomes como index.tsx, comuns em outras ferramentas, '
    'não são reconhecidos, e o endereço responde com a página de erro 404.',
    contexto=[p('Uma desenvolvedora criou a pasta app/contato/ e, dentro dela, o arquivo index.tsx com o conteúdo da página de contato.')],
)

assercao(
    4, 'medio',
    'Em uma aplicação Next.js, recomenda-se usar o componente Link, de next/link, em vez da tag <a> para navegar entre as páginas internas.',
    'A tag <a> comum recarrega a página inteira a cada clique, perdendo o estado do React, enquanto o Link troca apenas o conteúdo necessário.',
    0,
    'As duas são verdadeiras, e a II justifica a I. O Link mantém a navegação instantânea, típica de uma aplicação de página única (SPA), '
    'sem recarregar a página e sem perder o estado dos componentes.',
)

afirmativas(
    4, 'medio',
    [
        ('O layout.tsx da raiz define as tags <html> e <body> e envolve todas as páginas da aplicação.', True),
        ('Só pode existir um arquivo layout.tsx em todo o projeto: o da raiz.', False),
        ('As pastas de rota devem ficar uma dentro da outra, como app/sobre/projetos/, para gerar os endereços /sobre e /projetos.', False),
    ],
    'I é verdadeira. II é falsa: cada pasta de rota pode ter o seu layout.tsx, que envolve só as páginas daquela seção (layouts aninhados). '
    'III é falsa: pastas uma dentro da outra geram endereços aninhados (app/sobre/projetos/ vira /sobre/projetos); '
    'para /sobre e /projetos, as duas pastas ficam lado a lado dentro de app/.',
    intro='Sobre a estrutura de um projeto Next.js com App Router, avalie as afirmativas a seguir.',
)

multipla(
    4, 'dificil',
    'Quais endereços são atendidos por essa página?',
    'Endereços como /blog/primeiro-post e /blog/novidades, em que o último trecho da URL é variável.',
    [
        'Apenas o endereço literal /blog/[slug].',
        'Apenas o endereço /slug.',
        'Apenas o endereço /blog.',
        'Qualquer endereço com vários níveis após /blog, como /blog/2025/03/post.',
    ],
    'Uma pasta com o nome entre colchetes cria um segmento dinâmico: [slug] aceita qualquer valor naquele trecho da URL, e a página recebe esse valor. '
    'Ela atende um nível só; para vários níveis seria preciso outra convenção. O endereço /blog é atendido pelo page.tsx da pasta blog, se existir.',
    contexto=[p('Em um projeto com App Router, existe o arquivo app/blog/[slug]/page.tsx.')],
)

multipla(
    4, 'dificil',
    'Comparando um projeto React criado com o Vite e um projeto Next.js com App Router, assinale a alternativa correta.',
    'O projeto do Vite tem uma única página (index.html) que carrega o App.tsx; no Next.js, cada pasta com page.tsx vira um endereço próprio.',
    [
        'Os dois projetos criam automaticamente uma página para cada componente da pasta src/.',
        'O projeto do Vite já tem endereços como /projetos e /contato, criados pelos nomes dos componentes.',
        'No Next.js, todas as páginas ficam empilhadas dentro de um único App.tsx, como no Vite.',
        'O Vite roda tudo no servidor, enquanto o Next.js roda tudo no navegador.',
    ],
    'Um projeto React "puro" com Vite é uma única página que carrega um único componente; não há endereços separados. '
    'O Next.js resolve isso com o roteamento por pastas e ainda oferece renderização no servidor, o que o Vite sozinho não faz.',
)

multipla(
    4, 'dificil',
    'Considerando o funcionamento dos layouts aninhados, assinale a alternativa correta.',
    'A página /sobre é envolvida apenas pelo layout da raiz, e a página /blog/primeiro-post é envolvida pelo layout da raiz e pelo layout do blog.',
    [
        'O menu lateral do blog também aparece na página /sobre, porque todo layout vale para o site inteiro.',
        'A página /blog/primeiro-post é envolvida só pelo layout do blog, que substitui o layout da raiz.',
        'O layout do blog precisa repetir as tags <html> e <body>, senão as páginas do blog ficam sem elas.',
        'Cada page.tsx precisa importar o layout da sua pasta para que ele seja aplicado.',
    ],
    'Os layouts se acumulam do mais externo para o mais interno: a raiz envolve tudo, e o layout do blog envolve só o que está dentro de app/blog/. '
    'As tags <html> e <body> ficam só no layout da raiz, e o Next.js aplica os layouts sozinho, sem importação nas páginas.',
    contexto=[
        p('Um site tem a estrutura de pastas abaixo. O layout do blog acrescenta um menu lateral.'),
        codigo('''
app/
  layout.tsx          <- layout da raiz
  sobre/
    page.tsx
  blog/
    layout.tsx        <- menu lateral do blog
    [slug]/
      page.tsx
'''),
    ],
)

# =====================================================================================
# Módulo 5: Server e Client Components
# =====================================================================================

multipla(
    5, 'facil',
    'No App Router do Next.js, um componente criado dentro da pasta app/ sem nenhuma diretiva é',
    'um Server Component: renderizado no servidor, envia ao navegador só o HTML, sem o JavaScript do componente.',
    [
        'um Client Component: renderizado no navegador, como em um projeto React com Vite.',
        'um componente híbrido, que decide sozinho onde rodar conforme a velocidade da conexão.',
        'um componente estático, que não pode receber props.',
        'um componente inválido, porque toda página precisa declarar "use server" ou "use client".',
    ],
    'No App Router, todo componente dentro de app/ é Server Component por padrão. Ele vira HTML no servidor, e o código dele não vai para o navegador. '
    'Para rodar no navegador, o arquivo precisa da diretiva "use client".',
)

multipla(
    5, 'facil',
    'Em uma página de notícias feita com Next.js, qual componente precisa ser um Client Component?',
    'Um botão de curtir que guarda com useState se a notícia foi curtida.',
    [
        'A página que busca as notícias com await e as lista na tela.',
        'Um rodapé fixo com o nome do site e os links das redes sociais.',
        'Um título que apenas exibe o texto recebido por props.',
        'Um componente que consulta o banco de dados para contar as notícias publicadas.',
    ],
    'Estado (useState), efeitos (useEffect) e eventos (onClick, onChange) só funcionam no navegador, em Client Components. '
    'Buscar dados e apenas exibir informação são tarefas de Server Components, o padrão.',
)

multipla(
    5, 'facil',
    'Sobre os Server Components do Next.js, assinale a alternativa INCORRETA.',
    'Podem usar useState e useEffect diretamente, sem nenhuma diretiva.',
    [
        'Reduzem o JavaScript enviado ao navegador, porque o código deles não vai para o cliente.',
        'Podem buscar dados direto de um banco de dados, sem precisar de uma API intermediária.',
        'Deixam o carregamento mais rápido, porque o HTML já chega pronto ao navegador.',
        'Podem ser funções assíncronas e usar await dentro do componente.',
    ],
    'Um Server Component nunca chega a existir no navegador; ele já virou HTML antes de sair do servidor. Por isso não tem como guardar estado '
    'nem reagir a cliques: useState e useEffect exigem "use client". As demais afirmações são vantagens reais dos Server Components.',
)

multipla(
    5, 'medio',
    'O que acontece ao abrir a página?',
    'O Next.js trata Contador como Server Component e o uso do useState provoca erro; é preciso colocar "use client" no topo de Contador.tsx.',
    [
        'O contador funciona normalmente, porque todo componente importado por uma página vira Client Component.',
        'O contador aparece, mas fica sempre em 0, sem nenhum erro.',
        'O Next.js acrescenta "use client" sozinho ao perceber o useState.',
        'Basta transformar Contador em função async para o useState funcionar.',
    ],
    'Sem a diretiva, o componente é tratado como Server Component, e Hooks como useState só existem no navegador. '
    'A solução é a primeira linha "use client"; no Next.js isso não é automático, e async não resolve.',
    contexto=[
        p('Considere os dois arquivos de um projeto Next.js com App Router.'),
        codigo('''
// components/Contador.tsx
import { useState } from "react";

export default function Contador() {
  const [contagem, setContagem] = useState(0);
  return (
    <button onClick={() => setContagem(contagem + 1)}>
      Cliquei {contagem} vezes
    </button>
  );
}

// app/page.tsx
import Contador from "@/components/Contador";

export default function Inicio() {
  return <Contador />;
}
'''),
    ],
)

assercao(
    5, 'medio',
    'Colocar "use client" no topo do page.tsx "só para garantir" é uma boa prática no App Router.',
    'A diretiva "use client" no page.tsx transforma a página inteira em Client Component, que perde a vantagem de buscar dados direto no servidor.',
    3,
    'A I é falsa e a II é verdadeira. A boa prática é usar "use client" só nos componentes que realmente precisam de interatividade, '
    'o mais "embaixo" possível na árvore. Na página inteira, ela manda mais JavaScript ao navegador e perde o acesso direto aos dados no servidor.',
)

afirmativas(
    5, 'medio',
    [
        ('Um Server Component pode importar e renderizar um Client Component.', True),
        ('Um Client Component pode importar diretamente um Server Component.', False),
        ('Para que um Client Component exiba conteúdo gerado no servidor, esse conteúdo pode ser passado a ele pela prop children.', True),
    ],
    'I é verdadeira: é o padrão mais comum, com a página (Server) buscando os dados e renderizando componentes interativos (Client). '
    'II é falsa: o caminho inverso não é permitido diretamente. III é verdadeira: passar o conteúdo por children (props) é a forma de contornar essa restrição.',
    intro='Sobre a combinação de Server Components e Client Components, avalie as afirmativas a seguir.',
)

multipla(
    5, 'medio',
    'Sobre o componente acima, assinale a alternativa correta.',
    'É válido como Server Component: no servidor, o componente pode ser assíncrono e usar await diretamente.',
    [
        'É inválido, porque componentes React nunca podem ser funções async.',
        'Só funciona se o arquivo tiver "use client" no topo, porque o await roda no navegador.',
        'Só funciona se a busca for colocada dentro de um useEffect.',
        'É válido apenas dentro de API Routes, e não em arquivos page.tsx.',
    ],
    'A possibilidade de ser async é exclusiva dos Server Components: o componente espera os dados no servidor e devolve o HTML já pronto. '
    'Em componentes que rodam no navegador (os dos módulos de React e os Client Components), isso não é permitido.',
    contexto=[
        codigo('''
// app/projetos/page.tsx
export default async function Projetos() {
  const projetos = await buscarProjetos();

  return (
    <ul>
      {projetos.map((p) => (
        <li key={p.id}>{p.titulo}</li>
      ))}
    </ul>
  );
}
'''),
    ],
)

multipla(
    5, 'dificil',
    'Qual classificação segue a regra de decisão entre Server e Client Components?',
    '1 e 4 como Server Components; 2 e 3 como Client Components.',
    [
        '1 e 2 como Server Components; 3 e 4 como Client Components.',
        'Todos como Client Components, para que a página fique interativa.',
        'Todos como Server Components, pois a página está dentro de app/.',
        '2 e 4 como Server Components; 1 e 3 como Client Components.',
    ],
    'Buscar dados (1) e só exibir informação recebida por props (4) ficam no servidor, o padrão. '
    'O filtro que reage à digitação (2) usa estado e onChange, e o botão do modal (3) usa onClick e estado; os dois precisam de "use client".',
    contexto=[p('Uma página de painel administrativo terá quatro partes: (1) a lista de pedidos, lida de uma consulta ao banco de dados; '
                '(2) um campo de busca que filtra os pedidos enquanto o usuário digita; (3) um botão que abre uma janela de detalhes; '
                '(4) um cabeçalho que apenas exibe o título recebido por props.')],
)

assercao(
    5, 'dificil',
    'Colocar a diretiva "use client" o mais "embaixo" possível na árvore de componentes reduz o JavaScript enviado ao navegador.',
    'O código dos Server Components não é enviado ao cliente; só os Client Components precisam ter o seu JavaScript carregado no navegador.',
    0,
    'As duas são verdadeiras, e a II explica a I. Quanto menos componentes forem Client, menos código vai para o navegador. '
    'Por isso a página e as partes que só exibem dados ficam no servidor, e só os pedaços interativos (um botão, um campo) recebem "use client".',
)

afirmativas(
    5, 'dificil',
    [
        ('Um Server Component nunca chega a existir no navegador e, por isso, não reage a cliques nem a digitação.', True),
        ('Um Server Component pode buscar dados em um banco de dados sem precisar de uma API intermediária.', True),
        ('Quando um Server Component passa dados a um Client Component por props, o Client Component precisa saber de onde esses dados vieram.', False),
    ],
    'I e II são verdadeiras: o Server Component vira HTML no servidor, onde pode acessar dados diretamente. '
    'III é falsa: o Client Component só recebe os dados prontos por props e cuida da parte interativa, sem precisar saber de onde vieram.',
    contexto=[p('Na página de projetos de um portfólio, o componente Projetos (Server) busca a lista de projetos e, para cada um, '
                'renderiza um BotaoFavoritar (Client), passando o id do projeto por props.')],
)


# =====================================================================================

def validar():
    erros = []
    ids = set()
    for q in questoes:
        if q['id'] in ids:
            erros.append(f'{q["id"]}: id repetido')
        ids.add(q['id'])
        if len(q['alternativas']) != 5:
            erros.append(f'{q["id"]}: {len(q["alternativas"])} alternativas')
        if len(set(q['alternativas'])) != len(q['alternativas']):
            erros.append(f'{q["id"]}: alternativas repetidas')
        texto = json.dumps(q, ensure_ascii=False).lower()
        for palavra in PROIBIDAS:
            if palavra in texto:
                erros.append(f'{q["id"]}: contém "{palavra}"')
    por_cap = {}
    for q in questoes:
        por_cap.setdefault(q['capituloId'], []).append(q['nivel'])
    for cap, niveis in sorted(por_cap.items()):
        if len(niveis) != 10:
            erros.append(f'{cap}: {len(niveis)} questões (esperado 10)')
    return erros, por_cap


def main():
    erros, por_cap = validar()
    if erros:
        print('\n'.join(erros))
        sys.exit(1)
    existentes = json.loads(ARQUIVO.read_text(encoding='utf-8'))
    praticas = [q for q in existentes if q['tipo'] != 'objetiva']
    ARQUIVO.write_text(json.dumps(praticas + questoes, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for cap, niveis in sorted(por_cap.items()):
        print(cap, {n: niveis.count(n) for n in ('facil', 'medio', 'dificil')})
    print(f'{len(questoes)} objetivas + {len(praticas)} práticas gravadas em {ARQUIVO.name}')


if __name__ == '__main__':
    main()
