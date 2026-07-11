"""
Day 32 - Best Time to Buy and Sell Stock

Problem:
You are given an array where each element represents the stock price
on a particular day.

Find the maximum profit you can achieve by buying one stock
and selling it later.

Example:
Input:
prices = [7,1,5,3,6,4]

Output:
5

Explanation:
Buy at 1
Sell at 6
Profit = 5
"""


def max_profit(prices):

    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:

        # Update minimum buying price
        if price < min_price:
            min_price = price

        # Calculate current profit
        profit = price - min_price

        # Update maximum profit
        if profit > max_profit:
            max_profit = profit

    return max_profit


# ------------------------

prices = [7, 1, 5, 3, 6, 4]

print("Prices:", prices)
print("Maximum Profit:", max_profit(prices))

print()

prices = [7, 6, 4, 3, 1]

print("Prices:", prices)
print("Maximum Profit:", max_profit(prices))

print()

prices = [2, 4, 1]

print("Prices:", prices)
print("Maximum Profit:", max_profit(prices))