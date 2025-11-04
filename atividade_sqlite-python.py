import sqlite3

# 1️⃣ Conexão com o banco de dados
conexao = sqlite3.connect("escola_v2.db")
cursor = conexao.cursor()

# 2️⃣ Exibir todos os alunos cadastrados
print("=== TABELA ALUNO ===")
cursor.execute("SELECT * FROM Aluno;")
alunos = cursor.fetchall()
for aluno in alunos:
    print(aluno)

# 3️⃣ Calcular a média (nota1 + nota2) / 2 e mostrar as 10 maiores médias
print("\n=== TOP 10 MÉDIAS DOS ALUNOS ===")
cursor.execute("""
    SELECT nome, (nota1 + nota2) / 2 AS media
    FROM Aluno
    ORDER BY media DESC
    LIMIT 10;
""")
top_alunos = cursor.fetchall()
for nome, media in top_alunos:
    print(f"{nome}: média {media:.2f}")

# 4️⃣ LEFT JOIN entre Aluno e Turma
print("\n=== LEFT JOIN: ALUNO + TURMA ===")
cursor.execute("""
    SELECT Aluno.id, Aluno.nome, Aluno.nota1, Aluno.nota2, 
           Turma.nome AS turma, Turma.ano
    FROM Aluno
    LEFT JOIN Turma ON Aluno.turma_id = Turma.id;
""")
alunos_turmas = cursor.fetchall()
for linha in alunos_turmas:
    print(linha)

# 5️⃣ LEFT JOIN filtrando apenas os alunos da turma 2
print("\n=== ALUNOS DA TURMA 2 ===")
cursor.execute("""
    SELECT Aluno.id, Aluno.nome, Aluno.nota1, Aluno.nota2, 
           Turma.nome AS turma, Turma.ano
    FROM Aluno
    LEFT JOIN Turma ON Aluno.turma_id = Turma.id
    WHERE Turma.id = 2;
""")
alunos_turma2 = cursor.fetchall()
for linha in alunos_turma2:
    print(linha)

# 6️⃣ Encerrar a conexão
conexao.close()
