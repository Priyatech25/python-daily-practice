import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model(file_path):
    df = pd.read_csv(file_path)

    # Convert attrition Yes/No to 1/0
    df["attrition"] = df["attrition"].map({"Yes": 1, "No": 0})

    # One-hot encode department
    df = pd.get_dummies(df, columns=["department"], drop_first=True)

    X = df.drop(["employee_id", "attrition"], axis=1)
    y = df["attrition"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\n====== MODEL PERFORMANCE ======")
    print("Accuracy:", accuracy_score(y_test, predictions))
    print("\nClassification Report:\n")
    print(classification_report(y_test, predictions))

    # Save model
    joblib.dump(model, "attrition_model.pkl")
    print("\nModel saved as attrition_model.pkl")

if __name__ == "__main__":
    train_model("data/employee_data.csv")
