"""
Assertions (Afirmações)

Em Python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não. Se
a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo
AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma
mensagem de erro personalizada

# OBS:  A palavra 'assert' pode ser utilizada em qualquer função ou código nosso...
não precisa ser exclusivamente nos testes.


# ALERTA: CUIDADO ao utilizar o 'assert'

Se um programa Python for executado com o parametro -O, nenhum assertion será
executado. Ou seja, as duas validações não funcionaram.
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos numeros precisam ser positivos'
    return a + b


ret = soma_numeros_positivos(2, 6)  # 8
ret = soma_numeros_positivos(2, -2)  # AssertionError
print(ret)


def comer_fastfood(comida):
    assert comida.lower() in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita'
        'cachorro quente'
    ], 'A comida precisa ser fastfood'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')

print(comer_fastfood(comida))
