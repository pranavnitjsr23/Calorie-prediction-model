import joblib
import streamlit as st
import pandas as pd
from PIL import Image
import time

# Page configuration
st.set_page_config(
    page_title="Calorie Predictor",
    page_icon="🔥",
    layout="centered"
)

image = Image.open("burn.png")
st.image(image, caption="Calorie Predictor", use_container_width=True)

# Load trained model
model = joblib.load("calorie_model.pkl")

# Title
st.title("🔥 Calorie Burn Predictor")
st.write("Enter your exercise details to estimate calories burned.")

# User inputs
gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=22
)

height = st.number_input(
    "Height (cm)",
    min_value=50,
    max_value=250,
    value=170
)

weight = st.number_input(
    "Weight (kg)",
    min_value=20,
    max_value=200,
    value=70
)

duration = st.number_input(
    "Exercise Duration (minutes)",
    min_value=1,
    max_value=300,
    value=30
)

heart_rate = st.number_input(
    "Heart Rate (bpm)",
    min_value=40,
    max_value=220,
    value=100
)

body_temp = st.number_input(
    "Body Temperature (°C)",
    min_value=30.0,
    max_value=45.0,
    value=37.0
)

# Prediction
if st.button("🔥 Predict Calories", use_container_width=True):

    # Basic input validation
    if age <= 0 or height <= 0 or weight <= 0 or duration <= 0:
        st.error("Please enter valid positive values for all fields.")

    elif heart_rate < 40 or heart_rate > 220:
        st.error("Please enter a valid heart rate between 40 and 220 bpm.")

    elif body_temp < 30 or body_temp > 45:
        st.error("Please enter a valid body temperature.")

    else:
        try:
            gender_encoded = 0 if gender == "Male" else 1

            input_data = pd.DataFrame({
                "Gender": [gender_encoded],
                "Age": [age],
                "Height": [height],
                "Weight": [weight],
                "Duration": [duration],
                "Heart_Rate": [heart_rate],
                "Body_Temp": [body_temp]
            })

            with st.spinner("Calculating..."):
                time.sleep(2)
                prediction = model.predict(input_data)

            st.success(
                f"Estimated Calories Burned: **{prediction[0]:.2f} kcal**"
            )

        except Exception as e:
            st.error(
                "Something went wrong while making the prediction. "
                "Please check your inputs and try again."
            )


