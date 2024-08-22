from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0

    @classmethod
    def criar_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        if self._saques_realizados >= self._limite_saques:
            print("Limite de saques excedido.")
            return False
        if valor > self._limite:
            print(f"O valor do saque excede o limite de R$ {self._limite}.")
            return False
        if super().sacar(valor):
            self._saques_realizados += 1
            return True
        return False

    def __str__(self):
        return f"Agência: {self.agencia}\nConta: {self.numero}\nTitular: {self.cliente.nome}"

