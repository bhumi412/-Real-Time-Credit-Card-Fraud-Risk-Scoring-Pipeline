-- Databricks notebook source
-- Fraud alerts analysis by risk level

SELECT
    risk_level,
    COUNT(*) AS total_alerts,
    SUM(amount) AS total_fraud_amount
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY risk_level;

-- COMMAND ----------

-- Top high amount suspicious transactions

SELECT
    transaction_id,
    customer_id,
    merchant,
    amount,
    risk_level
FROM workspace.fraud_db.gold_fraud_alerts
ORDER BY amount DESC
LIMIT 10;

-- COMMAND ----------

-- Identify merchants with highest fraud activity

SELECT
    merchant,
    COUNT(*) AS fraud_transactions,
    SUM(amount) AS total_amount
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY merchant
ORDER BY total_amount DESC;

-- COMMAND ----------

-- Customer wise risk analysis

SELECT
    customer_risk_category,
    COUNT(*) AS customers,
    AVG(total_spend) AS avg_spend
FROM workspace.fraud_db.gold_customer_risk_profile
GROUP BY customer_risk_category;

-- COMMAND ----------

-- Fraud distribution by location

SELECT
    location,
    COUNT(*) AS fraud_count,
    SUM(amount) AS fraud_amount
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY location
ORDER BY fraud_amount DESC;