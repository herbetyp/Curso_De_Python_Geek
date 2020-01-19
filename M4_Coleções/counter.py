"""
Módulo Collections - Counter (contador)

# Documetação Oficial
https://docs.python.org/3.7/library/collections.html?highlight=collections#collections.Counter

Collections -> High-perfomance Container Datatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro
e como valor a quantidade de ocorrências desse elemento.


# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Python Essencial'))
Counter({'n': 2, 's': 2, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, ' ': 1, 'E': 1, 'e': 1, 'c': 1, 'i': 1, 'a': 1, 'l': 1})

from collections import Counter

# Exemplo 3

texto = 

A história pública é um campo de práticas da historiografia, geralmente praticado por pessoas ligadas ao estudo de História,
com o objetivo de interagir com públicos mais amplos do que o das universidades. Através das mais variadas práticas, 
como a elaboração de amostras em museus, intervenções artísticas, projetos de extensão universitária, documentários, 
aulas públicas, e muitas outras, a história pública busca ampliar a interação do público geral com o conhecimento histórico. 
O termo história pública foi cunhado originalmente na década de 1970 nos Estados Unidos pelo historiador Robert Kelley em meio 
à crise de desemprego dos recém formados do país. No entanto, práticas que buscam levar o conhecimento histórico para amplas 
audiências existiam muito antes da cunhagem do termo, de modo que vários historiadores reconheçam formas de história pública anteriores à publicação de Kelley. 

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
# print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
"""
from collections import Counter

texto = """A história pública é um campo de práticas da historiografia, geralmente praticado por pessoas ligadas ao estudo de História,
com o objetivo de interagir com públicos mais amplos do que o das universidades. Através das mais variadas práticas,
como a elaboração de amostras em museus, intervenções artísticas, projetos de extensão universitária, documentários,
aulas públicas, e muitas outras, a história pública busca ampliar a interação do público geral com o conhecimento histórico.
O termo história pública foi cunhado originalmente na década de 1970 nos Estados Unidos pelo historiador Robert Kelley em meio
à crise de desemprego dos recém formados do país. No entanto, práticas que buscam levar o conhecimento histórico para amplas
audiências existiam muito antes da cunhagem do termo, de modo que vários historiadores reconheçam formas de história pública anteriores à publicação de Kelley."""

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
# print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
