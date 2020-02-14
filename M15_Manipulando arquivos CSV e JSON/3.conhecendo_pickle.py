"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

# OBS: O módulo Pickle NÃO é deguro contra dados maliciosos e desta forma não
é recomendado trabalhar com arquivos pickle vindos de outras pessoas que você 
não conheça ou de fontes desconhecidas.


# Fazendo escrita em arquivos pickle

felix = Gato('Felix')

pluto = Cachorro('Pluto')

with open('M15_Manipulando arquivos CSV e JSON/animais.pickle', 'wb') as file:
    pickle.dump((felix, pluto), file)

"""
import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')

# Fazendo a leitura de dados em arquivos pickle


with open('M15_Manipulando arquivos CSV e JSON/animais.pickle', 'rb') as file:
    gato, cachorro = pickle.load(file)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')
