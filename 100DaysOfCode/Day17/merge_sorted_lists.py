# Day 18 - Merge Two Sorted Lists

def merge_sorted_lists(list1, list2):

    merged = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

result = merge_sorted_lists(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Merged List:", result)