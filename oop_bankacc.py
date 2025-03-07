from libs.bank_account import BankAccount

print("*" * 50)

john_acc = BankAccount("John Doe")
print(john_acc.username)
john_acc.deposit(1000)
john_acc.withdraw(500)
john_acc.check_balance()

print("*" * 50)

jane_acc = BankAccount("Jane Doe")
print(jane_acc.username)
jane_acc.deposit(10000)
jane_acc.withdraw(15000)
jane_acc.check_balance()
