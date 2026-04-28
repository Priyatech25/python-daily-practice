# Day 1 - Array Basics

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Append
numbers.append(60)
print("After Append:", numbers)

# Insert
numbers.insert(2, 25)
print("After Insert:", numbers)

# Remove
numbers.remove(40)
print("After Remove:", numbers)

# Sort
numbers.sort()
print("Sorted List:", numbers)

# Reverse
numbers.reverse()
print("Reversed List:", numbers)

# Find max and min
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Sum
print("Sum:", sum(numbers))