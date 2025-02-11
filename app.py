import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# Define the directory where models are stored
MODEL_DIR = "saved_models/"

# Load trained model
best_model_name = "Random Forest.pkl" # can be changed to any model
model_path = os.path.join(MODEL_DIR, best_model_name)
model = joblib.load(model_path)

# Load scaler & encoders
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
target_encoder = joblib.load(os.path.join(MODEL_DIR, "target_encoder.pkl"))
selected_features = joblib.load(os.path.join(MODEL_DIR, "selected_features.pkl"))

# Define feature min/max values
feature_ranges = {
    "Insulin Levels": (5, 49), "Age": (0, 79), "BMI": (12, 39),
    "Blood Pressure": (60, 149), "Cholesterol Levels": (100, 299),
    "Waist Circumference": (20, 54), "Blood Glucose Levels": (80, 299),
    "Weight Gain During Pregnancy": (0, 39), "Pancreatic Health": (10, 99),
    "Pulmonary Function": (30, 89), "Neurological Assessments": (1, 3),
    "Digestive Enzyme Levels": (10, 99), "Birth Weight": (1500, 4499)
}

# Get original diabetes types from encoder
diabetes_types = {i: label for i, label in enumerate(target_encoder.classes_)}

# Streamlit UI
st.title("🏥 Diabetes Type Prediction App")
st.write("Enter patient details to predict **which type of diabetes** a patient has.")

# Collect user input
input_data = {}
for feature in selected_features:
    input_data[feature] = st.number_input(f"{feature}", value=0)  # Allow any value

# Convert inputs into DataFrame
input_df = pd.DataFrame([input_data])

# Prediction button
predict_clicked = st.button("Predict Diabetes Type")

# Run input validation & prediction only after button click
if predict_clicked:
    if all(value == 0 for value in input_data.values()):  # Check if all values are 0
        st.error("❌ Error: All input values are 0. Please enter valid data.")
    else:
        # Cap values to prevent out-of-range errors (No warning messages)
        for feature, (min_val, max_val) in feature_ranges.items():
            if feature in input_df.columns:
                input_df[feature] = np.clip(input_df[feature], min_val, max_val)

        # Standardize numerical inputs
        input_df[selected_features] = scaler.transform(input_df[selected_features])

        # Predict diabetes type
        prediction = model.predict(input_df)
        diabetes_result = diabetes_types.get(prediction[0], "Unknown Type")

        # Display result
        st.subheader(f"🔍 **Prediction: {diabetes_result}**")
        
        if diabetes_result in ["Prediabetic", "Type 2 Diabetes", "Gestational Diabetes"]:
            st.warning(f"⚠️ {diabetes_result} detected. Please follow medical advice.")
        else:
            st.error(f"🚨 {diabetes_result} detected. Seek immediate medical attention.")
