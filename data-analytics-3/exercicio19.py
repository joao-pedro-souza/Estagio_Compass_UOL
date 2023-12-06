import random

random_list = random.sample(range(500), 50)
lista_ordenada = sorted(random_list)

soma_numeros = sum(lista_ordenada)
c = 0
mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

for n in lista_ordenada:
    c += 1
    
    if n > valor_maximo:
        valor_maximo = n
    if valor_minimo == 0:
        valor_minimo = n
    elif n < valor_minimo:
        valor_minimo = n
    if c == 25 or c == 26:
        mediana += n

mediana = mediana / 2
media = soma_numeros / 50

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
