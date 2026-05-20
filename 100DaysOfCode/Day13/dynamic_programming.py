# Day 13 - Dynamic Programming

# Fibonacci using Dynamic Programming (Memoization)

memo = {}

def fibonacci(n):

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]


num = 10

print("Fibonacci Series:")

for i in range(num):
    print(fibonacci(i), end=" ")