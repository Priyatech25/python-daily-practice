# DAY 9 - DSA Practice (Hashing)

# Count Frequency
def count_frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq


# Check Anagram
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq = {}
    
    for char in s1:
        freq[char] = freq.get(char, 0) + 1
    
    for char in s2:
        if char not in freq:
            return False
        freq[char] -= 1
        if freq[char] < 0:
            return False
            
    return True


# Find Duplicates
def find_duplicates(arr):
    freq = {}
    duplicates = []
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
    for key, value in freq.items():
        if value > 1:
            duplicates.append(key)
            
    return duplicates


# Two Sum Problem
def two_sum(arr, target):
    hashmap = {}
    
    for i in range(len(arr)):
        complement = target - arr[i]
        
        if complement in hashmap:
            return [hashmap[complement], i]
        
        hashmap[arr[i]] = i
        
    return []


# Testing
arr = [1, 2, 3, 2, 4, 1, 5]
print("Frequency:", count_frequency(arr))
print("Anagram (listen, silent):", is_anagram("listen", "silent"))
print("Duplicates:", find_duplicates(arr))
print("Two Sum (target=6):", two_sum([2, 7, 11, 15], 9))