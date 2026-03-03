# DAY 8 - DSA Practice (Queue)

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue (Insert at end)
    def enqueue(self, data):
        self.queue.append(data)

    # Dequeue (Remove from front)
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue.pop(0)

    # Get front element
    def front(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue[0]

    # Check if empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display queue
    def display(self):
        print(self.queue)


# Testing
q = Queue()

q.enqueue(100)
q.enqueue(200)
q.enqueue(300)

print("Queue Elements:")
q.display()

print("Dequeue:", q.dequeue())
print("Front:", q.front())
print("Is Empty:", q.is_empty())