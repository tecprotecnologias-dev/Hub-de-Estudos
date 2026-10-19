"""
Questões médias e difíceis do capítulo 4 (Programação Orientada a Objetos) de Engenharia de
Software e da Usabilidade: 10 objetivas no estilo de concursos públicos e exames nacionais e
2 discursivas com um único comando. As funções comuns ficam em engsoft_questoes.py.
Uso (dentro de site/):

    python ferramentas/engsoft_cap4_objetivas.py

Grava em src/data/questoes/engsoft.json, trocando só as questões engsoft-cap4-o* e
engsoft-cap4-d*; as que já existiam (engsoft-cap4-q*) e as dos outros capítulos ficam como estão.
"""

from engsoft_questoes import Banco, codigo, p

banco = Banco('engsoft-cap4')


# =====================================================================================
# Médias
# =====================================================================================

banco.multipla(
    'medio',
    'Sobre o modelo descrito, assinale a alternativa correta.',
    'numero, titular e saldo são atributos; depositar() e transferir() são métodos; contaDaAna e contaDoBruno são '
    'objetos.',
    [
        'numero, titular e saldo são métodos; depositar() e transferir() são atributos; ContaCorrente é um objeto.',
        'numero, titular e saldo são atributos; depositar() e transferir() são métodos; ContaCorrente é um objeto.',
        'contaDaAna e contaDoBruno são classes diferentes, pois cada uma tem o seu próprio número e o seu próprio saldo.',
        'numero e titular são atributos, mas saldo é um método, pois o seu valor muda a cada depósito ou transferência.',
    ],
    'Atributos são as características ou dados de um objeto (numero, titular, saldo); métodos são as ações que ele pode '
    'executar (depositar, transferir). ContaCorrente é a classe, o molde, e a classe em si não é um objeto. contaDaAna '
    'e contaDoBruno são objetos, instâncias da mesma classe, cada uma com os seus próprios valores. Um valor que muda '
    'continua sendo um atributo.',
    contexto=[p('Em um sistema bancário, a classe ContaCorrente define numero, titular e saldo, além de depositar() e '
                'transferir(). A partir dela, o sistema cria contaDaAna, com saldo de R$ 500,00, e contaDoBruno, com '
                'saldo de R$ 1.200,00.')],
)

banco.multipla(
    'medio',
    'Para incluir a categoria Estagiario, com a sua própria regra de salário, é preciso:',
    'apenas criar a classe Estagiario com o seu método calcular_salario(); a função folha() não precisa mudar.',
    [
        'alterar a função folha(), incluindo um teste para descobrir se cada funcionário é um Estagiario ou não.',
        'criar a classe Estagiario e copiar para dentro dela o código de Gerente, ajustando o cálculo do salário.',
        'alterar a classe Funcionario, incluindo nela a regra de salário do estagiário, ao lado das outras regras.',
        'reescrever Gerente e Vendedor, pois cada nova categoria obriga a mudar todas as subclasses já existentes.',
    ],
    'A função folha() trabalha com a abstração Funcionario e chama calcular_salario() de cada objeto, sem saber o tipo '
    'exato; cada objeto responde com o seu próprio cálculo. Esse é o poder do polimorfismo: para incluir Estagiario, '
    'basta criar a classe e implementar o método esperado, e o restante do código funciona sem nenhuma modificação.',
    contexto=[
        p('Observe o código abaixo, escrito em Python.'),
        codigo('''
class Funcionario:
    def calcular_salario(self):
        return 3000

class Gerente(Funcionario):
    def calcular_salario(self):
        return 3000 + 2000

class Vendedor(Funcionario):
    def calcular_salario(self):
        return 2000 + self.comissao

def folha(funcionarios):
    total = 0
    for f in funcionarios:
        total += f.calcular_salario()
    return total
'''),
    ],
)

banco.assercao(
    'medio',
    'O sistema não pode criar diretamente um objeto da classe Pagamento.',
    'As classes abstratas servem como base para outras classes e não podem ser instanciadas diretamente.',
    0,
    'As duas são verdadeiras, e a II explica a I. Pagamento é abstrata: ela define o que todo pagamento deve ter, como o '
    'método processar(), mas não diz como. Quem é instanciado são as classes concretas, como CartaoCredito, Pix e '
    'Boleto, cada uma processando à sua maneira. É assim que a abstração se manifesta como pilar da POO.',
    contexto=[p('Em uma loja virtual, Pagamento é uma classe abstrata com o método processar(). As classes CartaoCredito, '
                'Pix e Boleto herdam de Pagamento e implementam processar() cada uma à sua maneira. Um desenvolvedor '
                'novo tentou criar um objeto escrevendo Pagamento() e o programa recusou.')],
)

banco.multipla(
    'medio',
    'As relações 1, 2, 3 e 4 devem ser modeladas, respectivamente, com',
    'herança, composição, herança e composição.',
    [
        'composição, herança, herança e composição.',
        'herança, herança, herança e composição.',
        'herança, composição, composição e herança.',
        'composição, composição, herança e herança.',
    ],
    'A herança deve ser usada quando há uma relação genuína "é um": Gerente é um Funcionario (1) e Labrador é um Cachorro '
    '(3). Quando a relação é "tem um", a composição é mais flexível: um Carro tem um Motor (2) e um Pedido tem itens (4). '
    'A apostila usa exatamente os exemplos de Gerente e Funcionario, Animal, Cachorro e Labrador, e Carro com Motor.',
    contexto=[p('Ao modelar um sistema, uma equipe precisa decidir como representar quatro relações: '
                '(1) Gerente e Funcionario; (2) Carro e Motor; (3) Labrador e Cachorro; (4) Pedido e ItemPedido.')],
)

banco.afirmativas(
    'medio',
    [
        ('A herança é menos flexível, pois a relação entre as classes é estática.', True),
        ('A composição deve ser usada quando a relação entre as classes é do tipo "é um".', False),
        ('Na herança, o acoplamento é alto, pois a subclasse conhece a superclasse.', True),
    ],
    'I é verdadeira: a herança é estática, definida no código, e por isso menos flexível; na composição, os componentes '
    'podem ser trocados. II é falsa: a composição é para a relação "tem um"; a relação "é um" é a da herança. III é '
    'verdadeira: a subclasse conhece a superclasse, o que gera acoplamento alto, enquanto na composição os objetos '
    'compostos são independentes.',
    contexto=[p('Em uma revisão de código, a equipe comparou herança e composição para decidir como modelar os '
                'acessórios de um carro.')],
)

# =====================================================================================
# Difíceis
# =====================================================================================

banco.multipla(
    'dificil',
    'Ao executar o código, o programa exibe e o conceito que explica esse resultado são:',
    '"Pix de 10", "Boleto de 10" e "Pix de 10"; o polimorfismo por sobrescrita.',
    [
        '"genérico" três vezes; o encapsulamento, que esconde as subclasses.',
        '"Pix de 10", "Boleto de 10" e "Pix de 10"; o polimorfismo por sobrecarga.',
        '"genérico", "Boleto de 10" e "genérico"; a herança, pois Pix herda o método.',
        'um erro, pois a lista mistura objetos de classes diferentes; a abstração.',
    ],
    'Cada objeto executa a sua própria versão de processar(): Pix e Boleto redefinem o método herdado de Pagamento com a '
    'mesma assinatura, o que é sobrescrita. Por isso a mesma chamada, p.processar(10), produz resultados diferentes '
    'conforme o objeto, que é o polimorfismo. Sobrecarga seria a mesma classe ter métodos com o mesmo nome e parâmetros '
    'diferentes. A lista pode misturar os objetos, pois todos são Pagamento.',
    contexto=[
        p('Observe o código abaixo, escrito em Python.'),
        codigo('''
class Pagamento:
    def processar(self, valor):
        return "genérico"

class Pix(Pagamento):
    def processar(self, valor):
        return f"Pix de {valor}"

class Boleto(Pagamento):
    def processar(self, valor):
        return f"Boleto de {valor}"

for p in [Pix(), Boleto(), Pix()]:
    print(p.processar(10))
'''),
    ],
)

banco.afirmativas(
    'dificil',
    [
        ('Uma classe obrigada a implementar métodos que deixa com o corpo vazio indica violação da Segregação de '
         'Interfaces.', True),
        ('Um bloco if/else que cresce a cada novo tipo indica violação da Inversão de Dependência.', False),
        ('O uso de new ConcreteClass() dentro de uma classe de alto nível indica violação da Inversão de Dependência.',
         True),
        ('Uma subclasse que lança exceção em um método herdado indica violação da Substituição de Liskov.', True),
    ],
    'I é verdadeira: métodos com corpo vazio mostram uma interface grande demais, que obriga a classe a depender do que '
    'não usa. II é falsa: o if/else crescente a cada novo tipo é o indicador de violação do Aberto/Fechado, e não da '
    'Inversão de Dependência. III é verdadeira: criar a implementação concreta dentro da classe de alto nível a prende '
    'aos detalhes. IV é verdadeira: a subclasse que recusa um método herdado não pode substituir a superclasse.',
    contexto=[p('Para ajudar a equipe nas revisões de código, a líder técnica montou uma lista de sinais que indicam a '
                'violação de cada princípio SOLID.')],
)

banco.assercao(
    'dificil',
    'A classe Paciente do hospital deve ter exatamente os mesmos atributos que a classe Cliente da loja virtual, pois as '
    'duas representam pessoas.',
    'A abstração consiste em focar apenas no que é relevante para o problema, ignorando os detalhes desnecessários.',
    3,
    'A II é a definição correta de abstração, e é por ela que a I é falsa. O que é relevante depende do problema: para o '
    'hospital, importam dados como tipo sanguíneo, alergias e convênio; para a loja, endereço de entrega e histórico de '
    'compras. Duas classes que representam pessoas podem, e devem, ter atributos diferentes quando servem a problemas '
    'diferentes.',
    contexto=[p('Uma empresa que já tem uma loja virtual vai criar um sistema para um hospital. Para economizar tempo, um '
                'desenvolvedor propôs copiar a classe Cliente da loja, com nome, CPF, endereço de entrega e histórico de '
                'compras, e usá-la como a classe Paciente do hospital.')],
)

banco.multipla(
    'dificil',
    'A análise correta do problema é:',
    'Pilha não "é uma" lista com acesso livre; ela "tem uma" lista, e a composição expõe só empilhar e desempilhar.',
    [
        'O código está correto, pois toda pilha é uma lista e, por isso, deve herdar todos os métodos da classe list.',
        'O problema é de sobrecarga, que se resolve criando uma segunda versão do método insert() com outros parâmetros.',
        'A solução é documentar que os outros desenvolvedores não devem usar insert() nem remove() em objetos Pilha.',
        'A herança está certa, e a falha vem só da falta de testes unitários que confiram a ordem dos elementos da pilha.',
    ],
    'Ao herdar de list, a Pilha recebe todos os métodos da lista, como insert() e remove(), que permitem mexer no meio e '
    'quebram a regra de que só o topo é acessado. A relação não é um "é um" genuíno. Com composição, a Pilha guarda uma '
    'lista como atributo privado e expõe só empilhar() e desempilhar(), protegendo a regra, o que também é '
    'encapsulamento. Documentar ou testar não impede o uso errado.',
    contexto=[
        p('Um desenvolvedor criou a classe abaixo, em Python, para representar uma pilha, em que o último elemento a '
          'entrar deve ser o primeiro a sair.'),
        codigo('''
class Pilha(list):
    def empilhar(self, item):
        self.append(item)

    def desempilhar(self):
        return self.pop()
'''),
        p('Pouco depois, outros módulos passaram a usar pilha.insert(0, item) e pilha.remove(item), colocando e tirando '
          'elementos do meio da pilha.'),
    ],
)

banco.multipla(
    'dificil',
    'Sobre os pilares da POO, assinale a alternativa INCORRETA.',
    'A sobrecarga ocorre quando a subclasse redefine um método herdado, mantendo exatamente a mesma assinatura.',
    [
        'No encapsulamento, os métodos públicos que dão acesso aos atributos privados podem validar os dados antes de '
        'aceitá-los.',
        'Uma interface é um contrato que define quais métodos uma classe deve implementar, sem especificar como.',
        'A subclasse pode acrescentar novos atributos e métodos, além de sobrescrever os métodos que herdou.',
        'Uma classe é o molde a partir do qual os objetos são criados, e a classe em si não é um objeto.',
    ],
    'A afirmação incorreta é a da sobrecarga: redefinir um método herdado com a mesma assinatura é a sobrescrita '
    '(override). A sobrecarga (overload) é a mesma classe definir métodos com o mesmo nome e parâmetros diferentes. As '
    'demais estão corretas: getters e setters podem validar os dados, a interface define o contrato, a subclasse pode '
    'acrescentar e sobrescrever, e a classe é o molde, e não um objeto.',
    contexto=[p('Em uma monitoria de POO, os alunos escreveram afirmações sobre os quatro pilares para revisar a matéria.')],
)

# =====================================================================================
# Discursivas: um único comando (sem itens a, b, c...), com a resposta esperada
# =====================================================================================

banco.discursiva(
    'dificil',
    {
        'citacao': '"OOP to me means only messaging, local retention and protection and hiding of state-process, and '
                   'extreme late-binding of all things."',
        'traducao': '(Tradução livre: "Para mim, POO significa apenas troca de mensagens, retenção local, proteção e '
                    'ocultação do estado e do processo, e vinculação tardia extrema de todas as coisas.")',
        'fonte': 'KAY, A. Mensagem a Stefan Ram sobre o significado de "programação orientada a objetos", 2003. Alan Kay '
                 'é um dos criadores do Smalltalk.',
    },
    [
        'O sistema de notas de uma escola foi escrito sem orientação a objetos: as notas de todos os alunos ficam em '
        'listas globais, e qualquer função do programa pode alterá-las. Na semana passada, uma função de relatórios '
        'apagou sem querer as notas de uma turma inteira, e ninguém consegue descobrir qual das 80 funções fez isso. '
        'Para cada novo tipo de avaliação (prova, trabalho, seminário), a equipe acrescenta mais um if em várias funções.',
    ],
    'Com base no texto de Kay e no caso apresentado, explique como a orientação a objetos ajudaria a organizar esse '
    'sistema e a evitar os problemas relatados.',
    'O problema central é que o estado, as notas, está exposto a todo o programa, que é o contrário da "proteção e '
    'ocultação do estado" de que fala Kay. Na POO, o sistema seria modelado como objetos que trocam mensagens. Uma classe '
    'Aluno (ou Boletim) guardaria as notas como atributos privados, e a única forma de alterá-las seria pelos seus '
    'métodos públicos, como lancar_nota(), que validam os dados antes de aceitá-los. Isso é o encapsulamento: nenhuma '
    'função de relatório poderia apagar notas diretamente, e, se algo der errado, o problema fica restrito aos métodos '
    'da própria classe. Para os tipos de avaliação, uma classe abstrata ou interface Avaliacao definiria um método como '
    'calcular_peso(), sobrescrito em Prova, Trabalho e Seminario. Pelo polimorfismo, o código chama o mesmo método sem '
    'saber o tipo, e um novo tipo de avaliação passa a ser só uma nova classe, sem mais ifs espalhados.',
)

banco.discursiva(
    'dificil',
    None,
    [
        'Um desenvolvedor recém-formado decidiu aplicar todos os princípios SOLID a um pequeno programa que lê uma '
        'planilha e envia, uma vez por mês, um e-mail com o total de vendas. O programa, que caberia em cerca de 50 '
        'linhas, passou a ter 18 classes e 12 interfaces, cada uma com um único método, e até a leitura do nome do '
        'arquivo ganhou uma interface própria. Os colegas reclamam que ninguém entende mais o programa, e uma alteração '
        'simples no texto do e-mail exigiu mexer em seis arquivos.',
    ],
    'Analise a decisão do desenvolvedor à luz do que a apostila diz sobre os princípios SOLID e explique como eles '
    'deveriam ser aplicados nesse caso.',
    'A apostila lembra que os princípios SOLID não são regras rígidas: são guias de design para tornar o código mais '
    'limpo, flexível e testável. O objetivo deles é facilitar a manutenção; quando a aplicação produz o efeito '
    'contrário, como uma mudança simples exigir seis arquivos, o design ficou mais complexo do que o problema. Cada '
    'princípio resolve um problema específico, que deve existir de fato: o Aberto/Fechado combate o if/else que cresce '
    'a cada novo tipo, a Inversão de Dependência combate classes de alto nível presas a implementações concretas, e a '
    'Segregação de Interfaces combate interfaces gordas. Em um programa pequeno, estável e com uma única tarefa, quase '
    'nenhum desses problemas aparece. Uma aplicação equilibrada separaria só as responsabilidades que mudam por motivos '
    'diferentes, como ler a planilha, calcular o total e enviar o e-mail, em poucas classes, e criaria abstrações '
    'apenas onde há chance real de troca, por exemplo se o envio por e-mail puder virar WhatsApp. Os indicadores de '
    'violação da apostila servem para decidir quando aplicar cada princípio, e não para aplicá-los em tudo.',
)


if __name__ == '__main__':
    banco.gravar()
