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
conector.commit()
cursor.close()
conector.close()

def Read():
  sql = "select * from cadastro"
  cursor.execute(sql)
  dados = cursos.fetchall()
  cursor.close()
  conector.close()

for d in dados:
  print(d[0], d[1], d[2])

def Update(Cod, new):
  cursor.execute("""
    UPDATE cadastro
    SET idade = ?
    where codigo = ?
  """, (new, Cod))

  connector.commit()

def ExcluiCliente(Cod):
  sql = "delete from cadastro where codigo = :param"
  cursor.execute(sql, {'param': Cod})
  conector.commit()
  return "Cliente {} Excluido".format(Cod)"

