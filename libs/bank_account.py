class BankAccount:
    def __init__(self, username, balance=0):
        self.username = username
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal failed.")

    def check_balance(self):
        print(f"Account balance for {self.username}: ${self.balance}")
