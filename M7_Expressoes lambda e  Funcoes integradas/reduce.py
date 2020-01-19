"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Agora
temos que importar e utilizar esta função a partir do módulo 'functools' 

Guido Van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo
caso 99% das vezes um loop for é mais legível.

Para entender o reduce()

# Imagine que você tem uma coloção de dados:

dados = [a1, a2, a3, ..., an]

def funcao(x, y):
    return x * y


# Assim como map() e filter(), a função reduce() recebe dois parametros: a função e o iteravel

reduce(funcao, dados)


A função reduce(), funciona da seguinte forma:

    Passo 1: resul1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: resul2 = f(resul1, a3) # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o resultado

    Isso é repetido até o final
    passo 3: resul3 = f(resul2, a4)
    .
    .
    .
    Até o passo n: resuln = f(resn, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final
reduce() irá retornar o resultado final

Alternativamento poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""
from functools import reduce


# Como funciona na prática

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que recebe dois parametros

resul = reduce(lambda x, y: x * y, dados)

print(resul)


# Utilizando um loop normal

res = 1

for n in dados:
    res *= n

print(res)
