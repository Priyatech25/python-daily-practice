import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def analyze_churn(file_path):
    df = pd.read_csv(file_path)

    # Churn Rate
    churn_rate = (df["churn"] == "Yes").mean() * 100
    print("\n===== CUSTOMER CHURN SUMMARY =====")
    print(f"Churn Rate: {churn_rate:.2f}%")

    # Encode churn
    df["churn"] = df["churn"].map({"Yes": 1, "No": 0})

    # One-hot encoding
    df = pd.get_dummies(df, columns=["gender", "contract_type"], drop_first=True)

    X = df.drop(["customer_id", "churn"], axis=1)
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=500),
        "Decision Tree": DecisionTreeClassifier()
    }

    print("\n===== MODEL PERFORMANCE =====")
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        print(f"\n{name}")
        print("Accuracy:", accuracy_score(y_test, preds))
        print(classification_report(y_test, preds))

if __name__ == "__main__":
    analyze_churn("data/churn_data.csv")
