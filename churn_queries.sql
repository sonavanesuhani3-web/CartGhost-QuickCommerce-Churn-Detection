-- 1. Total Active vs Silent Churned Customers Count
SELECT 
    is_churned,
    COUNT(user_id) AS total_users,
    ROUND(AVG(total_orders), 2) AS avg_orders_per_user,
    ROUND(AVG(total_spend), 2) AS avg_customer_spend
FROM user_churn_summary
GROUP BY is_churned;

-- 2. Top 10 High-Value Churned Customers (Priority Re-engagement List)
SELECT 
    user_id,
    days_since_last_order,
    total_orders,
    total_spend
FROM user_churn_summary
WHERE is_churned = 1
ORDER BY total_spend DESC
LIMIT 10;

-- 3. Churn Rate Percentage
SELECT 
    ROUND((COUNT(CASE WHEN is_churned = 1 THEN 1 END) * 100.0) / COUNT(*), 2) AS churn_rate_percentage
FROM user_churn_summary;