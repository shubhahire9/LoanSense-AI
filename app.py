import streamlit as st
import requests


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="LoanSense AI",
    page_icon="💰",
    layout="centered"
)


# =========================================================
# DARK THEME CSS
# =========================================================

st.markdown("""
<style>

/* =========================
   MAIN BACKGROUND
========================= */

.stApp {
    background-color: #080a0f;
    color: #f8fafc;
}

.block-container {
    max-width: 900px;
    padding-top: 35px;
    padding-bottom: 50px;
}


/* =========================
   HEADER
========================= */

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 16px;
    margin-bottom: 30px;
}


/* =========================
   SECTION TITLE
========================= */

.section-title {
    font-size: 20px;
    font-weight: 700;
    color: #f8fafc;
    margin-top: 20px;
    margin-bottom: 12px;
}


/* =========================
   CONTAINER
========================= */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #0d1118;
    border: 1px solid #1f2937;
    border-radius: 14px;
    padding: 12px 18px 8px 18px;
}


/* =========================
   LABELS
========================= */

label {
    color: #dbeafe !important;
    font-weight: 500 !important;
}


/* =========================
   INPUT BOXES
========================= */

div[data-baseweb="input"] {
    background-color: #151b26 !important;
    border: 1px solid #273244 !important;
    border-radius: 8px !important;
}

div[data-baseweb="input"] input {
    color: #f8fafc !important;
}

div[data-baseweb="select"] > div {
    background-color: #151b26 !important;
    border: 1px solid #273244 !important;
    border-radius: 8px !important;
}

div[data-baseweb="select"] span {
    color: #f8fafc !important;
}


/* =========================
   BUTTON
========================= */

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 10px;
    border: none;
    background: linear-gradient(
        90deg,
        #2563eb,
        #3b82f6
    );
    color: white;
    font-size: 17px;
    font-weight: 700;
    margin-top: 10px;
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #1d4ed8,
        #2563eb
    );
    color: white;
}


/* =========================
   RESULT
========================= */

.result-title {
    color: #f8fafc;
    font-size: 22px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 15px;
}


/* =========================
   APPROVED
========================= */

.approved-box {
    background-color: #052e1b;
    border: 1px solid #047857;
    border-radius: 10px;
    padding: 16px;
    color: #34d399;
    font-size: 20px;
    font-weight: 700;
}


/* =========================
   REJECTED
========================= */

.rejected-box {
    background-color: #350a0a;
    border: 1px solid #991b1b;
    border-radius: 10px;
    padding: 16px;
    color: #f87171;
    font-size: 20px;
    font-weight: 700;
}


/* =========================
   PROBABILITY
========================= */

.probability-text {
    color: #cbd5e1;
    font-size: 18px;
    margin-top: 18px;
}

.probability-value {
    color: #34d399;
    font-weight: 800;
}


/* =========================
   INFO
========================= */

.info-box {
    background-color: #101827;
    border: 1px solid #263b5a;
    border-radius: 10px;
    padding: 14px;
    margin-top: 18px;
    color: #bfdbfe;
    font-size: 14px;
}


/* =========================
   FOOTER
========================= */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    margin-top: 40px;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">💰 LoanSense AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Smart loan approval prediction powered by Machine Learning'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# APPLICANT DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">👤 Applicant Details</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        applicant_income = st.number_input(
            "Applicant Income",
            min_value=0.0,
            value=10000.0,
            step=500.0
        )

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30,
            step=1
        )

        employment_status = st.selectbox(
            "Employment Status",
            [
                "Salaried",
                "Self-employed",
                "Contract",
                "Unemployed"
            ]
        )

        education_level = st.selectbox(
            "Education Level",
            [
                "Graduate",
                "Not Graduate"
            ]
        )

    with col2:

        coapplicant_income = st.number_input(
            "Coapplicant Income",
            min_value=0.0,
            value=2000.0,
            step=500.0
        )

        dependents = st.number_input(
            "Dependents",
            min_value=0,
            value=1,
            step=1
        )

        marital_status = st.selectbox(
            "Marital Status",
            [
                "Married",
                "Single"
            ]
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ]
        )

    employer_category = st.selectbox(
        "Employer Category",
        [
            "Private",
            "Government",
            "MNC",
            "Business",
            "Unemployed"
        ]
    )


# =========================================================
# FINANCIAL DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">💳 Financial Details</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        credit_score = st.number_input(
            "Credit Score",
            min_value=300.0,
            max_value=900.0,
            value=750.0,
            step=10.0
        )

        savings = st.number_input(
            "Savings",
            min_value=0.0,
            value=20000.0,
            step=1000.0
        )

        existing_loans = st.number_input(
            "Existing Loans",
            min_value=0,
            value=1,
            step=1
        )

    with col2:

        dti_ratio = st.number_input(
            "DTI Ratio",
            min_value=0.0,
            value=0.25,
            step=0.01,
            format="%.2f"
        )

        collateral_value = st.number_input(
            "Collateral Value",
            min_value=0.0,
            value=50000.0,
            step=5000.0
        )


# =========================================================
# LOAN DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">🏦 Loan Details</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        loan_amount = st.number_input(
            "Loan Amount",
            min_value=0.0,
            value=25000.0,
            step=1000.0
        )

        loan_purpose = st.selectbox(
            "Loan Purpose",
            [
                "Business",
                "Car",
                "Education",
                "Home",
                "Personal"
            ]
        )

    with col2:

        loan_term = st.selectbox(
            "Loan Term (months)",
            [12, 24, 36, 48, 60, 84, 120],
            index=4
        )

        property_area = st.selectbox(
            "Property Area",
            [
                "Urban",
                "Semiurban",
                "Rural"
            ]
        )


# =========================================================
# PREDICT BUTTON
# =========================================================

st.write("")

predict = st.button(
    "🔮  Check Loan Eligibility",
    use_container_width=True
)


# =========================================================
# API REQUEST
# =========================================================

if predict:

    payload = {
        "Applicant_Income": applicant_income,
        "Coapplicant_Income": coapplicant_income,
        "Employment_Status": employment_status,
        "Age": age,
        "Marital_Status": marital_status,
        "Dependents": dependents,
        "Credit_Score": credit_score,
        "Existing_Loans": existing_loans,
        "DTI_Ratio": dti_ratio,
        "Savings": savings,
        "Collateral_Value": collateral_value,
        "Loan_Amount": loan_amount,
        "Loan_Term": loan_term,
        "Loan_Purpose": loan_purpose,
        "Property_Area": property_area,
        "Education_Level": education_level,
        "Gender": gender,
        "Employer_Category": employer_category
    }

    try:

        with st.spinner("Analyzing application..."):

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=payload,
                timeout=10
            )


        # =================================================
        # SUCCESS
        # =================================================

        if response.status_code == 200:

            result = response.json()

            approval = result["loan_approved"]

            probability = (
                float(result["approval_probability"]) * 100
            )


            # =================================================
            # RESULT TITLE
            # =================================================

            st.markdown(
                '<div class="result-title">📊 Prediction Result</div>',
                unsafe_allow_html=True
            )


            # =================================================
            # APPROVAL RESULT
            # =================================================

            if approval == "Yes":

                st.markdown(
                    """
                    <div class="approved-box">
                        ✅ &nbsp; Loan Approved
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    """
                    <div class="rejected-box">
                        ❌ &nbsp; Loan Not Approved
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # =================================================
            # PROBABILITY
            # =================================================

            st.markdown(
                f"""
                <div class="probability-text">
                    Approval Probability:
                    <span class="probability-value">
                        {probability:.2f}%
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(
                min(max(probability / 100, 0.0), 1.0)
            )


            # =================================================
            # MESSAGE
            # =================================================

            if approval == "Yes":

                st.markdown(
                    """
                    <div class="info-box">
                        ℹ️ Based on the provided information,
                        the model predicts a likely loan approval.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    """
                    <div class="info-box">
                        ℹ️ Based on the provided information,
                        the model predicts a likely loan rejection.
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # =================================================
        # API ERROR
        # =================================================

        else:

            st.error(
                f"FastAPI Error: {response.status_code}"
            )

            st.code(response.text)


    # =====================================================
    # CONNECTION ERROR
    # =====================================================

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Cannot connect to FastAPI."
        )

        st.info(
            "Start FastAPI using:"
        )

        st.code(
            "uvicorn main:app --reload"
        )


    # =====================================================
    # TIMEOUT
    # =====================================================

    except requests.exceptions.Timeout:

        st.error(
            "⏱️ Request timed out."
        )


    # =====================================================
    # OTHER ERROR
    # =====================================================

    except Exception as e:

        st.error(
            f"❌ Something went wrong: {str(e)}"
        )
