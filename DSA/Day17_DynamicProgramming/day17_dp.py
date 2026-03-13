# DAY 17 - DSA Practice (Dynamic Programming)

# Fibonacci using Memoization (Top Down)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


# Fibonacci using Tabulation (Bottom Up)
def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# Testing
n = 10

print("Fibonacci using Memoization:", fib_memo(n))
print("Fibonacci using Tabulation:", fib_tab(n))