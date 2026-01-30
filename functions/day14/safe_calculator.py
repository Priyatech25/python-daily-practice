def calc(a, b, op):
    try:
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b
        raise ValueError("Invalid operator")
    except ZeroDivisionError:
        return "Divide by zero error"

a = int(input())
b = int(input())
op = input()
print(calc(a, b, op))
