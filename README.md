# Customer Churn Prediction & Retention Strategy

A data analytics project that predicts which telecom customers are likely to churn, explains *why* using SHAP, and translates the model into a concrete revenue-saving action plan — not just an accuracy score.

**Live Dashboard:** https://customer-churn-prediction-uzlpveqpaxmvtxzmlkrytg.streamlit.app

## Problem
Customer churn directly costs revenue. This project identifies which customers are most likely to leave, quantifies how much revenue is at risk, and recommends a targeted retention strategy.

## Dataset
Telco Customer Churn (Kaggle) — 7,043 customers, 20 features (contract type, tenure, charges, services, payment method, etc.)

## Tech Stack
- **Python** — pandas, scikit-learn, XGBoost, SHAP
- **Streamlit** — interactive dashboard, deployed on Streamlit Cloud
- **Git/GitHub** — version control

## Approach
1. Cleaned data and handled missing values (`TotalCharges` type mismatch, nulls)
2. Encoded categorical features for modeling
3. Trained and compared two models: Logistic Regression (82% accuracy) and XGBoost (80% accuracy)
4. Used SHAP to explain which features drive churn predictions
5. Calculated revenue-at-risk and projected savings from a targeted retention campaign

## Key Findings
- Month-to-month contract customers churn far more than annual-contract customers
- Churn risk is highest in a customer's first few months, then drops with tenure
- Fiber optic internet and electronic check payment correlate with higher churn

## Business Impact
- **$23,893.55/month** in revenue tied to customers likely to churn
- Targeting the **top 20% highest-risk customers** (282 people) covers **$21,771.50/month** of that risk
- Assuming a 30% retention campaign success rate: **~$78,377.40 saved annually**

## Key Files
- `explore.ipynb` — full EDA, feature engineering, and modeling code
- `app.py` — Streamlit dashboard source
- `top_risk_customers.csv` — ranked list of highest-risk customers
- `churn_model.pkl` — saved trained XGBoost model

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
