from pathlib import Path
from ingestion import read_csv_data, check_required_columns
from cleaning import clean_student_data

DATA_FILE = Path("data/student_data.csv")

def run():
    df = read_csv_data(DATA_FILE)

    if df.empty:
        print("No data loaded")
        return

    try:
        check_required_columns(df)
    except ValueError as err:
        print(err)
        return

    cleaned_df = clean_student_data(df)

    print("\n--- Cleaned Student Data ---")
    print(cleaned_df.head())
    print(f"\nTotal records after cleaning: {len(cleaned_df)}")

if __name__ == "__main__":
    run()
