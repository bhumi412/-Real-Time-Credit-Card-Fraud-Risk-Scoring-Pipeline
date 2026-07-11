# Databricks notebook source
# MAGIC %md
# MAGIC # Gold Layer - Fraud Detection and Business Analytics
# MAGIC
# MAGIC This notebook creates business-ready tables from the Silver layer.
# MAGIC
# MAGIC The Gold layer applies fraud detection rules, calculates risk scores, and creates analytical tables for decision-making.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Read Silver Delta Table
# MAGIC
# MAGIC In this step, we read the cleaned transaction data from the Silver Delta layer.

# COMMAND ----------

gold_df = spark.read \
    .format("delta") \
    .table("workspace.fraud_db.silver_transactions")

# COMMAND ----------

display(gold_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Apply Fraud Detection Rules
# MAGIC
# MAGIC In this step, fraud detection rules are applied to identify suspicious transactions.

# COMMAND ----------

from pyspark.sql.functions import *

fraud_df = gold_df.withColumn(
    "risk_score",
    when(col("amount") > 50000, 90)
    .when(col("amount") > 10000, 50)
    .otherwise(10)
)

# COMMAND ----------

display(fraud_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Generate Risk Level
# MAGIC
# MAGIC In this step, the numeric risk score is converted into business-friendly risk categories.

# COMMAND ----------

fraud_df = fraud_df.withColumn(
    "risk_level",
    when(col("risk_score") >= 80, "HIGH")
    .when(col("risk_score") >= 40, "MEDIUM")
    .otherwise("LOW")
)

# COMMAND ----------

display(fraud_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: Create Gold Fraud Alert Table
# MAGIC
# MAGIC In this step, the fraud detection output is stored as a Gold Delta table.

# COMMAND ----------

fraud_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.fraud_db.gold_fraud_alerts")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5: Create Customer Risk Profile
# MAGIC
# MAGIC In this step, transaction-level fraud insights are aggregated at customer level.

# COMMAND ----------

from pyspark.sql.functions import *

customer_risk_df = fraud_df.groupBy("customer_id") \
    .agg(
        count("transaction_id").alias("total_transactions"),
        round(avg("amount"), 2).alias("average_transaction_amount"),
        sum(when(col("risk_level") == "HIGH", 1).otherwise(0)).alias("high_risk_transactions")
    )

# COMMAND ----------

display(customer_risk_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6: Create Gold Customer Risk Profile Table
# MAGIC
# MAGIC In this step, the customer-level risk analysis data is stored as a Gold Delta table.

# COMMAND ----------

customer_risk_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.fraud_db.gold_customer_risk_profile")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 7: Verify Gold Fraud Alert Table
# MAGIC
# MAGIC In this step, we validate the Gold fraud alert table to ensure that fraud detection results are successfully stored.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.fraud_db.gold_fraud_alerts;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 8: Verify Gold Customer Risk Profile Table
# MAGIC
# MAGIC In this step, we validate the customer-level risk analysis table.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.fraud_db.gold_customer_risk_profile;