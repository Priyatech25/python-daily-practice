def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error"

a, b = map(int, input().split())
print(add(a,b), sub(a,b), mul(a,b), div(a,b))
