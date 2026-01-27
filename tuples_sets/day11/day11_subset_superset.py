a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(a.issubset(b))
print(a.issuperset(b))
