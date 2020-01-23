"""
Geradores 

- Geradores (Generators) são (Iteradores):

OBS: O contrário não é verdadeiro. Ou seja, nem todo Iterador é um generator

Outras informações:
- Generators podem ser criados com funções geradoras
- Funções geradoras utilizam a palavra reservada yield
- Generators podem ser criados com Expressões Geradoras

Diferenças entre Funções e Generator Functions (Funções Geradoras)

-------------------------------------------------------------------------------
| Funções                              | Generator Functions                  |
-------------------------------------------------------------------------------
| utilizam return                      | utilizam yield                       |
-------------------------------------------------------------------------------
| retorna uma vez                      | podem utilizar yield multiplas vezes |
-------------------------------------------------------------------------------
| quando executada, retorna um valor   |quando executada, retorna um generator|
-------------------------------------------------------------------------------


# Exemplo de Função geradora (Generator Functions)


def conta_ate(max_value):
    contador = 1
    while contador <= max_value:
        yield contador
        contador = contador + 1

# OBS: Um Generator Function não é um Genarator. Ele gera um generator!


gen = conta_ate(5)

# print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# Exemplo de Função geradora (Generator Functions)


def conta_ate(max_value):
    contador = 1
    while contador <= max_value:
        yield contador
        contador = contador + 1

# OBS: Um Generator Function não é um Genarator. Ele gera um generator!


gen = conta_ate(10)

for num in gen:
    print(num)

gen = conta_ate(10)

print(next(gen))
print()

for num in gen:
    print(num)

"""

# Exemplo de Função geradora (Generator Functions)


def conta_ate(max_value):
    contador = 1
    while contador <= max_value:
        yield contador
        contador = contador + 1

# OBS: Um Generator Function não é um Genarator. Ele gera um generator!


gen = list(conta_ate(10))

print(gen)
