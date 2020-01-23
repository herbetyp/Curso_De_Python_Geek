"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio


print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True
print(all([]))  # Todos os números são verdadeiros? True
print(all((1, 2, 3, 4)))  # Todos os números são verdadeiros? True
print(all({1, 2, 3, 4}))  # Todos os números são verdadeiros? True
print(all('Geek'))  # Todos os números são verdadeiros? True

# Exemplo

# Verifica se os nomes começam com a letra 'C'
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all(nome[0] == 'C' for nome in nomes))

# OBS:  um iteravel vazio comvertido em bool é False, mais o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 != 0]))

#####

any() -> Retorna True se qualquer elemento do iterável for verdadeiro, se o iterável estiver vazio, retorna False

"""

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, (), []]))  # False


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))  # True

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))  # True
