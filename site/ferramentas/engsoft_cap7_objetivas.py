"""
Questões médias e difíceis do capítulo 7 (Gestão da Configuração de Software) de Engenharia de
Software e da Usabilidade: 10 objetivas no estilo de concursos públicos e exames nacionais e
2 discursivas com um único comando. As funções comuns ficam em engsoft_questoes.py.
Uso (dentro de site/):

    python ferramentas/engsoft_cap7_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap7-o* e
engsoft-cap7-d*; as que já existiam (engsoft-cap7-m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import Banco, codigo, p

banco = Banco('engsoft-cap7')


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Considerando os tipos de sistema de controle de versão, a análise correta da situação é:',
    'Com o Git, um sistema distribuído, cada desenvolvedor tem o repositório completo e pode fazer commit e ver o '
    'histórico sem conexão, enviando tudo quando a rede voltar.',
    [
        'Com o Git, a equipe também ficaria sem registrar versões, pois todo commit precisa ser gravado no servidor '
        'central no momento em que é feito.',
        'O problema seria resolvido mantendo o SVN e pedindo que cada desenvolvedor faça um backup diário da sua pasta '
        'de trabalho, o que equivale a ter um repositório local.',
        'Com o Git, só seria possível trabalhar sem conexão em uma única branch, pois criar e trocar de branch exige '
        'acesso ao repositório remoto.',
        'O SVN e o Git funcionam da mesma forma sem conexão; a diferença entre eles está apenas na interface usada '
        'pelos desenvolvedores.',
    ],
    'O SVN é centralizado: há um único servidor, e operações como commit e consulta ao histórico exigem conexão com ele. '
    'O Git é distribuído: cada desenvolvedor tem uma cópia completa do repositório, com todo o histórico, e commit, log '
    'e diff são operações locais, assim como criar branches. Sem rede, a equipe continua versionando e sincroniza com '
    'push quando a conexão voltar. Uma pasta copiada como backup não tem histórico, commits nem branches.',
    contexto=[p('Uma equipe desenvolve o sistema de manutenção de uma plataforma de petróleo e passa vários dias seguidos '
                'em alto-mar, sem acesso à internet. Ela usa o SVN, e o servidor fica na sede da empresa. Durante os '
                'embarques, os desenvolvedores não conseguem registrar versões nem consultar o histórico, e acumulam '
                'mudanças sem nenhum controle até voltar a terra.')],
)

banco.afirmativas(
    'medio',
    [
        ('A verificação 1 é uma Auditoria Funcional de Configuração (FCA), que responde à pergunta "o que foi prometido '
         'foi entregue?".', True),
        ('A verificação 2 é uma Auditoria Física de Configuração (PCA), um inventário completo do produto a ser entregue.',
         True),
        ('A verificação 2 pode revelar, por exemplo, que o script de atualização do banco de dados não foi incluído no '
         'pacote, mesmo que todos os requisitos estejam implementados.', True),
    ],
    'As três estão corretas. A FCA confere o software com a baseline de requisitos: cada requisito prometido precisa '
    'estar implementado. A PCA confere os artefatos: se tudo o que compõe o produto está presente, completo e '
    'corretamente identificado. As duas se completam: um sistema pode implementar todos os requisitos e, mesmo assim, '
    'ser entregue sem um artefato necessário, como o script do banco, o que só a PCA revela.',
    contexto=[p('Antes de entregar a versão final de um sistema a um órgão público, a equipe fez duas verificações: '
                '(1) conferiu, um a um, se cada requisito da baseline de requisitos aprovada está implementado no '
                'software; (2) conferiu se todos os artefatos da entrega (executáveis, scripts do banco de dados, '
                'manual de instalação e arquivos de configuração) estão presentes e identificados com a versão correta.')],
)

banco.multipla(
    'medio',
    'Seguindo o padrão Conventional Commits, os tipos mais adequados para as mensagens dos commits 1, 2, 3 e 4 são, '
    'respectivamente,',
    'feat, fix, docs e refactor.',
    [
        'fix, feat, docs e chore.',
        'feat, fix, chore e test.',
        'refactor, fix, docs e feat.',
        'feat, refactor, docs e fix.',
    ],
    'feat marca uma funcionalidade nova (o filtro por categoria); fix, uma correção (o cálculo de frete); docs, uma '
    'mudança só na documentação (o README); refactor, uma reorganização do código sem mudar o comportamento. '
    'test seria usado para commits que só tratam de testes, e chore, para tarefas de manutenção, como atualizar '
    'dependências.',
    contexto=[p('Uma desenvolvedora fez quatro commits em um dia: (1) incluiu um filtro por categoria na página de produtos; '
                '(2) corrigiu o cálculo do frete, que somava a taxa duas vezes; (3) atualizou o README com as instruções '
                'de instalação; (4) dividiu uma função longa em três funções menores, sem alterar o que ela faz.')],
)

banco.assercao(
    'medio',
    'Para marcar a versão 2.1.0 que foi para produção, a equipe deveria ter usado uma tag, e não uma branch.',
    'A tag é um marcador imutável em um commit, enquanto a branch é uma linha de desenvolvimento que continua '
    'avançando a cada novo commit.',
    0,
    'As duas são verdadeiras, e a II explica a I. A branch "versao-2.1.0" continuou recebendo commits e deixou de '
    'apontar para o que estava em produção. A tag v2.1.0 ficaria presa ao commit exato da release, servindo como '
    'ponto de referência estável para reproduzir ou voltar àquela versão.',
    contexto=[p('Depois de publicar a versão 2.1.0, um desenvolvedor criou uma branch chamada "versao-2.1.0" para marcar '
                'o que foi para produção. Semanas depois, outros colegas fizeram commits nessa branch, e ninguém mais '
                'sabe dizer exatamente qual código estava em produção na versão 2.1.0.')],
)

banco.multipla(
    'medio',
    'Os momentos 1, 2, 3 e 4 correspondem, respectivamente, às baselines de',
    'requisitos, release, produção e arquitetura.',
    [
        'requisitos, produção, release e arquitetura.',
        'arquitetura, release, produção e requisitos.',
        'requisitos, release, arquitetura e produção.',
        'release, requisitos, produção e arquitetura.',
    ],
    'A baseline de requisitos é aprovada no fim do levantamento, com o SRS e as histórias priorizadas (1). '
    'A de release é formada antes de cada implantação, com código, executáveis e scripts do banco (2). '
    'A de produção registra, após cada deploy bem-sucedido, a versão exata de tudo o que está em produção (3). '
    'A de arquitetura é aprovada junto com o design, com os documentos e diagramas (4).',
    contexto=[p('Em um projeto, a equipe registrou quatro baselines: '
                '(1) no fim do levantamento, o documento de requisitos aprovado e as histórias priorizadas; '
                '(2) antes de implantar, o código-fonte, os executáveis e os scripts do banco de dados da versão; '
                '(3) logo após um deploy bem-sucedido, a versão exata de tudo o que passou a rodar em produção; '
                '(4) após a aprovação do design, os documentos de arquitetura e os diagramas.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Seguindo o Versionamento Semântico, o número da nova versão deve ser',
    '4.0.0.',
    [
        '3.8.0.',
        '3.8.3.',
        '4.8.3.',
        '4.1.2.',
    ],
    'Quando uma release junta mudanças de vários tipos, vale a mais forte. Renomear uma função pública e remover o nome '
    'antigo quebra o código de quem usa a biblioteca: é uma mudança incompatível, que exige subir o MAJOR. '
    'Ao subir o MAJOR, MINOR e PATCH voltam a zero, por isso a versão é 4.0.0, e não a soma das mudanças. '
    'A 3.8.0 trataria a release como se tivesse só uma novidade retrocompatível, ignorando a quebra.',
    contexto=[p('Uma biblioteca de pagamentos está na versão 3.7.2. A próxima release reúne três mudanças: a correção de '
                'dois defeitos, uma função nova para parcelamento e a troca do nome da função pública pagar() para '
                'processar_pagamento(), com a remoção do nome antigo.')],
)

banco.afirmativas(
    'dificil',
    [
        ('A correção deve ser feita em uma branch criada a partir da develop, que é a branch de integração do projeto.',
         False),
        ('Depois de pronta, a correção deve ser integrada à main e também à develop, para que o defeito não volte na '
         'próxima versão.', True),
        ('Pelo Versionamento Semântico, a versão publicada com a correção deve ser a 5.3.0.', False),
        ('A versão corrigida que for para produção deve ser marcada com uma tag, como v5.2.1.', True),
    ],
    'I é falsa: a develop já tem funcionalidades incompletas da 5.3; partir dela levaria esse código para produção. '
    'No Git Flow, a correção urgente é feita em uma branch hotfix/* criada a partir da main. II é verdadeira: a '
    'correção volta para a main (produção) e para a develop, senão a próxima versão traria o defeito de novo. '
    'III é falsa: é uma correção retrocompatível, que sobe só o PATCH: 5.2.1. IV é verdadeira: a tag marca de forma '
    'imutável o commit da versão publicada.',
    contexto=[p('Uma empresa usa Git Flow. A versão 5.2.0 está em produção, e a branch develop já reúne várias '
                'funcionalidades da futura versão 5.3, ainda incompletas. Os clientes relatam um defeito grave no '
                'cálculo de impostos da versão em produção, que precisa ser corrigido hoje.')],
)

banco.assercao(
    'dificil',
    'Com feature flags, a equipe pode integrar na branch principal o código de uma funcionalidade ainda incompleta, '
    'sem que ela apareça para os usuários.',
    'O Trunk-Based Development exige times com alta maturidade em CI/CD.',
    1,
    'As duas são verdadeiras, mas a II não explica a I. A I é verdadeira porque a feature flag controla a visibilidade: '
    'o código entra na main desligado e só é ativado quando estiver pronto. A II também é verdadeira: integrar várias '
    'vezes ao dia só funciona com testes automatizados e pipeline confiáveis. Mas a maturidade em CI/CD não é o '
    'motivo de o código incompleto ficar invisível; quem garante isso é a própria flag.',
    contexto=[p('Uma equipe vai adotar o Trunk-Based Development: todos passarão a integrar commits pequenos na branch '
                'principal várias vezes ao dia. Um desenvolvedor pergunta como fica uma funcionalidade grande, que vai '
                'levar três semanas para ficar pronta.')],
)

banco.multipla(
    'dificil',
    'A análise correta da matriz de rastreabilidade é:',
    'A rastreabilidade forward mostra que o RF03 foi implementado, mas não testado, e que o RF04 não foi implementado; '
    'a versão não passaria na FCA.',
    [
        'Como o RF03 já tem código, ele pode ser considerado concluído, e só o RF04 impede a entrega.',
        'A matriz não indica problemas, pois a rastreabilidade serve apenas para encontrar a origem de defeitos '
        'em produção.',
        'A rastreabilidade backward mostra que o RF04 não foi implementado, pois ela parte dos requisitos em direção '
        'ao código e aos testes.',
        'Os problemas do RF03 e do RF04 só seriam encontrados em uma Auditoria Física (PCA), que confere se os '
        'requisitos foram implementados.',
    ],
    'A rastreabilidade forward segue o caminho Requisito → Design → Código → Teste e mostra se cada requisito foi '
    'implementado e testado. Na matriz, o RF03 para no código (sem teste) e o RF04 não passou nem do requisito. '
    'A backward faz o caminho contrário, do código ou do defeito até o requisito de origem. Conferir se o que foi '
    'prometido foi entregue é papel da FCA; a PCA confere os artefatos do produto.',
    contexto=[
        p('Na véspera de uma entrega, a equipe consultou a matriz de rastreabilidade do projeto:'),
        codigo('''
Requisito  Design  Código  Teste
RF01       sim     sim     sim
RF02       sim     sim     sim
RF03       sim     sim     não
RF04       não     não     não
'''),
    ],
)

banco.multipla(
    'dificil',
    'Sobre o controle de mudanças nessa situação, assinale a alternativa INCORRETA.',
    'Na equipe ágil, como não existe CCB, as mudanças nos itens de configuração podem ser feitas sem registro nem '
    'avaliação, se passarem nos testes.',
    [
        'Na equipe ágil, o backlog priorizado pela Product Owner cumpre o papel de controle de mudanças, de forma mais '
        'leve, mas com a mesma essência.',
        'A análise de impacto vem antes da aprovação, para que quem decide conheça os efeitos da mudança antes de '
        'autorizá-la.',
        'O Dockerfile e o pipeline de CI/CD são itens de configuração e, por isso, também devem passar pelo controle '
        'de mudanças.',
        'Depois de implementada, a mudança passa por revisão, com code review e testes, antes de ir para produção.',
    ],
    'A afirmação incorreta é a da equipe ágil: nenhuma mudança em item de configuração controlado deve acontecer sem '
    'ser registrada, avaliada e autorizada. Em ambientes ágeis, quem faz esse papel é o backlog priorizado pela PO. '
    'Passar nos testes é só uma das etapas do fluxo. As demais alternativas descrevem corretamente a ordem do fluxo '
    '(solicitação, análise de impacto, aprovação, implementação, revisão, deploy e fechamento) e o alcance dos itens '
    'de configuração, que vão além do código.',
    contexto=[p('Uma empresa tem duas equipes. A que mantém o sistema de um órgão público usa um Change Control Board '
                '(CCB), que se reúne toda semana para avaliar as solicitações de mudança. A que desenvolve o aplicativo '
                'da própria empresa trabalha com Scrum e não tem CCB.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"Configuration management is the art of identifying, organizing, and controlling modifications to '
                   'the software being built by a programming team."',
        'traducao': '(Tradução livre: "Gestão da configuração é a arte de identificar, organizar e controlar as '
                    'modificações no software que está sendo construído por uma equipe de programação.")',
        'fonte': 'BABICH, W. A. Software Configuration Management: Coordination for Team Productivity. '
                 'Boston: Addison-Wesley, 1986.',
    },
    [
        'Em uma sexta-feira à noite, o pagamento de uma loja virtual parou de funcionar. Na investigação, a equipe '
        'descobriu que, durante a semana, um desenvolvedor havia corrigido um arquivo direto no servidor, por FTP, e '
        'que a equipe de infraestrutura havia alterado à mão uma configuração do servidor. Nada disso foi registrado.',
        'Como não havia marcação das versões publicadas nem registro do que estava em produção, a equipe levou dois '
        'dias para descobrir o que tinha mudado e colocar a loja de volta no ar.',
    ],
    'Com base no texto e no caso apresentado, explique quais práticas de Gestão da Configuração teriam evitado o '
    'problema ou reduzido o tempo de recuperação da loja.',
    'A loja ficou sem as três ações citadas no texto: identificar, organizar e controlar as modificações. Primeiro, '
    'faltou tratar como itens de configuração não só o código, mas também a configuração do servidor, versionando '
    'tudo no Git; assim, cada mudança teria um commit com autor, data e motivo. Segundo, nenhuma mudança deveria ir '
    'direto ao servidor: pelo fluxo de controle de mudanças, ela seria solicitada, teria o impacto analisado, seria '
    'aprovada, revisada com code review e testes, e só então publicada pelo pipeline. Terceiro, cada versão publicada '
    'deveria ter uma tag e uma baseline de produção, registrando a versão exata de tudo o que estava no ar. Com isso, '
    'a equipe compararia a versão atual com a anterior em minutos, encontraria a mudança que causou a falha e '
    'voltaria para a última baseline estável, em vez de levar dois dias.',
)

banco.discursiva(
    'dificil',
    {
        'citacao': '"Continuous Integration is a software development practice where members of a team integrate their '
                   'work frequently, usually each person integrates at least daily - leading to multiple integrations '
                   'per day."',
        'traducao': '(Tradução livre: "Integração Contínua é uma prática de desenvolvimento de software em que os '
                    'membros de uma equipe integram o seu trabalho com frequência; normalmente, cada pessoa integra '
                    'pelo menos uma vez por dia, o que leva a várias integrações por dia.")',
        'fonte': 'FOWLER, M. Continuous Integration. 2006. Disponível em: martinfowler.com.',
    },
    [
        'Uma equipe de seis desenvolvedores mantém um sistema on-line de agendamento e usa Git Flow. Cada funcionalidade '
        'é desenvolvida em uma branch feature/* que dura de quatro a seis semanas. Na hora de integrar, os conflitos '
        'são enormes, e a equipe chega a gastar dias inteiros resolvendo merges. Há uma única versão em produção, e as '
        'publicações acontecem a cada dois meses.',
        'A diretoria quer passar a publicar novidades toda semana.',
    ],
    'Com base no texto de Fowler e no caso apresentado, analise a estratégia de branching atual da equipe e proponha '
    'uma estratégia mais adequada ao novo objetivo, justificando a sua escolha.',
    'O problema está na duração das branches, e não no Git. Ficando de quatro a seis semanas separadas, as branches se '
    'afastam muito da principal, e os conflitos se acumulam até a hora do merge. É o contrário do que Fowler descreve: '
    'integrar pouco e tarde, em vez de pelo menos uma vez por dia. Além disso, o Git Flow é indicado para releases '
    'planejadas e para várias versões em produção ao mesmo tempo, o que não é o caso dessa equipe, que tem uma versão '
    'só. Para publicar toda semana, a estratégia mais adequada é o GitHub Flow: a main fica sempre pronta para '
    'implantação, e as branches de feature duram poucos dias e são integradas por Pull Request, com revisão e testes '
    'automatizados no pipeline. Com a equipe mais madura em CI/CD, ela pode evoluir para o Trunk-Based Development, '
    'integrando várias vezes ao dia e usando feature flags para esconder as funcionalidades incompletas. Em qualquer '
    'dos dois casos, a integração frequente só é segura com testes automatizados rodando a cada commit.',
)


if __name__ == '__main__':
    banco.gravar()
