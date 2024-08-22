import unittest
from cliente import PessoaFisica
from conta import Conta

class TestConta(unittest.TestCase):
    def setUp(self):
        self.cliente = PessoaFisica("João Dias", "01-01-1990", "12345678900", "Avenida Paulista 123")
        self.conta = Conta(1, self.cliente)

    def test_depositar(self):
        self.conta.depositar(500)
        self.assertEqual(self.conta.saldo, 500)

    def test_sacar_com_sucesso(self):
        self.conta.depositar(500)
        result = self.conta.sacar(300)
        self.assertTrue(result)
        self.assertEqual(self.conta.saldo, 200)

    def test_sacar_com_saldo_insuficiente(self):
        result = self.conta.sacar(300)
        self.assertFalse(result)
        self.assertEqual(self.conta.saldo, 0)

if __name__ == '__main__':
    unittest.main()
