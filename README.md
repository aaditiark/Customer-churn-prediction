readme = """# Customer Churn Prediction & Retention Strategy

# Problem
Predict which telecom customers are likely to churn and translate that into a revenue-saving action plan.

# Data
Telco Customer Churn (Kaggle) — 7,043 customers, 20 features.

# Approach
- Cleaned data, encoded categorical features
- Trained Logistic Regression (82% acc) and XGBoost (80% acc)
- Explained predictions with SHAP
- Calculated revenue-at-risk and savings from targeted retention

# Key Files
- explore.ipynb — full analysis and modeling code
- summary.txt — key results
- top_risk_customers.csv — ranked list of highest-risk customers
- churn_model.pkl — saved trained model

# Headline Result
Model flags $23,893.55/month at risk. Targeting the top 20% highest-risk
customers ($21,771.50/month) with a retention campaign could save an
estimated $78,377.40/year.
"""

with open('README.md', 'w') as f:
    f.write(readme)
print("README saved")