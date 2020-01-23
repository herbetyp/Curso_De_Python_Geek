"""
Decorators com diferentes assinaturas

# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern

# Relembrando Decorator


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o(a) {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá eu gostario de {principal}, acompanhado de {acompanhamento}, por favor.'


# Teste

# print(saudacao('Angelina'))

# Dessa forma é gerado um
# TypeError: aumentar() takes 1 positional argument but 2 were given

print(ordenar('Picanha', 'Batata Frinta'))

# Refatorando com a Decorator Pattern
# A assinatura de uma função é representada pelo seu retorno, nome e parametros
# de entrada


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o(a) {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}'


# Teste
print(saudacao('Felicity'))

print(ordenar('Picanha', 'Batata Frita'))


@gritar
def lol():
    return 'lol'


print(lol())


# OBS: Vale lembrar que podemos utilizar parametros nomeados

print(ordenar(principal='Pincanha', acompanhamento='Batata Frita'))

"""
# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto. Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Teste

print(soma_dez(10, 12))

print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churrasco'))

print(comida_favorita('sanduiche', 'pizza'))
