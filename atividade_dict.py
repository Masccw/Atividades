#1

aluno = {            
    "nome":"Marina",
    "idade": 18,
    "nota": 10
}

#2

produto = {          
    "nome": "Fini",
    "preço": 3.0,
    "estoque": 10
}

print(f"Há {produto['estoque']} unidades de {produto['nome']} no estoque") 

#3

pessoa = {           
    "nome": "Carlos",
    "idade": 30
}

pessoa["cidade"] = "São Paulo"

print(pessoa)       

#4

carro = {
    "marca": "Ford",
    "modelo": "Fiesta",
    "ano": 2010
}

carro.popitem()

print(carro)

#5

contato = {
    "nome": "Ana",
    "email": "ana@gmail.com"
}

if "Telefone" in contato:
    print("Chave 'Telefone' encontrada")
else:
    print("chave 'Telefone' não encontrada")

print(contato.keys())

#6

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

frutas = {}

for fruta in palavras:
    if fruta in frutas:
        frutas[fruta] += 1
    else:
        frutas[fruta] = 1
print(frutas)

#7

d = {
    "a":1,
    "b": 2,
    "c": 3 
}

reverse_d = {}

for key in d:
    values = d[key]
    reverse_d[values] = key
print(reverse_d)
#8

aluno = {}

for i in range(1):
    notas = []
    nome = input(str("Digite seu nome: "))
    for j in range(3):
        nota = float(input(f"digite sua nota {nome}: "))
        notas.append(nota)
    aluno[nome] = notas
    print(aluno)

for nome, notas in aluno.items():
    media = sum(notas)/ len(notas)
    print(media)

#9

d1 = {
    "manga": "Com sal",
    "morango": "vitamina"
}

d2 = {
    "manga": "verde com sal",
    "laranja": "cravo"
}

# forma 1
def mesclar_dicts(d1, d2):
    complete = {}
    for key in d1:
        complete[key] = d1[key]  
    for key in d2:
        complete[key] = d2[key]  
    return complete

new_dict = mesclar_dicts(d1, d2)
print(new_dict)

#10

pontuacoes = {
    "João": 50, 
    "Maria": 80, 
    "Pedro": 70
}

ordenated = dict(sorted(pontuacoes.items(), key = lambda item: item[1], reverse = True))

print(ordenated)







