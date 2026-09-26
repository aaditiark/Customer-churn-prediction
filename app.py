

#st.title("Customer Churn Dashboard")
#st.write("Hello — dashboard is working!")

import streamlit as st
import pandas as pd

st.title("Customer Churn Dashboard")

st.header("Key Results")
st.metric("Overall Churn Rate", "26.5%")
st.metric("Monthly Revenue at Risk", "$23,893.55")
st.metric("Top 20% Risk Revenue", "$21,771.50")
st.metric("Estimated Annual Savings", "$78,377.40")


st.header("Top Risk Customers")
top_risk = pd.read_csv("top_risk_customers.csv")
st.dataframe(top_risk)

st.header("Churn Rate by Contract Type")

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
churn_by_contract = df.groupby('Contract')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
st.bar_chart(churn_by_contract)

st.header("Explore by Contract Type")
contract_filter = st.selectbox("Select Contract Type", df['Contract'].unique())
filtered = df[df['Contract'] == contract_filter]
st.write(f"Churn rate for {contract_filter}: {(filtered['Churn'] == 'Yes').mean()*100:.1f}%")