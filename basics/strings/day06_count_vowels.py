# Count vowels in a string

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
