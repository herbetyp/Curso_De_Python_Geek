"""
Módulo Random / O que são módulos

- Em python módulos nada mais são do que outros arquivos Python

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório


# OBS: Existe duas formas de utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (Não recomendado)

import random

# random() -> Gera um número real pseudo-aleatório entre 0 e 1

# OBS: Ao realizar o import de todo módulo, todas as funções, atributos, classes e propiedades
# que estiverem dentro do módulo, ficaram disponíveis (Ficarão em memória). Caso você
# saiba quais funções você precisa utilizar deste módulo, entao esta não seria a forma
# ideal de utilização

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome
# do pacote e o nome da função, separados por ponto

# OBS: Não confunda a função random() com o pacote random. Pose parecer confuso, mas
# a função random() é apenas uma função dentro modulo random


# Forma 2 - Importando uma função especifica do módulo (Forma recomendada)

from random import random

# No import acima estamos falando: Do módulo random import a função random

for i in range(10):
    print(random())


# uniform() -> Gera um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluido


# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ') # começa em 1 e vai até 60
print()


# choice() -> Mostra um valor aleatório entre um iterável

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

"""
# shuffle() -> Tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'O', 'J', 'A', '2', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)
print(cartas.pop())
