"""
Tipo Float

Tipo real
Tipo decimal,que possui casas decimais

OBS: Os separadores de casas decimais na programação é o ponto(ponto_flutuante) e não a vírgula.
"""

# Errado do ponto de vista do float, porém gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

# É possível dupla atribuição
# OBS: Os valores serão atríbuidos para respectiva variável
# Exemplo: variavel1, variave2 = valor1, valor2 ('variavel1' <- 'valor1') ('variavel2' <- 'valor2').....

valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
# OBS: Ao coverter valores float para int perdemos a precisão

res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
print(variavel)
print(type(variavel))
