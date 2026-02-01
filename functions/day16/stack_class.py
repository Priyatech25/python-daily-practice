class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop() if self.items else None

s = Stack()
s.push(1)
s.push(2)
print(s.pop())
