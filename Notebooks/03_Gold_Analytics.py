# Databricks notebook source
# MAGIC %md
# MAGIC # Gold Layer - Fraud Analytics
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC The objective of the Gold layer is to create business-ready analytical tables from Silver data for fraud detection and customer risk analysis.
# MAGIC
# MAGIC ## Overview
# MAGIC
# MAGIC In this layer:
# MAGIC - Silver transaction data is used as the input source
# MAGIC - Fraud risk score is calculated based on transaction behavior
# MAGIC - High-risk transactions are identified
# MAGIC - Customer-level risk profiles are generated
# MAGIC - Data is stored as Gold Delta Tables for analytics and reporting

# COMMAND ----------

# Read Silver transaction data

silver_df = spark.read \
    .format("delta") \
    .table("workspace.fraud_db.silver_transactions")

silver_df.show(5)

# COMMAND ----------

# Create fraud score

from pyspark.sql.functions import *

gold_df = silver_df.withColumn(
    "fraud_score",
    when(col("amount") > 20000, 90)
    .when(col("amount") > 10000, 70)
    .when(col("amount") > 5000, 50)
    .otherwise(20)
)

gold_df.show(5)

# COMMAND ----------

# Categorize fraud risk level

gold_alerts = gold_df.withColumn(
    "risk_level",
    when(col("fraud_score") >= 70, "High Risk")
    .when(col("fraud_score") >= 50, "Medium Risk")
    .otherwise("Low Risk")
)

gold_alerts.show(5)

# COMMAND ----------

# Create fraud alerts table

gold_fraud_alerts = gold_alerts.filter(
    col("risk_level") != "Low Risk"
)

gold_fraud_alerts.show(5)

# COMMAND ----------

# Save fraud alerts Gold table

gold_fraud_alerts.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.fraud_db.gold_fraud_alerts")

# COMMAND ----------

# Create customer risk profile

gold_customer_risk_profile = gold_alerts.groupBy("customer_id") \
    .agg(
        count("transaction_id").alias("total_transactions"),
        sum("amount").alias("total_spend"),
        avg("amount").alias("average_transaction_amount"),
        max("fraud_score").alias("max_fraud_score")
    )

gold_customer_risk_profile.show(5)

# COMMAND ----------

# Create customer risk category based on spending behavior

gold_customer_risk_profile = gold_customer_risk_profile.withColumn(
    "customer_risk_category",
    when(col("total_spend") > 50000, "High Risk")
    .when(col("total_spend") > 20000, "Medium Risk")
    .otherwise("Low Risk")
)

# COMMAND ----------

# Create fraud alerts table

gold_fraud_alerts = gold_alerts.filter(
    col("risk_level") != "Low Risk"
)

gold_fraud_alerts.show(5)

# COMMAND ----------

# Save fraud alerts Gold table

gold_fraud_alerts.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.fraud_db.gold_fraud_alerts")

# COMMAND ----------

# Save customer risk profile Gold table

gold_customer_risk_profile.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.fraud_db.gold_customer_risk_profile")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.fraud_db.gold_fraud_alerts
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.fraud_db.gold_customer_risk_profile
# MAGIC LIMIT 10;