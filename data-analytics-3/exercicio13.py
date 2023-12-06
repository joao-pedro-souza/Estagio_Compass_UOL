def my_map(list, f):
    nova_lista = []
    for i in lista:
        nova_lista.append(potencia2(i))
    return nova_lista


def potencia2(n):
    return n ** 2
    

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_map(lista, potencia2))    
