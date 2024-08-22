import unittest
from cliente import PessoaFisica
from conta_corrente import ContaCorrente

class TestContaCorrente(unittest.TestCase):
    def setUp(self):
        self.cliente = PessoaFisica("João Dias", "01-01-1990", "12345678900", "Avenida Paulista 123")
        self.conta = ContaCorrente(1, self.cliente, limite=1000, limite_saques=2)

    def test_criar_conta(self):
        self.assertIsInstance(self.conta, ContaCorrente)
        self.assertEqual(self.conta.numero, 1)
        self.assertEqual(self.conta.cliente.nome, "João Dias")

    def test_sacar_com_sucesso(self):
        self.conta.depositar(500)
        result = self.conta.sacar(300)
        self.assertTrue(result)
        self.assertEqual(self.conta.saldo, 200)

    def test_sacar_acima_limite(self):
        result = self.conta.sacar(1500)
        self.assertFalse(result)
        self.assertEqual(self.conta.saldo, 0)

    def test_limite_saques(self):
        self.conta.depositar(1000)
        self.conta.sacar(100)
        self.conta.sacar(100)
        result = self.conta.sacar(100)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
