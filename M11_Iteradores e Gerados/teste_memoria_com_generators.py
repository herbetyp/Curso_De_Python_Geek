"""
Teste de Memória com Generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...

# Função usando listas 454MB


def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste 1
for n in fib_list(100000):
    print(n)

"""
# Função usando geradores 7.9MB


def fib_gen_max(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2
for n in fib_gen_max(100000):
    print(n)
