"""
POO - Herança (Inheritance)

A idéia de herança é a de reaproveitar código. Também extender nossas classes

OBS: Com a herança a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente:
    - nome:
    - sobrenome:
    - cpf:
    - renda:

Funcionario:
    - nome:
    - sobrenome:
    - cpf:
    - matricula:

Existe alguma entidade genérica o suficiente para encapsular os atributos e
métodos comuns a outras entidades?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Herbety', 'Paulo', '123.456.789-00', 5000)
funcionario1 = Funcionario('Paulo', 'Mendes', '789.456.123-11', 3000)


print(cliente1.nome_completo())
print(funcionario1.nome_completo())


OBS: Quando uma classe herda de outra classe, ela herda TODOS os atributos e
métodos da classe herdada

Quando uma classe herda de outra classe, a classe herdada é conhecida como por:
    (Pessoa)
    - Super Classe:
    - Classe Mãe:
    - Classe Pai:
    - Classe Base:
    - Classe Genérica:

Quando uma classe herda de outra classe, ela é chamada:
    (Cliente, Funcionário)
    - Sub Classe:
    - Classe - Filha:
    - Classe Especifica:

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa 

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Herbety', 'Paulo', '123.456.789-00', 5000)
funcionario1 = Funcionario('Paulo', 'Mendes', '789.456.123-11', 3000)


print(cliente1.nome_completo())
print(funcionario1.nome_completo())


Sobrescrita de Método (Override), ocorre quando reescrevemos/reeplementamos um método 
presente na super classe em classes filhas 

"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        # Override, sobescrevendo o metodo nome_completo da classe Pessoa
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Herbety', 'Paulo', '123.456.789-00', 5000)
funcionario1 = Funcionario('Paulo', 'Mendes', '789.456.123-11', 3000)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
