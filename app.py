import streamlit as st
import pandas as pd
import joblib

from sklearn.base import BaseEstimator, TransformerMixin

# ---------------- CUSTOM TRANSFORMER (REQUIRED) ----------------
class InteractionFeatures(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        # Interaction terms (must match training logic)
        if "smoker_yes" in X.columns:
            X["bmi_smoker"] = X["bmi"] * X["smoker_yes"]
            X["age_smoker"] = X["age"] * X["smoker_yes"]

        return X


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="💊",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return joblib.load("medical_insurance_pipeline.pkl")

model = load_model()

# ---------------- UI HEADER ----------------
st.markdown(
    "<h1 style='text-align: center;'>💊 Medical Insurance Cost Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: gray;'>Estimate annual medical charges using Machine Learning</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- INPUT FORM ----------------
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 18, 64, 30)
        bmi = st.slider("BMI", 15.0, 50.0, 25.0)
        children = st.selectbox("Children", [0, 1, 2, 3, 4, 5])

    with col2:
        sex = st.selectbox("Sex", ["male", "female"])
        smoker = st.selectbox("Smoker", ["yes", "no"])
        region = st.selectbox(
            "Region",
            ["southeast", "southwest", "northwest", "northeast"]
        )

    submit = st.form_submit_button("🔮 Predict Cost")

# ---------------- PREDICTION ----------------
if submit:
    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    prediction = model.predict(input_data)[0]

    st.success("✅ Prediction Complete")

    st.metric(
        label="Estimated Annual Medical Cost",
        value=f"${prediction:,.2f}"
    )

# ---------------- FOOTER ----------------
st.divider()
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with ❤️ using Streamlit & Scikit-Learn</p>",
    unsafe_allow_html=True
)
