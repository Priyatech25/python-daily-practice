t = tuple(map(int, input().split()))
x = int(input())
t = tuple(i for i in t if i != x)
print(t)
