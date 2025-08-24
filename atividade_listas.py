livros = ["O Ceifador", "A Nuvem", "O Timbre"] #1

print(livros[0:3:2]) #2

livros.append("As Foices") #3
livros.append("todo dia")

livros.insert(2, "Duna") #4

if "Silêncio dos Inocentes" in livros: #5
    livros.remove("Silêncio dos Inocentes")
else:
    print("Livro não encontrado")

print(livros)

for livro in livros: #7
    print(f"O livro {livro} é interessante")

numeros =  [1, 2, 3, 2, 4, 2, 5] #6
qtd = numeros.count(2)

print(numeros, f"O número 2 aparece {qtd} vezes") #6

idades = [12, 18, 25, 14, 30] #8

for idade in idades:
    if idade >= 18:
       print(idade) 

valores = [10, 20, 20, 40] #9

soma = 0
for valor in valores:
    soma += valor 
    print(f"A soma dos valores é {soma}") #9

notas = []  #10

for i in range(2):
    aluno = []
    print(f"digite sua nota aluno {i + 1}: ")
    for j in range(3):
        nota = float(input(f"\n nota {j + 1}: "))
        aluno.append(nota)
    
    notas.append(aluno) #10

for i, aluno in enumerate(notas):
    media = sum(aluno)/ len(aluno)
    print(f"média do aluno {i+1} :{media}")

tabuleiro = [["[]" for _ in range(8)]for _ in range(8)] #11

pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]

tabuleiro[0] = pecas #peças brancas
tabuleiro[1] = ["pea"] * 8 #peças brancas
tabuleiro[2] = ["[ ]"] * 8
tabuleiro[3] = ["[ ]"] * 8
tabuleiro[4] = ["[ ]"] * 8
tabuleiro[5] = ["[ ]"] * 8
tabuleiro[6] = ["pea"] * 8 #pecas pretas
tabuleiro[7] = pecas

for linha in tabuleiro: #imprime cada linha uma baixo da outra
 print(linha) #11
