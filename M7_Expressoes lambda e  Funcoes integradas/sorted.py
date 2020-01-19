"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() de listas. O sort() só
funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o propio nome diz, o sorted() serve para ordenar elementos

OBS: O sorted() sempre retorna uma lista com os elementos do iteravel ordenados

numeros = {1, 3, 2, 4, 6, 5}
print(numeros)

print(sorted(numeros))  # Ordena do menor pro maior

print(numeros)

# Adicionando parametros ao sorted()
numeros = [1, 3, 2, 4, 6, 5]
print(numeros)

print(sorted(numeros))

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "Samuel", "tweets": ["Eu gosto de Python", "Django é massa"]},
    {"username": "Carla", "tweets": ["Eu gosto de C"]},
    {"username": "Jeff", "tweets": [], "Cor": "Amarelo"},
    {"username": "Bob123", "tweets": ["Eu gosto de Java", "Spring é massa"]},
    {"username": "Dogo", "tweets": ["C# é massa"]},
    {"username": "Gal", "tweets": [], "Cor": "Preto", "Musica": "Rock"},
]

print(usuarios)
print()

# Ordenando pelo "username" - Ordem Alfabetica
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numero de "tweets"
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
"""

# Ultimo Exemplo

musicas = [
    {"título": "Thundertruck", "tocou": 3},
    {"título": "Dead Skin Mask", "tocou": 2},
    {"título": "Back in Black", "tocou": 4},
    {"título": "Too old rock'in'roll, too ynoung to die", "tocou": 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
print()

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
