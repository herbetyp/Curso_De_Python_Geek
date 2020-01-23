"""
Módulo Collections: Ordered Dict

# Documentação Oficial
https://docs.python.org/3.7/library/collections.html?highlight=collections#collections.OrderedDict

# Em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}, valor={valor}')

OrderedDict ->  um dicionário, que nos garante a ordem de inserção dos elementos.

# Fazendo import

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')
"""
from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

# Dict

dict1 = {'a': 1, 'b': 2}
# True -> Já que a ordem dos elementos não importa para o dicionário
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
# False -> Já que a ordem dos elementos importa para o OrderedDict
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)
