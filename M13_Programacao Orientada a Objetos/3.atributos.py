"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos
    atributos conseguimos representar computacionalmente os estados de um 
    objeto. 

Em Python dividimos os atributos em 3 grupos
    - Atibutos de instâncias.
    - Atributos de classe.
    - Atributos dinâmicos.

# Atributos de instância: são atributos declarados dentro do método construtor.


# Atributos Públicos e Atributos Privados

Em Python, por convenção ficou estabelecido que, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como privado,
ou seja, que deve ser acessado/utilizado somente dentro da própia classe onde
está declarado, utiliza-se __ duplo underscore no inicio de seu nome

# Isso é conhecido também como Name Mangling

Lembre-se que isso é apenas uma convenção, ou seja, a linguagem  Python não
vai impedir que façamos acesso aos atributos sinalizados como privados fora
da classe


## Atributos de Instância

Atributos de Instância, significa que ao criarmos intâncias/objetos de uma classe
todas as instâncias terão estes atributos.

# Classes com atributos Públicos

# OBS: Método construtor: É um método especial utilizado para a construção do objeto


class Lampada:

    def __init__(self, voltagem, cor):  # Método Construtor
        self.voltagem = voltagem    |
        self.cor = cor              | Atributos de instância
        self.ligada = False         |


class ContaCorrente:

    def __init__(self, numero, limite, saldo):  # Método Construtor
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):  # Método Construtor
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):  # Método Construtor
        self.nome = nome       |
        self.email = email     | Atributos de instância
        self.senha = senha     |


# Classes com atributos Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha  # Atributo Privado

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


user = Acesso('user@email.com', '123456')

print(user.email)  # AtributeError

# Temos acesso, mais não deveriamos fazer esse acesso.
print(user._Acesso__senha)  # (Name Mangling)

user.mostra_email()
user.mostra_senha()


user1 = Acesso('user1@email.com', '123456')
user2 = Acesso('user2@email.com', '789456')

user1.mostra_email()
user2.mostra_email()


## Atributos de Classe

Atributos de classe, são atributos, claro, que são declarados diretamente na
classe, ou seja, fora do construtor. Geralmente ja inicializamos um valor, e
esse valor é compartilhado entre todas as instâncias da classe. Ou seja, ao
invés de cada instância da classe ter seus própios valores, como é o caso dos
atributos de instancia, com os atributos de classe todas as intancias teram o
mesmo valor para este atributo

# Refatorar a classe produto


class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):  # Método Construtor
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4200)

print(p1.valor)  # Acesso possivel mais incorreto de um atributo de classe
print(p2.valor)

# OBS: Não precisamos criar uma instancia de uma classe para fazer acesso a um
atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)
"""

# Atributos Dinâmicos -> Um atributo de instância que pode ser cirado em tempo
# de execução

# OBS: O atributo dinâmico será exclusivo da instância que o criou


class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):  # Método Construtor
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4200)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso

print(
    f'Produto: {p2.nome}\nDescrição: {p2.descricao}\nValor: {p2.valor}\nPeso: {p2.peso}')

# print(
#    f'Produto: {p1.nome}\nDescrição: {p1.descricao}\nValor: {p1.valor}\nPeso: {p1.peso}')

# Deletando atributos

print('## Antes da deleção ##')
print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)
del p2.peso
del p2.valor
del p2.descricao

print('## Após a deleção ##')
print(p1.__dict__)
print(p2.__dict__)
