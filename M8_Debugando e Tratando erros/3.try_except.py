"""
Bloco try/except

Utilizamos o bloco try/except para tratar erros que podem acontecer no nosso codigo.
Previnindo assim que o programa pare de funcionar e o usuario receba mensagens de 
erros inesperados

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problemas

# Tente executar a função geek(), se encontrar erros, imprima a mensagem de erro


# Exemplo 1 - Tratando erro generico

try:
    geek(5)
except:
    print('Deu algum problema')

# Tente executar a função geek(), se encontrar erros, imprima a mensagem de erro


# Exemplo 2 - Tratando erro generico

try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a função len(), se encontrar erros, imprima a mensagem de erro

OBS: Tratar erro de forma generica não é o correto, o ideal é SEMPRE tratar de 
forma especifica


# Exemplo 3 - Tratando erro especifico

try:
    geek()
except NameError:
    print('Você está utilizando a função de forma inexistente')


# Exemplo 4 - Tratando erro especifico

try:
    len(5)
except TypeError:
    print('Você está utilizando a função de forma inexistente')


# Exemplo 5 - Tratando um erro especifico com detalhe do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte error: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez

try:
    len(5)
except NameError as err:
    print(f'Deu NameError: {err}')
except TypeError as err:
    print(f'Deu TypeError: {err}')
except Exception:
    print('Deu um erro diferente')

"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dicionario = {'nome': 'Geek'}

print(pega_valor(dicionario, 7))
