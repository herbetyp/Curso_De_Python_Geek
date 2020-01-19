"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuario é DESTRUIR seu sistema.


# Else é executado somente se não ocorrer o erro

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')


# Finally

try:
    num = int(input('Inform um número: '))
except ValueError:
    print('Você digitou um valor invalido')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: o bloco finally sempre é executado, indepedente se houve exceção ou não

# O finally geralmente é utilizado para fechar ou desalocar recursos

# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro número: '))
try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')


# Exemplo mais complexo CORRETO
# Você é responsavel pelas entradas das suas funções, então trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por 0'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


"""
# Exemplo mais complexo SEMI-GENERICO
# Você é responsavel pelas entradas das suas funções, então trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o erro: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
