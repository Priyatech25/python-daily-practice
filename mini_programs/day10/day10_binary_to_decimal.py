b = input().strip()
decimal = 0

for digit in b:
    decimal = decimal * 2 + int(digit)

print(decimal)
