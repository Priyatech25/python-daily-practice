# DAY 11 - DSA Practice (Greedy Algorithms)

#  Coin Change (Minimum Coins)
def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
            
    return count


# Activity Selection
def activity_selection(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])
    
    count = 1
    last_end = activities[0][1]
    
    for i in range(1, len(activities)):
        if activities[i][0] >= last_end:
            count += 1
            last_end = activities[i][1]
            
    return count


# Minimum Platforms (Train Problem)
def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()
    
    i = j = 0
    platforms = 0
    max_platforms = 0
    
    while i < len(arrival) and j < len(departure):
        if arrival[i] <= departure[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
            
    return max_platforms


# Testing
coins = [1, 2, 5, 10]
print("Minimum Coins:", coin_change(coins, 18))

start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
print("Max Activities:", activity_selection(start, end))

arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
print("Minimum Platforms Needed:", min_platforms(arrival, departure))