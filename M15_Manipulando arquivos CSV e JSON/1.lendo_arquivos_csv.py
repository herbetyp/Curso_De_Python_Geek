"""
Lendo arquivos CSV

csv - Comma Separeted Values - (Valores separados por vírgulas)

# Separado por vírgula

1, 2, 3, 4, 5, 6

# Separado por ponto e vírgula

'geek'; 'university'; 'python'

# Separado por espaço

1 2 3 4 5 6

'geek' 'university' 'python'

# Possivel de se trabalhar mais não é o ideal (trabalhoso)

with open('M15_Manipulando arquivos CSV e JSON/lutadores.csv') as file:
    dados = file.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

# A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts

# reader

from csv import reader

with open('M15_Manipulando arquivos CSV e JSON/lutadores.csv') as file:
    leitor_csv = reader(file)
    next(leitor_csv)  # pular cabeçalho
    for linha in leitor_csv:
        # cada linha é uma lista
        print(
            f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]}cm.')


# DictReader

from csv import DictReader

with open('M15_Manipulando arquivos CSV e JSON/lutadores.csv') as file:
    leitor_csv = DictReader(file)
    for linha in leitor_csv:
        # cada linha é OrderedDict
        print(
            f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}cm")

"""
# DictReader com outro separador

# OBS: Por padrão o reader e o DictReader usam a vírgula como separador(delimitador)
# se caso o arquivo CSV estiver com outro separador como ;(ponro e vírgula) pode-se
# usar o parametro delimiter=

from csv import DictReader

with open('M15_Manipulando arquivos CSV e JSON/lutadores.csv') as file:
    leitor_csv = DictReader(file, delimiter=',')  # muda o separador
    for linha in leitor_csv:
        # cada linha é OrderedDict
        print(
            f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}cm")
