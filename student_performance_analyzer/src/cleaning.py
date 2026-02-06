import pandas as pd

def clean_student_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Drop rows with missing marks
    df.dropna(subset=["marks"], inplace=True)

    # Convert marks to numeric
    df["marks"] = pd.to_numeric(df["marks"], errors="coerce")

    # Remove invalid marks
    df = df[(df["marks"] >= 0) & (df["marks"] <= 100)]

    return df
