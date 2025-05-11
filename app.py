import streamlit as st
import numpy as np
import pickle
from joblib import load

# Load trained model
with open("pcos_model_.pkl", "rb") as file:
    model = load("pcos_model_.pkl")


# Set title
st.title("PCOS Prediction App")

st.write("Provide the following information to check for PCOS:")

#input features
cycle_length = st.number_input("Cycle length(days)", min_value=0, max_value=10)
follicle_count_right = st.number_input("Follicle No. (R)", min_value=0, max_value=50)
follicle_count_left = st.number_input("Follicle No. (L)", min_value=0, max_value=50)
AMH = st.number_input("AMH Level", min_value=0.0, max_value=15.0)


# Yes/No binary features
Pimples = st.radio("Pimples?", ["Yes", "No"])
hair_growth = st.radio("Hair Growth?", ["Yes", "No"])
weight_gain = st.radio("Weight Gain?", ["Yes", "No"])
skin_Darkening=st.radio("Skin Darkening?", ["Yes", "No"])
Fast_Food=st.radio("Fast Food?",["Yes","No"])


# Convert Yes/No to 1/0
Pimples_val=  1 if Pimples == "Yes" else 0
hair_growth_val = 1 if hair_growth == "Yes" else 0
weight_gain_val = 1 if weight_gain == "Yes" else 0
skin_Darkening_val= 1 if skin_Darkening == "Yes" else 0
Fast_Food_val= 1 if Fast_Food == "Yes" else 0


# Prepare input for model
if st.button("Predict"):
    # You may need to match the exact feature order from training
    input_data = np.array([[cycle_length, follicle_count_right,follicle_count_left, AMH, Pimples_val, hair_growth_val, weight_gain_val, skin_Darkening_val,Fast_Food_val]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("The model predicts: PCOS Positive 😔")
    else:
        st.success("The model predicts: Relax, No PCOS ✅")
