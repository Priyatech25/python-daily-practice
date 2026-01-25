#day09_remove_duplicates from list

nums = list(map(int, input().split()))
unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print(unique)
