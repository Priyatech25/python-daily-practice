# DAY 30 - DSA Practice (Reverse Linked List)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # store next
        curr.next = prev        # reverse link
        prev = curr             # move prev
        curr = next_node        # move curr

    return prev


# Helper function
def print_list(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")


# Creating list: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original List:")
print_list(head)

head = reverse_list(head)

print("Reversed List:")
print_list(head)