
from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("models/fraud_model_xgboost.pkl")
scaler = joblib.load("models/scaler.pkl")

@app.post("/score_transaction")
def score(data: dict):
    df = pd.DataFrame([data])
    scaled = scaler.transform(df)
    score = model.predict_proba(scaled)[0][1]
    return {"fraud_score": round(score, 4), "fraud_flag": int(score > 0.5)}
