# average_marks.py
total = count = 0
with open("students.txt") as f:
    for line in f:
        _, m = line.strip().split(",")
        total += int(m); count += 1
print(total / count if count else 0)
