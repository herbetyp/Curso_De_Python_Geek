"""
Debugando com PDB

PDB -> Python Debug

# OBS: A utilização do print() para debugar o código é uma má pratica

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o erro: {err}'


print(dividir(4, 7))

# Existem formas mais profissionais de se fazer o 'debug', utilizamos o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o Pycharm, Vscode entre
# outras os utilizando o PDB (Python Debugger)

# Exemplo com o Vscode


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o erro: {err}'


print(dividir(4, 0))


# Comandos básicos do PDB
# l (listar onde estamos no codigo)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finalizando o debugging)

# Exemplo com PDB (Python Debugger) - Exemplo 1

# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então
# utilizar a função set trace()

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Comandos básicos do PDB
# l (listar onde estamos no codigo)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finalizando o debugging)


# Exemplo com PDB (Python Debugger) - Exemplo 2

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então
# utilizar a função set trace()

# A partir do Python 3.7, não é mais necessário importar a bliblioteca pdb, pois o comando
# de debug foi incorporado como função built-in (integrada) chamada de breakpoint

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

OBS: Cuidado com conflitos entre nomes de variaveis e os tamanhos do pdb
"""


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))

# Como os nome das variaveis são os mesmos do pdb, devemos utilizar o comando 'p'
# para imprimir as variaveis. Ou seja: p nome_da_variavel
