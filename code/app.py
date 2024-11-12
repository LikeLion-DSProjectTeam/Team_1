import streamlit as st
import pandas as pd
import joblib


# model = joblib.load("churn_prediction_model.pkl")
# agent = joblib.load("q_learning_agent_model.pkl")

st.title("Bank Customer Churn Prediction & Action Recommendation")

gender = st.selectbox("Gender", ["Female", "Male"])
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
age = st.slider("Age", 18, 92, 38)
is_active_member = st.selectbox("Is an Active Bank Member?", ["Yes", "No"])
has_credit_card = st.selectbox("Has an Active Credit Card?", ["Yes", "No"])
card_type = st.selectbox("Card Type", ["DIAMOND", "GOLD", "PLATINUM", "SILVER"])
num_of_products = st.selectbox("Number of Products", [1, 2, 3, 4])
credit_score = st.slider("Credit Score", 350, 850, 650)
tenure = st.slider("Years as Bank Customer (Tenure)", 0, 10, 5)
point_earned = st.slider("Point Earned", 119, 1000, 600)
balance = st.number_input("Account Balance", min_value=0, value=100000, max_value= 255000)
estimated_salary = st.number_input("Estimated Salary", min_value=0, max_value=200000, value = 100000)
complain = st.selectbox("Complain", ["Yes", "No"])

satisfaction_score = st.selectbox("Satisfaction Score", [1, 2, 3, 4, 5])

if st.button("Predict Churn Probability & Recommend Action"):
    input_data = pd.DataFrame({
        'CreditScore': [credit_score],
        'Age': [age],
        'Tenure': [tenure],
        'Balance': [balance],
        'HasCrCard': [1 if has_credit_card == "Yes" else 0],
        'IsActiveMember': [1 if is_active_member == "Yes" else 0],
        'EstimatedSalary': [estimated_salary],
        'Complain': [1 if complain == "Yes" else 0],
        'Point Earned': [point_earned],
        'Geography': [geography],
        'Gender': [gender],
        'Card Type': [card_type],
        'NumOfProducts': [num_of_products],
        'Satisfaction Score': [satisfaction_score]
    })

    churn_probability = model.predict_proba(input_data)[0][1]
    st.write(f"Predicted Churn Probability: {churn_probability:.2%}")

    state = tuple(input_data.iloc[0].values)
    if state in agent:
        action = max(agent[state], key = agent[state].get)
        st.write(f"Recommended Action: {action}")
    else:
        st.write(f"No recommended actsion for this state.")