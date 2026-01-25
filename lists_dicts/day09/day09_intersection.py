#Day 9: list intersection

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

intersection = list(set(list1) & set(list2))
print(intersection)
