def conserta_lista(lista):
    conjunto_concertado = set(lista)
    lista_concertada = list(conjunto_concertado)
    return list(lista_concertada)
    
    
lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
nova_lista = conserta_lista(lista)
print(nova_lista)