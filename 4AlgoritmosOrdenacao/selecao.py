"""
O princípio de funcionamento deste algoritmo é transferir o menor valor do vetor para a primeira posição e, em seguida, o segundo menor valor para a segunda posição, e assim sucessivamente, para os n-1 elementos até os últimos dois elementos
"""

def executar_selection_sort(lista):
  n = len(lista)   
  for i in range(0, n-1):
    min = i
	  for j in range(i+1, n):
      if lista[j] < lista[min]:
        min = j
    lista[i], lista[min] = lista[min], lista[i]
  return lista	
lista = [10, 8, 7, 3, 2, 1]
executar_selection_sort(lista)