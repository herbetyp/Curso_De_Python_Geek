"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro do mesmo

Se agente pensar em um programa qualquer, geralmente temos

entrada -> processamento -> saida

Se agente em uma função, já sabemos que temos funções que 

- Não possuem entrada
- Não possuem saída
- Possuem entrada mais não possuem saída
- Não possuem entrada mais possuem saída
- Possuem entrada e saída

def quadrado(num):
    # return num * num
    return num ** 2
    
# Refatorando uma função

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(8)
print(ret)

print(quadrado())  # TypeError

# Refatorando a função


def cantar_parabens(aniversariante):
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas Felicidades')
    print(f'Muitos anos de vida {aniversariante}')


cantar_parabens('Herbety')

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma funçãoquantos parâmetros forem necessários. Eles são separados por vírgula

# Exemplos


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print('## Soma')
print(soma(2, 5))
print(soma(10, 20))

print('## Multiplica')
print(multiplica(4, 5))
print(multiplica(2, 8))

print('## Outra')
print(outra(3, 2, 'Python'))
print(outra(5, 4, 'Django'))


# Se agente informar um número errado de parâmetro ou argumento, teremos TypeError

# print(soma(1, 2, 3))  # TypeError - Passando agumentos a mais

# print(soma(1))  # TypeError - Passando argumentos de menos

# Nomeando parâmetros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Agenlina', 'Jolie'))


# A diferença entre Parâmetros e Argumentos

# Parâmetros são variaveis na definição de uma função
# Argumentos são dados passados durante a execução de uma função

# A ordem dos parâmetros importa

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utlizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

"""

# Erro comum na utlização do return

# Cuidado ao usar o return dentro de loops, pois se a função executar o loop
# e cair no return a mesma será encerrada


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num

    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
