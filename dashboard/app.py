
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/fraud_model_xgboost.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("Fraud Transaction Scoring")
uploaded_file = st.file_uploader("Upload CSV")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    X_scaled = scaler.transform(df)
    preds = model.predict_proba(X_scaled)[:,1]
    df["fraud_score"] = preds
    df["fraud_flag"] = (preds > 0.5).astype(int)
    st.dataframe(df)
    csv = df.to_csv(index=False).encode()
    st.download_button("Download Results", csv, "scored_transactions.csv")
