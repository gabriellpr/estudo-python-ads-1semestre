"""
O algoritmo de ordenação por inserção é iniciado a partir do segundo valor no vetor, pois o primeiro elemento será uma referência para a ordenação. Ou seja, o segundo elemento do vetor será comparado com o primeiro.
O vetor é percorrido da esquerda para a direita. Nesse caminho, compara-se sempre o elemento da direita com os elementos à esquerda de modo que os elementos mais à esquerda sejam organizados e ordenados. 
"""

def executar_insertion_sort(lista):
  n = len(lista)
  for i in range(1, n):
    valor_inserir = lista[i] 
    j = i - 1
	  while j >= 0 and lista[j] > valor_inserir:
      lista[j + 1] = lista[j]
      j -= 1
      lista[j + 1] = valor_inserir 
  return lista	
lista = [10, 8, 7, 3, 2, 1]
print(executar_insertion_sort(lista))