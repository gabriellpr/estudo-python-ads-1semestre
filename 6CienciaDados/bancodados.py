import sqlite3

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()

sql = """
create table cadastro (nome text, idade integer, telefone integer)
"""

cursor.execute(sql)

sql = """
insert into cadastro (nome, idade, telefone) values ('Marcelo', 33, 9999)
"""

cursor.execute(sql)




conector.commit()
cursor.close()