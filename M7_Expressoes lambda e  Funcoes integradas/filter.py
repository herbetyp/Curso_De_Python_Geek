"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

print(f'Média: {media}')
# Assim como a função map() a filter() recebe 2 parametros, sendo uma função e um iterável

res = filter(lambda valor: valor > media, dados)

# OBS: Assim como na função map() após serem utilizados os dados de filter() eles são excluídos da memória
print(list(res))
print(list(res))

paises = ['', 'Argentina', '', '', 'Brasil', 'Chile',
          '', 'Colombia', '', '', 'Equador', '', 'Venezuela']

# Exemplos
res = filter(None, paises)

print(list(res))

paises = ['', 'Argentina', '', '', 'Brasil', 'Chile',
          '', 'Colombia', '', '', 'Equador', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)

print(tuple(res))

# A diferença entre map() e filter() é:

# - No map() recebe 2 parametros, uma funcao e um iteravel e retorna um objeto mapeado
# da função para cada elemento do iterável

# - No filter() recebe 2 parametros, uma função e um iterável e retorna umn objeto
# filtrando apenas os elemntos de acordo com a função


# Exemplo mais complexo

usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu gosto de Python', 'Django é massa']},
    {'username': 'Carla', 'tweets': ['Eu gosto de Java']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'Bob123', 'tweets': ['Eu gosto de Java', 'Spring é massa']},
    {'username': 'Dogo', 'tweets': ['C# é massa']},
    {'username': 'Gal', 'tweets': []},
]

# Filtrar os usuários que estão inativo acima -> Inativos sáo os que estão vazios -> []

# Forma 1
inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda user: not user['tweets'], usuarios))
print(inativos)

"""
# Combinar filter() e map()

# Devemos criar uma lista 'Sua instrutora é ' + nome, desde que cada nome tenha menos de 5 caracteres

nomes = ['Vanessa Maia', 'Ana', 'Maria']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(
    lambda nome: len(nome) < 5, nomes)))

print(lista)
