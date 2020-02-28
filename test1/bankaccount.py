class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient Funds')

    def print_balance(self):
        return self.balance

account = BankAccount()
account.deposit(1000)
account.deposit(1000)
account.deposit(5000)
# print(account.print_balance())

account.withdraw(6000)
print(account.print_balance())