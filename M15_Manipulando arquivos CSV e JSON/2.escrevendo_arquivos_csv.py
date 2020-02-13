"""
Escrevendo em arquivos CSV

reader() -> leitor, writer() -> escrita

writerow() -> Escreve uma linha


# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos
# o método writerow() para escrever cada linha. Este método recebe uma lista.

from csv import writer

with open('M15_Manipulando arquivos CSV e JSON/filmes.csv', 'w') as file:
    escritor_csv = writer(file)
    filme = ''
    cabecalho = escritor_csv.writerow(['Título', 'Genêro', 'Duração'])
    while filme.lower() != 'sair':
        filme = input(
            'Informe o nome do filme ou "sair" para finalizar o programa: ')
        if filme.lower() != 'sair':
            genero = input('Informe o genêro do filme: ')
            duracao = input('Informe a duração do filme (em min.): ')
            escritor_csv.writerow([filme, genero, duracao])

"""
# DictWriter

# OBS: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.

from csv import DictWriter

with open('M15_Manipulando arquivos CSV e JSON/filmes.csv', 'w') as file:
    cabecalho = ['Título', 'Gênero', 'Duração (em min.)']
    escritor_csv = DictWriter(file, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = ''
    while filme.lower() != 'sair':
        filme = input(
            'Informe o nome do filme ou "sair" para finalizar o programa: ')
        if filme.lower() != 'sair':
            genero = input('Informe o genêro do filme: ')
            duracao = input('Informe a duração do filme (em min.): ')
            escritor_csv.writerow(
                {"Título": filme, "Gênero": genero, "Duração (em min.)": duracao})
