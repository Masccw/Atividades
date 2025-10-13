# Definição de classe abstrata
# Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). 
# Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. 
# Mostre o uso criando objetos e chamando o método falar().
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("AUAU")

class Gato(Animal):
    def falar(Self):
        print("MIAUMIAU")

salsicha = Cachorro()
laranja = Gato()

salsicha.falar()
laranja.falar()

# Proibição de instanciamento
# Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.
animal = Animal() #A classe não pode ser instanciada por esse objeto, porque ela é uma classe abstrata, ou seja, serve como um esqueleto para outras classes e não tem o poder de colocar algo em prática. Então, precisa de uma classe filha para ser exercida.

# Múltiplos métodos abstratos
# Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: area() e perimetro(). 
# Crie uma classe concreta Retangulo que herde de FormaGeometrica e implemente os dois métodos. 
# Teste criando um objeto e calculando sua área e perímetro.

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self, num1, num2):
        pass
    @abstractmethod
    def perimetro(self, num1, num2):
        pass

class Retangulo(FormaGeometrica):
    def area(self, num1, num2):
        return num1 * num2
    
    def perimetro(self, num1, num2):
        return (num1 * 2) + (num2 * 2)
    
r1 = Retangulo()

print(r1.area(2, 2))
print(r1.perimetro(2, 2))
    
# Herança parcial
# Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar(). 
# Depois, crie uma subclasse Carro que implemente apenas o método mover(). 
# O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        print("O motor ligado e o carro começou a se mover")

class Fiat(Carro):
    def parar(self):
        print("O motor desligou e o carro parou")

car1 = Carro() # Aparece: TypeError: Can't instantiate abstract class Carro with abstract method parar
mobi = Fiat()

mobi.mover()
mobi.parar()


