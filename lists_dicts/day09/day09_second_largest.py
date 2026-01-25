#Day 9: finding second largest element

nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()
print(nums[-2])
