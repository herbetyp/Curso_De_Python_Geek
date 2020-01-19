"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)

________________________
|Python|Módulos Builtin|
------------------------

# Utilizando o alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())


# Podemos importar todas as funções de módulo usando asterisco
from random import *

print(random())


# Importando todo o módulo
import random

print(random.random())


# Utilizando o alias (apelidos) para módulos/funções
from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())


# Módulos Python

https://docs.python.org/3/py-modindex.html
"""
# É de costume utilizar tuple para colocar multiplos imports de um  mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(2, 85))

lista = ['Python', 'é', 'top!']
shuffle(lista)
print(lista)

print(choice('Univesity'))
