
CREATE TABLE Curso ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, mensalidade REAL NOT NULL ); 

CREATE TABLE Turma ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, ano INTEGER NOT NULL, curso_id INTEGER, FOREIGN KEY (curso_id) REFERENCES Curso(id) ); 
 
CREATE TABLE Aluno ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, data_nascimento DATE, nota1 REAL, nota2 REAL, turma_id INTEGER, FOREIGN KEY (turma_id) REFERENCES Turma(id) ); 

INSERT INTO Curso (nome, mensalidade) VALUES ('Python', 750), ('Java', 650), ('C++', 500), ('Banco de Dados', 800); 

INSERT INTO Turma (nome, ano, curso_id) VALUES ('Turma A', 2022, 1), ('Turma B', 2023, 1), ('Turma C', 2023, 2), ('Turma D', 2024, 3), ('Turma E', 2024, 4), ('Turma F', 2024, 4); 

INSERT INTO Aluno (nome, data_nascimento, nota1, nota2, turma_id) VALUES ('Ana Silva', '2001-05-10', 9.0, 8.5, 1), ('Bruno Souza', '1999-09-20', 7.5, 9.0, 2), ('Carla Dias', '2003-02-12', 8.0, 7.5, 3), ('Diego Lima', '2005-07-25', 6.5, 9.5, 4), ('Eduarda Ramos', '2002-01-15', 9.5, 8.0, 5), ('Felipe Rocha', '2004-11-03', 7.0, 6.5, 6);

SELECT COUNT(*) AS total_alunos
FROM Aluno;

SELECT MIN(mensalidade) AS menor_mensalidade
FROM Curso;

SELECT MAX(nota1) AS maior_nota1
FROM Aluno;

SELECT SUM(mensalidade) AS total_mensalidades
FROM Curso;

SELECT AVG(nota2) AS media_geral_nota2
FROM Aluno;