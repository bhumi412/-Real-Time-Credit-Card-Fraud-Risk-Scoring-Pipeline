-- Databricks notebook source
-- MAGIC %md
-- MAGIC # SQL Fraud Analysis
-- MAGIC
-- MAGIC This notebook performs SQL-based analysis on Gold layer tables.
-- MAGIC
-- MAGIC The objective is to generate business insights from fraud detection results.
-- MAGIC
-- MAGIC Analysis includes:
-- MAGIC - High-risk transaction identification
-- MAGIC - Customer risk analysis
-- MAGIC - Fraud pattern exploration
-- MAGIC - Business reporting metrics

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Query 1: Identify High Risk Transactions

-- COMMAND ----------

SELECT 
    transaction_id,
    customer_id,
    amount,
    risk_score,
    risk_level,
    location
FROM workspace.fraud_db.gold_fraud_alerts
WHERE risk_level = 'HIGH';

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Query 2: Identify High Risk Customers

-- COMMAND ----------

SELECT
    customer_id,
    total_transactions,
    average_transaction_amount,
    high_risk_transactions
FROM workspace.fraud_db.gold_customer_risk_profile
ORDER BY high_risk_transactions DESC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Query 3: Risk Level Distribution

-- COMMAND ----------

SELECT
    risk_level,
    COUNT(*) AS transaction_count
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY risk_level
ORDER BY transaction_count DESC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Query 4: Location-wise Fraud Analysis

-- COMMAND ----------

SELECT
    location,
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN risk_level = 'HIGH' THEN 1 ELSE 0 END) AS high_risk_transactions
FROM workspace.fraud_db.gold_fraud_alerts
GROUP BY location
ORDER BY high_risk_transactions DESC;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Query 5: High Value Suspicious Transactions

-- COMMAND ----------

SELECT
    transaction_id,
    customer_id,
    amount,
    location,
    risk_score,
    risk_level
FROM workspace.fraud_db.gold_fraud_alerts
WHERE risk_level IN ('HIGH', 'MEDIUM')
ORDER BY amount DESC
LIMIT 10;