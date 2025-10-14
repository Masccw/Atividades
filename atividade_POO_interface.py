# Criando uma interface
# Crie uma interface chamada Pagamento com um método abstrato processar(valor). 
# Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. 
# Mostre como chamar processar() para cada uma.
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor: float):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor: float):
        print(f"Processando o valor de R$ {valor},00 no cartão de crédito")

class Boleto(Pagamento):
    def processar(self, valor: float):
        print(f"Processando o valor de R$ {valor},00 no boleto")

pag1 = CartaoCredito()
pag2 = Boleto()

pag1.processar(20)
pag2.processar(20)

# Interface múltipla
# Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). 
# Crie uma classe Computador que implemente ambas. Mostre seu uso.
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Ligando o computador")
    
    def desligar(self):
        print("Desligando o computador")

PC = Computador()

PC.ligar()
PC.desligar()

# Interface em herança múltipla
# Crie uma interface Imprimivel com o método imprimir(). 
# Crie outra interface Exportavel com o método exportar(). 
# Implemente uma classe Relatorio que herde de ambas e implemente os métodos
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("Imprimindo relatório")
    
    def exportar(self):
        print("Exportando relatório")

r1 = Relatorio()

r1.imprimir()
r1.exportar()

# Forçando contrato
# Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). 
# Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. 
# O que acontece quando você tenta instanciá-la? Corrija o código.
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Salvando objeto {objeto}")

class RepositorioMemoriaCorrigido(Repositorio):
    def salvar(self, objeto):
        print(f"Salvando objeto {objeto}")
    
    def buscar(self, id):
        print(f"Buscando ID {id}")

# re = RepositorioMemoria()
rm = RepositorioMemoriaCorrigido()

# re.salvar()

rm.salvar(rm)
rm.buscar(1)


