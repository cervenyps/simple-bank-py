
import unittest
from cliente import PessoaFisica
from conta_corrente import ContaCorrente
from banco import Banco

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()

    def test_criar_cliente(self):
        self.banco.criar_cliente = lambda: self.banco.clientes.append(PessoaFisica("João Dias", "01-01-1990", "12345678900", "Avenida Paulista 123"))
        self.banco.criar_cliente()
        self.assertEqual(len(self.banco.clientes), 1)
        self.assertEqual(self.banco.clientes[0].cpf, "12345678900")

    def test_buscar_cliente(self):
        self.banco.criar_cliente = lambda: self.banco.clientes.append(PessoaFisica("João Dias", "01-01-1990", "12345678900", "Avenida Paulista 123"))
        self.banco.criar_cliente()
        cliente = self.banco.buscar_cliente("12345678900")
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.nome, "João Dias")

    def test_criar_conta(self):
        cliente = PessoaFisica("João Dias", "01-01-1990", "12345678900", "Avenida Paulista 123")
        self.banco.clientes.append(cliente)
        self.banco.criar_conta = lambda: self.banco.contas.append(ContaCorrente.criar_conta(cliente, 1))
        self.banco.criar_conta()
        self.assertEqual(len(self.banco.contas), 1)
        self.assertEqual(self.banco.contas[0].numero, 1)
        self.assertEqual(self.banco.contas[0].cliente.nome, "João Dias")

    def test_depositar(self):
        cliente = PessoaFisica("João Dias", "01-01-1990", "12345678900", "Avenida Paulista 123")
        self.banco.clientes.append(cliente)
        conta = ContaCorrente.criar_conta(cliente, 1)
        self.banco.contas.append(conta)
        self.banco.selecionar_conta = lambda cliente: conta
        self.banco.depositar = lambda: conta.depositar(500)
        self.banco.depositar()
        self.assertEqual(conta.saldo, 500)

    def test_sacar(self):
        cliente = PessoaFisica("João Dias", "01-01-1990", "12345678900", "Avenida Paulista 123")
        self.banco.clientes.append(cliente)
        conta = ContaCorrente.criar_conta(cliente, 1)
        self.banco.contas.append(conta)
        conta.depositar(500)
        self.banco.selecionar_conta = lambda cliente: conta
        self.banco.sacar = lambda: conta.sacar(300)
        self.banco.sacar()
        self.assertEqual(conta.saldo, 200)

if __name__ == '__main__':
    unittest.main()
