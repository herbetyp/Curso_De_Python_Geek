"""
Estruturas Lógicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True
Para o 'is', o valor é comparado com um segundo valor
"""

ativo = True
logado = False

if ativo or logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conra. Por favor, cheque seu email')

#--------------------------------------------------------------------------#

ativo = True
logado = True

if ativo and logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conra. Por favor, cheque seu email')

#---------------------------------------------------------------------------#

# Se não estiver ativo
ativo = False
logado = True

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu email')
else:
    print('Bem vindo usuário')
#-------------------------------------------------------------------------#

ativo = False
logado = True

if ativo is False:
    print('Você precisa ativar sua conta. Por favor, cheque seu email')
else:
    print('Bem vindo usuário')

# ativo é Falso:
print(ativo is True)
