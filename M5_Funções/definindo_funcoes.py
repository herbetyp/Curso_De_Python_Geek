"""
Definindo Funções

- Funções são pequenas partes partes de código que realizam tarefas específicas
- Pode ou não receber entradas de dados e retornar uma saída de dados
- Muitos uteis para executar procedimentos similares por repetidas vezes

OBS: Se você escrever uma função que realiza várias tarefas dentro dela
é bom fazer uma verificação para que a função seja simplificada

- Já utilizamos várias funções desde que iniciamos este curso

- print()
- len()
- max()
- min()
- sum()
- count()
- e muitas outras

"""
# Exemplo de utilização de funções:

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (built-in) do python print()

# print(cores)

# curso = 'Programação em Python: Essencial'

# print(curso)

# cores.append('roxo')
# print(cores)

# curso.append('Mais dados...')  # AtributeError
# # print(curso)

# cores.clear()
# print(cores)

# print(help(print))


# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código

# Mas então, como definir funções?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros de entrada):
    bloco da funcao

Onde: 

- nome_da_funcao -> SEMPRE com letras minúsculas, e se for nome composto, separado por
underline (Snake Case)

- parametros_de_entrada -> OPCIONAIS, onde tendo mais de um, cada um é separado por
vírgula, podendo ser opcoinais ou não

- bloco_da_funcao -> Tambem chamado de corpo da função ou implementação, é onde o
processamento da função acontece, neste bloco, pode ter ou não retorno da função

OBS:  Veja que para definir uma função utlizamos a palavra reservada 'def' informando
para o Python que estamos definindo uma função. Tambem abrimos o bloco de código, com o
já conhecido dois pontos (:) que é utilizado em Python para definir blocos

"""
# Definindo a primeira função

# Definição

# def diz_oi():
#    print('oi')


"""
OBS: 

1 - Veja que dentro das nossas funções podemos utilizar outras funções
2 - Veja que nossa função só executa uma taref, ou seja, a única coisa que ela faz é dizer oi
3 - Veja que esta função não recebe nenhum parametro de entrada
4 - Veja que esta função não retorna nada
"""

# Utilizando funções

# Chamada de execução

# diz_oi()

"""
ATENÇÃO:

Nunca esqueça de utiçlizar o parenteses ao executar uma função

Exemplo:

# ERRADO
diz_oi

# ERRADO
diz_oi ()

# CERTO
diz_oi()
"""

# Exemplo 2


def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas Felicidades')
    print('Muitos anos de vida')


# for n in range(4):
#     cantar_parabens()
#     print()

# Em Python podemos inclusive criar variáveis do tipode uma função e executar esta
# função atraves da variável

canta = cantar_parabens
canta()
