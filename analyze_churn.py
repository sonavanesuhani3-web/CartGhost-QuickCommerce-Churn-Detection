import pandas as pd
from datetime import datetime

# 1. Dataset load karne
df = pd.read_csv('cartghost_orders.csv')

# Timestamp column la datetime format madhe convert karne
df['order_timestamp'] = pd.to_datetime(df['order_timestamp'])

print("--- Dataset Summary ---")
print(f"Total Orders: {len(df)}")
print(f"Total Unique Users: {df['user_id'].nunique()}")

# 2. Pratyek user cha saglyat latest (last) order date shodhne
user_summary = df.groupby('user_id').agg(
    last_order_date=('order_timestamp', 'max'),
    total_orders=('order_id', 'count'),
    total_spend=('order_amount', 'sum'),
    avg_delivery_time=('delivery_time_mins', 'mean')
).reset_index()

# 3. Dataset madhli maximum date mhanun reference date ghene
reference_date = df['order_timestamp'].max()
print(f"Reference Date for Analysis: {reference_date.strftime('%Y-%m-%d')}")

# 4. Inactivity (Days since last order) calculate karne
user_summary['days_inactive'] = (reference_date - user_summary['last_order_date']).dt.days

# 5. Silent Churn Threshold: 45 divasapeksha jast inactiveness
churn_threshold = 45
user_summary['is_silent_churn'] = user_summary['days_inactive'] > churn_threshold

# 6. Results Terminal var dakhvane
churn_counts = user_summary['is_silent_churn'].value_counts()
print("\n--- Silent Churn Analysis Results ---")
print(f"Active Users (<= 45 days): {churn_counts.get(False, 0)}")
print(f"Silent Churn Users (> 45 days): {churn_counts.get(True, 0)}")

# 7. Analysis-ready summary file save karne
user_summary.to_csv('user_churn_summary.csv', index=False)
print("\nUser churn summary successfully saved as 'user_churn_summary.csv'!")