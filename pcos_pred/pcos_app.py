import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("pcos_pred/pcos_model_).pkl", "rb") as file:
    model = pickle.load(file)

# Set title
st.title("PCOS Prediction App")

st.write("Provide the following information to check for PCOS:")

#input features
age = st.number_input("Age", min_value=10, max_value=50, step=1)
weight = st.number_input("Weight (Kg)", min_value=30.0, max_value=200.0)
height = st.number_input("Height(cm) ", min_value=120.0, max_value=210.0)
cycle_length = st.number_input("Cycle length(days)", min_value=10, max_value=45)
follicle_count = st.number_input("Follicle No. (R)", min_value=0, max_value=50)

# Prepare input for model
if st.button("Predict"):
    # You may need to match the exact feature order from training
    input_data = np.array([[age, weight, height, cycle_length, follicle_count]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("The model predicts: PCOS Positive ❌")
    else:
        st.success("The model predicts: No PCOS ✅")
