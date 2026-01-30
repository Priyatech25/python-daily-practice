age = int(input())
if age < 18:
    raise ValueError("Underage")
print("Allowed")
