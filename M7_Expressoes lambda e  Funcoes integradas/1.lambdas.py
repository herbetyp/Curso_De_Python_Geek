"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome,
ou seja, funções anônimas

# Função em Python

def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressão Lambda

lambda x: 3 * x + 1

# Como utlizar a expressão lambda

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com multiplas entradas


nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('angelina', 'JOLIE   '))
print(nome_completo(' FELICITY       ', 'jones'))

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas tambem

python = lambda: 'Como não amar Python'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(python())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))


# OBS:  Se passarmos mais argumentos do que parametros esperados teremos TypeError

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke',
           'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Bracket']

autores.sort(key=lambda sobrenome: sobrenome.split()[-1].lower())
print(autores)
"""

# Funções Qudrática
# f(x) = a * x ** 2 + b * x + c

# Defininindo a função


def gera_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x +c"""
    return lambda x: a * x ** 2 + b * x + c


# (3,0,1) argumentos da função (0) argumento das lambda
print(gera_funcao_quadratica(3, 0, 1)(0))
# (3,0,1) argumentos da função (1) argumento das lambda
print(gera_funcao_quadratica(3, 0, 1)(1))
# (3,0,1) argumentos da função (2) argumento das lambda
print(gera_funcao_quadratica(3, 0, 1)(2))
