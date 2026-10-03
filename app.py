import streamlit as st
import pandas as pd

st.set_page_config(page_title="Churn Prediction Dashboard", layout="wide")

st.markdown("""
<style>
[data-testid="stMetric"] {
    background-color: #1e2130;
    border: 1px solid #3d4256;
    border-left: 4px solid #00c2a8;
    border-radius: 10px;
    padding: 15px;
}
[data-testid="stMetricLabel"] {
    color: #a0a4b8 !important;
}
[data-testid="stMetricValue"] {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# ---- Load real data (everything below is computed, nothing is typed in) ----
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
top_risk = pd.read_csv("top_risk_customers.csv")

df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# ---- Sidebar ----
st.sidebar.title("Navigation")
st.sidebar.markdown("**Customer Churn Prediction & Retention Strategy**")
st.sidebar.markdown("Data Analyst Project — Telco Churn Dataset")

# ---- Title ----
st.title("Customer Churn Dashboard")
st.markdown("**Goal:** Identify at-risk customers and quantify the revenue impact of a targeted retention strategy.")

# ---- Key Results (all computed live) ----
churn_rate = df['Churn'].mean() * 100
at_risk_revenue = top_risk['MonthlyCharges'].sum()
n_at_risk = len(top_risk)
estimated_annual_savings = at_risk_revenue * 0.30 * 12

st.header("📊 Key Results")

st.header("⚠️ Top Risk Customers")

st.header("📈 Churn Rate by Contract Type")

st.header("🔍 Explore by Contract Type")

st.header("🎚️ Adjust Risk Threshold")

st.header("⏳ Filter by Tenure")

st.header("✅ Recommendation")

st.header("Key Results")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Overall Churn Rate", f"{churn_rate:.1f}%")
col2.metric("Customers Flagged At-Risk", f"{n_at_risk}")
col3.metric("Monthly Revenue at Risk", f"${at_risk_revenue:,.2f}")
col4.metric("Est. Annual Savings", f"${estimated_annual_savings:,.2f}")

# ---- Risk Table ----
st.header("Top Risk Customers")
st.dataframe(top_risk)

# ---- Churn by Contract ----
st.header("Churn Rate by Contract Type")
churn_by_contract = df.groupby('Contract')['Churn'].apply(lambda x: x.mean() * 100)
st.bar_chart(churn_by_contract)

# ---- Interactive Contract Filter ----
st.header("Explore by Contract Type")
contract_filter = st.selectbox("Select Contract Type", df['Contract'].unique())
filtered = df[df['Contract'] == contract_filter]
st.write(f"Churn rate for **{contract_filter}**: {filtered['Churn'].mean()*100:.1f}%")

# ---- Threshold Slider ----
st.header("Adjust Risk Threshold")
threshold = st.slider("Churn probability threshold", 0.0, 1.0, 0.5)
flagged = top_risk[top_risk['churn_prob'] >= threshold]
flagged_revenue = flagged['MonthlyCharges'].sum()
st.write(f"Customers flagged at this threshold: **{len(flagged)}**")
st.write(f"Revenue at risk: **${flagged_revenue:,.2f}**")

# ---- Tenure Filter ----
st.header("Filter by Tenure")
min_tenure, max_tenure = st.slider("Tenure range (months)", 0, 72, (0, 72))
tenure_filtered = df[(df['tenure'] >= min_tenure) & (df['tenure'] <= max_tenure)]
tenure_churn_rate = tenure_filtered['Churn'].mean() * 100
st.write(f"Churn rate for customers with {min_tenure}-{max_tenure} months tenure: **{tenure_churn_rate:.1f}%**")

# ---- Auto-Generated Recommendation (recalculates from current data) ----
avg_risk_prob = top_risk['churn_prob'].mean()

st.header("Recommendation")
st.success(
    f"Target the top **{n_at_risk}** highest-risk customers "
    f"(**${at_risk_revenue:,.2f}/month** in revenue, average churn probability **{avg_risk_prob*100:.0f}%**) "
    f"with a retention campaign. Assuming a 30% retention success rate, "
    f"this could save an estimated **${estimated_annual_savings:,.2f} annually**."
)