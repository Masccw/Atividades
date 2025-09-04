#1
def saudacao():
    print("Olá, seja bem vindo ao Python!")

saudacao()

#2
def dobro(num):
    return num * 2

print(dobro(2))

#3
def soma(num1, num2):
    return num1 + num2

print(soma(10,20))

#4

def mensagem(nome = "visitante"):
     print(f"Olá, {nome}!")

mensagem()
mensagem("Professor Frederico")

#5

def operacoes(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2

somar, subtração, multiplicação = operacoes(1, 2)

print(f"\nsoma: {somar}\nsubtração: {subtração}\nmultiplicação: {multiplicação}\n")

#6

def media(*num):
    medi = sum(num)/len(num)
    return medi
    
print(media(1, 2, 3)) 
print(media(1, 2, 3, 4, 5))
print(media(1, 2, 3, 4, 5, 6, 7))

#7
def dados_pessoais(**dados):
    for chave in dados:
        valor = dados[chave]
        print(f"{chave}: {valor}")

dados_pessoais(nome = "Marina", idade = 18, cidade = "Paulista")

#8

def calculadora(a,b):
    def somar(a,b):
        return a + b
    def subtração(a,b):
        return a - b
    def multiplicar(a,b):
        return a * b
    def dividir(a,b):
        return a / b
    operacao = str(input("Escolha: \n+\n-\n.\n:\n"))
    if operacao == "+":
        return somar(a,b)
    elif operacao == "-":
        return subtração(a,b)
    elif operacao == ".":
        return multiplicar(a,b)
    elif operacao == ":":
        return dividir(a,b)
print(calculadora(1, 2))

#9

def somarr(a,b):
    return a + b
def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a / b
def aplicar_operacao(a,b, tipo = somarr):
    return tipo(a,b)
    
print(aplicar_operacao(2, 2, somarr))
print(aplicar_operacao(2, 2, subtrair))
print(aplicar_operacao(2, 2, multiplicar))
print(aplicar_operacao(2, 2, dividir))
    
          
        

        
    
    