def executar_quicksort(lista, inicio, fim):
  if inicio < fim:
    pivo = executar_particao(lista, inicio, fim)
  return lista

def executar_particao(lista, inicio, fim):
  pivo = lista[fim]
  esquerda = inicio
  for direita in range(inicio, fim):
    if lista[direita] <= pivo:
      lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
      esquerda += 1
  lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
  return esquerda