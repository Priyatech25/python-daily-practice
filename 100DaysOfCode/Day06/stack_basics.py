# Day 6 - Stack Basics

# Stack Implementation using List
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Pop element
removed = stack.pop()
print("Popped element:", removed)
print("Stack after pop:", stack)

# Peek top element
print("Top element:", stack[-1])

# Check empty
print("Is stack empty?", len(stack) == 0)


# Reverse a String using Stack
def reverse_string(text):
    s = []

    for char in text:
        s.append(char)

    reversed_text = ""

    while s:
        reversed_text += s.pop()

    return reversed_text


word = "Python"
print("Original String:", word)
print("Reversed String:", reverse_string(word))