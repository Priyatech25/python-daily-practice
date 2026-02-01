import pandas as pd

def load_data(filename):
   
    #Load raw CSV data
    
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print("File not found")
        return pd.DataFrame()


def rename_columns(df):
    
    #Rename columns to standard format
    
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df


def clean_marks_column(df):
    
    #Convert marks to numeric and handle invalid values
    
    df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
    return df


def handle_missing_values(df):
    
   # Fill missing marks with average marks
   
    avg_marks = df["marks"].mean()
    df["marks"] = df["marks"].fillna(avg_marks)
    return df


def clean_data_pipeline(filename):
    
    #Full cleaning pipeline
    
    df = load_data(filename)

    if df.empty:
        return df

    df = rename_columns(df)
    df = clean_marks_column(df)
    df = handle_missing_values(df)

    return df


if __name__ == "__main__":
    df = clean_data_pipeline("raw_student_data.csv")

    if df.empty:
        print("No data available")
    else:
        print("\n--- Cleaned Dataset ---")
        print(df)

        print("\n--- Data Info After Cleaning ---")
        print(df.info())
