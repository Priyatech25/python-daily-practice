import pandas as pd

def search_student(input_file):
    try:
        df = pd.read_csv(input_file)

        name = input("Enter student name to search: ")

        student_df = df[df["student_name"].str.lower() == name.lower()]

        if student_df.empty:
            print("Student not found.")
            return

        print("\nSubject-wise Marks:")
        print(student_df[["subject", "marks"]])

        avg = student_df["marks"].mean()
        print(f"\nAverage Marks: {avg:.2f}")

    except FileNotFoundError:
        print("CSV file not found.")
