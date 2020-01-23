"""
Módulos Externos 

Utilizamos o gerenciador de pacotes Python chamado Pip - Python installer Package

Você pode conhecer todos os pacotes oficiais em: https://pypi.org


colorama -> É utilizado para permitir impressao de textos coloridos no terminal

# Intalando o pacote Colorama -> pip install colorama

# Utilizando o pacote instalado

from colorama import init, Fore, Back

init()

print(Fore.MAGENTA + 'PYTHON')
print(Fore.CYAN + 'PYTHON')
print(Fore.RED + 'PYTHON')
print(Fore.GREEN + 'PYTHON')
print(Fore.YELLOW + 'PYTHON')
"""

import pydf

pdf = pydf.generate_pdf('<h1>Hello Python</h1>')
with open('Teoria_Pratica/M10 - Leitura e Escrita de Arquivos/test_doc.pdf', 'wb') as f:
    f.write(pdf)
