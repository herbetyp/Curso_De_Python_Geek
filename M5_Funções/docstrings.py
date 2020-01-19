# Documentando funções com Docstrings
#
# OBS: Podemos ter acesso de uma função em Python utilizando a propiedade
# especial __doc__
#
# Podemos ainda ter acesso a documentação com a função help()
#
#
# # Exemplos
#
#
# def diz_oi():
#     """ Uma função simples que retorna a string 'Oi' """
#     return 'Oi'
#
#
# print(diz_oi())
#
# print(help(diz_oi))
#
# print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencia' informada
    :param numero: Número que deseja gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia


print(exponencial.__doc__)

print(help(exponencial))
