"""
Day 36 - Valid Anagram

Problem:
Given two strings s and t,
return True if t is an anagram of s,
otherwise return False.

An Anagram is a word formed by rearranging
the letters of another word.

Example:

Input:
s = "anagram"
t = "nagaram"

Output:
True
"""


def is_anagram(s, t):

    if len(s) != len(t):
        return False

    char_count = {}

    # Count characters in first string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrease count using second string
    for char in t:

        if char not in char_count:
            return False

        char_count[char] -= 1

        if char_count[char] < 0:
            return False

    return True


# -------------------------
# Test Cases
# -------------------------

s1 = "anagram"
t1 = "nagaram"

print("String 1:", s1)
print("String 2:", t1)
print("Output  :", is_anagram(s1, t1))

print()

s2 = "rat"
t2 = "car"

print("String 1:", s2)
print("String 2:", t2)
print("Output  :", is_anagram(s2, t2))

print()

s3 = "listen"
t3 = "silent"

print("String 1:", s3)
print("String 2:", t3)
print("Output  :", is_anagram(s3, t3))

print()

s4 = "hello"
t4 = "world"

print("String 1:", s4)
print("String 2:", t4)
print("Output  :", is_anagram(s4, t4))