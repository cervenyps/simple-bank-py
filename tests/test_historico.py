import unittest
from historico import Historico
from transacao import Deposito

class TestHistorico(unittest.TestCase):
    def setUp(self):
        self.historico = Historico()
        self.deposito = Deposito(100)

    def test_adicionar_transacao(self):
        self.historico.adicionar_transacao(self.deposito)
        self.assertEqual(len(self.historico.transacoes), 1)
        self.assertEqual(self.historico.transacoes[0]["valor"], 100)

    def test_listar_transacoes(self):
        self.historico.adicionar_transacao(self.deposito)
        transacoes = self.historico.listar_transacoes()
        self.assertIn("Deposito", transacoes)

if __name__ == '__main__':
    unittest.main()
