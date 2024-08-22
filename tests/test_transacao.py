import unittest
from cliente import PessoaFisica
from conta_corrente import ContaCorrente
from transacao import Deposito, Saque

class TestTransacao(unittest.TestCase):
    def setUp(self):
        self.cliente = PessoaFisica("João Dias", "01-01-1990", "12345678900", "Avenida Paulista 123")
        self.conta = ContaCorrente(1, self.cliente)

    def test_deposito(self):
        deposito = Deposito(300)
        result = deposito.executar(self.conta)
        self.assertTrue(result)
        self.assertEqual(self.conta.saldo, 300)

    def test_saque(self):
        self.conta.depositar(500)
        saque = Saque(200)
        result = saque.executar(self.conta)
        self.assertTrue(result)
        self.assertEqual(self.conta.saldo, 300)

if __name__ == '__main__':
    unittest.main()
