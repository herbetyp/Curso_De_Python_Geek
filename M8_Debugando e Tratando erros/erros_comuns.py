"""
Erros mais comuns em Python

Atenção: É importante prestar atenção e aprender a ler as saidas de erro geradas 
pela execução do nosso código

Os erros mais comuns

1 - SyntaxError -> Ocorre quando o python encorntra um erro de sintax. Ou seja, você 
escreveu algo que o Python não reconhece como parte da linguagem

# Exemplos SyntaxError 

a)

def funcao:
    print('Python é massa')

b)

def = 1

c)

return

2 - NameError -> Ocorre quando uma variável ou função nao foi definida

# Exemplos NameError

a)

print(python)

b)

python()

c)

a = 18

if a < 10:
    msg = 'É maior que 10'

print(msg)

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado

# Exemplos TypeError

a)

print(len(5))

b)

print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro
tipo de dado indexado utilizando um indice invalido

# Exemplos IndexError

a)

lista = ['Geek']
print(lista[2])

b)

lista = ['Geek']
print(lista[0][10])

c)

tupla = ('Geek',)
print(tupla[0][10])

5 - ValueError -> Ocorre quando uma função ou operação built-in (integrada) recebe
um argumento com tipo correto, mais valor inapropiado

# Exemplos ValueError

a)

print(int('Geek'))

b)
print(float('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave
que nao existe

# Exemplos KeyError

a)

dic = {}
print(dic['geek'])

7 - AttributeError -> Ocorre quando uma variavel não tem um atributo ou função

# Exemplos AttributeError

a)

tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

# Exemplos IndentationError

a)

def nova():
print('Geek')

b)

for i in range(10):
i + 1

OBS: Exceptions e Erros são equivalentes na programação

OBS: Importante ler e prestar atenção na saída de erro
"""
