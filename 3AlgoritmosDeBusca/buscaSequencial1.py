def BuscaSeq(list, item):
  pos=0
  x=False

  while pos<len(list) and not x:
    if list[pos] == item:
      return True
    else:
      pos = pos + 1
  return x

lista = [5, 6, 8, 12, 1, 5, 7]
print(BuscaSeq(lista, 8))
print(BuscaSeq(lista, 13))