# Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, livro, dono):
        self.livro = livro
        self.dono = dono
    
    def informacao(self):
        print(f"Leitor: {self.dono.nome}\nLivro: {self.livro}")

leitor1 = Pessoa("Joana")

meu_livro = Livro("O Timbre", leitor1)

meu_livro.informacao()  #“O livro sabe quem é seu dono, mas o dono pode existir mesmo sem o livro.”
                        #  👉 Isso é associação, não agregação nem composição.

# Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.
class Onibus:
    def __init__(self, tipo):
        self.tipo = tipo

class Aluno:
    def __init__(self, nome, transporte):
        self.nome = nome
        self.transporte = transporte
    
    def registro(self):
        print(f"Estudante {self.nome} utiliza {self.transporte.tipo}")

onibus = Onibus("Ônibus escolar")

aluno1 = Aluno("Maria", onibus)

aluno1.registro()  
print()

#agregação
# Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.
# Departamento deve agregar funcionários já criados.
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome 
        self.funcionarios = []
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def lista_funcionarios(self):
        print(f"---{self.nome}---\n")
        print(f"Quadro de funcionários:")
        for f in self.funcionarios:
            print(f"-{f.nome}")

f1 = Funcionario("Douglas")
f2 = Funcionario("Isabela")

financeiro = Departamento("Departamento Financeiro")

financeiro.adicionar_funcionario(f1)
financeiro.adicionar_funcionario(f2)

financeiro.lista_funcionarios()
print()

#agregação
# Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.
class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self):
        self.equipe = []

    def adicionar_jogador(self, titular):
        self.equipe.append(titular)
    
    def informações_time(self):
        print("Seleção Brasileira de Voleibol\n")
        for a in self.equipe:
            print(f"{a.nome} - {a.posicao}")

j1 = Jogador("Gabriela Guimarães", "Ponta(Capitã)")
j2 = Jogador("Macris Carneiro", "Levantadora")

titulares = Time()

titulares.adicionar_jogador(j1)
titulares.adicionar_jogador(j2)

titulares.informações_time()
print()

#composição
# Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro. Se o Carro deixar de existir, o Motor também deixa. 
# Mostre isso criando e depois apagando o objeto.
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor("Boxer")
    
    def informacao_carro(self):
        print(f"Modelo: {self.modelo}\nMotor: {self.motor.tipo}")

volksvagen = Carro("Fusca")

volksvagen.informacao_carro()
print()

#composição
# Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). Cada Comodo deve ser criado dentro da Casa.
class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = [
            Comodo("Sala"),
            Comodo("Cozinha"),
            Comodo("Quarto"),
            Comodo("Banheiro")
        ]
    
    def informacoes_casa(self):
        print(f"Endereço: {self.endereco}")
        print("Cômodos da casa:")
        for c in self.comodos:
            print(f"- {c.nome}")

minha_casa = Casa("Rua 12, 345")

minha_casa.informacoes_casa()

del minha_casa
print("\nA casa foi deletada — os cômodos também deixaram de existir.")
