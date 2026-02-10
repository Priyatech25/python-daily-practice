import matplotlib.pyplot as plt
import pandas as pd

def plot_subject_average(df: pd.DataFrame):
    avg_df = df.groupby("subject")["marks"].mean()

    plt.figure()
    avg_df.plot(kind="bar")
    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.tight_layout()
    plt.show()

def plot_marks_distribution(df: pd.DataFrame):
    plt.figure()
    plt.hist(df["marks"], bins=10)
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
