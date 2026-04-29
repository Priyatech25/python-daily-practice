# Day 2 - String Basics

text = "Hello Python"

print("Original String:", text)

# Length
print("Length:", len(text))

# Uppercase
print("Uppercase:", text.upper())

# Lowercase
print("Lowercase:", text.lower())

# Replace
print("Replace:", text.replace("Python", "World"))

# Split
print("Split:", text.split())

# Reverse
print("Reversed:", text[::-1])

# Count
print("Count of 'o':", text.count("o"))

# Find
print("Index of Python:", text.find("Python"))

# Check
print("Starts with Hello:", text.startswith("Hello"))
print("Ends with Python:", text.endswith("Python"))