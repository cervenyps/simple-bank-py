class Account:
    def __init__(self, withdrawal_limit=500, max_withdrawals=3):
        self.balance = 0
        self.withdrawal_limit = withdrawal_limit
        self.max_withdrawals = max_withdrawals
        self.withdrawal_count = 0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount:.2f}")
            return f"Successfully deposited ${amount:.2f}."
        else:
            return "Failed! Invalid deposit amount."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Failed! Insufficient funds."
        elif amount > self.withdrawal_limit:
            return f"Failed! Withdrawal exceeds the limit of ${self.withdrawal_limit:.2f}."
        elif self.withdrawal_count >= self.max_withdrawals:
            return f"Failed! Maximum number of {self.max_withdrawals} withdrawals exceeded."
        elif amount > 0:
            self.balance -= amount
            self.withdrawal_count += 1
            self.transaction_history.append(f"Withdrawal: ${amount:.2f}")
            return f"Successfully withdrew ${amount:.2f}."
        else:
            return "Failed! Invalid withdrawal amount."

    def get_balance(self):
        return f"Current Balance: ${self.balance:.2f}"

    def get_transaction_history(self):
        if not self.transaction_history:
            return "No transactions made."
        return "\n".join(self.transaction_history)
