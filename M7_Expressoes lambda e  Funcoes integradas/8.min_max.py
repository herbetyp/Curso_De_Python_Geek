"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior entre dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129]

print(max(lista))


tupla = (1, 8, 4, 99, 34, 129)

print(max(lista))


conjunto = {1, 8, 4, 99, 34, 129}

print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}

print(max(dicionario.values()))

# Faça um programa que receba 2 valores do usuário e mostre o maior

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.145, 5.789))

print(max('Geek University'))

###################

min() -> Retorna o menor valor em um iterável ou o menor entre dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129]

print(min(lista))


tupla = (1, 8, 4, 99, 34, 129)

print(min(lista))


conjunto = {1, 8, 4, 99, 34, 129}

print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}

print(min(dicionario.values()))

# Faça um programa que receba 2 valores do usuário e mostre o maior

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))

print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.145, 5.789))

print(min('Geek University'))

# Outros exemplos

nomes = ['Arya', 'Samson', 'Bora', 'Tim', 'Olivander']

print(max(nomes))  # Tim
print(min(nomes))  # Arya


print(max(nomes, key=lambda nome: len(nome)))  # Olivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim

"""
musicas = [
    {"título": "Thundertruck", "tocou": 64},
    {"título": "Dead Skin Mask", "tocou": 81},
    {"título": "Back in Black", "tocou": 200},
    {"título": "Too old rock'in'roll, too ynoung to die", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Imprimir somente o título da mais tocada e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['título'])
print(min(musicas, key=lambda musica: musica['tocou'])['título'])

# Encontrando a musica que menos tocou e a que mais tocou sem lambda sem max() sem min()
tit_max, maxi = '', 0
tit_min, mini = '', 9999

for musica in musicas:
    if musica['tocou'] > maxi:
        maxi = musica['tocou']
        tit_max = musica['título']

    elif musica['tocou'] < mini:
        mini = musica['tocou']
        tit_min = musica['título']

print(f'{tit_max} - Tocou: {maxi}x')
print(f'{tit_min} - Tocou: {mini}x')
