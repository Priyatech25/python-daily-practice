"""
Day 38 - Longest Common Prefix

Problem:
Write a function to find the longest common prefix string
among an array of strings.

If there is no common prefix, return an empty string.

Example:

Input:
["flower", "flow", "flight"]

Output:
"fl"
"""


def longest_common_prefix(strs):

    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:

        while not word.startswith(prefix):

            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


soln 
# -------------------------

words1 = ["flower", "flow", "flight"]
print("Input :", words1)
print("Output:", longest_common_prefix(words1))

print()

words2 = ["dog", "racecar", "car"]
print("Input :", words2)
print("Output:", longest_common_prefix(words2))

print()

words3 = ["interview", "internet", "internal", "interval"]
print("Input :", words3)
print("Output:", longest_common_prefix(words3))

print()

words4 = ["apple", "application", "appetite"]
print("Input :", words4)
print("Output:", longest_common_prefix(words4))