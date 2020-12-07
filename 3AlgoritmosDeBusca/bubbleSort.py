def BubbleSort(lista):
  n = len(lista)
  for j in range(n - 1):
    for i in range(n - 1):
      if lista[i] > lista[i+1]:
        temp = lista[i]
        lista[i] = lista[i + 1]
        lista[i + 1] = temp
        #print(lista)

lista = [54,26, 93, 17,77, 31, 44, 55, 20]
BubbleSort(lista)
print(lista)