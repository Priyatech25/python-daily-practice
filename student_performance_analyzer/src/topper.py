import pandas as pd

def subject_topper(df: pd.DataFrame) -> pd.DataFrame:
    """Return the student(s) with highest marks in each subject"""
    top_df = df.loc[df.groupby("subject")["marks"].idxmax()]
    return top_df.reset_index(drop=True)

def generate_mini_report(df: pd.DataFrame) -> str:
    """Generate a simple text report for the class"""
    report = "=== Mini Report ===\n"
    subjects = df['subject'].unique()
    for sub in subjects:
        top_students = subject_topper(df[df['subject'] == sub])
        for i, row in top_students.iterrows():
            report += f"\nSubject: {sub}\n"
            report += f"Topper: {row['student_name']}, Marks: {row['marks']}\n"
    return report

