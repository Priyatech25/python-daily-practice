"""
Day 41 - Linked List Cycle

Problem:
Given the head of a linked list,
determine whether the linked list contains a cycle.

A cycle exists if a node can be reached again
by continuously following the next pointer.

Example:

1 → 2 → 3 → 4
      ↑     ↓
      ← ← ←
Output:
True
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

    # Create a cycle
    def create_cycle(self, position):

        if position < 0:
            return

        cycle_node = None
        current = self.head
        index = 0

        while current.next:

            if index == position:
                cycle_node = current

            current = current.next
            index += 1

        current.next = cycle_node

    # Detect cycle using Floyd's Algorithm
    def has_cycle(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Test Case 1
# -------------------------

ll1 = LinkedList()

for value in [1, 2, 3, 4]:
    ll1.append(value)

ll1.create_cycle(1)

print("Linked List 1 has cycle:", ll1.has_cycle())


# Test Case 2
# -------------------------

ll2 = LinkedList()

for value in [10, 20, 30, 40]:
    ll2.append(value)

print("Linked List 2 has cycle:", ll2.has_cycle())