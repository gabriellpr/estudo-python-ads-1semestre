"""
1 - Encontra o item no meio da sequência.
2 - Se o valor procurado for igual ao item do meio, a busca encerra.
3 - Se não, verifica se o valor buscado é maior ou menor que o valor central.
4 - Se for maior, então a busca acontecerá na metade superior da sequência (a inferior é descartada), se não for maior, a busca acontecerá na metade inferior da sequência (a superior é descartada).
5 - Repete os passos: 1, 2, 3, 4.
"""

def busca_binaria(lista, elemento):
        minimo = 0 
        maximo = len(lista)-1
        encontrado = False
    
        while minimo < =maximo and not encontrado:
            meio_lista = (minimo + maximo)//2
            if lista[meio_lista] == elemento:
                encontrado = True
            else:
                if elemento < lista[meio_lista]:
                    maximo = meio_lista-1
                else:
                    minimo = meio_lista+1
    
        return encontrado
    
 testelista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
 print(busca_binaria(testelista, 14)