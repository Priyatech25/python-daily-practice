#Day 9: frequency of elements

nums = list(map(int, input().split()))
freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)
