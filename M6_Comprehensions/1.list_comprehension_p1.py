"""
List Comprehension - pt 1

- Utilizando list comprehension nós podemos gerar novas listas com dados processados
a partir de outo iterável

# Sintax da List Comprehesion

[ dado for dado in iteravel ]

numeros = [1, 2, 3, 4, 5]

resul = [num * 10 for num in numeros]
print(resul)

Para entender oq está acontecendo devemos dividir a expressão em duas partes

1 - A primeira parte: for num in numeros
2 - Segunda parte: numero * 10

resul = [num / 2 for num in numeros]

print(resul)


def funcao(valor):
    return valor * valor


res = [funcao(num) for num in numeros]
print(res)

# List Comprehension vs Loop

# Loop
numeros_dobrados = []

for num in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(num * 2)

print(numeros_dobrados)


# List Comprehension
print([num * 2 for num in [1, 2, 3, 4, 5]])
"""
# Outros Exemplos

# 1
nome = 'Curso de Python'

print([letra.upper() for letra in nome])

# 2
amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']


def caixa_alta(nome):
    return nome.title()


print([caixa_alta(amigo) for amigo in amigos])

# 3
print([num * 3 for num in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(num) for num in [1, 2, 3, 4]])
