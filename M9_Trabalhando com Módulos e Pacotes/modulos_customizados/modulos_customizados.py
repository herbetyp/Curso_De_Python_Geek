"""
Módulos Customizados

Como módulos POython nada mais são arquivos Python, então TODOS os arquivos que criamos
até agora são módulos Python prontos para serem utilizados


# Importanto uma função especifica do nosso modulo

from funcoes_com_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Importanto todo o módulo (Temos acesso a todas funções do módulo)

import funcoes_com_parametros as fcp


# Acessando e imprimindo variável contida no módulo

print(fcp.soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

print(fcp.lista)

print(fcp.tupla)
"""
from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))
