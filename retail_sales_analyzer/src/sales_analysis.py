import pandas as pd
import matplotlib.pyplot as plt

def analyze_sales(file_path):
    df = pd.read_csv(file_path)

    df["revenue"] = df["quantity"] * df["price"]

    total_revenue = df["revenue"].sum()

    top_product = df.groupby("product")["revenue"].sum().idxmax()
    top_region = df.groupby("region")["revenue"].sum().idxmax()

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    monthly_sales = df.groupby("month")["revenue"].sum()

    # Print Summary
    print("\n========== SALES SUMMARY ==========")
    print("Total Revenue:", total_revenue)
    print("Top Product:", top_product)
    print("Best Region:", top_region)
    print("\nMonthly Revenue:\n", monthly_sales)

    # Export Summary Report
    summary_df = pd.DataFrame({
        "Metric": ["Total Revenue", "Top Product", "Best Region"],
        "Value": [total_revenue, top_product, top_region]
    })

    summary_df.to_csv("sales_summary_report.csv", index=False)

    monthly_sales.to_csv("monthly_summary.csv")

    # Plot Graph
    monthly_sales.plot(kind="bar")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    analyze_sales("data/sales_data.csv")

