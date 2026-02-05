import pandas as pd

REQUIRED_COLUMNS = {"student_name", "subject", "marks"}

def read_csv_data(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print("CSV file not found")
    except Exception as e:
        print(f"Error while loading data: {e}")
    return pd.DataFrame()

def check_required_columns(df):
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return True
