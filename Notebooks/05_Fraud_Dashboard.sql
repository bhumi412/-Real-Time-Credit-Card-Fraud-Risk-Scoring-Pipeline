-- Databricks notebook source
-- MAGIC %md
-- MAGIC ## Dashboard Metric 1: Total Transactions
-- MAGIC
-- MAGIC This metric shows the total number of transactions processed through the fraud detection pipeline.

-- COMMAND ----------

SELECT 
    COUNT(*) AS total_transactions
FROM workspace.fraud_db.gold_fraud_alerts;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Dashboard Metric 2: High Risk Transactions

-- COMMAND ----------

SELECT
    COUNT(*) AS high_risk_transactions
FROM workspace.fraud_db.gold_fraud_alerts
WHERE risk_level = 'HIGH';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Dashboard Metric 3: Risk Level Distribution

-- COMMAND ----------

SELECT
    risk_level,
    COUNT(*) AS transaction_count
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY risk_level
ORDER BY transaction_count DESC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Dashboard Metric 4: Top Risky Customers

-- COMMAND ----------

SELECT
    customer_id,
    total_transactions,
    high_risk_transactions,
    average_transaction_amount
FROM workspace.fraud_db.gold_customer_risk_profile
ORDER BY high_risk_transactions DESC
LIMIT 10;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Dashboard Metric 5: Location-wise Fraud Analysis

-- COMMAND ----------

SELECT
    location,
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN risk_level = 'HIGH' THEN 1 ELSE 0 END) AS high_risk_transactions
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY location
ORDER BY high_risk_transactions DESC
LIMIT 10;