"""
Day 39 - Reverse Linked List

Problem:
Given the head of a singly linked list,
reverse the linked list and return the new head.

Example:

Input:
1 -> 2 -> 3 -> 4 -> 5

Output:
5 -> 4 -> 3 -> 2 -> 1
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

    # Reverse linked list
    def reverse(self):

        previous = None
        current = self.head

        while current:

            next_node = current.next

            current.next = previous

            previous = current

            current = next_node

        self.head = previous


soln
# -------------------------

linked_list = LinkedList()

values = [1, 2, 3, 4, 5]

for value in values:
    linked_list.append(value)

print("Original Linked List:")
linked_list.display()

linked_list.reverse()

print("\nReversed Linked List:")
linked_list.display()