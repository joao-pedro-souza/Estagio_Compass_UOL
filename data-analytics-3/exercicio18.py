speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
lista_todos_valores = []
lista_sem_repeticao = []

for chave, valor in speed.items():
    lista_todos_valores.append(valor)

conjunto = set(lista_todos_valores)
lista_sem_repeticao = list(conjunto)

lista_sem_repeticao.sort()
print(lista_sem_repeticao)
