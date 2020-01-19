"""
Tipo None

O tipo None em Python representa o tipo sem tipo, ou poderia ser conhecido também
como tipo vazio, porém, falar que é um tipo sem tipo é mais apropiado.

Obs: O tipo None é SEMPRE especificado com a primeira letra maiúscula.

Certo: None
Errado: none

Quando utilizamos:
- Podemos utilizar None quando queremos criar variável e inicializá-la com um tipo sem tipo, antes
de recebermos um valor final.

Obs:  O tipo None em Python sempre será considerado como False
"""

numeros = None

print(numeros)
print(type(numeros))

numeros = 1.44, 1.34, 5.67
print(numeros)
print(type(numeros))