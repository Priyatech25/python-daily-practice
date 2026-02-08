from pathlib import Path
from ingestion import read_csv_data, check_required_columns
from cleaning import clean_student_data
from ranking import rank_students, calculate_percentile

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

    print("\n--- Student Ranking ---")
    ranked_df = rank_students(df)
    print(ranked_df)

    print("\n--- Percentile Scores ---")
    percentile_df = calculate_percentile(df)
    print(percentile_df)

if __name__ == "__main__":
    run()
