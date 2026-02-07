from pathlib import Path
from ingestion import read_csv_data, check_required_columns
from cleaning import clean_student_data
from aggregation import subject_wise_average, class_summary

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

    print("\n--- Subject-wise Average Marks ---")
    print(subject_wise_average(df))

    print("\n--- Class Summary ---")
    summary = class_summary(df)
    for key, value in summary.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    run()
