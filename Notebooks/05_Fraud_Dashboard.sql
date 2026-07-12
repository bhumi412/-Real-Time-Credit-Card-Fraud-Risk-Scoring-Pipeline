-- Databricks notebook source
-- Fraud distribution by risk level

SELECT
    risk_level,
    COUNT(*) AS total_alerts
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY risk_level;

-- COMMAND ----------

-- Fraud amount analysis by risk level

SELECT
    risk_level,
    SUM(amount) AS total_fraud_amount
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY risk_level;

-- COMMAND ----------

-- Top merchants with fraud transactions

SELECT
    merchant,
    COUNT(*) AS fraud_count,
    SUM(amount) AS total_amount
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY merchant
ORDER BY fraud_count DESC
LIMIT 10;

-- COMMAND ----------

-- Customer risk category distribution
SELECT
    customer_risk_category,
    COUNT(*) AS customer_count
FROM workspace.fraud_db.gold_customer_risk_profile
GROUP BY customer_risk_category;

-- COMMAND ----------

-- Fraud trend based on transaction date

SELECT
    DATE(transaction_time) AS transaction_date,
    COUNT(*) AS fraud_count
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY DATE(transaction_time)
ORDER BY transaction_date;