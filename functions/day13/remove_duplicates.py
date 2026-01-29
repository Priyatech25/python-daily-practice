# remove_duplicates.py
with open("data.txt") as f:
    unique = list(dict.fromkeys(f.readlines()))
with open("data.txt", "w") as f:
    f.writelines(unique)
