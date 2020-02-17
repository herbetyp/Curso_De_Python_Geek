"""
Doctests

Doctests são teste que colocamos nas docstrings das funções/métodos Python

def soma(a, b):
    # soma os numeros a e b

    # >>> soma(1, 2)
    3

    # >>> soma(4, 6)
    10
    
    return a + b

print(soma(3, 4))


Para rodar um test doctest:

python3 -m doctest -v nome_do_modulo.py

# Saída

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.


# Outro exemplo. Aplicando o TDD


def duplicar(valores):
    # Duplica os valores em um uma lista

    # >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    # >>> duplicar([])
    []

    # >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    # >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    #
    
    return [2 * elemento for elemento in valores]


# Erro inesparado...

# OBS: Dentro do doctest, p python não reconhece string com aspas duplas, precisa
ser aspas simples

def fala_oi():
    # Fala oi

    # >>> fala_oi()
    'oi'
    #
    return "oi"

"""

# Um ultimo caso estranho...

# OBS: Se houver espaços na saida espera, seu teste não passará
# - Como exemplo abaixo se houver espaço após o True do doctest,
# o mesmo falhará


def verdade():
    """Retona verdade

    >>> verdade()
    True
    """
    return True
