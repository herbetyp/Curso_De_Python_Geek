"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variável = valor_da_variável

Python é uma línguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atríbuirmos a mesma.

Exemplo em  C:
int numero = 42

Exemplo em java:
int numero = 42

"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = "Python"
print(numero)
print(type(numero))

nao_existo = "oi"
print(nao_existo)

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco if. Portanto, é local
    print(novo)

# print(novo)

