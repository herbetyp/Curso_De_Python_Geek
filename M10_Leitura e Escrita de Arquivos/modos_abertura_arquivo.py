"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita. (Temos o controle do cursor)

#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
será adicionado SEMPRE ao final do arquivo. Com o modo 'a', não controlamos o cursor.

http://docs.python.org/3/library/functions.html#open

# Exemplo x
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe')


# Exemplo a
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break


# Exemplo r+
with open('outro.txt', 'r+') as arquivo:
    arquivo.write('Adicionada\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(32)
    arquivo.write('Mais uma linha.\n')
"""
"""
Validar um CPF
"""
cpf_completo = "168.995.350.09".rjust(
    11, '0').replace('.', '')  # Número do CPF a ser validado, formato com zeros a esquerda até 11 posições
cpf = cpf_completo[:9]  # Seleciona somente os 9 primeiro dígitos do CPF
pesos = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
digitos = []

for n in range(2):
    soma = 0
    peso = 0
    # Ler os dígitos do CPF da direita para a esquerda
    for indice in range(len(cpf)-1, -1, -1):
        soma += int(cpf[indice]) * pesos[peso]
        peso = 0 if peso == 9 else peso + 1

    digito = 11 - (soma % 11)
    # Se o dígito for maior que 9 tem o dígito recebe 0
    digito = 0 if digito > 9 else digito
    digitos.append(digito)
    cpf += str(digito)

print()
print(f"Digitos = {digitos}")
print("O CPF é válido" if cpf == cpf_completo else "O CPF NÃO É válido")
