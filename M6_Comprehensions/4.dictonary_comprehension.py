"""
Dictonary Comprehension

Pense no seguinte:

Se quizermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quizermos criar uma tupla:

tupla = (1, 2, 3, 4) ou 1, 2, 3, 4

Se quizermos criar um set (conjunto)

conjuto = {1, 2, 3, 4}

Se quizermos criar um dicionário

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintax

# dictonary comprehension
{chave: valor para valor in iterável}

# list comprehension
[valor for valor in iterável]


# Exemplos


numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


quadrado = {chave: valor **
            2 for chave, valor in numeros.items()}

print(quadrado)

numeros = [1, 2, 3, 4, 5, 1, 2]

quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
"""

# Exemplo com lógica condicional

numeros = [1, 2, 3, 4, 5]

resul = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(resul)
