import pandas as pd

df = pd.read_csv("C:\Users\K.PRIYA DARSHINI\python-daily-practice\data\netflix.csv")

print("----- Dataset Loaded Successfully -----")
print(df.head())


print("\n----- Content Type Count -----")
print(df['type'].value_counts())


print("\n----- Top 10 Countries -----")
print(df['country'].value_counts().head(10))

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

print("\n----- Content Added Per Year -----")
print(df['year_added'].value_counts().sort_index())
print("\n----- Most Common Genres -----")
print(df['listed_in'].value_counts().head(10))