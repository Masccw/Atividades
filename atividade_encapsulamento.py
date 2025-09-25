#1
class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print("O saldo não pode ser negativo")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido para depósito")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido")

conta = ContaBancaria("Joana", 1000)

print(conta.get_saldo())
conta.depositar(500)
conta.sacar(300)
print(conta.get_saldo())

#2
class Pessoa:
    def __init__(self, nome, data_de_nascimento, cpf, identidade):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        if 10000000000 < novo_cpf <= 99999999999:
            self.__cpf = novo_cpf
        else:
            print("CPF inválido")

    def get_identidade(self):
        return self.__identidade
    
    def set_identidade(self, nova_identidade):
        if 100000000 < nova_identidade <= 999999999:
            self.__identidade = nova_identidade 
        else:
            print("Identidade inválida")
 
pessoa = Pessoa("Jonas", "01/01/2001", 12345689010, 123456789)

print(pessoa.get_cpf())
print(pessoa.get_identidade())

pessoa.set_cpf(12312312333)
pessoa.set_identidade(123123)




