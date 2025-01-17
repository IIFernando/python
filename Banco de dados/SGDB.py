import sqlite3

con = sqlite3.connect('BDestudo.sql')
print('Conexão bem sucedida!')

cursor = con.cursor()
cursor.execute(''''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER)
''')

con.commit()
print('Usuarios criados!')
