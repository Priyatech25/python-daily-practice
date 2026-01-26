n = int(input())
temp = n
digits = len(str(n))
s = 0

while temp > 0:
    d = temp % 10
    s += d ** digits
    temp //= 10

print("Armstrong" if s == n else "Not Armstrong")
