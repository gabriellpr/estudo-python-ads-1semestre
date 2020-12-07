import sqlite3

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()
sql = """
create table cadastro (codigo integer, nome text, idade integer)
"""

cursor.execute(sql)

sql = """
insert into cadastro (codigo,nome,idade) values(1284, 'Pedro Oliveira', 32)
"""

cursor.execute(sql)

sql = """
insert into cadastro (codigo,nome,idade) values(1234, 'Maria Antonia', 65)
"""

cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()
