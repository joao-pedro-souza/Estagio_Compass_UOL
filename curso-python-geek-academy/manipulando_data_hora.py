"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

2023-03-16 09:48:47.359427

2023-03-16 15:41:38.359427

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)


# Retorna a data e hora corrente

print(datetime.datetime.now()) # 2023-03-16 09:45:21.249334 BR 16/03/2023


# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))


# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minutos, 0 segundos, 0 microsegundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usuário e convertendo para data
print(type(evento))

print(type('31/12/2018'))


print(evento)


nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')

nascimento = nascimento.split('/')


nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))
"""

import datetime



evento = datetime.datetime.now()

# Acesso individual dos elementos de data e hora

print(evento.year) # Ano
print(evento.month) # Mês
print(evento.day) # Dia
print(evento.hour) # Hora
print(evento.minute) # Minuto
print(evento.second) # Segundo
print(evento.second) # Microsegundo

print(dir(evento))