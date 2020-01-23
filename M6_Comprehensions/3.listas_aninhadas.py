"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamados de arrays
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

Em Python nós temos as listas

numeros = [1, 'b', 3.25, True, 5]

print(listas)

print(type(listas))

# Exemplos

# Como fazemos para acessar os dados

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas[0][1])  # 2

print(listas[2][1])  # 8

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)


# List Comprehension
[[print(num) for num in lista] for lista in listas]


"""
# Outros Exemplos

# Gerando um tabuleiro/matriz 3X3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)


# Gerando jogadas para o jogo da velha
j_velha = [['X' if num %
            2 == 0 else 'O' for num in range(1, 4)] for valor in range(1, 4)]
print(j_velha)


# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
