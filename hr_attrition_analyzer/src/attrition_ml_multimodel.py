import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

def train_models(file_path):
    df = pd.read_csv(file_path)

    # Encode attrition Yes/No as 1/0
    df["attrition"] = df["attrition"].map({"Yes": 1, "No": 0})

    # One-hot encode department
    df = pd.get_dummies(df, columns=["department"], drop_first=True)

    # Features & Target
    X = df.drop(["employee_id", "attrition"], axis=1)
    y = df["attrition"]

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=500),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    best_model = None
    best_accuracy = 0

    print("\n====== MODEL COMPARISON ======")
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"\n{name}:")
        print("Accuracy:", acc)
        print(classification_report(y_test, preds))

        if acc > best_accuracy:
            best_accuracy = acc
            best_model = model

        # Plot confusion matrix
        cm = confusion_matrix(y_test, preds)
        plt.figure(figsize=(4,3))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        plt.title(f"Confusion Matrix - {name}")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()

    # Save best model
    joblib.dump(best_model, "best_attrition_model.pkl")
    print(f"\nBest Model Saved as 'best_attrition_model.pkl' with Accuracy: {best_accuracy:.2f}")

if __name__ == "__main__":
    train_models("data/employee_data.csv")
