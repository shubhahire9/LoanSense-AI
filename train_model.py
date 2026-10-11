import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from model_pipeline import create_preprocessor


# -----------------------------------
# 1. Load dataset
# -----------------------------------

df = pd.read_csv("LoanSense AI.csv")

print("Dataset shape:", df.shape)


# -----------------------------------
# 2. Remove rows with missing target
# -----------------------------------

df = df.dropna(subset=["Loan_Approved"])


# -----------------------------------
# 3. Separate X and y
# -----------------------------------

X = df.drop(columns=["Loan_Approved"])

y = df["Loan_Approved"].map({
    "No": 0,
    "Yes": 1
})


# -----------------------------------
# 4. Remove Applicant_ID
# -----------------------------------

X = X.drop(columns=["Applicant_ID"])


# -----------------------------------
# 5. Train-test split
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("Training data:", X_train.shape)
print("Testing data :", X_test.shape)


# -----------------------------------
# 6. Create preprocessing pipeline
# -----------------------------------

preprocessor = create_preprocessor()


# -----------------------------------
# 7. Fit preprocessing on training data
# -----------------------------------

X_train_processed = preprocessor.fit_transform(X_train)

X_test_processed = preprocessor.transform(X_test)


print("Processed training data:", X_train_processed.shape)


# -----------------------------------
# 8. Create Naive Bayes model
# -----------------------------------

model = GaussianNB()


# -----------------------------------
# 9. Train model
# -----------------------------------

model.fit(
    X_train_processed,
    y_train
)


# -----------------------------------
# 10. Make predictions
# -----------------------------------

y_pred = model.predict(X_test_processed)


# -----------------------------------
# 11. Evaluate model
# -----------------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n========== MODEL RESULTS ==========")

print("Accuracy :", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# -----------------------------------
# 12. Save model + preprocessing
# -----------------------------------

os.makedirs("model", exist_ok=True)

model_bundle = {
    "model": model,
    "preprocessor": preprocessor
}

joblib.dump(
    model_bundle,
    "model/loan_model.pkl"
)


print("\nModel saved successfully!")
print("Location: model/loan_model.pkl")
