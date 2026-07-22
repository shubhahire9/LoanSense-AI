# 💰 LoanSense AI – Loan Approval Prediction using Machine Learning

## Overview

LoanSense AI is a machine learning-based loan approval prediction system that automates applicant screening using historical loan application data. The project follows an end-to-end machine learning workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, and performance evaluation to support data-driven loan approval decisions.

---

## Objectives

- Predict loan approval status using applicant financial and demographic information.
- Perform data cleaning and preprocessing.
- Conduct exploratory data analysis (EDA).
- Engineer features to improve model performance.
- Train and evaluate machine learning classification models.
- Interpret model performance using multiple evaluation metrics.

---

## Dataset

The dataset contains **950 loan application records** with **20 features** describing applicant demographics, financial details, employment information, and loan characteristics.

### Features

| Category | Features |
|----------|----------|
| Applicant Details | Applicant_ID, Age, Gender, Marital_Status, Dependents, Education_Level |
| Financial Details | Applicant_Income, Coapplicant_Income, Savings, Credit_Score, DTI_Ratio, Existing_Loans |
| Employment | Employment_Status, Employer_Category |
| Loan Details | Loan_Amount, Loan_Term, Loan_Purpose, Collateral_Value |
| Property | Property_Area |
| Target Variable | Loan_Approved |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook / Google Colab

---

## Project Workflow

1. Load the dataset
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Performance Analysis

---

## Key Features

- End-to-end Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Classification
- Model Evaluation
- Performance Metrics Analysis

---

## Model Evaluation

The trained model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report
- Confusion Matrix

---

## Results

- Developed a machine learning-based loan approval prediction system using historical loan application data.
- Performed end-to-end data preprocessing, exploratory data analysis (EDA), and feature engineering.
- Built and evaluated classification models to predict loan approval status.
- Assessed model performance using Accuracy, Precision, Recall, F1-Score, Classification Report, and Confusion Matrix.

---

## Future Improvements

- Compare multiple machine learning models such as Random Forest, XGBoost, and LightGBM.
- Perform hyperparameter tuning for improved performance.
- Handle class imbalance using SMOTE or class weighting techniques.
- Deploy the model as a web application using FastAPI or Streamlit.
- Incorporate Explainable AI (SHAP/LIME) for model interpretation.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/shubhahire9/LoanSense-AI.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook using Jupyter Notebook or Google Colab.

---

## Project Structure

```
LoanSense-AI/
│
├── LoanSense_AI.ipynb
├── README.md
└── images/
    ├── correlation_heatmap.png
    ├── confusion_matrix.png
```

---

## Screenshots

### Correlation Heatmap

![Correlation Heatmap](images/correlation_heatmap.png)

### Confusion Matrix

![Confusion Matrix](images/confusion_matrix.png)

---

## Author

**Shubh Ahire**

Computer Engineering Student | Machine Learning Enthusiast
