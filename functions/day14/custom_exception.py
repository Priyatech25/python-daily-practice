class BalanceError(Exception):
    pass

balance = 500
withdraw = int(input())

if withdraw > balance:
    raise BalanceError("Insufficient balance")
print("Withdraw successful")
