"""
Levantando os própios erros com o raise

raise -> lança exceções

OBS: O raise não é uma função, é uma palavra reservada, assim como def ou qualquer outra em Python

Para simplicar, pense no raise como sendo util para que possamos criar nossas própias exceções
e menssagens de erro

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

# Exemplo

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')

    print(f'O texto {texto} será impresso na cor {cor}')


colore(10, 'branco')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado

"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) != str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) != str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')

    print(f'O texto {texto} será impresso na cor {cor}')


colore('Top', 'vermelho')
