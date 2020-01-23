"""
Preservando Metadatas com Wraps

Metadados -> São dados intrísecos em arquivos

wraps -> São funções que envolvem elementos com diversas finalidades


# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        '''Eu sou uma função(logar) de outra'''
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    '''Soma 2 números'''
    return a + b


# print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)

"""
# Resolução do Problema acima
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma 2 números"""
    return a + b


# print(f'Soma = {soma(10, 30)}')

print(soma.__name__)
print(soma.__doc__)

print(help(soma))
