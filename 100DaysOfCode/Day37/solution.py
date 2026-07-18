"""
Day 37 - Group Anagrams

Problem:
Given an array of strings, group the anagrams together.

Example:

Input:
["eat","tea","tan","ate","nat","bat"]

Output:
[
 ['eat','tea','ate'],
 ['tan','nat'],
 ['bat']
]
"""


def group_anagrams(words):

    anagram_groups = {}

    for word in words:

        # Use sorted word as key
        key = "".join(sorted(word))

        if key not in anagram_groups:
            anagram_groups[key] = []

        anagram_groups[key].append(word)

    return list(anagram_groups.values())



# soln
# -------------------------

words1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

print("Input:")
print(words1)

print("\nGrouped Anagrams:")
print(group_anagrams(words1))

print()

words2 = ["listen", "silent", "enlist", "hello", "below", "elbow"]

print("Input:")
print(words2)

print("\nGrouped Anagrams:")
print(group_anagrams(words2))

print()

words3 = ["abc", "cab", "bac", "xyz", "zyx"]

print("Input:")
print(words3)

print("\nGrouped Anagrams:")
print(group_anagrams(words3))