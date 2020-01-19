"""
Funções com parâmetros Padrão (Default Parameters)


- Funções onde a passagem de parâmetro é opcional

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Python)

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado())  # TypeError

def exponencial(numero=0, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))  # por padrão eleva ao quadrado
print(exponencial(3, 3))  # eleva a potência informada pelo usuário


# OBS: Se o usuário passar somento um atributo, este será atribuído ao parâmetro
# numero, e será calculado o quadrado deste número. Sé o usuário passar dois argumentos
# o primeiro será atribuido ao parametro numero e o segundo ao parametro potencia. Entao
# sera calculada esta potencia

print(exponencial())

# OBS: Em funções Python, os paramêtros com valores default (padrão) DEVEM estar
# ao final da declaração

# ERRO:

def teste(potencia, num=2, ):
    return num ** potencia


print(teste(6))

# Outros exemplos


def soma(num1=0, num2=0):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())  # TypeError

# Exemplo mais complexo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Sthefany'))

# Porque utilizar parâmetros com valor default (padrao)

# 1 - Nos permite ser mais flexiveis nas funçoes
# 2 - Evita erros com parametros incorretos
# 3 - Nos permite trabalhar com exemplos mais legiveis de codigo


# Quais são tipos de dados podemos utilizar como valores default para paramêtros

# - Qualquer tipo de dado:
#    - numeros, strings, floats, booleanos, tuplas, dicionarios, funcoes e etc

# Exemplos de funções como parametro

def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))


# Exemplo de Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # variável global


def diz_oi():
    instrutor = 'Python'  # variável local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a
# local terá preferencia

def diz_oi():
    prof = 'Geek'
    return f'Olá {prof}'


print(diz_oi())
print(prof)  # NameError

# ATENÇÃO com variaveis globais, se puder evitar, evite!

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variavel global

    total = total + 1
    return total


# UnboundLocalError (A variavel local esta sendo utilizada, para processamento, sem ter sido inicializada)
print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())

"""
# Podemos ter funcoes que sao declaradas dentro de funcoes e tamebm tem uma forma
# especial de escopo de variavel


def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())  # NameError
