"""
Tuples (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças:

1 - As tuplas são representadas po parênteses ()
2 - As tuplas são imutáveis, isso significa que ao se criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # isso não é uma tupla é um int
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4, # Isso é uma tupla
print(tupla5)
print(type(tupla5))

(4) -> não é tupla
(4,) -> é tupla
4, -> é tupla

# CONCLUSÃO: podemos concluir que tuplas são definidas pelo uso da vírgula e não pelo parênteses


# Podemos gerar uma tupla dinamicamente com range(inicio, fim, parada)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de Tupla
tupla = ("Python", "Essencial")
linguagem, curso = tupla
print(linguagem)
print(curso)
# Obs: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar

# Métodos de adição e remoção de elementos nas tuplas nãi existem, dado o fato qeu tuplas são imutáveis

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de Tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

tupla3 = (tupla1 + tupla2)  # tuplas são imutáveis

print(tupla3)

tupla1 = tupla1 + tupla2  # tupla são imutáveis, mas podemos subscrever os valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'e', 'a', 'b')
print(tupla.count('c'))

linguagem = tuple('Python')
print(linguagem)

print(linguagem.count('y'))

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho')
print(meses)

# Dicas na utilização de tuplas


# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho')

# Slicing

# tupla[inicio:fim:passo]

print(meses[2:4])

# Acesso de elementos de uma tupla é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificamos em qual índice um elemento está na tupla
print(meses.index('Abril'))

# Obs: Caso o elemento não exista, será gerado ValueError

# Por que utlizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*.

# - Isso porque trabalhar com elementos imutáveis traz segurança ao código.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de Shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)

"""
tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de Shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova += outra

print(nova)
print(tupla)
