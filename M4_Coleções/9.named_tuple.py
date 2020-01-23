"""
Módulo Collections - Named Tuple

https://docs.python.org/3.7/library/collections.html?highlight=collections#collections.namedtuple

# Recaptulando tupla

tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para mesma e também parâmetros

from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

apollo = cachorro(idade=2, raca='Pitbull', nome='Apollo')
print(apollo)

# Acessando os dados

# Forma 1

print(apollo[0])  # idade
print(apollo[1])  # raça
print(apollo[2])  # nome

# Forma 2

print(apollo.idade)  # idade
print(apollo.raca)  # raça
print(apollo.nome)  # nome

"""
from collections import namedtuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

meu_cachorro = cachorro(idade=2, raca='Pitbull', nome='Apollo')

print(f'Nome = {meu_cachorro.nome}')  # nome
print(f'Idade = {meu_cachorro.idade}')  # idade
print(f'Raça = {meu_cachorro.raca}')  # raça
