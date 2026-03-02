# DAY 7 - DSA Practice (Stack)

class Stack:
    def __init__(self):
        self.stack = []

    # Push element
    def push(self, data):
        self.stack.append(data)

    # Pop element
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack.pop()

    # Peek element
    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        print(self.stack)


# Reverse string using stack
def reverse_string(text):
    stack = Stack()

    for char in text:
        stack.push(char)

    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()

    return reversed_text


# Testing
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack Elements:")
s.display()

print("Pop:", s.pop())
print("Peek:", s.peek())
print("Is Empty:", s.is_empty())

text = "Priya"
print("Reversed String:", reverse_string(text))