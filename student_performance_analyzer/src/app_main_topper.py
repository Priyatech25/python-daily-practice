from pathlib import Path
from ingestion import read_csv_data, check_required_columns
from cleaning import clean_student_data
from topper import subject_topper, generate_mini_report

DATA_FILE = Path("data/student_data.csv")

def run():
    df = read_csv_data(DATA_FILE)

    if df.empty:
        print("No data found")
        return

    try:
        check_required_columns(df)
    except ValueError as err:
        print(err)
        return

    df = clean_student_data(df)

    print("\n--- Subject-wise Topper ---")
    print(subject_topper(df))

    print("\n--- Mini Report ---")
    report = generate_mini_report(df)
    print(report)

if __name__ == "__main__":
    run()
