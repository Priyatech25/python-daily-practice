def read_txt_file(filename):
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, marks = line.strip().split(",")
                students.append((name, int(marks)))
    except FileNotFoundError:
        print("Text file not found")
    return students


def read_csv_file(filename):
    students = []
    try:
        with open(filename, "r") as file:
            next(file)  # skip header
            for line in file:
                name, marks = line.strip().split(",")
                students.append((name, int(marks)))
    except FileNotFoundError:
        print("CSV file not found")
    return students


def display_students(students):
    for name, marks in students:
        print(f"{name} scored {marks}")

def calculate_average(students):
    if not students:
        return 0
    total = sum(marks for _, marks in students)
    return total / len(students)



if __name__ == "__main__":
    txt_students = read_txt_file("sample_data.txt")
    csv_students = read_csv_file("sample_data.csv")

    print("From TXT file:")
    display_students(txt_students)

    print("\nFrom CSV file:")
    display_students(csv_students)

print("\nAverage marks (TXT):", calculate_average(txt_students))
print("Average marks (CSV):", calculate_average(csv_students))

