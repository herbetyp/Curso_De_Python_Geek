"""
Tipo Booleano

Algebra Booleana, criada por George Boole

O constante, verdadeiro e falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial 'maiúscula'

Errado:

true, false

Certo:

True, False

"""

ativo = True
print(ativo)

"""
Operações básicas:

"""
# Negação (not):
"""
Fazendo a negação, se o valor booleano for veraddeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""

print(not ativo)

logado = False

# ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""

print(ativo or logado)

# e (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os
devem ser verdadeiro

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""