# DAY 5 - DSA Practice (Recursion)

# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


#  Sum of First N Numbers
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)


# Reverse String using Recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]


# Testing
num = 5
text = "hello"

print("Factorial:", factorial(num))
print("Fibonacci:", fibonacci(num))
print("Sum of first N numbers:", sum_n(num))
print("Reversed String:", reverse_string(text))