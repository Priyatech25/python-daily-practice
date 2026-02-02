import pandas as pd

def load_data(filename):
   
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print("File not found")
        return pd.DataFrame()


def subject_wise_statistics(df):
       return df.groupby("subject")["marks"].agg(["mean", "max", "min"])


def student_overall_average(df):
   
    return df.groupby("student_name")["marks"].mean()


def top_students(df, threshold=85):
  
    return df[df["marks"] >= threshold]


def generate_insights(df):
   
    print("\n--- Subject-wise Statistics ---")
    print(subject_wise_statistics(df))

    print("\n--- Student Overall Average ---")
    print(student_overall_average(df))

    print("\n--- Top Performing Records ---")
    print(top_students(df))


if __name__ == "__main__":
    df = load_data("cleaned_student_data.csv")

    if df.empty:
        print("No data to analyze")
    else:
        generate_insights(df)
