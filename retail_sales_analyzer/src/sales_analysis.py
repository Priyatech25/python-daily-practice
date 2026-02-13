import pandas as pd

def analyze_sales(file_path):
    df = pd.read_csv(file_path)

    df["revenue"] = df["quantity"] * df["price"]

    print("\nTotal Revenue:", df["revenue"].sum())

    top_product = df.groupby("product")["revenue"].sum().idxmax()
    print("Top Selling Product:", top_product)

    top_region = df.groupby("region")["revenue"].sum().idxmax()
    print("Best Performing Region:", top_region)

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    monthly_sales = df.groupby("month")["revenue"].sum()
    print("\nMonthly Revenue:\n", monthly_sales)

    monthly_sales.to_csv("monthly_summary.csv")

if __name__ == "__main__":
    analyze_sales("data/sales_data.csv")
