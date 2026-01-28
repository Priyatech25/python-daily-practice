def square(n): return n*n
def cube(n): return n*n*n

while True:
    print("1.Square  2.Cube  3.Exit")
    ch = int(input())
    if ch == 3:
        break
    n = int(input())
    print(square(n) if ch == 1 else cube(n))
