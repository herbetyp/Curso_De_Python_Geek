"""
Generator Expression

Em aulas anteriores no estudamos:
- List Comprehension
- Dictonary Comprehension
- Set Comprehension

Não vimos:
- Tuple Comprehension, porque eles se chamam Generators Expressions

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes])


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

# Poderiamos ter feito utilizando Generators

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade de getsizeof() -> retorna a quantidade de bytes em memoria do elemento passado como parametro
from sys import getsizeof

# Mostra quantos bytes a string está ocupando em memoria, Quanto maior a string, mais espaço ocupa

print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(15.624874))
print(getsizeof(True))

from sys import getsizeof

# Gerando uma lista de numeros com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Dictonary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Generator
gen = getsizeof((x * 10 for x in range(1000)))

print(f'Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictonary Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')
"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))

[print(num) for num in gen]
