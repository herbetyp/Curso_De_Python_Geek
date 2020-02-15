"""
Manipulando data e hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora


# print(dir(datetime))

print(datetime.MAXYEAR)  # máximo ano que o módulo datetime suporta
print(datetime.MINYEAR)  # mínimo ano que o módulo datetime suporta

print(datetime.datetime.now())  # retorna a data e hora corrente

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 1 hora, 0 minuto, 0 segundos, 0 microsegundos
inicio = inicio.replace(hour=1, minute=0, second=0, microsecond=0)

print(inicio)


# Recebendo dados do usuário e convertendo para data

print(type(evento))

print(type('31/12/2021'))

print(evento)

nascimento = input('Informe sua data de nascimento [dd/mm/yyyy]: ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(
    int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))

"""

import datetime


evento = datetime.datetime.now()


# Acesso individual dos elementos da data e hora

print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # microsegundo


print(dir(evento))
