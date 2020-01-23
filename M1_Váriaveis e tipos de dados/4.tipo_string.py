"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre áspas simples -> 'uma string', '234', 'a', 'True' , '42.3'
- Estiver entre áspas duplas -> "uma string", "234", "a", "True" , "42.3"
- Estiver entre áspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''' , '''42.3'''

nome = 'Python'
print(nome)
print(type(nome))

nome = "Gina's Bar" -> O bom é usar áspas duplas
print(nome)
print(type(nome)

nome = Linguagem \nPython" -> O caractere \n serve para pular uma linha.
print(nome)
print(type(nome))

nome = "Linguagem \" Python"
print(nome)
print(type(nome))

print(nome.upper()) -> Converte para maiúsculo toda string

print(nome.lower()) -> Converte para minúsculo toda string

print(nome.split()) -> Transforma em uma lista de strings



"""
# Estiver entre áspas duplas triplas -> """uma string""", """234""", """a""", """True""" , """42.3"""

# [ 0,   1,   2,   3,   4,   5 ,  6,   7,   8,   9,   10,  11,  12,  13,  14,   15]
#
# ['L', 'i', 'n', 'g', 'u', 'a', 'g', 'e', 'm', ' ' , 'P', 'y', 't', 'h', 'o', 'n']
nome = "Linguagem Python"
print(nome[0:9])# -> Slice de string

print(nome[0:16])# -> Slice de string

# [     0,         1    ]
# ['Linguagem' 'Python' ]
print(nome.split()[0])

print(nome.split()[1])

# [::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
print(nome[::-1]) #Inversão de string Pythônica

print(nome.replace('h', 't')) # -> Substitui um caractere por outro

texto = "Socorram me subino onibus em marrocos" # Palíndromo
print(texto)

print(texto[::-1])

nome = "Ana" # Palíndromo
print(nome)

print(nome[::-1])











