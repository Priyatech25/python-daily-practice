# student_records.py
def add_student(name, marks):
    with open("students.txt", "a") as f:
        f.write(f"{name},{marks}\n")

def view_students():
    with open("students.txt") as f:
        for line in f:
            print(line.strip())

add_student("Asha", 85)
add_student("Ravi", 90)
view_students()
