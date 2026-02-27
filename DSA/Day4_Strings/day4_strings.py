# DAY 4 - DSA Practice (Strings)

# Reverse String
def reverse_string(s):
    return s[::-1]


# Check Palindrome
def is_palindrome(s):
    return s == s[::-1]


#  Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# First Non-Repeating Character
def first_non_repeating(s):
    frequency = {}

    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    for char in s:
        if frequency[char] == 1:
            return char

    return None


# Testing
text = "programming"

print("Original:", text)
print("Reversed:", reverse_string(text))
print("Is Palindrome:", is_palindrome(text))
print("Vowel Count:", count_vowels(text))
print("First Non-Repeating Character:", first_non_repeating(text))