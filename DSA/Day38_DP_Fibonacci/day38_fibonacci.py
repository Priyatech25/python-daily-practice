# DAY 38 - Dynamic Programming (Fibonacci)

def fibonacci(n, dp):
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibonacci(n-1, dp) + fibonacci(n-2, dp)
    return dp[n]


n = 10
dp = [-1] * (n + 1)

print("Fibonacci:", fibonacci (n, dp))