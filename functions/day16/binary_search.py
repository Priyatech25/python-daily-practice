arr = sorted(list(map(int, input().split())))
key = int(input())

l, r = 0, len(arr)-1
while l <= r:
    mid = (l + r) // 2
    if arr[mid] == key:
        print(mid)
        break
    elif arr[mid] < key:
        l = mid + 1
    else:
        r = mid - 1
else:
    print(-1)
