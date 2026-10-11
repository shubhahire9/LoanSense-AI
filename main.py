from pathlib import Path

import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel, Field


# ==========================================
# 1. Load saved model
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "model" / "loan_model.pkl"

model_bundle = joblib.load(MODEL_PATH)

model = model_bundle["model"]
preprocessor = model_bundle["preprocessor"]


# ==========================================
# 2. Create FastAPI application
# ==========================================

app = FastAPI(
    title="LoanSense AI API",
    description="Loan approval prediction API",
    version="1.0.0"
)


# ==========================================
# 3. Input data structure
# ==========================================

class LoanRequest(BaseModel):

    Applicant_Income: float = Field(..., ge=0)

    Coapplicant_Income: float = Field(..., ge=0)

    Employment_Status: str

    Age: float = Field(..., ge=18, le=100)

    Marital_Status: str

    Dependents: float = Field(..., ge=0)

    Credit_Score: float = Field(
        ...,
        ge=300,
        le=900
    )

    Existing_Loans: float = Field(..., ge=0)

    DTI_Ratio: float = Field(..., ge=0)

    Savings: float = Field(..., ge=0)

    Collateral_Value: float = Field(..., ge=0)

    Loan_Amount: float = Field(..., ge=0)

    Loan_Term: float = Field(..., gt=0)

    Loan_Purpose: str

    Property_Area: str

    Education_Level: str

    Gender: str

    Employer_Category: str


# ==========================================
# 4. Home endpoint
# ==========================================

@app.get("/")
def home():

    return {
        "message": "LoanSense AI API is running",
        "status": "success"
    }


# ==========================================
# 5. Health check
# ==========================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model_loaded": True
    }


# ==========================================
# 6. Prediction endpoint
# ==========================================

@app.post("/predict")
def predict(data: LoanRequest):

    # Convert request into DataFrame
    input_data = pd.DataFrame([
        data.model_dump()
    ])

    # Apply same preprocessing used during training
    processed_data = preprocessor.transform(
        input_data
    )

    # Make prediction
    prediction = model.predict(
        processed_data
    )[0]

    # Get probability
    probabilities = model.predict_proba(
        processed_data
    )[0]

    approval_probability = probabilities[1]

    # Convert 0/1 to Yes/No
    result = "Yes" if prediction == 1 else "No"

    return {
        "loan_approved": result,
        "prediction": int(prediction),
        "approval_probability": round(
            float(approval_probability),
            4
        ),
        "message": (
            "Loan is likely to be approved."
            if prediction == 1
            else "Loan is likely to be rejected."
        )
    }