nums = list(map(int, input().split()))
result = tuple((n, nums.count(n)) for n in set(nums))
print(result)
