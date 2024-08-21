from account import Account

class ATM:
    def __init__(self):
        self.account = Account()

    def run(self):
        menu = """
        [d] Deposit
        [w] Withdraw
        [b] Balance
        [q] Quit

        => """

        while True:
            option = input(menu).lower()

            match option:
                case "d":
                    amount = float(input("Enter the deposit amount: "))
                    print(self.account.deposit(amount))

                case "w":
                    amount = float(input("Enter the withdrawal amount: "))
                    print(self.account.withdraw(amount))

                case "b":
                    print("\n============= BALANCE =============")
                    print(self.account.get_transaction_history())
                    print(f"\n{self.account.get_balance()}")
                    print("===================================\n")

                case "q":
                    print("Exiting the system. Goodbye!")
                    break

                case _:
                    print("Invalid option, please select a valid operation.\n")
