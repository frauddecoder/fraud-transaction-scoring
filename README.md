# ⚡️ Real-Time Fraud Detection Scoring System

> A production-ready fraud scoring pipeline using Python, XGBoost, FastAPI, and Streamlit for fintech, SaaS, and e-commerce.

---

## 📌 Overview
This repository showcases an end-to-end ML system for real-time transaction fraud detection. Built with scalability and interpretability in mind, the project includes:

- ✅ Data simulation (50,000+ synthetic transactions)
- ✅ Feature engineering for behavioral fraud patterns
- ✅ XGBoost classifier trained with `sklearn` pipeline
- ✅ REST API (FastAPI) for JSON scoring
- ✅ UI interface (Streamlit) for CSV/manual scoring
- ✅ GitHub-structured repo for deployability and hiring demos

---

## 🧠 Tech Stack
| Layer           | Tool               |
|----------------|--------------------|
| Programming    | Python 3.10        |
| Modeling       | XGBoost, Scikit-learn |
| API            | FastAPI            |
| UI             | Streamlit          |
| Serialization  | Joblib             |
| Data Handling  | Pandas, NumPy      |

---

## 📁 Project Structure
```
├── api/                   # FastAPI app for scoring
│   └── score_transaction_api.py
├── dashboard/             # Streamlit interface
│   └── app.py
├── models/                # Trained model and scaler
│   ├── fraud_model_xgboost.pkl
│   └── scaler.pkl
├── data/                  # Sample and full transaction datasets
│   ├── transactions_50k.csv
│   └── transactions_test_sample.csv
├── notebooks/             # EDA and feature exploration
│   └── exploration_notebook.ipynb
├── project_description.md # Summary for portfolio
├── fraud_project_summary.txt # Text one-pager for LinkedIn
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🔧 Setup & Usage

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run API Server (for JSON scoring)
```bash
uvicorn api.score_transaction_api:app --reload
```
**POST example:**
```json
{
  "amount": 430.5,
  "is_new_device": 1,
  "velocity_risk": 1,
  "txn_per_minute": 6,
  ...
}
```
**Response:** `{ "fraud_score": 0.82, "fraud_flag": 1 }`

### 3. Launch Streamlit Dashboard
```bash
streamlit run dashboard/app.py
```
- Upload a CSV of transactions
- View fraud scores and download results

---

## 📊 Model Info
- Model: **XGBoostClassifier**
- Feature inputs: 10+ behavioral + time-based features
- AUC ROC: ~0.93
- Fraud rate simulated: ~2.7%
- Threshold: 0.5 (adjustable)

---

## 📄 Licensing & Credits
Built by [Ilya Kostikov](https://www.linkedin.com/in/ilya-kostikov/) — fraud analytics & AI consultant. 

---
Made with ❤️ by a developer who spent too many nights building fraud detectors.
