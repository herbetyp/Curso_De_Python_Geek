"""
Trabalhando com Json e Pìckle

Json -> Javascript Object Notation

Api -> São meios de comunicação entre os serviços oferecidos por empresas:

Exemplo: Twitter, Facebook, YouTube... e terceiros (nós desenvolvedores)


import json


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Angora')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)


ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))

print(ret)


# Integrando o Json com o Pickle

pip install jsonpickle


import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Angora')

ret = jsonpickle.encode(felix)

print(ret)


# Escrevendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Angora')

with open('M15_Manipulando arquivos CSV e JSON/felix.json', 'w') as file:
    ret = jsonpickle.encode(felix)
    file.write(ret)

"""

# Lendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('M15_Manipulando arquivos CSV e JSON/felix.json', 'r') as file:
    conteudo = file.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
