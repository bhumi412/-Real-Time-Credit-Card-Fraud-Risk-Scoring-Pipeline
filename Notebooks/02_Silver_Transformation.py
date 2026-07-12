# Databricks notebook source
# MAGIC %md
# MAGIC # Silver Layer - Data Transformation
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC The objective of the Silver layer is to clean, transform, and enrich Bronze data to make it ready for analytics and fraud detection.
# MAGIC
# MAGIC ## Operations Performed
# MAGIC
# MAGIC - Read Bronze Delta table
# MAGIC - Read customer profile data
# MAGIC - Perform data cleaning
# MAGIC - Handle missing values
# MAGIC - Remove duplicate records
# MAGIC - Join transaction data with customer information
# MAGIC - Store transformed data as Silver Delta Table

# COMMAND ----------

# Read Bronze Delta Table

bronze_df = spark.read \
    .format("delta") \
    .table("workspace.fraud_db.bronze_transactions")

bronze_df.show(5)

# COMMAND ----------

customer_df = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/workspace/default/fraud_data/raw_customer/customer_profile.csv")

customer_df.show(5)

# COMMAND ----------

# Join transaction data with customer profile

silver_df = bronze_df.join(
    customer_df,
    on="customer_id",
    how="left"
)

silver_df.show(5)

# COMMAND ----------

# Remove duplicate transactions

silver_df = silver_df.dropDuplicates(["transaction_id"])

silver_df.show(5)

# COMMAND ----------

# Handle missing values

silver_df = silver_df.fillna({
    "home_location": "Unknown",
    "preferred_category": "Unknown",
    "avg_spend_per_day": 0
})

silver_df.show(5)

# COMMAND ----------

# Check duplicate transaction IDs

silver_df.groupBy("transaction_id") \
    .count() \
    .filter("count > 1") \
    .show()

# COMMAND ----------

# Create Silver Delta Table

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.fraud_db.silver_transactions")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.fraud_db.silver_transactions
# MAGIC LIMIT 10;