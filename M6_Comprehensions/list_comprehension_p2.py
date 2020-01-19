"""
List Comprehension - pt 2

Nós podemos adicionar estruturas condicionais lógicas as nossas List Comprehension

"""
from collections import namedtuple
# Exemplos

# 1
numeros = [1, 2, 3, 4, 5, 6]

par = [num for num in numeros if num % 2 == 0]
impar = [num for num in numeros if num % 2 != 0]

print(par)
print(impar)


# Refatorando

# Qualquer numero par modulo de 2 é 0 e 0 em Python é False, not False = True
print([num for num in numeros if not num % 2])  # Par

# Qualquer número impar modulo de 2 é 1 e 1 em Python é True
print([num for num in numeros if num % 2])  # Impar


# 2

res = [num * 2 if num % 2 == 0 else num / 2 for num in numeros]
print(res)
