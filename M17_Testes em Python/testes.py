import unittest

from atividade import comer, dormir, eh_engracada


class AtividadeTest(unittest.TestCase):
    """Testando o retorno com comida saudável"""

    def test_comer_saudavel(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo, estou de dieta.'
        )

    """Testando o retorno com comida não saudável"""

    def test_comer_nao_saudavel(self):
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza, comida preferida.'
        )

    """Testando o retorno dormindo pouco"""

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Estou dormindo pouco, vou para o trabalho cansado.'
        )

    """Testando o retorno domindo muito"""

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Estou dormindo muito, estou atrasado para o trabalho.'
        )

    def test_eh_engracada(self):
        # self.assertEqual(
        #     eh_engracada('Sergio Malandro'),
        #     False
        # )
        self.assertFalse(eh_engracada('Sergio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'),
                        'Jim Carrey deveria ser engraçado')


if __name__ == "__main__":
    unittest.main()
