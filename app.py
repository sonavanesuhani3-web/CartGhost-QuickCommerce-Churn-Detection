import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration for wide dashboard layout
st.set_page_config(page_title="CartGhost Dashboard", layout="wide")

st.title("🛒 CartGhost - Silent Churn Detection Dashboard")
st.markdown("---")

# Load data
df = pd.read_csv("user_churn_summary.csv")

# 1. Top Metrics Summary Row (Cards)
total_users = len(df)
churned_users = int(df['is_silent_churn'].sum())
avg_spend = df['total_spend'].mean()

col1, col2, col3 = st.columns(3)
col1.metric(label="👥 Total Users", value=f"{total_users:,}")
col2.metric(label="⚠️ Silent Churned Users", value=f"{churned_users:,}")
col3.metric(label="💰 Avg Spend (₹)", value=f"₹{avg_spend:.2f}")

st.markdown("---")

# 2. Side-by-Side Colorful Charts (Row 1)
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    churn_counts = df['is_silent_churn'].value_counts().reset_index()
    churn_counts.columns = ['is_silent_churn', 'count']
    fig_donut = px.pie(churn_counts, names='is_silent_churn', values='count', 
                      title="Active vs Silent Churned Customers", hole=0.4,
                      color_discrete_sequence=['#00CC96', '#EF553B'])
    st.plotly_chart(fig_donut, use_container_width=True)

with chart_col2:
    fig_bar = px.box(df, x='is_silent_churn', y='total_spend', 
                     title="Total Spend Distribution by Churn Status",
                     color='is_silent_churn',
                     color_discrete_sequence=['#636EFA', '#AB63FA'])
    st.plotly_chart(fig_bar, use_container_width=True)

# 3. Side-by-Side Colorful Charts (Row 2)
chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    fig_delivery = px.box(df, x='is_silent_churn', y='avg_delivery_time',
                         title="Average Delivery Time vs Churn Status",
                         color='is_silent_churn',
                         color_discrete_sequence=['#FFA15A', '#19d3f3'])
    st.plotly_chart(fig_delivery, use_container_width=True)

with chart_col4:
    fig_hist = px.histogram(df, x='days_inactive', nbins=20,
                            title="Distribution of Days Inactive among Users",
                            color_discrete_sequence=['#FF6692'])
    st.plotly_chart(fig_hist, use_container_width=True)