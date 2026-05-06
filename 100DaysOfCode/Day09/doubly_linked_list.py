# Day 9 - Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Delete a node
    def delete(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                # If node to delete is head
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                return
            temp = temp.next

        print("Value not found")

    # Display forward
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Display backward
    def display_backward(self):
        temp = self.head
        if temp is None:
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# Driver code
dll = DoublyLinkedList()

dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)

print("Forward Traversal:")
dll.display_forward()

print("Backward Traversal:")
dll.display_backward()

dll.delete(20)

print("After deleting 20:")
dll.display_forward()