import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

def churn_eda(file_path):
    df = pd.read_csv(file_path)

    print("\n===== BASIC INFO =====")
    print(df.info())
    print("\nChurn Distribution:\n", df["churn"].value_counts())

    # Convert churn to binary
    df["churn"] = df["churn"].map({"Yes": 1, "No": 0})

    # Visualization 1: Tenure vs Churn
    plt.figure()
    df.groupby("churn")["tenure"].mean().plot(kind="bar")
    plt.title("Average Tenure by Churn")
    plt.xlabel("Churn (0=No, 1=Yes)")
    plt.ylabel("Average Tenure")
    plt.show()

    # Visualization 2: Monthly Charges vs Churn
    plt.figure()
    df.groupby("churn")["monthly_charges"].mean().plot(kind="bar")
    plt.title("Average Monthly Charges by Churn")
    plt.xlabel("Churn (0=No, 1=Yes)")
    plt.ylabel("Average Monthly Charges")
    plt.show()

    # One-hot encode categorical features
    df = pd.get_dummies(df, columns=["gender", "contract_type"], drop_first=True)

    X = df.drop(["customer_id", "churn"], axis=1)
    y = df["churn"]

    # Train Random Forest for feature importance
    model = RandomForestClassifier()
    model.fit(X, y)

    importance = pd.Series(model.feature_importances_, index=X.columns)
    importance = importance.sort_values(ascending=False)

    print("\n===== FEATURE IMPORTANCE =====")
    print(importance)

    # Plot feature importance
    plt.figure()
    importance.plot(kind="bar")
    plt.title("Feature Importance")
    plt.ylabel("Importance Score")
    plt.show()

    # Export importance
    importance.to_csv("feature_importance_report.csv")

if __name__ == "__main__":
    churn_eda("data/churn_data.csv")
