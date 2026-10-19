"""
Questões médias e difíceis do capítulo 12 (Segurança para Desenvolvimento de Software) de
Engenharia de Software e da Usabilidade: 10 objetivas no estilo de concursos públicos e exames
nacionais e 2 discursivas com um único comando. As funções comuns ficam em engsoft_questoes.py.
Uso (dentro de site/):

    python ferramentas/engsoft_cap12_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap12-o* e
engsoft-cap12-d*; as que já existiam (engsoft-cap12-m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import Banco, codigo, p

banco = Banco('engsoft-cap12')


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As ferramentas de segurança que atuam nas etapas 1, 2, 3 e 4 são, respectivamente,',
    'SAST, SCA, DAST e IaC Security Scan.',
    [
        'DAST, SCA, SAST e IaC Security Scan.',
        'SAST, DAST, SCA e Secrets Detection.',
        'SCA, SAST, DAST e IaC Security Scan.',
        'SAST, SCA, IaC Security Scan e DAST.',
    ],
    'Analisar o código-fonte sem executá-lo, a cada commit, é o SAST (1). Encontrar vulnerabilidades em bibliotecas de '
    'terceiros, no build, é o SCA (2). Testar a aplicação em execução, simulando ataques contra o ambiente de staging, '
    'é o DAST (3). Verificar configurações inseguras em arquivos do Terraform, do Docker ou do Kubernetes é o IaC '
    'Security Scan (4). O Secrets Detection procura credenciais e chaves commitadas por engano.',
    contexto=[p('O pipeline de uma empresa tem quatro verificações de segurança: '
                '(1) a cada commit, uma ferramenta analisa o código-fonte, sem executá-lo, em busca de padrões '
                'inseguros; '
                '(2) no build, outra ferramenta aponta que uma biblioteca usada pelo projeto tem uma vulnerabilidade '
                'conhecida; '
                '(3) na fase de testes, uma ferramenta envia requisições maliciosas à aplicação rodando em staging; '
                '(4) antes do deploy, uma ferramenta avisa que um arquivo do Terraform deixa um repositório de arquivos '
                'aberto para a internet.')],
)

banco.afirmativas(
    'medio',
    [
        ('Automatizar as verificações de segurança no pipeline, a cada commit, está ligado ao pilar Automation.', True),
        ('O pilar Sharing significa concentrar toda a responsabilidade pela segurança em um time de especialistas, que '
         'compartilha os relatórios com os demais.', False),
        ('Tratar os erros como oportunidade de aprendizado, e não como motivo de punição, faz parte do pilar Culture.',
         True),
    ],
    'I é verdadeira: Automation é automatizar testes, builds e verificações de segurança. II é falsa: Sharing é '
    'compartilhar conhecimento e responsabilidades entre os times; no DevSecOps, a segurança é responsabilidade de toda '
    'a equipe, e não só dos especialistas. III é verdadeira: Culture envolve colaboração e tolerância ao erro como '
    'aprendizado.',
    contexto=[p('Uma empresa está adotando DevSecOps e quer organizar as suas práticas segundo os pilares CALMS '
                '(Culture, Automation, Lean, Measurement e Sharing).')],
)

banco.multipla(
    'medio',
    'Segundo o modelo STRIDE, as situações 1, 2, 3 e 4 correspondem, respectivamente, às ameaças',
    'Tampering, Repudiation, Denial of Service e Elevation of Privilege.',
    [
        'Spoofing, Repudiation, Denial of Service e Elevation of Privilege.',
        'Tampering, Information Disclosure, Denial of Service e Spoofing.',
        'Tampering, Repudiation, Elevation of Privilege e Denial of Service.',
        'Information Disclosure, Tampering, Denial of Service e Elevation of Privilege.',
    ],
    'Alterar o preço no meio do caminho é modificar dados: Tampering (1). Negar uma ação sem que haja como provar o '
    'contrário é Repudiation, combatida com logs de auditoria imutáveis (2). Tornar o sistema indisponível com um volume '
    'enorme de requisições é Denial of Service, combatido com rate limiting e WAF (3). Um usuário comum que passa a ter '
    'poderes de administrador é Elevation of Privilege, combatida com menor privilégio e RBAC (4). Spoofing seria se '
    'passar por outro usuário.',
    contexto=[p('A equipe de uma loja virtual registrou quatro incidentes: '
                '(1) um atacante alterou o preço de um produto na requisição enviada ao servidor e comprou um celular por '
                'R$ 1,00; '
                '(2) um funcionário apagou pedidos de clientes e depois negou ter feito isso, e não havia registro que '
                'provasse o contrário; '
                '(3) milhares de requisições por segundo deixaram o site fora do ar durante a Black Friday; '
                '(4) um cliente comum trocou o valor "cliente" por "admin" em um campo da requisição e passou a acessar o '
                'painel administrativo.')],
)

banco.assercao(
    'medio',
    'A decisão da equipe viola o princípio da Falha Segura.',
    'Pelo princípio da Falha Segura, quando o sistema falha, ele deve negar o acesso por padrão.',
    0,
    'As duas são verdadeiras, e a II explica a I. Liberar o acesso a todos quando a verificação de permissões cai é o '
    'contrário da Falha Segura: qualquer pessoa, inclusive um atacante, ganharia acesso aos prontuários justamente '
    'quando o sistema está mais vulnerável. O correto é negar o acesso por padrão e tratar a falha do serviço.',
    contexto=[p('Em um sistema de prontuários, quando o serviço que verifica as permissões dos usuários fica fora do ar, '
                'a aplicação passa a liberar o acesso a todos os prontuários, "para não parar o atendimento".')],
)

banco.multipla(
    'medio',
    'Os problemas encontrados pertencem principalmente à categoria do OWASP Top 10',
    'A05 – Security Misconfiguration.',
    [
        'A01 – Broken Access Control.',
        'A03 – Injection.',
        'A07 – Authentication Failures.',
        'A10 – SSRF.',
    ],
    'Senha padrão que nunca foi trocada e modo de depuração ligado em produção são erros de configuração, e não de '
    'código: é a A05 (Security Misconfiguration), a vulnerabilidade mais comum na prática, cujo exemplo típico são '
    'credenciais padrão não alteradas. A01 trata de acessar recursos além das permissões; A03, de dados não confiáveis '
    'enviados a um interpretador; A07, de falhas no login e na sessão; A10, de o servidor buscar URLs fornecidas pelo '
    'usuário.',
    contexto=[p('Em uma auditoria, foram encontrados dois problemas no sistema de uma escola: o painel do servidor de '
                'banco de dados continua com o usuário "admin" e a senha "admin" que vieram na instalação, e a aplicação '
                'roda em produção com o modo de depuração ligado, mostrando aos usuários mensagens de erro com detalhes '
                'internos do sistema.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.afirmativas(
    'dificil',
    [
        ('Apagar o arquivo em um novo commit não resolve o problema, pois a chave continua no histórico do repositório.',
         True),
        ('A chave deve ser considerada comprometida e precisa ser revogada e substituída por uma nova.', True),
        ('Uma ferramenta de Secrets Detection, executada a cada commit, teria barrado o envio da chave.', True),
        ('Esse tipo de problema seria encontrado pelo DAST, que testa a aplicação em execução no ambiente de staging.',
         False),
    ],
    'I é verdadeira: cada commit é um snapshot guardado no histórico, e qualquer pessoa pode voltar ao commit anterior e '
    'ler a chave. II é verdadeira: o repositório ficou público por uma hora, então não há como saber quem copiou a '
    'chave; ela precisa ser trocada. III é verdadeira: o Secrets Detection identifica credenciais e chaves commitadas '
    'por engano, a cada commit. IV é falsa: o DAST simula ataques à aplicação em execução e não examina o conteúdo do '
    'repositório.',
    contexto=[p('Um desenvolvedor fez commit de um arquivo .env com a chave de acesso da conta da empresa na nuvem e '
                'enviou para um repositório público no GitHub. Uma hora depois, percebeu o erro e fez um novo commit '
                'apagando o arquivo.')],
)

banco.assercao(
    'dificil',
    'A ausência de qualquer limite de tentativas no login é um exemplo de Insecure Design (A04).',
    'As falhas de Insecure Design (A04) são corrigidas por completo com uma ferramenta de SAST, que aponta a linha de '
    'código em que está o erro.',
    2,
    'A I é verdadeira: o próprio OWASP cita a falta de rate limiting na autenticação como exemplo de A04, a ausência de '
    'um controle que deveria ter sido pensado desde o design. A II é falsa: no design inseguro, não existe uma linha '
    'errada para corrigir; falta um controle inteiro. Esse tipo de falha se previne na fase de design, com modelagem de '
    'ameaças e segurança por design, e não só com análise do código.',
    contexto=[p('O login de um aplicativo bancário aceita quantas tentativas de senha o usuário quiser, sem bloqueio nem '
                'atraso entre elas. Um atacante usou um programa para testar milhões de senhas em uma única conta.')],
)

banco.multipla(
    'dificil',
    'O trecho apresenta, entre outras, vulnerabilidades das categorias do OWASP Top 10',
    'A03 (Injection), pela consulta montada com o texto digitado, e A02 (Cryptographic Failures), pelo uso de MD5 nas '
    'senhas; a correção passa por prepared statements e por bcrypt ou Argon2.',
    [
        'A10 (SSRF), pois o servidor executa uma consulta, e A01 (Broken Access Control), pois a função cria uma sessão.',
        'apenas A03 (Injection), pois o MD5 é um algoritmo de hash seguro para armazenar senhas.',
        'A05 (Security Misconfiguration) e A09 (Logging Failures), pois o código não grava logs das tentativas de login.',
        'nenhuma, desde que o formato do e-mail seja validado no navegador antes do envio.',
    ],
    'A consulta junta o e-mail digitado ao texto do SQL; um valor malicioso muda a consulta. É SQL Injection (A03), '
    'prevenida com prepared statements (consultas parametrizadas). Guardar senhas com MD5 é proteção inadequada de dados '
    '(A02); para senhas, usa-se bcrypt ou Argon2. Validar o e-mail só no navegador não protege nada, pois toda entrada '
    'externa é não confiável e precisa ser tratada no servidor.',
    contexto=[
        p('Ao revisar o código de login de um sistema, uma desenvolvedora encontrou a função abaixo.'),
        codigo('''
def login(email, senha):
    sql = ("SELECT * FROM usuarios WHERE email = '"
           + email + "'")
    usuario = banco.executar(sql)
    if usuario and usuario.senha == md5(senha):
        return criar_sessao(usuario)
    return None
'''),
    ],
)

banco.multipla(
    'dificil',
    'A ordem correta das etapas no Security Pipeline é:',
    'modelagem de ameaças, SAST e Secrets Detection, SCA, DAST, IaC Scan, e WAF e SIEM em produção.',
    [
        'SAST e Secrets Detection, modelagem de ameaças, SCA, DAST, IaC Scan, e WAF e SIEM em produção.',
        'modelagem de ameaças, DAST, SCA, SAST e Secrets Detection, IaC Scan, e WAF e SIEM em produção.',
        'SCA, SAST e Secrets Detection, DAST, IaC Scan, WAF e SIEM em produção e, por último, modelagem de ameaças.',
        'WAF e SIEM em produção, IaC Scan, DAST, SCA, SAST e Secrets Detection e modelagem de ameaças.',
    ],
    'O Security Pipeline segue o fluxo: Planejamento (modelagem de ameaças, antes de qualquer linha de código) → '
    'Codificação (SAST e Secrets Detection, a cada commit) → Build (SCA) → Testes (DAST, contra staging) → Staging (IaC '
    'Scan) → Produção (WAF e SIEM) → Feedback (análise de incidentes blameless). Deixar a modelagem de ameaças para o '
    'fim contraria o Shift Left; o DAST exige a aplicação em execução, por isso não vem antes do SAST.',
    contexto=[p('Uma empresa quer montar o seu Security Pipeline, conectando a modelagem de ameaças, as ferramentas de '
                'segurança e a proteção da aplicação em produção, do planejamento até o feedback.')],
)

banco.multipla(
    'dificil',
    'Sobre os princípios fundamentais de segurança, assinale a alternativa INCORRETA.',
    'O usuário do banco de dados usado pela aplicação pode ter permissão de administrador, pois o princípio do Menor '
    'Privilégio vale para pessoas, e não para sistemas.',
    [
        'Pelo princípio da Validação de Entradas, toda entrada externa deve ser tratada como não confiável.',
        'A Defesa em Profundidade usa várias camadas independentes, como firewall, WAF, autenticação e criptografia.',
        'Pela Segurança por Design, a segurança é considerada desde o início do projeto, e não acrescentada no final.',
        'Controle de acesso baseado em papéis (RBAC) é uma contramedida para a ameaça de Elevation of Privilege.',
    ],
    'A afirmação incorreta é a do Menor Privilégio: ele vale para pessoas e para sistemas. Se a aplicação se conecta ao '
    'banco como administrador, uma única falha, como uma SQL Injection, dá ao atacante poder para apagar tudo. A '
    'aplicação deve ter só as permissões mínimas necessárias. As demais estão corretas: entradas externas são não '
    'confiáveis, a defesa em profundidade usa várias camadas, a segurança entra desde o design, e o RBAC limita o que '
    'cada papel pode fazer.',
    contexto=[p('Para simplificar a configuração, a equipe de um sistema de vendas fez a aplicação se conectar ao banco '
                'de dados com o usuário administrador, que pode criar, alterar e apagar qualquer tabela. Em uma revisão, '
                'a equipe discutiu esse e outros princípios de segurança.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"Security is a process, not a product."',
        'traducao': '(Tradução livre: "Segurança é um processo, não um produto.")',
        'fonte': 'SCHNEIER, B. Secrets and Lies: Digital Security in a Networked World. New York: John Wiley & Sons, 2000.',
    },
    [
        'Uma empresa de software contrata um teste de invasão (pentest) uma vez por ano, sempre às vésperas da versão '
        'anual, e acaba de comprar um WAF de última geração. A diretoria considera que, com isso, os sistemas estão '
        'protegidos.',
        'Três meses depois, a empresa sofreu dois incidentes: um vazamento de dados causado por uma biblioteca '
        'desatualizada, com vulnerabilidade conhecida, e o uso indevido de uma chave de acesso que um desenvolvedor havia '
        'enviado por engano ao repositório.',
    ],
    'Com base no texto e no caso apresentado, explique como a empresa deveria integrar a segurança ao seu processo de '
    'desenvolvimento.',
    'A empresa tratou a segurança como um produto (o WAF) e como um portão no final (o pentest anual), que é a '
    'abordagem tradicional que o DevSecOps mostrou ser insuficiente. Os dois incidentes vieram de problemas que '
    'surgiram entre um pentest e outro e que o WAF não barra. A segurança deveria ser um processo contínuo, com Shift '
    'Left: começar no planejamento, com modelagem de ameaças (STRIDE), e seguir por todo o pipeline. Na codificação, '
    'SAST e Secrets Detection a cada commit teriam barrado a chave enviada ao repositório. No build, o SCA teria '
    'apontado a biblioteca com vulnerabilidade conhecida (A06). Nos testes, o DAST simularia ataques contra a '
    'aplicação em staging; antes do deploy, o IaC Scan conferiria as configurações; e, em produção, o WAF e o SIEM '
    'seriam mais camadas, de acordo com a defesa em profundidade, e não a única proteção. Por fim, cada incidente '
    'deveria ser analisado sem culpados, para melhorar o processo. A segurança passa a ser responsabilidade de toda a '
    'equipe, e os problemas são corrigidos mais cedo, quando custam muito menos.',
)

banco.discursiva(
    'dificil',
    {
        'citacao': '"Every program and every user of the system should operate using the least set of privileges '
                   'necessary to complete the job."',
        'traducao': '(Tradução livre: "Todo programa e todo usuário do sistema devem operar com o menor conjunto de '
                    'privilégios necessário para realizar o trabalho.")',
        'fonte': 'SALTZER, J. H.; SCHROEDER, M. D. The Protection of Information in Computer Systems. Proceedings of the '
                 'IEEE, v. 63, n. 9, p. 1278-1308, 1975.',
    },
    [
        'Em uma clínica, todos os funcionários (recepcionistas, médicos e o setor de faturamento) entram no sistema de '
        'prontuários com o mesmo login, que tem permissão de administrador. A própria aplicação se conecta ao banco de '
        'dados com o usuário administrador do banco, e o sistema não guarda registro de quem fez cada operação.',
        'Depois de ser demitido, um funcionário apagou dezenas de prontuários, e a clínica não conseguiu descobrir quem '
        'foi o responsável.',
    ],
    'Com base no texto e no caso apresentado, analise as falhas de segurança do sistema e proponha as correções '
    'necessárias.',
    'O sistema viola o princípio do Menor Privilégio, que vale para usuários e para programas. Todos os funcionários '
    'usam o mesmo login de administrador, embora uma recepcionista não precise ver nem apagar prontuários. A correção '
    'é dar a cada funcionário o seu próprio login e usar controle de acesso por papéis (RBAC): a recepção agenda, o '
    'médico lê e escreve prontuários, o faturamento vê só o necessário para cobrar, e o acesso é verificado sempre no '
    'servidor (A01). A aplicação também deve se conectar ao banco com um usuário que tenha só as permissões de que '
    'precisa, e não como administrador. O login compartilhado e a falta de registros abrem caminho para as ameaças de '
    'Spoofing (qualquer um se passa por qualquer um) e de Repudiation (ninguém pode ser responsabilizado). Por isso, '
    'é preciso guardar logs de auditoria imutáveis de cada operação, monitorados (A09), e desativar o acesso de quem '
    'deixa a clínica. Autenticação com MFA e cópias de segurança dos prontuários acrescentam camadas, de acordo com a '
    'defesa em profundidade.',
)


if __name__ == '__main__':
    banco.gravar()
