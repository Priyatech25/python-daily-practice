from pathlib import Path
from ingestion import read_csv_data, check_required_columns
from cleaning import clean_student_data
from visualization import plot_subject_average, plot_marks_distribution

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

    print("Showing visualizations...")
    plot_subject_average(df)
    plot_marks_distribution(df)

if __name__ == "__main__":
    run()
