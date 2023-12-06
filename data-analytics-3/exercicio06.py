a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
intersecao_ab = set()

for n in a:
    if n in b:
        intersecao_ab.add(n)
        
lista_ab = list(intersecao_ab)

print(lista_ab)