"""
Questões médias e difíceis do capítulo 4 (Crimes Cibernéticos e Segurança) de Legislação em Negócios Digitais:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/legislacao_cap4_objetivas.py

Grava em src/data/questoes/legislacao.json, trocando só as questões legislacao-cap4-o* e
legislacao-cap4-d*; as que já existiam (q* e f*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import LEGISLACAO, Banco, p

banco = Banco('legislacao-cap4', LEGISLACAO)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Quais das condutas são crimes cibernéticos puros e quais são impróprios?',
    'São puros o 1 e o 3, em que o sistema é o alvo; são impróprios o 2 e o 4, crimes comuns praticados por meio digital.',
    [
        'São puros o 1, o 2 e o 3, pois todos usam tecnologia; só o 4 é impróprio, por ofender a honra da pessoa.',
        'São puros o 2 e o 4, que só existem nas redes; são impróprios o 1 e o 3, que já existiam antes da internet.',
        'Todos são puros, pois qualquer crime praticado com um computador ou um celular é crime cibernético puro.',
        'Todos são impróprios, pois o Código Penal não prevê nenhum crime em que o sistema informático seja o alvo.',
    ],
    'No crime cibernético puro, o sistema informático é o alvo e o crime não existiria sem a tecnologia: é o caso do '
    'ransomware (1) e do ataque de negação de serviço (3), que pode ser enquadrado na interrupção de serviço telemático '
    '(art. 266, § 1º, do CP). No impróprio, o meio digital é usado para um crime tradicional: ameaça (art. 147) por '
    'aplicativo de mensagens (2) e calúnia (art. 138) em rede social (4).',
    contexto=[p('Considere as condutas: '
                '(1) criptografar os arquivos de um hospital com um ransomware; '
                '(2) enviar ameaças de morte a um ex-colega por um aplicativo de mensagens; '
                '(3) derrubar o site de uma prefeitura com um ataque de negação de serviço (DDoS); '
                '(4) acusar falsamente um vizinho de um crime em uma rede social.')],
)

banco.multipla(
    'medio',
    'As tentativas 1, 2, 3 e 4 correspondem, respectivamente, a',
    'spear phishing, vishing, smishing e credential stuffing.',
    ['phishing, smishing, vishing e man-in-the-middle.', 'spear phishing, smishing, vishing e credential stuffing.',
     'spear phishing, vishing, smishing e engenharia social.', 'vishing, spear phishing, smishing e credential stuffing.'],
    'O spear phishing é o phishing dirigido a uma pessoa específica, com dados reais dela (1). O vishing usa ligações de '
    'voz, como a falsa central do banco (2). O smishing usa mensagens de SMS com links falsos (3). O credential stuffing '
    'são tentativas automatizadas de login com senhas vazadas de outros serviços, explorando o reuso de senhas (4).',
    contexto=[p('A equipe de segurança de uma empresa registrou quatro tentativas de golpe em uma semana: '
                '(1) um e-mail falso enviado só à diretora financeira, citando o nome dela, o cargo e um fornecedor real; '
                '(2) uma ligação de alguém que se dizia da central do banco e pedia o código de segurança; '
                '(3) um SMS com um link sobre uma "entrega pendente" de encomenda; '
                '(4) milhares de tentativas automáticas de login com e-mails e senhas vazados de outros sites.')],
)

banco.multipla(
    'medio',
    'Os incidentes 1, 2, 3 e 4 são, respectivamente, violações de',
    'confidencialidade, integridade e disponibilidade, além de uma ameaça interna (insider threat).',
    [
        'integridade, confidencialidade e disponibilidade, além de um vazamento por terceiro.',
        'confidencialidade, disponibilidade e integridade, além de uma ameaça interna (insider threat).',
        'disponibilidade, integridade e confidencialidade, além de uma ameaça interna (insider threat).',
        'confidencialidade, integridade e disponibilidade, além de um vazamento por terceiro.',
    ],
    'Um banco de dados exposto por erro de configuração permite acesso não autorizado: viola a confidencialidade (1). '
    'Alterar registros sem autorização viola a integridade (2). Derrubar o sistema e impedir o acesso viola a '
    'disponibilidade (3). Um empregado que copia dados sem autorização é uma ameaça interna (4); o vazamento por terceiro '
    'ocorre quando o incidente é de um fornecedor.',
    contexto=[p('Uma rede de clínicas registrou quatro incidentes: '
                '(1) um banco de dados de pacientes ficou acessível na internet por erro de configuração; '
                '(2) um malware alterou os resultados de exames guardados no sistema; '
                '(3) um ataque de negação de serviço deixou o sistema de agendamento fora do ar por um dia; '
                '(4) uma funcionária copiou a lista de pacientes para levar a uma clínica concorrente.')],
)

banco.assercao(
    'medio',
    'O provedor de aplicações constituído como pessoa jurídica, que atua de forma profissional e com fins econômicos, deve '
    'guardar os registros de acesso a aplicações por 6 meses.',
    'Na provisão de conexão à internet, é vedado ao provedor guardar os registros de acesso a aplicações de internet.',
    1,
    'As duas são verdadeiras, mas a II não justifica a I. A I é o art. 15 do Marco Civil da Internet, que fixa a guarda '
    'dos registros de acesso a aplicações por 6 meses. A II é o art. 14, que proíbe o provedor de conexão de guardar '
    'esses registros, cabendo-lhe guardar só os registros de conexão, por 1 ano (art. 13). São regras sobre agentes '
    'diferentes.',
    contexto=[p('Uma investigação precisa saber quando um usuário acessou uma rede social e de qual endereço IP. O '
                'delegado tem dúvidas sobre quem deve guardar cada tipo de registro.')],
)

banco.multipla(
    'medio',
    'Qual é a responsabilidade da operadora de internet nesse caso?',
    'Ela não responde pelo conteúdo, mas pode ser obrigada, por ordem judicial, a fornecer registros para identificar o '
    'autor.',
    [
        'Ela responde solidariamente com o autor, pois foi pela conexão dela que as ofensas chegaram à internet.',
        'Ela responde se não bloquear o acesso do ofensor à internet em até 24 horas depois de notificada pela vítima.',
        'Ela não responde e também não pode ser obrigada a nada, pois os registros de conexão são sempre sigilosos.',
        'Ela responde sozinha, pois o autor das ofensas está protegido pela liberdade de expressão garantida no MCI.',
    ],
    'Pelo art. 18 do Marco Civil da Internet, o provedor de conexão não é responsabilizado civilmente por danos '
    'decorrentes de conteúdo gerado por terceiros. Os registros de conexão são sigilosos, mas podem ser fornecidos por '
    'ordem judicial (arts. 10, § 1º, e 22), o que permite identificar o autor das ofensas, que é quem responde por elas.',
    contexto=[p('Uma empresa foi alvo de ofensas publicadas em um fórum por um usuário anônimo. Descobriu que ele usa a '
                'internet de uma operadora local e decidiu processar a operadora, e não o fórum, pelos danos sofridos.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Como se enquadram, em regra, as condutas dos casos A e B?',
    'A é furto mediante fraude por meio eletrônico, e B é fraude eletrônica; os dois têm reclusão de 4 a 8 anos.',
    [
        'Os dois são fraude eletrônica, pois em ambos o golpista usou meios digitais para ficar com o dinheiro.',
        'A é fraude eletrônica, e B é furto mediante fraude, pois em B a vítima foi enganada pelo golpista.',
        'A é só invasão de dispositivo, com reclusão de 1 a 4 anos, e B não é crime, pois a vítima consentiu.',
        'Os dois são estelionato simples, com pena de 1 a 5 anos, pois a Lei 14.155/2021 não alcança essas condutas.',
    ],
    'No furto mediante fraude, a fraude serve para diminuir a vigilância da vítima, e o próprio agente subtrai o dinheiro: '
    'é o caso A, enquadrado no art. 155, § 4º-B, do CP. Na fraude eletrônica, a vítima, enganada, entrega ela mesma o '
    'dinheiro: é o caso B, art. 171, § 2º-A. Os dois foram criados pela Lei nº 14.155/2021, com reclusão de 4 a 8 anos '
    'e multa; no caso A, a invasão do celular também pode ser punida.',
    contexto=[p('Caso A: um golpista instalou um programa espião no celular de uma vítima, capturou as senhas do banco e '
                'ele mesmo transferiu R$ 10 mil da conta dela. Caso B: outro golpista, fingindo ser um parente em apuros, '
                'convenceu uma vítima a fazer, ela mesma, um Pix de R$ 10 mil para a conta dele.')],
)

banco.afirmativas(
    'dificil',
    [
        ('Para a maior parte dos conteúdos ilícitos, a plataforma pode responder se não remover após notificação.', True),
        ('Nos crimes contra a honra, a responsabilização da plataforma continua dependendo de ordem judicial.', True),
        ('Em anúncios pagos e impulsionamentos, a plataforma pode responder mesmo sem nenhuma notificação.', True),
        ('O STF declarou o art. 19 totalmente constitucional, mantendo a ordem judicial para todo conteúdo.', False),
    ],
    'I, II e III resumem o julgamento dos Temas 987 e 533 pelo STF, em junho de 2025, que declarou o art. 19 do Marco '
    'Civil parcialmente inconstitucional: para a maioria dos conteúdos ilícitos, vale o regime de notificação e '
    'retirada; nos crimes contra a honra, mantém-se a ordem judicial; e anúncios pagos e impulsionamentos geram '
    'responsabilidade sem notificação. IV é falsa, pelo mesmo motivo.',
    contexto=[p('Depois da decisão do STF de 2025 sobre o Marco Civil da Internet, uma rede social revisou a sua política '
                'de moderação de conteúdo.')],
)

banco.multipla(
    'dificil',
    'Qual é o enquadramento penal mais adequado e a pena prevista em abstrato?',
    'Difamação, com pena triplicada por ter sido divulgada em rede social: detenção de 9 meses a 3 anos, e multa.',
    [
        'Difamação, com a pena comum do crime, pois a internet não altera a pena: detenção de 3 meses a 1 ano, e multa.',
        'Difamação, com pena dobrada por ter sido divulgada em rede social: detenção de 6 meses a 2 anos, e multa.',
        'Calúnia, pois o fato atribuído é ofensivo à reputação: detenção de 6 meses a 2 anos, e multa.',
        'Injúria, pois ofende a honra da vítima: detenção de 1 a 6 meses, ou multa, sem nenhum aumento.',
    ],
    'Atribuir a alguém um fato ofensivo à reputação que não é crime (embriaguez no trabalho) é difamação (art. 139 do '
    'CP), com detenção de 3 meses a 1 ano e multa. A calúnia exige a imputação falsa de um crime, e a injúria ofende a '
    'dignidade sem atribuir fato. Pelo art. 141, § 2º, se o crime contra a honra é cometido ou divulgado em redes sociais, '
    'aplica-se a pena em triplo: de 9 meses a 3 anos.',
    contexto=[p('Um homem publicou em uma rede social, para milhares de seguidores, que um colega de trabalho "chega '
                'embriagado ao escritório todos os dias", o que não era verdade e prejudicou a reputação do colega.')],
)

banco.multipla(
    'dificil',
    'Considerando o art. 13 do Marco Civil, qual é o procedimento correto?',
    'O provedor guarda os registros além de 1 ano, em sigilo, e o MP tem 60 dias para pedir à Justiça o acesso a eles.',
    [
        'O provedor deve entregar os registros ao MP na hora, pois o pedido cautelar dispensa a ordem judicial.',
        'O provedor pode negar o pedido, pois a lei proíbe guardar os registros de conexão por mais de 1 ano.',
        'O provedor guarda os registros por mais tempo e avisa o usuário investigado, que pode se opor ao pedido.',
        'O provedor guarda os registros por mais tempo, e o MP tem 1 ano para pedir à Justiça o acesso a eles.',
    ],
    'O art. 13, § 2º, permite que a autoridade policial ou administrativa ou o Ministério Público peça, cautelarmente, '
    'que os registros de conexão sejam guardados por prazo superior a 1 ano. O § 3º dá à autoridade 60 dias, contados do '
    'pedido, para ingressar com o pedido de autorização judicial de acesso, e o § 4º obriga o provedor a manter sigilo '
    'sobre o requerimento. O acesso aos registros continua dependendo de ordem judicial.',
    contexto=[p('O Ministério Público investiga uma fraude cometida há 11 meses e pede a um provedor de conexão que guarde, '
                'por mais tempo que o prazo legal, os registros de conexão de um suspeito, para depois pedir acesso a '
                'eles.')],
)

banco.multipla(
    'dificil',
    'Com base no entendimento do STJ, o pedido de indenização por dano moral tende a ser',
    'negado se o cliente não provar o prejuízo, pois o vazamento de dados comuns não gera dano moral presumido.',
    [
        'aceito, pois todo vazamento de dados pessoais gera dano moral presumido, sem necessidade de nenhuma prova.',
        'aceito, pois a LGPD fixa uma indenização mínima de R$ 10 mil por titular afetado em qualquer vazamento.',
        'negado, pois a empresa só responde se o vazamento tiver sido causado por um empregado, e não por hackers.',
        'negado, pois as sanções da ANPD substituem as indenizações civis aos titulares, que não podem ir à Justiça.',
    ],
    'O STJ decidiu que o vazamento de dados pessoais comuns, como nome, e-mail e telefone, não gera dano moral presumido: '
    'o titular precisa demonstrar um prejuízo concreto, como golpes sofridos ou uso indevido dos dados. Com dados '
    'sensíveis, a análise tende a ser mais rigorosa. Isso não afasta a responsabilidade da empresa (arts. 42 a 44 da '
    'LGPD) nem as sanções da ANPD, que são independentes.',
    contexto=[p('Uma loja virtual sofreu um ataque que expôs o nome, o e-mail e o telefone de milhares de clientes. Um '
                'deles entrou na Justiça pedindo R$ 10 mil de indenização por dano moral, sem apontar nenhum golpe ou '
                'prejuízo que tenha sofrido depois do vazamento.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Na madrugada de uma segunda-feira, uma rede de clínicas descobre que um ransomware criptografou os seus servidores. '
        'Os criminosos dizem ter copiado os prontuários de 30 mil pacientes e exigem um resgate em criptomoeda, ameaçando '
        'publicar os dados em 72 horas. Parte da equipe quer formatar tudo e restaurar os backups imediatamente; outra '
        'parte quer pagar o resgate em silêncio para "evitar escândalo".',
    ],
    'Proponha a conduta jurídica e técnica que a rede de clínicas deve adotar nas primeiras horas e dias depois do '
    'incidente.',
    'A clínica deve acionar o plano de resposta a incidentes, a equipe de segurança, o encarregado e o jurídico. Na '
    'contenção, isola os sistemas afetados, sem formatar nem apagar nada antes de preservar as evidências, como logs, '
    'imagens dos discos e mensagens dos criminosos, necessárias à perícia, à investigação e à defesa da empresa; depois, '
    'restaura a partir de backups íntegros. Deve avaliar o escopo: quais dados, quantos titulares e o risco; prontuários '
    'são dados sensíveis de saúde, e o risco é relevante. Por isso, deve comunicar a ANPD em até 3 dias úteis (art. 48 da '
    'LGPD e Resolução CD/ANPD nº 15/2024) e avisar os pacientes, com informações claras e orientações, além de registrar '
    'boletim de ocorrência: há invasão de dispositivo (art. 154-A do CP) e extorsão (art. 158). Pagar o resgate em '
    'silêncio não resolve: não garante a devolução nem o sigilo dos dados, não dispensa as comunicações obrigatórias e '
    'pode financiar o crime; esconder o incidente agrava as sanções. A clínica responde pela segurança dos dados (art. '
    '46), pode sofrer sanções da ANPD e dos órgãos de saúde e indenizar danos, e, na fase pós-incidente, deve documentar '
    'tudo, corrigir as falhas e reforçar os controles, como autenticação multifator, backups 3-2-1 e treinamento.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma rede social brasileira, com milhões de usuários, recebe todos os dias denúncias de conteúdos como ofensas a '
        'pessoas, golpes financeiros anunciados por impulsionamento pago, vídeos íntimos divulgados sem consentimento e '
        'ameaças de ataques a escolas. Hoje, a empresa só remove conteúdos quando recebe uma ordem judicial.',
    ],
    'Com base no Marco Civil da Internet e na decisão do STF de 2025, avalie a política atual da rede social e proponha '
    'uma nova política de moderação.',
    'A política atual está desatualizada e expõe a empresa a responsabilidade. Desde o julgamento dos Temas 987 e 533, em '
    '2025, o art. 19 do Marco Civil é parcialmente inconstitucional: para a maior parte dos conteúdos ilícitos, incluindo '
    'crimes como golpes, a plataforma pode responder se não remover o conteúdo depois de notificação extrajudicial. Nas '
    'ofensas à honra, a responsabilização continua dependendo de ordem judicial, embora a empresa possa remover por '
    'notificação. Os vídeos íntimos sem consentimento já seguiam o art. 21: basta a notificação da vítima, e a remoção '
    'deve ser diligente. Para conteúdos graves, como ameaças de ataques e terrorismo, a plataforma tem dever de cuidado e '
    'responde por falha sistêmica, mesmo sem notificação, o que exige monitoramento ativo. Nos golpes por impulsionamento '
    'pago, responde sem notificação, pois lucrou com o anúncio. A nova política deve ter canal de denúncias acessível, '
    'prazos rápidos de análise, critérios claros por tipo de conteúdo, possibilidade de recurso para o autor, relatórios '
    'de transparência, verificação dos anunciantes, guarda dos registros de acesso por 6 meses (art. 15) e cooperação com '
    'as autoridades, fornecendo dados mediante ordem judicial.',
)


if __name__ == '__main__':
    banco.gravar()
