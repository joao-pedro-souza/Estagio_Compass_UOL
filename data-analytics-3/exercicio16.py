def soma_string(string):
    soma_numeros = 0
    lista = string.split(',')
    for n in lista:
        soma_numeros += int(n)
    return soma_numeros
    
    
print(soma_string("1,3,4,6,10,76"))
