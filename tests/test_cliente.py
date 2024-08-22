import unittest
from cliente import PessoaFisica

class TestPessoaFisica(unittest.TestCase):
    def setUp(self):
        self.cliente = PessoaFisica("João Dias", "01-01-1990", "12345678900", "Avenida Paulista 123")

    def test_cliente_creation(self):
        self.assertEqual(self.cliente.nome, "João Dias")
        self.assertEqual(self.cliente.data_nascimento, "01-01-1990")
        self.assertEqual(self.cliente.cpf, "12345678900")
        self.assertEqual(self.cliente.endereco, "Avenida Paulista 123")
        self.assertEqual(self.cliente.contas, [])

if __name__ == '__main__':
    unittest.main()
