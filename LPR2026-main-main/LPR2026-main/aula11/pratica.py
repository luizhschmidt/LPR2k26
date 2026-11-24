# Prática Guiada — SQL com SQLite
# Versão para executar localmente com Python 3.
from pathlib import Path

if Path('marvel.db').exists():
    raise SystemExit('marvel.db já existe. Mova o arquivo para outro local antes de executar novamente.')

# Importa a biblioteca sqlite3, que permite trabalhar com bancos SQLite.
# Ela já faz parte da instalação padrão do Python no Colab.

import sqlite3

# Cria (ou abre, se já existir) o arquivo do banco de dados.
conexao = sqlite3.connect("marvel.db")

# Cria um cursor: objeto utilizado para executar comandos SQL.
cursor = conexao.cursor()

# Execute o comando SQL para criar a tabela.
# IF NOT EXISTS evita erro caso a tabela já exista.

cursor.execute("""
CREATE TABLE IF NOT EXISTS Heroi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    identidade TEXT,
    universo TEXT,
    nivel_poder INTEGER
);
""")

# Confirma as alterações no banco.
conexao.commit()

# Insere cinco heróis na tabela.

herois = [
    ("Homem de Ferro", "Tony Stark", "Marvel", 95),
    ("Homem-Aranha", "Peter Parker", "Marvel", 85),
    ("Capitão América", "Steve Rogers", "Marvel", 80),
    ("Thor", "Thor Odinson", "Marvel", 100),
    ("Hulk", "Bruce Banner", "Marvel", 98)
]

cursor.executemany(
    """
    INSERT INTO Heroi (nome, identidade, universo, nivel_poder)
    VALUES (?, ?, ?, ?);
    """,
    herois
)

# Confirma a inserção dos dados.
conexao.commit()

# Consulta todos os registros da tabela Heroi.

cursor.execute("SELECT * FROM Heroi;")

# fetchall() retorna todos os resultados da consulta.
resultado = cursor.fetchall()

# Exibe os registros retornados.
for linha in resultado:
    print(linha)

# Altere a consulta para exibir somente nome e identidade.
# Complete o comando SQL no espaço indicado.

cursor.execute("SELECT nome, identidade FROM Heroi;")

resultado = cursor.fetchall()

for linha in resultado:
    print(linha)

# DESAFIO 1
# Consulte os heróis cujo nivel_poder seja maior ou igual a 90.
# Complete a consulta SQL.

cursor.execute("""
SELECT *
FROM Heroi
WHERE nivel_poder >= 90;
""")

for linha in cursor.fetchall():
    print(linha)

# DESAFIO 2
# Exiba nome e nivel_poder de todos os heróis,
# ordenados do maior para o menor nivel_poder.

cursor.execute("""
SELECT nome, nivel_poder
FROM Heroi
ORDER BY nivel_poder DESC;
""")

for linha in cursor.fetchall():
    print(linha)

# Exemplo: atualizar o nivel_poder do Homem-Aranha para 90.

cursor.execute("""
UPDATE Heroi
SET nivel_poder = 90
WHERE nome = 'Homem-Aranha';
""")

conexao.commit()

# Confira se a atualização ocorreu.
cursor.execute("SELECT nome, nivel_poder FROM Heroi;")

for linha in cursor.fetchall():
    print(linha)

# Exemplo: remover o Capitão América da tabela.

cursor.execute("""
DELETE FROM Heroi
WHERE nome = 'Capitão América';
""")

conexao.commit()

# Confira os registros restantes.
cursor.execute("SELECT * FROM Heroi;")

for linha in cursor.fetchall():
    print(linha)

# Cria a tabela Equipe.

cursor.execute("""
CREATE TABLE IF NOT EXISTS Equipe (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
""")

# Insere algumas equipes.
cursor.executemany(
    "INSERT INTO Equipe (nome) VALUES (?);",
    [
        ("Vingadores",),
        ("Defensores",),
        ("Guardiões da Galáxia",)
    ]
)

conexao.commit()

# Consulta as equipes cadastradas.
cursor.execute("SELECT * FROM Equipe;")

for linha in cursor.fetchall():
    print(linha)

# Habilita a verificação de chaves estrangeiras nesta conexão.
cursor.execute("PRAGMA foreign_keys = ON;")

# Cria uma nova tabela de relacionamento.
# Cada registro associa um herói a uma equipe.
cursor.execute("""
CREATE TABLE IF NOT EXISTS Heroi_Equipe (
    heroi_id INTEGER,
    equipe_id INTEGER,
    PRIMARY KEY (heroi_id, equipe_id),
    FOREIGN KEY (heroi_id) REFERENCES Heroi(id),
    FOREIGN KEY (equipe_id) REFERENCES Equipe(id)
);
""")

conexao.commit()

# Primeiro, consultamos os IDs para conferir os valores disponíveis.

cursor.execute("SELECT id, nome FROM Heroi;")
print("Heróis:")
for linha in cursor.fetchall():
    print(linha)

cursor.execute("SELECT id, nome FROM Equipe;")
print("Equipes:")
for linha in cursor.fetchall():
    print(linha)

# Vamos associar cada herói a uma equipe.
# Para isso, utilizamos os IDs das tabelas Heroi e Equipe.

# Homem de Ferro (id 1) -> Vingadores (id 1)
# Homem-Aranha (id 2) -> Defensores (id 2)
# Thor (id 4) -> Vingadores (id 1)
# Hulk (id 5) -> Vingadores (id 1)

cursor.executemany("""
INSERT INTO Heroi_Equipe (heroi_id, equipe_id)
VALUES (?, ?);
""", [
    (1, 1),
    (2, 2),
    (4, 1),
    (5, 1)
])

# Confirma as inserções no banco.
conexao.commit()

# Consulta as relações cadastradas.
cursor.execute("""
SELECT * FROM Heroi_Equipe;
""")

for linha in cursor.fetchall():
    print(linha)

# DESAFIO 3
# Complete a consulta para mostrar o nome do herói e o nome da equipe.
# Utilize JOIN para relacionar as três tabelas.
cursor.execute("""
SELECT Heroi.nome, Equipe.nome
FROM Heroi
JOIN Heroi_Equipe ON Heroi.id = Heroi_Equipe.heroi_id
JOIN Equipe ON Heroi_Equipe.equipe_id = Equipe.id;
""")

for linha in cursor.fetchall():
    print(linha)

# Desafio extra 1. Heróis com nível de poder inferior a 90
cursor.execute("""
SELECT * FROM Heroi WHERE nivel_poder < 90;
""")

resultado = cursor.fetchall()
for linha in resultado:
    print(linha)

if not resultado:
    print("Nenhum herói com nível de poder inferior a 90.")


# Desafio extra 2. Buscar um herói pelo nome
cursor.execute("""
SELECT * FROM Heroi WHERE nome = 'Thor';
""")

resultado = cursor.fetchall()
for linha in resultado:
    print(linha)


# Desafio extra 3. Heróis em ordem alfabética
cursor.execute("""
SELECT nome FROM Heroi ORDER BY nome ASC;
""")

resultado = cursor.fetchall()
for linha in resultado:
    print(linha)


# Desafio extra 4. Aumentar o poder do Homem-Aranha em 5 pontos
cursor.execute("""
UPDATE Heroi SET nivel_poder = nivel_poder + 5 WHERE nome = 'Homem-Aranha';
""")

conexao.commit()
cursor.execute("SELECT nome, nivel_poder FROM Heroi WHERE nome = 'Homem-Aranha';")

resultado = cursor.fetchall()
for linha in resultado:
    print(linha)


# Desafio extra 5. Consultar heróis e suas equipes
cursor.execute("""
SELECT Heroi.nome, Equipe.nome
FROM Heroi
JOIN Heroi_Equipe ON Heroi.id = Heroi_Equipe.heroi_id
JOIN Equipe ON Heroi_Equipe.equipe_id = Equipe.id;
""")

resultado = cursor.fetchall()
for linha in resultado:
    print(linha)


# Desafio extra 6. Contar os heróis cadastrados
cursor.execute("""
SELECT COUNT(*) AS total FROM Heroi;
""")

resultado = cursor.fetchall()
for linha in resultado:
    print(linha)


# Desafio extra 7. Maior e menor nível de poder
cursor.execute("""
SELECT MAX(nivel_poder) AS maior, MIN(nivel_poder) AS menor FROM Heroi;
""")

resultado = cursor.fetchall()
for linha in resultado:
    print(linha)


# Fecha a conexão com o banco de dados.
conexao.close()
