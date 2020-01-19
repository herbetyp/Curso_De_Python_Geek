"""
Módulo Collections - Default Dict

# Documentação Oficial
https://docs.python.org/3.7/library/collections.html?highlight=collections#collections.defaultdict

# Recaptulando Dicionários

dicionario = {'curso': 'Python Essencial'}
print(dicionario)
print(dicionario['curso'])

print(dicionario['outro'])

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada 
e o valor default será atribuído.
 
Obs: Lambdas são funções sem nome, e podem ou não receber parâmetros de entrada 
e retornar valores.
"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Python Essencial'

print(dicionario)

print(dicionario['outro'])  # KeyError no dicionário comum, mas aqui não.

print(dicionario)
