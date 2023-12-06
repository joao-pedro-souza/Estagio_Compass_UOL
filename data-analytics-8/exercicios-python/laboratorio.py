import random
import time
import names

random.seed(40)

qtd_nomes_unicos = 3000

qtd_nomes_aleatorios = 10000000

aux=[]

for i in range(0, qtd_nomes_unicos):

    aux.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

with open('nomes_aleatorios.txt', 'w') as nomes:

    for i in range(0,qtd_nomes_aleatorios):

        nomes.write(f'{random.choice(aux)}\n')
