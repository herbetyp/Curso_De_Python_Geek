"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

Python

for item in interavel:
    execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5 , 7, 9]
- Range
    numeros = range(1, 10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 (iterando sobre uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)

range(valor inicial, valor final)

OBS: O valor final não é inclusive. (exemplo de 1 até 10)
1
2
3
4
5
6
7
8
9
10 - (não)

Enumerate:

({0, 'G'}, {1, 'e'}, {2, 'e'}, {3, 'k'}, {4, ' '}, {5, 'u'}...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):  # Quando não precisamos de um valor, podemos descartá-lo utilizando um undeline (_)
    print(letra)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

# Original: U+F40D
# Modificado: U0001F40D
emoji = '\U0001F40D'

for _ in range(3):
    for num in range(1, 11):
        print(emoji * num)
