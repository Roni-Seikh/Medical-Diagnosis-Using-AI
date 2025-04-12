import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu

# Load all models
diabetes_model = pickle.load(open('Models/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('Models/parkinsons_model.sav', 'rb'))
lung_model = pickle.load(open('Models/lungs_disease_model.sav', 'rb'))
thyroid_model = pickle.load(open('Models/thyroid_model.sav', 'rb'))

# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Disease Prediction System",
        ["Diabetes", "Heart Disease", "Parkinson's", "Lung Cancer", "Thyroid"],
        icons=["activity", "heart", "person", "lungs", "thermometer"],
        default_index=0
    )

# Diabetes Prediction
if selected == "Diabetes":
    st.title("Diabetes Prediction")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Pregnancies", 0)
    with col2:
        Glucose = st.number_input("Glucose Level")
    with col3:
        BloodPressure = st.number_input("Blood Pressure")
    with col1:
        SkinThickness = st.number_input("Skin Thickness")
    with col2:
        Insulin = st.number_input("Insulin")
    with col3:
        BMI = st.number_input("BMI")
    with col1:
        DiabetesPedigreeFunction = st.number_input("Pedigree Function")
    with col2:
        Age = st.number_input("Age")

    if st.button("Predict Diabetes"):
        input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        prediction = diabetes_model.predict(input_data)
        st.success("🩺 Diabetic" if prediction[0] == 1 else "✅ Not Diabetic")

# Heart Disease Prediction
if selected == "Heart Disease":
    st.title("Heart Disease Prediction")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age")
    with col2:
        sex = st.selectbox("Sex (1 = Male, 0 = Female)", [0, 1])
    with col3:
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    with col1:
        trestbps = st.number_input("Resting Blood Pressure")
    with col2:
        chol = st.number_input("Cholesterol")
    with col3:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    with col1:
        restecg = st.selectbox("Rest ECG", [0, 1, 2])
    with col2:
        thalach = st.number_input("Max Heart Rate Achieved")
    with col3:
        exang = st.selectbox("Exercise Induced Angina", [0, 1])
    with col1:
        oldpeak = st.number_input("Oldpeak")
    with col2:
        slope = st.selectbox("Slope", [0, 1, 2])
    with col3:
        ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3, 4])
    with col1:
        thal = st.selectbox("Thal", [0, 1, 2, 3])

    if st.button("Predict Heart Disease"):
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                                exang, oldpeak, slope, ca, thal]])
        prediction = heart_model.predict(input_data)
        st.success("❤️ Heart Disease Detected" if prediction[0] == 1 else "✅ No Heart Disease")

# Parkinson's Prediction
if selected == "Parkinson's":
    st.title("Parkinson's Disease Prediction")

    st.write("Please enter the following voice measurements:")

    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.number_input("MDVP:Fo(Hz)")
        jitter_percent = st.number_input("MDVP:Jitter(%)")
        rap = st.number_input("MDVP:RAP")
        shimmer = st.number_input("MDVP:Shimmer")
        apq3 = st.number_input("Shimmer:APQ3")
        nhr = st.number_input("NHR")
        rpde = st.number_input("RPDE")
        spread1 = st.number_input("spread1")

    with col2:
        fhi = st.number_input("MDVP:Fhi(Hz)")
        jitter_abs = st.number_input("MDVP:Jitter(Abs)")
        ppq = st.number_input("MDVP:PPQ")
        shimmer_db = st.number_input("MDVP:Shimmer(dB)")
        apq5 = st.number_input("Shimmer:APQ5")
        hnr = st.number_input("HNR")
        dfa = st.number_input("DFA")
        spread2 = st.number_input("spread2")

    with col3:
        flo = st.number_input("MDVP:Flo(Hz)")
        ddp = st.number_input("Jitter:DDP")
        apq = st.number_input("MDVP:APQ")
        dda = st.number_input("Shimmer:DDA")
        d2 = st.number_input("D2")
        ppe = st.number_input("PPE")

    if st.button("Predict Parkinson's"):
        input_data = np.array([[
            fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
            shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr,
            rpde, dfa, spread1, spread2, d2, ppe
        ]])

        prediction = parkinsons_model.predict(input_data)

        if prediction[0] == 1:
            st.success("🧠 Parkinson's Disease Detected")
        else:
            st.success("✅ No Parkinson's Disease")

# Lung Cancer Prediction
if selected == "Lung Cancer":
    st.title("Lung Cancer Prediction")
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender (1 = Male, 0 = Female)", [0, 1])
        anxiety = st.selectbox("Anxiety", [0, 1])
        fatigue = st.selectbox("Fatigue", [0, 1])
        alcohol = st.selectbox("Alcohol Consuming", [0, 1])
        swallowing_difficulty = st.selectbox("Swallowing Difficulty", [0, 1])

    with col2:
        age = st.number_input("Age")
        peer_pressure = st.selectbox("Peer Pressure", [0, 1])
        allergy = st.selectbox("Allergy", [0, 1])
        coughing = st.selectbox("Coughing", [0, 1])
        chest_pain = st.selectbox("Chest Pain", [0, 1])

    with col3:
        smoking = st.selectbox("Smoking", [0, 1])
        yellow_fingers = st.selectbox("Yellow Fingers", [0, 1])
        chronic_disease = st.selectbox("Chronic Disease", [0, 1])
        wheezing = st.selectbox("Wheezing", [0, 1])
        shortness_of_breath = st.selectbox("Shortness of Breath", [0, 1])

    if st.button("Predict Lung Cancer"):
        input_data = np.array([[
            age, gender, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease,
            fatigue, allergy, wheezing, alcohol, coughing, shortness_of_breath,
            swallowing_difficulty, chest_pain
        ]])

        prediction = lung_model.predict(input_data)

        if prediction[0] == 1:
            st.success("🫁 Lung Cancer Detected")
        else:
            st.success("✅ No Lung Cancer")

# Thyroid Disease Prediction
if selected == "Thyroid":
    st.title("Thyroid Disease Prediction")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age")
    with col2:
        sex = st.selectbox("Sex (1 = Male, 0 = Female)", [0, 1])
    with col3:
        TSH = st.number_input("TSH")
    with col1:
        T3 = st.number_input("T3")
    with col2:
        TT4 = st.number_input("TT4")
    with col3:
        T4U = st.number_input("T4U")
    with col1:
        FTI = st.number_input("FTI")

    if st.button("Predict Thyroid"):
        input_data = np.array([[age, sex, TSH, T3, TT4, T4U, FTI]])
        prediction = thyroid_model.predict(input_data)
        st.success("🧪 Thyroid Issue Detected" if prediction[0] == 1 else "✅ No Thyroid Problem")
