def is_palindrome(s):
    return s == s[::-1]

s = input().lower()
print(is_palindrome(s))
