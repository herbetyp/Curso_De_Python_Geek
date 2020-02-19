"""
Unittest - Antes e após hooks

hooks -> São os testes em si. Ou seja, a execução dos testes

setUp() -> é executado antes de cada método de teste. É util para criar instâncias
de objetos e outros dados

tearDown() -> é executado ao final de cada método de teste. É util para excluir
dados ou fechar conexões com bancs de dados.

"""
import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configuração do setUp
        return super().setUp()

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown vai rodar apos o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown vai rodar apos o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        return super().tearDown()
