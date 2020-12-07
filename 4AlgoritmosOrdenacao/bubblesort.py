"""

"""

def executar_bubble_sort(lista):
  n = len(lista)
3	    for i in range(n-1):
4	        for j in range(n-1):
5	            if lista[j] > lista[j + 1]:
6	                lista[j], lista[j + 1] = lista[j + 1], lista[j]
7	    return lista
8	
9	lista = [10, 8, 7, 3, 2, 1]
10	executar_bubble_sort(lista)