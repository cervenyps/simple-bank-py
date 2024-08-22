from cliente import PessoaFisica
from conta_corrente import ContaCorrente
from transacao import Deposito, Saque


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def criar_cliente(self):
        cpf = input("CPF: ")
        if self.buscar_cliente(cpf):
            print("CPF já cadastrado.")
            return

        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço: ")

        cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
        self.clientes.append(cliente)
        print("Cliente criado com sucesso.")

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
    
    def selecionar_conta(self, cliente):
        if not cliente.contas:
            print("Cliente não possui contas.")
            return None

        print("Selecione uma conta:")
        for idx, conta in enumerate(cliente.contas, start=1):
            print(f"{idx}: Conta {conta.numero} - Agência {conta.agencia}")

        escolha = int(input("Escolha o número da conta: ")) - 1

        if 0 <= escolha < len(cliente.contas):
            return cliente.contas[escolha]
        else:
            print("Escolha inválida.")
            return None
        
    def criar_conta(self):
        cpf = input("CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if not cliente:
            print("Cliente não encontrado.")
            return

        numero_conta = len(self.contas) + 1
        conta = ContaCorrente.criar_conta(cliente, numero_conta)
        self.contas.append(conta)
        cliente.adicionar_conta(conta)
        print("Conta criada com sucesso.")

    def depositar(self):
        cpf = input("CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if not cliente:
            print("Cliente não encontrado.")
            return

        conta = self.selecionar_conta(cliente)
        if not conta:
            return

        valor = float(input("Valor do depósito: "))
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)

    def sacar(self):
        cpf = input("CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if not cliente:
            print("Cliente não encontrado.")
            return

        conta = self.selecionar_conta(cliente)
        if not conta:
            return

        valor = float(input("Valor do saque: "))
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)

    def extrato(self):
        cpf = input("CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if not cliente:
            print("Cliente não encontrado.")
            return

        conta = self.selecionar_conta(cliente)
        if not conta:
            return

        print("\nExtrato da conta:")
        print(conta.mostrar_historico())
        print(f"Saldo atual: R$ {conta.saldo:.2f}")

    def menu(self):
        opcoes = {
            "1": self.criar_cliente,
            "2": self.criar_conta,
            "3": self.depositar,
            "4": self.sacar,
            "5": self.extrato,
            "6": exit
        }

        while True:
            print("\nMenu de Opções:")
            print("1: Criar Cliente")
            print("2: Criar Conta")
            print("3: Depositar")
            print("4: Sacar")
            print("5: Extrato")
            print("6: Sair")
            escolha = input("Escolha uma opção: ")

            acao = opcoes.get(escolha)
            if acao:
                acao()
            else:
                print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    banco = Banco()
    banco.menu()
