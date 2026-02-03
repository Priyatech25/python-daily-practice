import pandas as pd

REQUIRED_COLUMNS = {"student_name", "subject", "marks"}

def load_data(filename):
    """
    Load CSV data with error handling
    """
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print("Error: File not found")
    except pd.errors.EmptyDataError:
        print("Error: File is empty")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return pd.DataFrame()


def validate_columns(df):
    """
    Ensure required columns exist
    """
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return True


def clean_marks(df):
    """
    Ensure marks column is numeric
    """
    df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
    df["marks"] = df["marks"].fillna(df["marks"].mean())
    return df


def subject_statistics(df):
    """
    Calculate subject-wise statistics
    """
    return df.groupby("subject")["marks"].agg(["mean", "max", "min"])


def student_averages(df):
    """
    Calculate student-wise averages
    """
    return df.groupby("student_name")["marks"].mean()


def main():
    df = load_data("cleaned_student_data.csv")

    if df.empty:
        print("No data loaded")
        return

    try:
        validate_columns(df)
    except ValueError as err:
        print(err)
        return

    df = clean_marks(df)

    print("\n--- Subject-wise Statistics ---")
    print(subject_statistics(df))

    print("\n--- Student-wise Averages ---")
    print(student_averages(df))


if __name__ == "__main__":
    main()
