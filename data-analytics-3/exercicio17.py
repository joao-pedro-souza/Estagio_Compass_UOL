def retorna_3listas(lista):
    slice1 = int((len(lista) / 3)) 
    slice2 = slice1 * 2
    lista1 = lista[:slice1]
    lista2 = lista[slice1:slice2]
    lista3 = lista[slice2:]
    print(lista1, lista2, lista3)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
retorna_3listas(lista)
