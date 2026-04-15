# DAY 40 - Longest Common Subsequence (LCS)

def lcs(text1, text2):
    m = len(text1)
    n = len(text2)

    # DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Testing
text1 = "abcde"
text2 = "ace"

print("LCS Length:", lcs(text1, text2))