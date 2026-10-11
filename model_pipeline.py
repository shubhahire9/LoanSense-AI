import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin


# Custom feature engineering
class FeatureEngineering(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        # Create squared features
        X["DTI_Ratio_sq"] = X["DTI_Ratio"] ** 2
        X["Credit_Score_sq"] = X["Credit_Score"] ** 2

        # Remove original columns
        X = X.drop(
            columns=["DTI_Ratio", "Credit_Score"],
            errors="ignore"
        )

        return X


# Numerical columns
NUMERIC_COLUMNS = [
    "Applicant_Income",
    "Coapplicant_Income",
    "Age",
    "Dependents",
    "Existing_Loans",
    "Savings",
    "Collateral_Value",
    "Loan_Amount",
    "Loan_Term",
    "DTI_Ratio_sq",
    "Credit_Score_sq"
]


# Categorical columns
CATEGORICAL_COLUMNS = [
    "Employment_Status",
    "Marital_Status",
    "Loan_Purpose",
    "Property_Area",
    "Education_Level",
    "Gender",
    "Employer_Category"
]


def create_preprocessor():

    numeric_pipeline = Pipeline([
        (
            "imputer",
            SimpleImputer(strategy="mean")
        ),
        (
            "scaler",
            StandardScaler()
        )
    ])

    categorical_pipeline = Pipeline([
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "encoder",
            OneHotEncoder(
                drop="first",
                handle_unknown="ignore",
                sparse_output=False
            )
        )
    ])

    preprocessor = Pipeline([
        (
            "feature_engineering",
            FeatureEngineering()
        ),
        (
            "columns",
            ColumnTransformer(
                transformers=[
                    (
                        "numeric",
                        numeric_pipeline,
                        NUMERIC_COLUMNS
                    ),
                    (
                        "categorical",
                        categorical_pipeline,
                        CATEGORICAL_COLUMNS
                    )
                ]
            )
        )
    ])

    return preprocessor