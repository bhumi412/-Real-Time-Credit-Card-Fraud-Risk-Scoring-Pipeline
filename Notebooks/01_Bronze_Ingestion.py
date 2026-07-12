# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze Layer - Raw Data Ingestion
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC The objective of the Bronze layer is to ingest raw transaction data from the source system and store it in Delta Lake format without applying major transformations.
# MAGIC
# MAGIC ## Overview
# MAGIC
# MAGIC In this layer:
# MAGIC - Raw transaction data is loaded from CSV files
# MAGIC - Basic schema inference is performed
# MAGIC - Metadata columns are added for data tracking
# MAGIC - Data is stored as a Bronze Delta Table

# COMMAND ----------

spark.sql("""
CREATE SCHEMA IF NOT EXISTS workspace.fraud_db
""")

# COMMAND ----------

# Read raw transaction data

transaction_df = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/workspace/default/fraud_data/raw_transactions/transaction.csv")

transaction_df.printSchema()

# COMMAND ----------

display(transaction_df)

# COMMAND ----------

from pyspark.sql.functions import *

bronze_df = transaction_df \
    .withColumn("ingest_timestamp", current_timestamp()) \
    .withColumn("source_file", lit("transaction.csv"))

bronze_df.printSchema()

# COMMAND ----------

bronze_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.fraud_db.bronze_transactions")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.fraud_db.bronze_transactions;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE workspace.fraud_db.bronze_transactions;