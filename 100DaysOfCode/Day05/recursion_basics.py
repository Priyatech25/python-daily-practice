# Day 5 - Recursion Basics

# Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


num = 5

print("Factorial of", num, "is:", factorial(num))

print("Fibonacci Series:")
for i in range(num):
    print(fibonacci(i), end=" ")