"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para linguagem Python

The Zen of Python

import this

A idéia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case(Capitalizar a palavra) para nomes de classes:

class Calculator:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes minúsculos, separados por underline para funções ou váriaveis:

def soma():
    pass

def soma_dois():
    pass


[3] - Utilize 4 espaços para indentaçâo: (NÃO USE TAB)

if 'a' in 'banana':
->  print('tem')


[4] - Linhas em branco:

class Classe:

- Separar funções e definições de classe com duas linhas em branco:
- Métodos dentro de uma classe devem ser separados com uma única linha em branco:


[5] - Imports:

# Import Errado

import sys, so

# Import Certo:

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import {
    Stringtype,
    ListType,
    Settype,
    OutroType
}

#imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docsstrings e
antes de constantes ou váriaveis globais.


[6] - Espaços em expressões e instruções:

# Não faça

funcao_algo{ algo[ 1 ], { outro: 2} }

#Faça

funcao{algo[1], {outro: 2}}

# Não faça

algo_(1)

#Faça

algo(1)

# Não faça

dict_['chave'] = lista_[indice]

# Faça

dict['chave'] = lista[indice]

# Não faça

x______________= 1
y______________= 3
variavel_longa = 5

#Faça

x = 1
y = 3
variavel_longa = 5


[7] - Termine sempre uma instrução como uma nova linha:

"""
import this
