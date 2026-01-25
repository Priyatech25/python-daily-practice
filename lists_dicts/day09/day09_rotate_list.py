nums = list(map(int, input().split()))
k = int(input())

k = k % len(nums)
rotated = nums[k:] + nums[:k]

print(rotated)
