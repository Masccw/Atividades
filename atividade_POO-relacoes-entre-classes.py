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

        

# Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.Departamento deve agregar funcionários já criados.

# Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.

# Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro. Se o Carro deixar de existir, o Motor também deixa. Mostre isso criando e depois apagando o objeto.

# Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). Cada Comodo deve ser criado dentro da Casa.