def fact_rec(n):
    return 1 if n == 0 else n * fact_rec(n-1)

def fact_loop(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

n = int(input())
print(fact_rec(n))
print(fact_loop(n))
