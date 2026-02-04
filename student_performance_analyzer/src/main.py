import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/student_data.csv")

def load_data(path):
    """
    Load student performance data
    """
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print("Data file not found")
        return pd.DataFrame()


def main():
    df = load_data(DATA_PATH)

    if df.empty:
        print("No data available")
        return

    print("\n--- Student Performance Data Preview ---")
    print(df.head())


if __name__ == "__main__":
    main()
