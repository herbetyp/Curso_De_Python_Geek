"""
**kwargs

Poderiamos chamar este parametro de **xis, mas por convenção chamamos de **kwargs

Este é so mais um paramtero, mais diferente do *args que coloca os valores extras
emuma tupla, o **kwargs exige que utilizemos parametros nomeados, e transforma
esses parametros extras em um dicionario

# Exemplos

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo',
                fernanda='azul', vanessa='branco')


# OBS:  Nem os parametros *args e **kwargs não são obrigatorios

cores_favoritas()
cores_favoritas(geek='navy')

# Exemplo mais complexo


def comprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um comprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem voce é'


print(comprimento_especial())
print(comprimento_especial(geek='Python'))
print(comprimento_especial(geek='Oi'))
print(comprimento_especial(geek='Especial'))

# Nas nossas funcoes podemos ter (NESTA ORDEM):

# - Parametros obrigatorios
# - *args
# - Parametros default (nao sao obrigatorios)
# - **kwargs

# Exemplo


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='vai')
minha_funcao(19, 9, 4, 3, java=False, python=True)

# Entendendo por que é importante manter a rodem dos parametros de declaracao


# Funcao com a ordem correta de parametros
# def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#     return [a, b, args, instrutor, kwargs]


# Funcao com a ordem incorreta de parametros
def mostra_info(a, b, instrutor='Geek', *args,  **kwargs):
    return [a, b, args, instrutor, kwargs]


a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))


"""


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS: Os nomes da chave em um dicionario devem ser os mesmos dos parametros da funcao

# dicionario = dict(d=1, e=2, f=3) # TypeError
#
# soma_multiplos_numeros(**dicionario)
dicionario = dict(a=1, b=2, c=3, nome='Geek')


soma_multiplos_numeros(**dicionario, lang='Python')
