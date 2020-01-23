"""
Listas (list)

Listas em Python funcionão como vetores/matrizes (arrays) em outras linguagens, com diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nessas linguagens se você criar um array do tipo int e com o tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ser SEMPRE no máximo 5 valores.

Já em Python:

- Dinâmico: Não possui tamanho fixo. Ou seja podemos criar a lista e simplismente ir adicionando elementos
- Qualquer tipo de dado: As listas não possui tipo de dado fixo. Ou seja, podemos colocar qualquer tipo de dado
- As listas em Python são representadas por colchetes: []

- Listas são mutáveis, ou seja, elas podem mudar constantemente

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1]

lista2 = ['G', 'e', 'e', 'k']

lista3 = []

lista4 = list(range(7))

lista5 = list('Geek')

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1]

lista2 = ['G', 'e', 'e', 'k']

lista3 = []

lista4 = list(range(7))

lista5 = list('Geek')

#  Podemos facilmente checar se determinado valor está contido na lista
num = 5
if num in lista4:
    print(f'Tem o número {num}')
else:
    print(f'não tem o número {num}')

#  Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

#  Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

#  Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append
Obs: Com append, nós só conseguimos adicionar 1 elemento por vez
lista1.append(12, 34, 66) <- erro

print(lista1)
lista1.append(42)  # Para adiconar um elemento por vez
print(lista1)

lista1.append([3, 9, 12])  # Coloca a lista como elemento único (sublista)
print(lista1)

if [3, 9, 12] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional a lista
print(lista1)

#  Podemos inserir um novo elemento na lista informando a posição do índice
# Obs: Isso não substitui o valor inicial. O mesmo será deslocado para direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas

lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1)
print(lista2)

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existe dentro da lista
print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista
# Obs: O pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# Obs: Os elementos a direita deste índice serão deslocados para esquerda
# Obs: Se não houver elemento no índice informado, teremos o erro "IndexError"
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos da lista
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente coverter uma string para uma lista

# Exemplo 1

curso = 'Python Essencial'
print(curso)
curso = curso.split()
print(curso)

# Obs: O split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Python', 'd', [1, 2, 3], 123456789]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
# Obs: Para entender melhor o índice negativo, pense na lista como um círculo, onde
# o final de um elemento está ligado ao ínicio da lista

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])
print(cores[-5])  # Erro, pois não existe índice -5 nessa lista

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = [42, 42, 33, 33, 42]
print(lista)

# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista
num = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice da lista está o valor 6
print(num.index(6))

# Em qual índice da lista está o valor 9
print(num.index(9))

# Obs: Caso não tenha este elemento na lista, será apresentado erro ValueError

# Obs: Retorna o índice do primeiro elemento encontrado
print(num.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(num.index(5, 1))  # Buscando a partir do índice 1
print(num.index(5, 2))  # Buscando a partir do índice 2
print(num.index(5, 3))  # Buscando a partir do índice 3
# print(num.index(5, 4))  # Buscando a partir do índice 4
# Obs: Caso não tenha este elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, ínicio/fim
print(num.index(8, 3, 6))  # Buscar o índice do valor 8, entre os índices 3 e 6

# Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parâmetro 'ínicio'

lista = [1, 2, 3, 4]

print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com parâmetro 'fim'

print(lista[:2])  # Começa em 0 pega até o índice 2 - 1

print(lista[:4])  # Começa em 0 pega até o índice 4 - 1

print(lista[1:3])  # Começa em 1 pega até o índice 3 - 1

# Trabalhando com slice de lista com parâmetro 'passo'

print(lista[1::2])  # Começa em 1, vai até o final, de 2 em 2

print(lista[::2])  # Começa em 0, vai até o final, de 2 em 2

# Invertendo valores em uma lista

nome = ['Python', 'Essencial']

nome.reverse()
print(nome)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # máximo valor
print(min(lista))  # mínimo valor
print(len(lista))  # tamanho da lista

# Transfromar lista em Tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Obs: Se tivermos um número diferente de elementos na lista ou váriaveis para receber os dados, teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.deepcopy()  # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista
# mas elas ficaram totalmente independentes, ou seja, modificando uma lista não afeta
# a outra. Isso em Python, é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para nova lista, mas
# após realizar modificação em uma das listas, essas modificações se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy (cópia rasa)

"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1]

lista1.insert(2, 'Novo valor')
print(lista1)
