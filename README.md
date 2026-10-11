# 💰 LoanSense AI: Loan Approval Prediction

LoanSense AI is a machine learning-based loan approval prediction application that combines an end-to-end ML workflow with a **FastAPI backend** and an interactive **Streamlit frontend**.

The project uses historical loan application data to predict loan approval outcomes based on applicant financial, demographic, employment, and loan-related information.

## 🚀 Features

- **Machine Learning:** Predicts loan approval outcomes using a trained Scikit-learn model.
- **Data Preprocessing:** Prepares applicant data using a saved preprocessing pipeline.
- **Exploratory Data Analysis:** Includes data analysis and visualization in the Jupyter Notebook.
- **FastAPI Backend:** Exposes REST API endpoints for loan predictions.
- **Streamlit Frontend:** Provides an interactive interface for entering applicant information and viewing predictions.
- **Input Validation:** Validates applicant information through Pydantic.
- **Prediction Probability:** Returns the model's estimated approval probability through the prediction API.
- **Interactive API Documentation:** Supports testing through FastAPI's Swagger UI.

## 🛠️ Tech Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy, Matplotlib
- **Machine Learning:** Scikit-learn
- **Backend:** FastAPI, Uvicorn
- **Frontend:** Streamlit
- **Data Validation:** Pydantic
- **Model Loading:** Joblib
- **Development:** Jupyter Notebook, VS Code

## 📊 Dataset

The project includes a loan application dataset containing applicant demographics, financial information, employment details, loan characteristics, and the target variable `Loan_Approved`.

The dataset description and feature analysis are available in the notebook. Verify the current CSV dimensions before publishing a specific record count.

## 🧠 Machine Learning Workflow

1. Load and explore the dataset.
2. Perform data cleaning and preprocessing.
3. Conduct exploratory data analysis (EDA).
4. Engineer relevant features.
5. Train and evaluate classification models.
6. Save the trained model and preprocessing pipeline.
7. Serve predictions through FastAPI.
8. Display predictions through Streamlit.

## 📁 Project Structure

```text
LoanSense-AI/
├── model/
│   └── loan_model.pkl
├── app.py
├── main.py
├── model_pipeline.py
├── train_model.py
├── requirements.txt
├── .gitignore
├── README.md
├── LoanSense AI.csv
└── LoanSense AI.ipynb
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/shubhahire9/LoanSense-AI.git
cd LoanSense-AI
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## ▶️ Run the Application

### Start the FastAPI backend

Open a terminal in the project directory and run:

```bash
uvicorn main:app --reload
```

The API will run locally at `http://127.0.0.1:8000`.

Interactive API documentation:

`http://127.0.0.1:8000/docs`

Health check:

`http://127.0.0.1:8000/health`

### Start the Streamlit frontend

Open a second terminal, activate the virtual environment, and run:

```bash
streamlit run app.py
```

Open the local URL printed in the terminal to use the application.

## 📈 Model Evaluation

The machine learning workflow evaluates classification performance using metrics such as:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Classification report

Refer to the notebook and training script for the actual evaluation results.

## 🔮 Future Improvements

- Deploy the application online.
- Add automated API and model tests.
- Improve model explainability using SHAP or LIME.
- Add model performance visualizations.
- Compare additional classification algorithms.
- Improve input validation and prediction explanations.

## 👨‍💻 Author

**Shubh Ahire**
