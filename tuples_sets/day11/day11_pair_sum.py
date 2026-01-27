nums = list(map(int, input().split()))
target = int(input())
seen = set()

for n in nums:
    if target - n in seen:
        print(n, target - n)
        break
    seen.add(n)
else:
    print("No pair found")
