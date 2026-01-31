import pandas as pd

def load_data(filename):
    
    Load CSV data into a pandas DataFrame
    
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print("CSV file not found")
        return pd.DataFrame()


def basic_overview(df):
    
    Display basic information about the dataset
    
    print("\n--- Data Preview ---")
    print(df.head())

    print("\n--- Data Info ---")
    print(df.info())

    print("\n--- Statistical Summary ---")
    print(df.describe())


def subject_wise_average(df):
    
    Calculate subject-wise average marks
    
    return df.groupby("subject")["marks"].mean()


def top_performers(df):
   
    Filter students who scored more than 85
    
    return df[df["marks"] > 85]


if __name__ == "__main__":
    
    df = load_data("student_data.csv")

    if df.empty:
        print("No data to analyze")
    else:
       
        basic_overview(df)

       
        print("\n--- Subject-wise Average Marks ---")
        print(subject_wise_average(df))

       
        print("\n--- Top Performers (Marks > 85) ---")
        print(top_performers(df))

