import pandas as pd

def subject_wise_average(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("subject")["marks"].mean().reset_index()

def class_summary(df: pd.DataFrame) -> dict:
    student_count = (
        df["student_id"].nunique()
        if "student_id" in df.columns
        else len(df)
    )

    return {
        "average_marks": df["marks"].mean(),
        "highest_marks": df["marks"].max(),
        "lowest_marks": df["marks"].min(),
        "student_count": student_count
    }

