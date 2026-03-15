# DAY 18 - DSA Practice (0/1 Knapsack)

def knapsack(weights, values, capacity):
    n = len(values)

    # DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


# Testing
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

print("Maximum Value:", knapsack(weights, values, capacity))