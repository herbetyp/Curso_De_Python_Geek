"""
POO - Abstração e Encapsulamento

O grande objetivo é encapsular nosso código, dentro de um grupo lógico e hierárquico
utilizando classes

Encapsular -> cápsula

  classe
---------------------------
|                          |
|     tributos e métodos   |
|                          |
----------------------------

# Relembrando atributos/métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado
chamado __falar()

Eses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenômeno chamado 
Name Mangling, que faz uma alteração na forma de se acessar os 
elementos privados, conforme:

_Classe__elemento

Exemplo - Acessandp elementos privados fora da classe:

instancia._Pessoa__nome  

instancia._Pessoa__falar()

# OBS: Isso não é recomendado

Abstração em POO -> É o ato de expor apenas dados relevantes de uma classe,
escondendo atributos e métodos privados ao usuário 
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        # atributos encapsulados
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(
            f'Saldo de {self.__saldo} do titular {self.__titular} com limite de'
            f' {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo Insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de tranferencia, paga pelo transferinte

        # Adicionar valor na conta destino
        conta_destino.__saldo += valor


# Testando


conta1 = Conta('Herbety', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Paulo', 300, 2000)
conta2.extrato()

"""
print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular)  # Name Mangling (Não recomendado)

conta1._Conta__titular = 'Paulo'

print(conta1.__dict__)

print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(2000)

print(conta1.__dict__)
"""

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()
