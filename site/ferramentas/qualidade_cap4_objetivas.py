"""
Questões médias e difíceis do capítulo 4 (Testes de Software) de Qualidade e Testes de Software:
10 objetivas no estilo de concursos públicos e exames nacionais e 2 discursivas com um único comando.
As funções comuns ficam em engsoft_questoes.py. Uso (dentro de site/):

    python ferramentas/qualidade_cap4_objetivas.py

Grava em src/data/questoes/qualidade.json, trocando só as questões qualidade-cap4-o* e
qualidade-cap4-d*; as que já existiam (q* e m*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import QUALIDADE, Banco, codigo, p

banco = Banco('qualidade-cap4', QUALIDADE)


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'As atividades 1, 2 e 3 são, respectivamente, de',
    'verificação, validação e verificação.',
    [
        'validação, verificação e verificação.',
        'verificação, verificação e validação.',
        'validação, validação e verificação.',
        'verificação, validação e validação.',
    ],
    'A verificação responde "estamos construindo o produto corretamente?", conferindo o software com as especificações: '
    'checar se o imposto segue a fórmula dos requisitos (1) e se o código segue o padrão definido (3). A validação '
    'responde "estamos construindo o produto correto?", conferindo se ele atende às necessidades reais: perguntar se o '
    'sistema é útil para o contador no dia a dia (2). O exemplo do imposto e do contador é o da própria apostila.',
    contexto=[p('Na avaliação de um sistema de cálculo de impostos: '
                '(1) um testador confere se o imposto é calculado exatamente conforme a fórmula definida nos requisitos; '
                '(2) um grupo de contadores usa o sistema por uma semana para dizer se ele é útil no trabalho do dia a dia; '
                '(3) um revisor confere se o código segue o padrão de codificação da empresa.')],
)

banco.multipla(
    'medio',
    'Pela tabela de custo relativo de correção da apostila, quanto custaria, aproximadamente, corrigir o mesmo defeito '
    'se ele fosse encontrado nos testes internos?',
    'Entre R$ 10.000 e R$ 20.000, pois nos testes internos o custo é de 20 a 40 vezes o da fase de requisitos.',
    [
        'Entre R$ 1.500 e R$ 3.000, pois nos testes internos o custo é de 3 a 6 vezes o da fase de requisitos.',
        'Cerca de R$ 5.000, pois nos testes internos o custo é de 10 vezes o da fase de requisitos.',
        'Entre R$ 20.000 e R$ 50.000, pois nos testes internos o custo é de 40 a 100 vezes o da fase de requisitos.',
        'Os mesmos R$ 500, pois o custo de corrigir um defeito não depende da fase em que ele é encontrado.',
    ],
    'Pela tabela da apostila, com o custo nos requisitos valendo 1x: design custa de 3x a 6x; codificação, 10x; testes '
    'internos, de 20x a 40x; e produção, de 40x a 100x. Com R$ 500 nos requisitos, os testes internos custariam de R$ '
    '10.000 a R$ 20.000. Por isso os testes devem deslocar a detecção para as fases mais baratas.',
    contexto=[p('Um requisito ambíguo foi identificado em uma revisão e corrigido ao custo de R$ 500. A equipe quer '
                'mostrar à diretoria quanto o mesmo problema custaria se tivesse sido descoberto mais tarde.')],
)

banco.multipla(
    'medio',
    'No teste de sistema, as verificações 1, 2, 3 e 4 correspondem, respectivamente, aos testes de',
    'recuperação, compatibilidade, segurança e desempenho.',
    [
        'desempenho, compatibilidade, segurança e recuperação.',
        'recuperação, usabilidade, segurança e desempenho.',
        'recuperação, compatibilidade, funcionais e desempenho.',
        'segurança, compatibilidade, recuperação e desempenho.',
    ],
    'Ver como o sistema se comporta e se recupera depois de uma falha é o teste de recuperação (1). Garantir que funcione '
    'em diferentes navegadores e dispositivos é o de compatibilidade (2). Procurar vulnerabilidades, como injeção de SQL '
    'e XSS, é o de segurança (3). Avaliar o tempo de resposta e o consumo de recursos sob carga é o de desempenho (4).',
    contexto=[p('No teste de sistema de um portal de matrículas, a equipe planejou quatro verificações: '
                '(1) desligar o banco de dados por alguns minutos e ver se o portal volta a funcionar sozinho; '
                '(2) acessar o portal no Chrome, no Firefox, no Safari e em celulares; '
                '(3) tentar injetar comandos SQL e scripts nos campos dos formulários; '
                '(4) medir o tempo de resposta com 2.000 alunos acessando ao mesmo tempo.')],
)

banco.afirmativas(
    'medio',
    [
        ('No UAT, os usuários finais validam se o sistema atende às necessidades reais do negócio.', True),
        ('No teste de contrato, a equipe técnica e o cliente verificam se o sistema cumpre os termos do contrato.', True),
        ('O teste de regulamentação é feito apenas pela equipe de desenvolvimento, sem a participação de órgãos externos.',
         False),
        ('No teste beta, usuários externos selecionados usam o sistema para dar feedback antes do lançamento oficial.', True),
    ],
    'I, II e IV estão de acordo com a tabela de modalidades do teste de aceitação da apostila. III é falsa: o teste de '
    'regulamentação é conduzido por um órgão regulador ou auditor, para verificar a conformidade com leis, normas e '
    'regulamentos, e o seu resultado é uma certificação ou homologação.',
    contexto=[p('Antes de colocar em produção um sistema para uma operadora de saúde, a equipe planejou as diferentes '
                'modalidades de teste de aceitação.')],
)

banco.assercao(
    'medio',
    'Um beta aberto tende a gerar um volume maior de feedback e a testar a escalabilidade em condições reais.',
    'No beta aberto, somente os usuários convidados pela empresa têm acesso ao software.',
    2,
    'A I é verdadeira: no beta aberto, qualquer usuário pode participar, o que gera mais feedback e expõe o sistema a uma '
    'carga real. A II é falsa: o acesso restrito a convidados é o beta fechado, comum em jogos e aplicativos que querem '
    'controlar a experiência inicial.',
    contexto=[p('Uma empresa de jogos vai lançar um novo título e discute se abre a versão beta para qualquer pessoa ou só '
                'para jogadores convidados.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Com os dois testes abaixo, qual cobertura a função atinge?',
    '100% de declarações e de desvios, mas não de condições, pois a condição score > 700 nunca foi falsa.',
    [
        '100% de declarações, de desvios e de condições, pois o if foi verdadeiro em um teste e falso no outro.',
        'Apenas 50% de declarações, pois cada teste executa só um dos dois return da função.',
        '100% de condições, mas não de desvios, pois a decisão do if foi avaliada só uma vez como falsa.',
        '100% de caminhos, pois a função tem apenas dois caminhos e os dois foram percorridos pelos testes.',
    ],
    'O primeiro teste entra no if e executa o "aprovado"; o segundo não entra e executa o "negado": todas as linhas '
    'rodaram (declarações) e a decisão foi verdadeira e falsa (desvios). A cobertura de condições exige que cada condição '
    'booleana seja avaliada como verdadeira e como falsa: renda > 3000 foi verdadeira e falsa, mas score > 700 só foi '
    'verdadeira. Faltaria um teste como aprovar(5000, 500).',
    contexto=[
        p('Observe a função abaixo, escrita em Python, e os dois testes executados.'),
        codigo('''
def aprovar(renda, score):
    if renda > 3000 and score > 700:
        return "aprovado"
    return "negado"

assert aprovar(5000, 800) == "aprovado"
assert aprovar(1000, 800) == "negado"
'''),
    ],
)

banco.afirmativas(
    'dificil',
    [
        ('A caixa branca não detecta funcionalidades ausentes, pois o que não foi implementado não pode ser testado.', True),
        ('A principal métrica da caixa preta é a cobertura de código, como a cobertura de desvios.', False),
        ('A cobertura de caminhos é o critério mais simples e menos rigoroso da caixa branca.', False),
        ('No mercado, uma cobertura de desvios acima de 80% costuma ser considerada uma boa prática.', True),
    ],
    'I é verdadeira: é a limitação chave da caixa branca na apostila. II é falsa: a principal métrica da caixa preta é a '
    'cobertura de requisitos, o percentual de requisitos cobertos por casos de teste; a cobertura de código é a da caixa '
    'branca. III é falsa: a cobertura de caminhos é a mais completa e pode ser inviável em códigos complexos; a mais '
    'simples é a de declarações. IV é verdadeira: é o padrão de mercado citado.',
    contexto=[p('Ao comparar as técnicas de caixa branca e de caixa preta, uma equipe reuniu algumas afirmações sobre as '
                'métricas e as limitações de cada uma.')],
)

banco.multipla(
    'dificil',
    'Qual estratégia de integração é a mais adequada e como lidar com os módulos que ainda não estão prontos?',
    'A top-down: começa pelos módulos de nível mais alto, já prontos, e usa stubs no lugar dos módulos de base que '
    'faltam.',
    [
        'A bottom-up: começa pelos módulos de base, mesmo que não estejam prontos, e deixa a interface para o fim.',
        'O Big Bang: espera todos os módulos ficarem prontos e integra tudo de uma vez, pois é a opção mais rápida.',
        'A top-down: começa pelos módulos de base e usa drivers no lugar da interface e do fluxo, ainda incompletos.',
        'Nenhuma: a integração só pode começar quando todos os módulos tiverem passado nos testes de sistema.',
    ],
    'A integração top-down começa pelos módulos de nível mais alto, como a interface, e desce, e é indicada quando o '
    'design de alto nível está consolidado. Os módulos de nível mais baixo que ainda não existem são substituídos por '
    'stubs, que simulam as suas respostas. A bottom-up começa pela base e é indicada quando os módulos de base estão '
    'prontos e estáveis, o oposto do caso.',
    contexto=[p('Em um sistema de reservas, a interface e o módulo que controla o fluxo das reservas já estão prontos e '
                'estáveis. Os módulos de nível mais baixo, de pagamento e de envio de e-mails, ainda estão em '
                'desenvolvimento, mas a equipe quer começar a testar a integração agora.')],
)

banco.multipla(
    'dificil',
    'Qual conjunto de casos de teste está de acordo com o exemplo de teste unitário da apostila?',
    '(100, 10) retorna 90; (200, 50) retorna 100; (100, 0) retorna 100; e (100, -5) lança uma exceção de valor inválido.',
    [
        '(100, 10) retorna 90; (200, 10) retorna 180; (300, 10) retorna 270; e (400, 10) retorna 360.',
        '(100, 10) retorna 90, pois um único caso que passa já mostra que a função está correta para qualquer valor.',
        '(100, 10) retorna 90; (200, 50) retorna 100; e (100, -5) retorna 105, pois um desconto negativo vira acréscimo.',
        '(100, 10) retorna 90 e (100, -5) lança uma exceção, testados com a função integrada ao carrinho e ao banco de dados.',
    ],
    'O exemplo da apostila combina casos válidos com percentuais diferentes, o caso sem desconto (percentual 0) e um valor '
    'inválido, que deve lançar exceção. Repetir o mesmo percentual não acrescenta cobertura, um caso só não basta, e '
    'aceitar um desconto negativo como acréscimo seria um defeito. O teste unitário verifica a função isolada, sem '
    'depender de outros módulos nem de banco de dados.',
    contexto=[p('Uma desenvolvedora vai escrever os testes unitários da função calcularDesconto(preco, percentual), que '
                'aplica um percentual de desconto a um preço.')],
)

banco.multipla(
    'dificil',
    'Sobre as boas práticas de testes de software, assinale a alternativa INCORRETA.',
    'Os casos de teste não precisam ser documentados, pois a rastreabilidade entre requisitos e testes é dispensável.',
    [
        'Os testes unitários e de regressão devem ser automatizados e integrados ao pipeline de CI/CD.',
        'O planejamento dos testes deve fazer parte do planejamento do projeto, e não ficar para o fim do ciclo.',
        'Os dados de teste devem refletir a diversidade dos dados reais, incluindo casos extremos e valores inválidos.',
        'Os casos de teste devem ser revisados periodicamente, para evitar o paradoxo do pesticida.',
    ],
    'A afirmação incorreta é a da documentação: a apostila recomenda documentar os casos de teste, pois isso permite a '
    'rastreabilidade entre requisitos e testes e facilita a manutenção. As demais alternativas estão na lista de boas '
    'práticas do capítulo, junto com a de combinar as técnicas de caixa branca e caixa preta.',
    contexto=[p('Uma equipe nova de QA está escrevendo o seu guia de boas práticas de teste.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    None,
    [
        'Uma loja virtual tem a seguinte regra de frete: pedidos de R$ 0,01 até R$ 99,99 pagam frete cheio; de R$ 100,00 '
        'até R$ 499,99 têm frete grátis; e a partir de R$ 500,00 têm frete grátis e um brinde. Valores iguais ou menores '
        'que zero devem ser rejeitados. Um testador escreveu só três casos: R$ 50,00, R$ 300,00 e R$ 800,00.',
    ],
    'Com base nas técnicas de particionamento de equivalência e de análise do valor limite, avalie os casos do testador '
    'e proponha um conjunto de casos de teste adequado para essa regra.',
    'Os três casos cobrem uma representante de cada faixa válida, mas deixam de fora a partição inválida (zero ou '
    'negativo) e as fronteiras, onde os defeitos são mais frequentes, como trocar um >= por um >. Pelo particionamento, há '
    'quatro partições: inválida (valor menor ou igual a 0), frete cheio (0,01 a 99,99), frete grátis (100,00 a 499,99) e '
    'frete grátis com brinde (500,00 ou mais); um representante de cada, por exemplo -10,00, 50,00, 300,00 e 800,00. Pela '
    'análise do valor limite, testam-se o valor no limite, o imediatamente abaixo e o imediatamente acima de cada '
    'fronteira: 0,00 (rejeitado), 0,01 e 0,02 (frete cheio); 99,99 (frete cheio), 100,00 e 100,01 (frete grátis); 499,99 '
    '(frete grátis), 500,00 e 500,01 (frete grátis com brinde). Para cada caso, o resultado esperado deve estar definido '
    'de forma clara.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Uma startup vai lançar um aplicativo de pagamentos por celular. Até agora, os desenvolvedores só testaram as telas '
        'manualmente, ao fim de cada funcionalidade. O sistema tem um módulo de cálculo de tarifas, já pronto e estável, um '
        'módulo de integração com os bancos, ainda em desenvolvimento, e a interface do aplicativo. O lançamento para o '
        'público está previsto para daqui a quatro meses.',
    ],
    'Proponha um plano de testes para esse aplicativo, organizado pelos níveis de teste estudados no capítulo.',
    'No nível unitário, os desenvolvedores testariam as funções isoladas, como o cálculo de tarifas, com JUnit, PyTest '
    'ou Jest, de preferência com TDD, cobrindo casos válidos, limites e valores inválidos; esses testes formam a base da '
    'pirâmide. Na integração, como o módulo de tarifas está pronto e estável e a integração com os bancos ainda não, a '
    'estratégia bottom-up faz sentido, começando pelos módulos de base, e o módulo bancário pode ser simulado até ficar '
    'pronto. No teste de sistema, em ambiente parecido com o de produção, entrariam os testes funcionais, de desempenho '
    '(muitos pagamentos ao mesmo tempo), de segurança (por se tratar de dinheiro), de usabilidade, de recuperação e de '
    'compatibilidade com os diferentes celulares. Na aceitação, o UAT com usuários e o teste de regulamentação, se o '
    'serviço exigir; depois, um teste alfa com usuários internos e, por fim, um teste beta, fechado e depois aberto, '
    'antes do lançamento oficial. A distribuição deve seguir a pirâmide, com muitos unitários e poucos testes de '
    'interface, combinando caixa branca e caixa preta.',
)


if __name__ == '__main__':
    banco.gravar()
