import unittest
from account import Account  # Import the class you're testing

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0)

    def test_deposit_valid_amount(self):
        result = self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)
        self.assertIn("Deposit: $100.00", self.account.transaction_history)
        self.assertEqual(result, "Successfully deposited $100.00.")

    def test_deposit_invalid_amount(self):
        result = self.account.deposit(-50)
        self.assertEqual(self.account.balance, 0)
        self.assertEqual(result, "Failed! Invalid deposit amount.")

    def test_withdraw_valid_amount(self):
        self.account.deposit(200)
        result = self.account.withdraw(150)
        self.assertEqual(self.account.balance, 50)
        self.assertIn("Withdrawal: $150.00", self.account.transaction_history)
        self.assertEqual(result, "Successfully withdrew $150.00.")

    def test_withdraw_exceeds_balance(self):
        result = self.account.withdraw(100)
        self.assertEqual(self.account.balance, 0)
        self.assertEqual(result, "Failed! Insufficient funds.")

    def test_withdraw_exceeds_limit(self):
        self.account.deposit(600)
        result = self.account.withdraw(600)
        self.assertEqual(result, f"Failed! Withdrawal exceeds the limit of ${self.account.withdrawal_limit:.2f}.")

    def test_withdraw_exceeds_max_withdrawals(self):
        self.account.deposit(1000)
        self.account.withdraw(100)
        self.account.withdraw(100)
        self.account.withdraw(100)
        result = self.account.withdraw(100)
        self.assertEqual(result, f"Failed! Maximum number of {self.account.max_withdrawals} withdrawals exceeded.")

    def test_transaction_history_no_transactions(self):
        history = self.account.get_transaction_history()
        self.assertEqual(history, "No transactions made.")

    def test_transaction_history_with_transactions(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        history = self.account.get_transaction_history()
        self.assertIn("Deposit: $200.00", history)
        self.assertIn("Withdrawal: $100.00", history)


if __name__ == "__main__":
    unittest.main()
