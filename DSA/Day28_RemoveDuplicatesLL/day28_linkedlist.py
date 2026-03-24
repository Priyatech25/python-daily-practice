# DAY 28 - DSA Practice (Remove Duplicates from Sorted Linked List)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_duplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next  # skip duplicate
        else:
            current = current.next

    return head


# Helper to print list
def print_list(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")


# Creating linked list: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

print("Original List:")
print_list(head)

head = remove_duplicates(head)

print("After Removing Duplicates:")
print_list(head)