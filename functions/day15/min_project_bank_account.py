class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt

    def show(self):
        print("Balance:", self.balance)

acc = BankAccount(500)
acc.deposit(300)
acc.withdraw(200)
acc.show()
