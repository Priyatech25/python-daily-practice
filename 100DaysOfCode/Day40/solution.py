"""
Day 40 - Middle of the Linked List

Problem:
Given the head of a singly linked list,
return the middle node.

If there are two middle nodes,
return the second middle node.

Example:

Input:
1 -> 2 -> 3 -> 4 -> 5

Output:
3

Input:
1 -> 2 -> 3 -> 4 -> 5 -> 6

Output:
4
"""


# -------------------------
# Node Class
# -------------------------

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# -------------------------
# Linked List Class
# -------------------------

class LinkedList:

    def __init__(self):
        self.head = None

    # Insert node at end
    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # Display linked list
    def display(self):

        current = self.head

        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next

        print()

    # Find middle node
    def find_middle(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# -------------------------
# Test Case 1
# -------------------------

ll1 = LinkedList()

for value in [1, 2, 3, 4, 5]:
    ll1.append(value)

print("Linked List:")
ll1.display()

middle = ll1.find_middle()
print("Middle Node:", middle.data)

print()

# -------------------------
# Test Case 2
# -------------------------

ll2 = LinkedList()

for value in [1, 2, 3, 4, 5, 6]:
    ll2.append(value)

print("Linked List:")
ll2.display()

middle = ll2.find_middle()
print("Middle Node:", middle.data)