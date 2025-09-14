#1

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
#2
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

pessoa1 = Pessoa("João",18)
pessoa2 = Pessoa("Maria", 20)

print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)

pessoa1.apresentar()
pessoa2.apresentar()

#3

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def __str__(self):
        return f"{self.marca}, {self.modelo}-{self.ano}"

car1 = Carro("Volksvagen", "Gol", 2010)
car2 = Carro("Chevrolet", "Onix", 2015)
car3 = Carro("Fiat", "Strada", 2021) 

print(car1)
print(car2)
print(car3)
#4
car4 = Carro("Hyundai", "HB20", 2022)
print(car4)

car4.ano = 2024
print(car4)
        
#5

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
       self.saldo = self.saldo + valor 
       print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")
          
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
            return True
        else:
            print("Saldo insuficiente")
            return False

conta1 = ContaBancaria("Jonas", 500)

conta1.depositar(500)
#6
if conta1.sacar(200):
    print("Operação realizada com sucesso")
else:
    print("Operação falhou")

#7
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
#8
    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"

class Turma:

    def __init__(self):
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
a1 = Aluno("Joana", 8.0)
a2 = Aluno("Carlos", 7.0)

turma1 = Turma()

turma1.adicionar_aluno(a1)
turma1.adicionar_aluno(a2)

for aluno in turma1.alunos:
    print(aluno)

#9

class Cachorro:
    especie = "Canis Familiaris"
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"

laranja = Cachorro("Laranja", 5)

print(laranja)

print(laranja.especie)
print(Cachorro.especie)






 
    