# A busca começa por uma das extremidades da sequência 
# e vai percorrendo-a até encontrar (ou não) o valor desejado.

def busca_sequencial(lista, elemento):
  pos = 0 
  encontrado = False
     
  while pos < len(lista) and not encontrado:
    if lista[pos] == elemento:
      encontrado = True
    else:
      pos = pos+1
  
  return encontrado
   
testelista = [2, 10, 8, 15, 18, 20, 12, 1]
print(busca_sequencial(testelista, 5))
print(busca_sequencial(testelista, 15))

def busca_sequencial_ordenada(lista, elemento):
  pos = 0
  encontrado = False
  para = False
  while pos < len(lista) and not encontrado and not para:
           if lista[pos] == elemento:
                encontrado = True
           else:
               if lista[pos] > elemento:
                   para = True
               else:  
                   pos = pos+1
  
 return encontrado
    
 testelista = [1, 2, 8, 10, 13, 15, 18, 20]
 print(busca_sequencial_ordenada(testelista, 5))
 print(busca_sequencial_ordenada(testelista, 15))