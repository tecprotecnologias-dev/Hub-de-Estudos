"""
Questões médias e difíceis do capítulo 9 (Testes de Segurança) de Qualidade e Testes de Software:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/qualidade_cap9_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap9-o* e
qualidade-cap9-d*; as que já existiam (m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import QUALIDADE, Banco, codigo, p

banco = Banco('qualidade-cap9', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Os incidentes 1, 2 e 3 violam, respectivamente, as propriedades da tríade CIA',
    'confidencialidade, integridade e disponibilidade.',
    [
        'integridade, confidencialidade e disponibilidade.',
        'confidencialidade, disponibilidade e integridade.',
        'disponibilidade, integridade e confidencialidade.',
        'confidencialidade, integridade e autenticidade.',
    ],
    'O vazamento dos dados de cartão expõe informações a quem não deveria vê-las: confidencialidade (1). A alteração dos '
    'preços modifica dados sem autorização: integridade (2). O ataque que derruba o site impede o acesso quando ele é '
    'necessário: disponibilidade (3). Os três exemplos são os da tabela da apostila.',
    contexto=[p('Uma loja virtual sofreu três incidentes em um ano: '
                '(1) os dados de cartão dos clientes foram copiados por meio de uma SQL Injection; '
                '(2) um atacante alterou os preços dos produtos no banco de dados; '
                '(3) um ataque DDoS deixou o site fora do ar durante a Black Friday.')],
)

banco.multipla(
    'medio',
    'Os elementos 1, 2, 3 e 4 correspondem, respectivamente, aos conceitos de',
    'vulnerabilidade, ameaça, risco e superfície de ataque.',
    [
        'ameaça, vulnerabilidade, risco e superfície de ataque.',
        'vulnerabilidade, ameaça, superfície de ataque e risco.',
        'vulnerabilidade, risco, ameaça e vetor de ataque.',
        'vetor de ataque, ameaça, risco e superfície de ataque.',
    ],
    'Uma fraqueza que pode ser explorada é uma vulnerabilidade (1). Um agente ou evento com potencial para explorá-la é '
    'uma ameaça (2). A combinação da probabilidade de a ameaça explorar a vulnerabilidade com o impacto resultante é o '
    'risco (3). O conjunto total de pontos de entrada disponíveis para um atacante é a superfície de ataque (4). O vetor '
    'de ataque é o caminho usado em um ataque específico.',
    contexto=[p('Em uma análise de segurança de um e-commerce, a equipe registrou: '
                '(1) o campo de busca aceita qualquer texto, sem validação; '
                '(2) um grupo criminoso que ataca lojas virtuais do setor; '
                '(3) a chance alta de esse grupo usar o campo de busca, combinada com o impacto alto de um vazamento; '
                '(4) o conjunto de todas as telas, APIs e serviços expostos à internet.')],
)

banco.multipla(
    'medio',
    'Os pentests 1, 2 e 3 são, respectivamente, do tipo',
    'black box, white box e gray box.',
    [
        'white box, black box e gray box.',
        'black box, gray box e white box.',
        'gray box, white box e black box.',
        'black box, white box e black box.',
    ],
    'No black box, o pen tester não tem conhecimento prévio do sistema e simula um atacante externo (1). No white box, '
    'tem acesso total, com código, arquitetura e credenciais, e o teste é o mais completo (2). No gray box, tem '
    'conhecimento parcial, normalmente as credenciais de um usuário comum, e simula um usuário legítimo mal-intencionado '
    'tentando elevar os seus privilégios (3).',
    contexto=[p('Um banco contratou três pentests: '
                '(1) a equipe recebe só o endereço do site, sem nenhuma outra informação; '
                '(2) a equipe recebe o código-fonte, os diagramas da arquitetura e senhas de administrador; '
                '(3) a equipe recebe o login de um cliente comum e tenta acessar funções restritas aos gerentes.')],
)

banco.afirmativas(
    'medio',
    [
        ('O spider percorre a aplicação e mapeia automaticamente os endpoints e recursos encontrados.', True),
        ('A varredura passiva envia payloads maliciosos para descobrir XSS e SQL Injection.', False),
        ('O fuzzer envia dados inesperados ou malformados para encontrar falhas de validação.', True),
        ('O modo daemon executa o ZAP sem interface gráfica, o que permite usá-lo em pipelines de CI/CD.', True),
    ],
    'I, III e IV descrevem corretamente recursos do OWASP ZAP. II é falsa: a varredura passiva só analisa o tráfego já '
    'capturado, sem enviar requisições extras, e encontra problemas como cabeçalhos de segurança ausentes; quem envia '
    'payloads maliciosos é a varredura ativa.',
    contexto=[p('Uma testadora vai usar o OWASP ZAP pela primeira vez e anotou o que faz cada recurso da ferramenta.')],
)

banco.assercao(
    'medio',
    'Codificar (encode) os dados exibidos no HTML e usar uma Content Security Policy (CSP) ajudam a prevenir o XSS.',
    'No XSS, scripts maliciosos são injetados na aplicação e executados no navegador de outros usuários.',
    0,
    'As duas são verdadeiras, e a II explica a I. Como o ataque depende de o navegador executar um script colocado pelo '
    'atacante, a defesa é impedir essa execução: o encode faz o navegador tratar o conteúdo como texto, e não como '
    'código, e a CSP limita quais scripts podem rodar na página. A sanitização das entradas completa a prevenção.',
    contexto=[p('Em um fórum, um usuário publicou um comentário com um script escondido. Todos que abriam a página tinham '
                'o seu login roubado. A equipe discute como impedir que isso se repita.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Pela metodologia STRIDE, as ameaças 1, 2, 3 e 4 são, respectivamente,',
    'Spoofing, Tampering, Repudiation e Elevation of Privilege.',
    [
        'Tampering, Spoofing, Repudiation e Elevation of Privilege.',
        'Spoofing, Tampering, Information Disclosure e Elevation of Privilege.',
        'Spoofing, Repudiation, Tampering e Denial of Service.',
        'Elevation of Privilege, Tampering, Repudiation e Spoofing.',
    ],
    'Usar o token de outra pessoa para se passar por ela é Spoofing (1). Alterar o valor do pedido no caminho é '
    'Tampering, a modificação de dados (2). Negar ter feito a transferência, sem que haja como provar o contrário, é '
    'Repudiation (3). Um usuário comum que obtém permissões de administrador é Elevation of Privilege (4). Information '
    'Disclosure é a exposição de dados confidenciais, e Denial of Service, tornar o sistema indisponível.',
    contexto=[p('Na modelagem de ameaças de um aplicativo bancário, a equipe identificou: '
                '(1) um atacante usa o token de sessão roubado de um cliente para agir em nome dele; '
                '(2) o valor de um pagamento é alterado entre o aplicativo e o servidor; '
                '(3) um cliente nega ter feito uma transferência, e o sistema não tem registro que prove o contrário; '
                '(4) um usuário comum consegue acessar as funções de administrador.')],
)

banco.afirmativas(
    'dificil',
    [
        ('Uma recuperação de senha baseada em perguntas fáceis de adivinhar é um exemplo de A04 (Insecure Design).', True),
        ('Uma dependência maliciosa publicada no npm e usada pelo projeto é um exemplo de A08 (Software and Data Integrity '
         'Failures).', True),
        ('Um sistema sem logs de autenticação, em que um ataque passa meses sem ser percebido, é um exemplo de A09 '
         '(Security Logging and Monitoring Failures).', True),
        ('Acessar o perfil de outro usuário trocando o ID na URL é um exemplo de A10 (Server-Side Request Forgery).', False),
    ],
    'I, II e III trazem os exemplos da tabela do OWASP Top 10 2021 da apostila. IV é falsa: trocar o ID na URL para ver '
    'os dados de outro usuário é A01 (Broken Access Control), no caso um IDOR. O SSRF (A10) acontece quando o servidor '
    'busca um recurso em uma URL fornecida pelo usuário, sem validá-la, como no acesso ao endereço de metadados da nuvem '
    'para roubar credenciais.',
    contexto=[p('Em um treinamento sobre o OWASP Top 10 2021, os alunos associaram exemplos às categorias.')],
)

banco.multipla(
    'dificil',
    'Na metodologia de pentest em cinco fases, a ordem correta das atividades é:',
    'pesquisa em fontes abertas, varredura de portas, exploração da falha, movimento lateral e relatório.',
    [
        'varredura de portas, pesquisa em fontes abertas, exploração da falha, relatório e movimento lateral.',
        'pesquisa em fontes abertas, exploração da falha, varredura de portas, movimento lateral e relatório.',
        'exploração da falha, movimento lateral, pesquisa em fontes abertas, varredura de portas e relatório.',
        'pesquisa em fontes abertas, varredura de portas, movimento lateral, exploração da falha e relatório.',
    ],
    'O pentest começa pelo reconhecimento, com a coleta de informações públicas, como OSINT e DNS; segue para a varredura '
    'e enumeração, com ferramentas como o Nmap, que encontram portas e serviços; depois vem a obtenção de acesso, com a '
    'exploração das vulnerabilidades (por exemplo, com o Metasploit); em seguida, a manutenção de acesso, que avalia o '
    'que dá para fazer com ele, como o movimento lateral; e, por fim, o relatório, com severidade, prova de conceito e '
    'recomendações.',
    contexto=[p('No relatório de um pentest, as atividades realizadas foram registradas fora de ordem: o movimento lateral '
                'para outros servidores; a varredura de portas e serviços com o Nmap; o relatório com as falhas '
                'classificadas por severidade; a pesquisa de informações públicas sobre a empresa (OSINT); e a exploração '
                'de uma falha encontrada no servidor web.')],
)

banco.assercao(
    'dificil',
    'Como as ferramentas automatizadas encontram a maior parte das vulnerabilidades, o pentest manual é dispensável em '
    'empresas que já adotam DevSecOps.',
    'As ferramentas automatizadas encontram cerca de 30% a 40% das vulnerabilidades, e as falhas de lógica e de negócio '
    'pedem a análise de um especialista.',
    3,
    'A II é verdadeira, e é justamente por ela que a I é falsa. Pela apostila, a automação encontra apenas uma parte das '
    'vulnerabilidades; falhas de lógica e de regras de negócio, que os scanners não detectam, exigem pentest manual. Por '
    'isso, mesmo com SAST, DAST e SCA no pipeline, a recomendação é fazer pentests periódicos, ao menos uma vez por ano '
    'e sempre depois de mudanças grandes na arquitetura.',
    contexto=[p('Depois de colocar SAST, DAST e SCA no pipeline, a diretoria de uma empresa propôs cancelar o contrato de '
                'pentest anual, "porque agora as ferramentas fazem esse trabalho".')],
)

banco.multipla(
    'dificil',
    'Sobre a segurança integrada ao pipeline no DevSecOps, assinale a alternativa INCORRETA.',
    'O DAST é executado no commit, analisando o código-fonte antes do build, sem precisar da aplicação em execução.',
    [
        'No commit ou no pull request, o SAST analisa o código, e o secret scanning procura credenciais enviadas por engano.',
        'No build, o SCA verifica se as dependências usadas pelo projeto têm vulnerabilidades conhecidas.',
        'Em staging, o DAST faz a varredura da aplicação em execução, junto com os testes funcionais de segurança.',
        'Em produção, entram o WAF, o monitoramento de comportamento anômalo e os alertas de intrusão (IDS/IPS).',
    ],
    'A afirmação incorreta é a do DAST: ele testa a aplicação em execução, simulando ataques externos, e por isso roda em '
    'staging, e não no commit. Quem analisa o código-fonte sem executar a aplicação é o SAST. As demais alternativas '
    'descrevem corretamente as etapas do pipeline DevSecOps da apostila.',
    contexto=[p('Uma empresa está montando o seu pipeline com práticas de DevSecOps e revisou em que etapa entra cada '
                'verificação de segurança.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Uma startup desenvolveu, durante um ano, uma plataforma de telemedicina sem nenhuma atividade de segurança. Uma '
        'semana antes do lançamento, contratou um pentest, que encontrou 40 vulnerabilidades, 12 delas ligadas ao próprio '
        'desenho do sistema, como a recuperação de senha por perguntas fáceis e a ausência de limite de tentativas de '
        'login. O lançamento atrasou três meses, e parte da arquitetura teve de ser refeita.',
    ],
    'Com base no capítulo, explique como a startup deveria ter integrado a segurança ao seu ciclo de desenvolvimento '
    'para evitar essa situação.',
    'A startup tratou a segurança como uma etapa no fim, o oposto do Shift-Left Security, que leva as atividades de '
    'segurança para as fases iniciais, onde corrigir custa muito menos; pela apostila, uma vulnerabilidade corrigida em '
    'produção pode custar até 30 vezes mais do que no design. Pelo ciclo de vida seguro: nos requisitos, incluir '
    'requisitos e critérios de aceitação de segurança e fazer a modelagem de ameaças (STRIDE), o que teria revelado as '
    'falhas de design (A04), como a recuperação de senha e a falta de limite de tentativas; no design, aplicar defesa em '
    'profundidade e menor privilégio; na implementação, treinar a equipe em codificação segura e revisar o código com '
    'foco em segurança; nos testes, SAST, SCA e DAST no pipeline, como em uma abordagem DevSecOps; no deploy, hardening e '
    'gestão de segredos; e, na operação, monitoramento, atualização de dependências e plano de resposta a incidentes. O '
    'pentest continuaria sendo importante, mas como uma camada a mais, e não como a única verificação, feita quando já é '
    'tarde demais.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'O relatório de um pentest em um sistema de notas fiscais trouxe os achados abaixo. A equipe tem poucos '
        'desenvolvedores e quer saber por onde começar.',
    ],
    'Com base na classificação CVSS e nas boas práticas de gestão de vulnerabilidades do capítulo, proponha a ordem de '
    'tratamento desses achados e explique como a equipe deve acompanhar as correções.',
    'A ordem segue a severidade do CVSS. Primeiro, a execução remota de código sem autenticação (9,8, crítica): correção '
    'imediata, em horas, por permitir que qualquer pessoa assuma o servidor. Em seguida, as altas, com correção urgente, '
    'em dias: o IDOR nas notas fiscais (8,1), que expõe documentos de outros clientes (A01) e deve ser resolvido checando '
    'a autorização no servidor, e o XSS persistente (7,5), com encode da saída e CSP. Depois, a média: o CSRF (5,4), com '
    'correção planejada, em semanas. Por fim, a baixa: a versão do servidor exposta (2,1), corrigida no próximo ciclo, '
    'escondendo a informação. Para acompanhar, cada vulnerabilidade deve ser registrada em uma ferramenta, como Jira ou '
    'DefectDojo, com responsável, prazo e status; depois de corrigida, deve ser testada de novo para confirmar a '
    'correção; e a equipe deve analisar as causas, como a falta de validação de autorização, para evitar que falhas do '
    'mesmo tipo voltem a aparecer.',
)
banco.discursivas[-1]['contexto'] = [
    codigo('''
Achado                                     CVSS
Execução remota de código sem autenticação  9,8
IDOR: acesso às notas de outros clientes    8,1
XSS persistente nos comentários             7,5
CSRF na troca de e-mail do perfil           5,4
Versão do servidor exposta nos cabeçalhos   2,1
'''),
]


if __name__ == '__main__':
    banco.gravar()
