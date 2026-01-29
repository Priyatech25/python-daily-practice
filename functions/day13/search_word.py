# search_word.py
word = input().strip()
with open("data.txt") as f:
    found = any(word in line for line in f)
print(found)
