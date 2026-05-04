# Day 7 - Queue Basics

from collections import deque

# Queue Implementation
queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", list(queue))

# Dequeue
removed = queue.popleft()
print("Dequeued element:", removed)
print("Queue after dequeue:", list(queue))

# Front element
print("Front element:", queue[0])

# Check empty
print("Is queue empty?", len(queue) == 0)


# Simple Task Queue Example
tasks = deque(["Study Python", "Practice DSA", "Push to GitHub"])

print("\nTasks in Queue:", list(tasks))

while tasks:
    current_task = tasks.popleft()
    print("Completed:", current_task)