"""
Reversed

Não confunda com a função reverse() que utilizamos em listas

A função reverse() só funciona nas listas

Já a funçãom reversed() funciona em qualquer iterável, sua função e reverter o iterável

A função reversed() retorna um iterável chamado List Reverse Iterator

"""
# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos, não definimos a ordem dos elementos
# Conjunto(set)
print(set(reversed(lista)))

# Podemos iterar sobre o reversed()

for letra in reversed('Geek University'):
    print(letra, end='')

print()
# Podemos fazer o mesmo sem uso do for
print(''.join(list(reversed('Geek University'))))


# Já vimos como fazer isso mais fácil com o slie de strings

print('Geek University'[::-1])

# Podemos tambem utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n, end='')

# Apesar que tambem ja vimos como fazer isso utilizando o propio range()
print()
for n in range(9, -1, -1):
    print(n, end='')
print()
