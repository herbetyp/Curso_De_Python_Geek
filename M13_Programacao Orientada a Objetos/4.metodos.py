"""
POO - Métodos

Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações
que este objeto pode realizar no seu sistema

Em Python dividimos os metodos, em dois grupos: Métodos de instância e os 
Métodos de Classe.


## Métodos de instância

# O método dunder init __init__ é um método especial chamado construtor e sua
função e contruir um objeto a partir da classe

# OBS: Todo elemento em Python que inicia e finaliza com duplo underline é 
chamado de dunder (Double Underline)

# OBS: Os métodos/funções em Python são chamados de métodos mágicos 

# ATENÇÃO: Pos mais que possamos criar nossas própias funções utilizando dunder
(undeline no inicio e no fim) não é aconselhado. Python possui varios metodos com 
esta forma de nomeclatura e pode ser que mudemos o comportamento dessas funções
mágicas internas da linguagem. Então, evite ao máximo. De preferencia nunca faça!

# Métodos são escritos com letras minusculas. Se o nome for composto, o nome terá
as palavras separadas por underline

from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):  # Método Construtor
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):  # Método Construtor
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):  # Método com nome simples
        ""Retorna o valor do produto com o desconto""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):  # Método com nome composto
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        ""Criptografa a senha""
        if cryp.verify(senha, self.__senha):
            return True
        return False


p1 = Produto('Playstation 4', 'Video Game', 2300)
print(p1.desconto(50))


user = Usuario('Herbety', 'Paulo', 'user@email.com', '123456')

print(user.nome_completo())

# Acesso de forma errada a um atributo de classe
print(f'Senha user: {user._Usuario__senha}')

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe o senha: ')
confirma_senha = input('Informe o confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para o acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido!')
else:
    print('Acesso negado!')


## Métodos de Classe

# Métodos de Classe em Python são conhecidos como métodos estáticos em outras linguagens

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @classmethod
    def ver(self):
        print('Teste')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):  # Método com nome composto
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        ""Criptografa a senha""
        if cryp.verify(senha, self.__senha):
            return True
        return False


user = Usuario('Herbety', 'Paulo', 'email@email.com', '123456')

Usuario.conta_usuario()  # Forma Correta
user.conta_usuario()  # Forma incorreta

"""
# Método Privado
from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    # Métodos de Classe
    @classmethod
    def conta_usuario(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @classmethod
    def ver(self):
        print('Teste')

    # Método Estático
    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):  # Método com nome composto
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        """Criptografa a senha"""
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):  # Metodo Privado
        return self.__email.split('@')[0]


user = Usuario('Herbety', 'Paulo', 'herbety@email.com', '123456')


# Método estático

print(Usuario.contador)
print(Usuario.definicao())

user = Usuario('Herbety', 'Paulo', 'herbety@email.com', '123456')

print(user.contador)
print(user.definicao())
