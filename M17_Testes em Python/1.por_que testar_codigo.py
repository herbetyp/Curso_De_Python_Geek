"""
Porque testar nosso código?

# Testes Automatizados

    Aplicação Web
-------------------------------                           |
|   frontend e backend        |
-------------------------------
|   testes automatizados      |
-------------------------------

Porque testar nosso código?
    - Reduzir bugs (problemas) no código existente
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos 
    - Testes garantem que a refatoração que costumamos fazer não traga novos bugs (problemas)

# TDD -> Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento
    - Você escreve seu teste primeiro
    - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso)
    - Então refatora o código para realizar a funcionalidade e testa novamente
    - Uma vez que o teste passe, o recurso é considerado completo

Estes estágios de desenvolvimento de TDD são quase um mantra que os desenvolvedores seguem, conhecidos como:
    - Red
    - Green
    - Refactor


"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')


felix = Gato('Felix')

felix.miar()

print(felix.nome)
