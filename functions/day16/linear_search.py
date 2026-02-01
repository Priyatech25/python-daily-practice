arr = list(map(int, input().split()))
key = int(input())

for i in range(len(arr)):
    if arr[i] == key:
        print(i)
        break
else:
    print(-1)
