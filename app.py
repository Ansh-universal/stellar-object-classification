import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model_1.pkl")

st.title("🌌 Stellar Object Classification")

alpha = st.number_input("Alpha")
delta = st.number_input("Delta")
u = st.number_input("u")
g = st.number_input("g")
r = st.number_input("r")
i = st.number_input("i")
z = st.number_input("z")
cam_col = st.number_input("cam_col")
field_ID = st.number_input("field_ID")
redshift = st.number_input("redshift")

if st.button("Predict"):

    data = pd.DataFrame([[
        alpha,
        delta,
        u,
        g,
        r,
        i,
        z,
        cam_col,
        field_ID,
        redshift
    ]], columns=[
        'alpha',
        'delta',
        'u',
        'g',
        'r',
        'i',
        'z',
        'cam_col',
        'field_ID',
        'redshift'
    ])

   
    prediction = model.predict(data)[0]

    class_map = {
    0: "GALAXY",
    1: "QSO",
    2: "STAR"
    }

    predicted_class = class_map[prediction]

    st.success(f"Predicted Class: {predicted_class}")
    
