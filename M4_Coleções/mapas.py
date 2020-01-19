"""
Mapas -> Conhecidos em Python como dicionários

Dicionários em Python são representados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# interar sobre dicionários
for chave in receita:
    print(chave)
    
for chave in receita:
    print(receita[chave])
    
for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves

print(receita.keys())

for chave in receita.keys(): # Recomendado
    print(receita[chave])

# Acessando os valores

print(receita.values())

for valor in receita.values(): # Recomendado
    print(valor)

print(receita.items())

# Desempacotamento de dicionários

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

# Soma*, Valor Máximo*, Valor Minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')
