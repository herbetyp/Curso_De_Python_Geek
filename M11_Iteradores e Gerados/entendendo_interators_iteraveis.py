"""
Entendendo Iterators e Iterables

Iterator -> 
    - Um obleto que pode ser iterado.
    - Um objeto que retorna um dado, sendo elemento por vez quando uma função next() é chamada
Iterable -> 
    - Um objeto que irá retornar um iterator quando a função iter() for chamada


nome = 'Geek'  # É um Iterable mais não é um Iterator
numeros = [1, 2, 3, 4, 5, 6]

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))


print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
"""

nome = 'Geek'  # É um Iterable mais não é um Iterator

for letra in nome:
    print(f'{letra}')
