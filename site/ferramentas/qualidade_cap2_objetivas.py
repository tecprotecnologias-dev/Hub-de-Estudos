"""
Questões médias e difíceis do capítulo 2 (Modelos de Qualidade de Software) de Qualidade e Testes de
Software: 10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um
único comando. As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/qualidade_cap2_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap2-o* e
qualidade-cap2-d*; as que já existiam (q* e m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import QUALIDADE, Banco, p

banco = Banco('qualidade-cap2', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As situações 1, 2, 3 e 4 ilustram, respectivamente, os benefícios de usar um modelo de qualidade ligados a',
    'padronização, mensurabilidade, melhoria contínua e conformidade.',
    [
        'mensurabilidade, padronização, conformidade e melhoria contínua.',
        'padronização, melhoria contínua, mensurabilidade e conformidade.',
        'conformidade, mensurabilidade, melhoria contínua e padronização.',
        'padronização, mensurabilidade, conformidade e melhoria contínua.',
    ],
    'Ter uma linguagem comum entre clientes, desenvolvedores e testadores é a padronização (1). Transformar "o sistema é '
    'confiável" em um número, como o tempo médio entre falhas, é a mensurabilidade (2). Comparar versões para descobrir os '
    'pontos fracos e decidir o que melhorar é a melhoria contínua (3). Facilitar auditorias e certificações exigidas por '
    'órgãos reguladores é a conformidade (4).',
    contexto=[p('Uma empresa adotou um modelo de qualidade e observou quatro efeitos: '
                '(1) clientes, desenvolvedores e testadores passaram a usar os mesmos termos para falar de qualidade; '
                '(2) a afirmação "o sistema é confiável" foi trocada por medidas, como o tempo médio entre falhas; '
                '(3) a comparação entre as versões mostrou os pontos fracos e orientou o que melhorar primeiro; '
                '(4) a auditoria exigida por um órgão regulador ficou mais simples de preparar.')],
)

banco.afirmativas(
    'medio',
    [
        ('O modelo de McCall, de 1977, foi o primeiro modelo estruturado em perspectivas.', True),
        ('O modelo FURPS, da Hewlett-Packard, organiza a qualidade em seis grupos principais.', False),
        ('A ISO/IEC 9126, de 1991, organiza a qualidade de produto em oito características.', False),
        ('O modelo de Dromey, de 1995, busca ligar as propriedades do produto à qualidade.', True),
    ],
    'I é verdadeira: é a contribuição principal de McCall na tabela da apostila. II é falsa: o FURPS classifica a '
    'qualidade em cinco grupos. III é falsa: a ISO/IEC 9126 tem seis características; as oito são da ISO/IEC 25010, de '
    '2011. IV é verdadeira: é a contribuição atribuída a Dromey.',
    contexto=[p('Para uma apresentação sobre a história dos modelos de qualidade de software, um aluno reuniu informações '
                'sobre os principais modelos propostos desde a década de 1970.')],
)

banco.multipla(
    'medio',
    'Na ISO/IEC 9126, os problemas 1, 2, 3 e 4 afetam, respectivamente, as subcaracterísticas da funcionalidade',
    'acurácia, interoperabilidade, segurança de acesso e conformidade.',
    [
        'adequação, interoperabilidade, segurança de acesso e conformidade.',
        'acurácia, conformidade, segurança de acesso e interoperabilidade.',
        'acurácia, interoperabilidade, conformidade e segurança de acesso.',
        'adequação, acurácia, interoperabilidade e segurança de acesso.',
    ],
    'Resultados com erro de arredondamento ferem a acurácia, que é produzir resultados corretos com a precisão '
    'necessária (1). Não conseguir trocar dados com o sistema legado fere a interoperabilidade (2). Um usuário comum '
    'entrar no painel de administração fere a segurança de acesso, que é impedir o acesso não autorizado (3). Descumprir '
    'a LGPD fere a conformidade, que é atender a normas e regulamentos (4). A adequação trata de as funções cobrirem as '
    'necessidades.',
    contexto=[p('A avaliação da funcionalidade de um sistema financeiro encontrou quatro problemas: '
                '(1) o cálculo de juros tem erros de arredondamento; '
                '(2) o sistema não consegue trocar dados com o sistema legado de cobrança; '
                '(3) usuários comuns conseguem abrir o painel de administração; '
                '(4) o tratamento dos dados pessoais dos clientes não segue a LGPD.')],
)

banco.assercao(
    'medio',
    'Medir se os vendedores, no dia a dia, concluem os pedidos mais rápido, com menos erros e mais satisfeitos é avaliar '
    'a qualidade em uso do sistema.',
    'Na ISO/IEC 9126, a qualidade em uso é avaliada pelo resultado do uso no contexto real de trabalho, com atributos '
    'próprios: efetividade, produtividade, segurança e satisfação.',
    0,
    'As duas são verdadeiras, e a II explica a I. A qualidade em uso olha a experiência do usuário no contexto real de '
    'trabalho, e não o código (qualidade interna) nem o comportamento em execução nos testes (qualidade externa). Ela '
    'tem atributos próprios: concluir o pedido é efetividade, fazer mais rápido é produtividade, e a opinião dos '
    'vendedores é satisfação.',
    contexto=[p('Seis meses depois de implantar um novo sistema de vendas, uma empresa passou a medir quanto tempo os '
                'vendedores levam para fechar um pedido, quantos erros cometem nas telas e quão satisfeitos estão com o '
                'sistema.')],
)

banco.multipla(
    'medio',
    'Na ISO/IEC 9126, as situações 1, 2 e 3 estão ligadas, respectivamente, às subcaracterísticas da confiabilidade',
    'maturidade, tolerância a falhas e recuperabilidade.',
    [
        'tolerância a falhas, maturidade e recuperabilidade.',
        'maturidade, recuperabilidade e tolerância a falhas.',
        'recuperabilidade, tolerância a falhas e maturidade.',
        'maturidade, tolerância a falhas e conformidade.',
    ],
    'A frequência de falhas causadas por defeitos é a maturidade, medida pelo MTBF (1). Manter o desempenho quando um '
    'componente falha é a tolerância a falhas (2). Restaurar os dados e o desempenho depois de uma falha é a '
    'recuperabilidade, medida pelo MTTR (3). A conformidade trata da aderência a normas de confiabilidade.',
    contexto=[p('Em um sistema de reservas: (1) defeitos no código fazem o sistema falhar, em média, a cada três dias; '
                '(2) quando um dos servidores cai, o sistema continua atendendo normalmente pelos outros; '
                '(3) depois de uma queda geral, os dados e o funcionamento normal são restaurados em dez minutos.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Sobre a evolução da ISO/IEC 9126 para a ISO/IEC 25010, assinale a alternativa INCORRETA.',
    'Na ISO/IEC 25010, a Portabilidade deixou de existir e foi substituída pela nova característica Compatibilidade.',
    [
        'A Funcionalidade da 9126 passou a se chamar Adequação Funcional, com o foco na adequação às necessidades.',
        'A Eficiência da 9126 passou a se chamar Eficiência de Desempenho, um nome considerado mais preciso.',
        'A Manutenibilidade foi mantida e ganhou as subcaracterísticas modularidade e reusabilidade.',
        'A Segurança passou a ser uma característica própria, com confidencialidade, integridade e autenticidade.',
    ],
    'A afirmação incorreta é a da Portabilidade: ela foi mantida na ISO/IEC 25010, com ajustes. A Compatibilidade é uma '
    'característica nova, que reúne coexistência e interoperabilidade, e não substitui nenhuma outra. As demais '
    'alternativas descrevem corretamente o comparativo da apostila: as renomeações, a expansão da manutenibilidade e a '
    'segurança como característica independente.',
    contexto=[p('Uma empresa que avaliava os seus produtos pela ISO/IEC 9126 vai passar a usar a ISO/IEC 25010 e '
                'preparou um resumo das mudanças entre as duas normas.')],
)

banco.afirmativas(
    'dificil',
    [
        ('A análise da complexidade e do acoplamento do código, sem executar o sistema, avalia a qualidade interna.',
         True),
        ('A medição do tempo de resposta durante os testes de sistema avalia a qualidade externa.', True),
        ('As seis características da ISO/IEC 9126 são usadas para avaliar a qualidade em uso.', False),
        ('A pesquisa com os funcionários sobre a produtividade no trabalho real avalia a qualidade em uso.', True),
    ],
    'I é verdadeira: a qualidade interna olha o código e a estrutura, antes da execução. II é verdadeira: a qualidade '
    'externa olha as propriedades observáveis durante a execução. III é falsa: as seis características valem para a '
    'qualidade interna e para a externa; a qualidade em uso tem quatro atributos próprios (efetividade, produtividade, '
    'segurança e satisfação). IV é verdadeira: a produtividade no trabalho real é um desses atributos.',
    contexto=[p('Na avaliação de um sistema de folha de pagamento pela ISO/IEC 9126, a equipe usou três medições: a '
                'análise da complexidade e do acoplamento do código; o tempo de resposta medido nos testes de sistema; e '
                'uma pesquisa com os funcionários do RH sobre a produtividade deles no trabalho do dia a dia.')],
)

banco.assercao(
    'dificil',
    'Um sistema pode ter ótima qualidade interna e, ainda assim, baixa qualidade em uso.',
    'A qualidade interna é medida com o sistema em execução, observando o seu comportamento diante dos usuários.',
    2,
    'A I é verdadeira: código simples, bem estruturado e testado não garante que o sistema resolva a tarefa do usuário '
    'de forma eficiente e satisfatória no trabalho real; são perspectivas diferentes da ISO/IEC 9126. A II é falsa: a '
    'qualidade interna avalia as propriedades do software antes da execução, como o código e a estrutura. O '
    'comportamento em execução é a qualidade externa.',
    contexto=[p('A análise do código de um sistema hospitalar mostrou baixa complexidade, pouco acoplamento e boa '
                'cobertura de testes. Mesmo assim, os enfermeiros reclamam que registrar uma medicação leva sete telas e '
                'que, nos plantões, eles preferem anotar no papel.')],
)

banco.multipla(
    'dificil',
    'Na ISO/IEC 25010, os problemas 1, 2, 3 e 4 afetam, respectivamente, as características',
    'Portabilidade, Compatibilidade, Segurança e Manutenibilidade.',
    [
        'Compatibilidade, Portabilidade, Segurança e Manutenibilidade.',
        'Portabilidade, Compatibilidade, Confiabilidade e Manutenibilidade.',
        'Portabilidade, Adequação Funcional, Segurança e Manutenibilidade.',
        'Manutenibilidade, Compatibilidade, Segurança e Portabilidade.',
    ],
    'Não funcionar em uma nova versão do sistema operacional fere a Portabilidade, a capacidade de ser transferido de um '
    'ambiente para outro (1). Trocar dados errados com o ERP fere a Compatibilidade, que inclui a interoperabilidade (2). '
    'Expor dados de cartão fere a Segurança, que inclui a confidencialidade (3). Não conseguir alterar o código sem '
    'quebrar outras partes fere a Manutenibilidade, que inclui a modificabilidade (4).',
    contexto=[p('A avaliação de um aplicativo de vendas pela ISO/IEC 25010 encontrou quatro problemas: '
                '(1) ele deixou de funcionar na nova versão do sistema operacional dos celulares; '
                '(2) os pedidos enviados ao ERP da empresa chegam com campos trocados; '
                '(3) os números de cartão dos clientes ficam visíveis em um arquivo de log; '
                '(4) qualquer alteração na tela de pagamento quebra outras partes do aplicativo.')],
)

banco.assercao(
    'dificil',
    'Como a ISO/IEC 25010 substituiu a ISO/IEC 9126, uma avaliação feita pela 9126 não diz nada sobre a qualidade do '
    'produto.',
    'A ISO/IEC 25010 é a evolução da 9126: manteve as seis características, renomeando algumas, e acrescentou '
    'Compatibilidade e Segurança.',
    3,
    'A II é verdadeira, e é justamente por ela que a I é falsa. A 25010 evoluiu a partir da 9126, com lições aprendidas '
    'na aplicação da norma anterior: Funcionalidade virou Adequação Funcional, Eficiência virou Eficiência de Desempenho, '
    'e as demais foram mantidas, com ajustes. Uma avaliação pela 9126 continua informando sobre essas características; '
    'o que ela não cobre por completo é o que a 25010 acrescentou, como a Segurança como característica própria.',
    contexto=[p('Uma empresa tem a avaliação de qualidade de um produto feita há alguns anos pela ISO/IEC 9126. Um novo '
                'diretor quer descartá-la por completo, "já que a norma foi substituída".')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '“Modelo de qualidade: conjunto definido de características, e das relações entre elas, que fornece uma '
                   'estrutura para especificar requisitos de qualidade e avaliar a qualidade.” (tradução nossa)',
        'fonte': 'ISO/IEC 25010:2011. Systems and software engineering — Systems and software Quality Requirements and '
                 'Evaluation (SQuaRE) — System and software quality models. Genebra: ISO, 2011.',
    },
    [
        'Uma rede de clínicas vai escolher entre dois fornecedores de sistema de prontuário. Os dois afirmam que o seu '
        'software "tem muita qualidade": o primeiro cita a quantidade de funções; o segundo, a beleza das telas. A '
        'diretoria não sabe como compará-los e está decidindo pela impressão causada nas apresentações.',
    ],
    'Com base no texto e no caso apresentado, explique como a rede de clínicas poderia usar um modelo de qualidade para '
    'comparar os dois sistemas de forma objetiva.',
    'Sem um modelo de referência, a avaliação fica subjetiva: cada fornecedor escolhe o critério que lhe favorece, e '
    'quantidade de funções e beleza das telas não dizem se o sistema atende às necessidades. Um modelo como a ISO/IEC '
    '25010 oferece uma linguagem comum e critérios mensuráveis. Primeiro, a rede escolheria as características mais '
    'importantes para um prontuário: adequação funcional, segurança (os dados de saúde são sensíveis e precisam de '
    'confidencialidade), confiabilidade (o sistema não pode cair no atendimento), usabilidade (para médicos e '
    'recepcionistas) e compatibilidade (para trocar dados com laboratórios). Depois, transformaria cada uma em requisitos '
    'de qualidade com medidas, como tempo de resposta, disponibilidade e tempo para um usuário novo concluir um '
    'cadastro, seguindo as divisões da família SQuaRE: requisitos (2503n), medição (2502n) e avaliação (2504n). Por fim, '
    'avaliaria os dois sistemas pelos mesmos critérios, com testes e demonstrações práticas, e compararia os resultados. '
    'A escolha passaria a se apoiar em dados, e não na impressão causada.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma empresa contratou um sistema de estoque para os seus armazéns. O código foi avaliado como excelente: baixa '
        'complexidade, pouco acoplamento e 90% de cobertura de testes. Nos testes de sistema, todas as funções deram o '
        'resultado esperado, e o tempo de resposta ficou dentro da meta. Três meses depois da implantação, porém, os '
        'operadores dos armazéns levam o dobro do tempo para registrar uma entrada de mercadoria e voltaram a usar '
        'planilhas para algumas tarefas.',
    ],
    'Analise o caso considerando as três perspectivas de qualidade da ISO/IEC 9126 e explique por que os bons '
    'resultados medidos não garantiram o sucesso do sistema.',
    'A ISO/IEC 9126 separa três perspectivas. A qualidade interna, avaliada pelo código e pela estrutura antes da '
    'execução, foi boa: baixa complexidade, pouco acoplamento e alta cobertura de testes. A qualidade externa, observada '
    'durante a execução, também foi boa: as funções deram os resultados certos e o tempo de resposta cumpriu a meta. Mas '
    'a qualidade em uso, que é o resultado do uso no contexto real de trabalho, foi ruim: os operadores levam o dobro do '
    'tempo (baixa produtividade), não completam algumas tarefas no sistema (baixa efetividade) e o trocaram por planilhas '
    '(baixa satisfação). As perspectivas se complementam, mas uma não garante a outra: o sistema faz o que foi '
    'especificado, mas não do jeito que o trabalho real nos armazéns exige. A empresa deveria ter avaliado também a '
    'qualidade em uso, com testes de usabilidade e observação dos operadores no ambiente real antes da implantação, e '
    'acompanhado os atributos de qualidade em uso depois dela.',
)


if __name__ == '__main__':
    banco.gravar()
