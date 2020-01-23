"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta perfomance

from collections import deque

# Criando deques

deq = deque('python')

# Adicionando elementos no deque

deq.append('10') # Adiciona no final

print(deq)

deq.appendleft('10')  # Adiciona no começo

print(deq)

# Remover elementos

print(deq.pop()) # Remove o último elemento

print(deq)

print(deq.popleft()) # Remove o primeiro elemento

print(deq)
"""
from collections import deque

# Criando deques

deq = deque('python')

# Adicionando elementos no deque

deq.append('10')  # Adiciona no final
print(deq)
