# Day 5: Functions – sum and product

def calculate_sum_product(a, b):
    return a + b, a * b

x, y = map(int, input("Enter two numbers: ").split())

s, p = calculate_sum_product(x, y)

print("Sum:", s)
print("Product:", p)
