#1

try:
    num = int(input("Digite um número inteiro: "))
except ValueError:
    print("Digite apenas números inteiros")

#2

try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    m = n1 * n2
    print(m)
except ValueError:
    print("Resposta inválida. Tente de novo.")

#3

try:
    n = int(input("Digite um número inteiro: "))
except ValueError:
    print("Digite apenas números inteiros")
else:
    print(f"Você digitou: {n}")

#4

try:
    open("dados.txt", "r")
except:
    print("Erro")
finally:
    print("Encerrando programa")

#5

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Número tem que ser diferente de zero")
    return a/b

print(dividir(2,1))

#6

class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade tem que ser maior que zero.")
    print(f"Idade {idade} cadastrada com sucesso.")

try:
    idade_usuario = int(input("Digite sua idade: "))
    cadastrar_idade(idade_usuario)
except ValueError:
    print("Resposta inválida")
except IdadeInvalidaError as e:
    print(f"erro: {e}")

#7

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    d = num1 / num2
    print(d)
except ValueError:
    print("Resposta inválida. Tente de novo.")
except ZeroDivisionError:
    print("Não é possível dividir por zero. Tente de novo.")

#8

try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Número inválido. Tente de novo.")
else:
    if numero % 2 == 0:
        print("O Número é par.")
    else:
        print("O número é ímpar.")
finally:
    print("Fim do programa")


#9


