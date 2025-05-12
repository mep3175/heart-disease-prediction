import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Set page config and background image only (no white form box)
st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://raw.githubusercontent.com/mep3175/heart-disease-prediction/refs/heads/main/static/background.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            padding: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("❤️ Heart Disease Prediction")
st.markdown("Fill out the following information to assess your heart health risk:")

with st.form("heart_form"):
    age = st.number_input("Age", 29, 77, 58)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", 94, 200, 120)
    chol = st.number_input("Cholesterol", 126, 564, 204)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ["Yes", "No"])
    restecg = st.selectbox("Rest ECG (0–2)", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate", 71, 202, 160)
    exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("Oldpeak", 0.0, 6.2, 1.0)
    slope = st.selectbox("Slope (0–2)", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
    thal = st.selectbox("Thal (1: Normal, 2: Fixed Defect, 3: Reversible)", [1, 2, 3])

    submitted = st.form_submit_button("Predict")

if submitted:
    input_df = pd.DataFrame({
        "age": [age],
        "sex": [1 if sex == "Male" else 0],
        "cp": [cp],
        "trestbps": [trestbps],
        "chol": [chol],
        "fbs": [1 if fbs == "Yes" else 0],
        "restecg": [restecg],
        "thalach": [thalach],
        "exang": [1 if exang == "Yes" else 0],
        "oldpeak": [oldpeak],
        "slope": [slope],
        "ca": [ca],
        "thal": [thal]
    })

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ High risk of heart disease.")
    else:
        st.success("✅ No significant risk detected.")
