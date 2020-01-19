"""
Recebendo dados do usuário

input() -> Todo dado recebido via input() é  do tipo 'String'

Em Python, tudo que estiver entre:

- Aspas simples
- Aspas duplas
- Aspas simples triplas
- Aspas duplas triplas

Exemplos:
- Aspas simples -> 'Python'
- Aspas duplas -> "Python"
- Aspas simples triplas -> '''Python'''
"""
# Aspas duplas triplas -> """Python"""


# Entrada de dados
# print("Qual seu nome: ")
# nome = input() # input -> entrada de dados

nome = input('Qual seu nome? ').title()

# Exemplo de print 'antigo' Python v2.x
# print("Seja bem vindo %s" % nome)

# Exemplo de print 'moderno' Python v3.x
# print("Seja bem vindo(a) {}".format(nome))

# Exemplo de print mais 'atual' Python v3.7
print(f'Seja Bem vindo(a) {nome}')

idade = int(input("Qual é sua idade? "))

# Processamento

# Saida de dados
# Exemplo de print 'antigo' Python v2.x
# print("A %s tem %s anos" % (nome, idade))

# Exemplo de print 'moderno' Python v3.x
# print("A {} tem {} anos ".format(nome, idade))

# Exemplo de print mais 'atual' Python v3.7
print(f'{nome} tem {idade} anos')

# Cast é a 'conversão' de um tipo de dado para outro.
# int(idade) -> cast

print(f'{nome} nasceu em {2019 - idade}')


