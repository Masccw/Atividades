#1-5
class Usuario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def exibir_informacoes(self):
        return f"Nome: {self.nome}\nEmail: {self.email}"
    
    def saudacao(self):
        return "Olá, Usuário"

class Cliente(Usuario):

    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

    def saudacao(self):
        return "Olá, cliente"
    
class Funcionario(Usuario):
    pass

class Gerente(Funcionario):
    pass

#6-7
class Autenticacao:

    def login(self):
        print("Login realizado com sucesso")
    
    def status(self):
        return "Status da autenticação"
        
class Permissao:
    
    def verificar_permissao(self):
        print("Permissão verificada")

    def status(self):
        return "Status da permissão"

class Administrador(Autenticacao, Permissao):
    pass

        
cliente1 = Cliente("Joana", "joana@email.com", 130)
print(cliente1.exibir_informacoes())
print(cliente1.saudacao())
print(f"Saldo: {cliente1.saldo}")

gerente1 = Gerente("Jonas", "gerentejonas@email.com")
print(gerente1.exibir_informacoes())

admin1 = Administrador()
admin1.login()
admin1.verificar_permissao()

print(admin1.status())
print(f"Ordem de MRO: {Administrador.__mro__}")

