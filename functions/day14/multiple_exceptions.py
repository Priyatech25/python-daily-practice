try:
    n = int(input())
    print(10 / n)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Zero not allowed")
