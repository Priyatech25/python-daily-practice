def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

nums = list(map(int, input().split()))
print(even_numbers(nums))
print(odd_numbers(nums))
