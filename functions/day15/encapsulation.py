class Bank:
    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance

b = Bank()
print(b.get_balance())