"""
Map

Com map, fazemos mapeamento de valores para função

import math


def area(raio):
    # Calcula a área de um círculo com raio 'raio'
    return math.pi * (raio ** 2)


print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum

areas = []

for r in raios:
    areas.append(area(r))

print(areas)


# Forma 2 - Utilizando Map

# Map é uma função que recebe 2 parametros: O primeiro a função o segundo um iterável

areas = map(area, raios)
print(type(areas))
print(list(areas))

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map(), depois da primiera utilização ele zera
"""
# Para fixar - Map

# Temos dados iteráveis

# dados: a1, a2, .... an

# Temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados) onde o map irá 'mapear' cada elemento dos dados e aplicar a função

# O Map Object: f(a1), f(a2), f(...) f(an)


# Mais um Exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19),
           ('Los Agenles', 26), ('Tokio', 27), ('Nova York', 20)]

# f = 9/5 * C° + 32

# Usando Map com Lambda
lista = (
    list(map(lambda dado: (dado[0], round(9 / 5 * dado[1] + 32, 1)), cidades)))

print(lista)
