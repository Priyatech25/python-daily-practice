# Day 17 - Palindrome Checker

def is_palindrome(text):
    
    # Convert to lowercase and remove spaces
    text = text.lower().replace(" ", "")
    
    return text == text[::-1]


word1 = "madam"
word2 = "python"
word3 = "racecar"

print(word1, "->", is_palindrome(word1))
print(word2, "->", is_palindrome(word2))
print(word3, "->", is_palindrome(word3))