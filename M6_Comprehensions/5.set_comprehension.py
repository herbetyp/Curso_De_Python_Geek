"""
Set Comprehension

Lista = [1, 2, 3 , 4, 5]
Set = {1, 2, 3, 4, 5}
"""

# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Outro Exemplo
letras = {letra for letra in 'Geek University'}
print(letras)

# Gerando um dicionário
numeros = {x: x ** 2 for x in range(10)}
print(numeros)
