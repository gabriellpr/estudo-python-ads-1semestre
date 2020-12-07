aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))

if aluno['media'] >- 7:
  aluno['situacao'] = 'aprovado'
else:
  aluno['situacao'] = 'reprovado'

for x, y in aluno.items():
  print(f'-{x} eh igual a {y}')