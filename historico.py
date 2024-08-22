from datetime import datetime

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transacoes.append({"tipo": transacao.__class__.__name__, "valor": transacao.valor, "data": timestamp})

    def listar_transacoes(self):
        if not self.transacoes:
            return "Nenhuma transação realizada."
        return "\n".join([f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}" for transacao in self.transacoes])
