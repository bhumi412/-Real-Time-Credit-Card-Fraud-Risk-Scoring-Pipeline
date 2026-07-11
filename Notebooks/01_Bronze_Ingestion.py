# Databricks notebook source
# MAGIC %md
# MAGIC # Real-Time Credit Card Fraud Detection Data Pipeline
# MAGIC
# MAGIC ## Bronze Layer - Raw Data Ingestion
# MAGIC
# MAGIC This notebook implements the Bronze layer of the fraud detection pipeline using Databricks, PySpark, and Delta Lake.
# MAGIC
# MAGIC The Bronze layer is responsible for ingesting raw transaction data and maintaining the original data along with ingestion metadata for audit and tracking purposes.
# MAGIC
# MAGIC ### Technologies Used:
# MAGIC - Databricks
# MAGIC - PySpark
# MAGIC - Delta Lake
# MAGIC - Unity Catalog Volumes

# COMMAND ----------

print("Fraud Detection Project Started")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Verify Input Files
# MAGIC
# MAGIC Checking whether source files are available in Unity Catalog Volume.

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/workspace/default/fraud_data"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Read Transaction Data
# MAGIC
# MAGIC In this step, we read the raw transaction CSV file using Spark DataFrame API.

# COMMAND ----------

transaction_df = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/workspace/default/fraud_data/transaction.csv")

# COMMAND ----------

display(transaction_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Schema Validation
# MAGIC
# MAGIC In this step, we check the schema of the transaction DataFrame.

# COMMAND ----------

transaction_df.printSchema()

# COMMAND ----------

from pyspark.sql.functions import *

bronze_df = transaction_df \
    .withColumn("ingest_timestamp", current_timestamp()) \
    .withColumn("source_file", lit("transaction.csv")) \
    .withColumn("batch_id", lit(1))

# COMMAND ----------

display(bronze_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: Add Ingestion Metadata
# MAGIC
# MAGIC Adding ingestion timestamp, source file name, and batch id to maintain data lineage and audit information in the Bronze layer.

# COMMAND ----------

from pyspark.sql.functions import *

bronze_df = transaction_df \
    .withColumn("ingest_timestamp", current_timestamp()) \
    .withColumn("source_file", lit("transaction.csv")) \
    .withColumn("batch_id", lit(1))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5.1: Create Database Schema
# MAGIC
# MAGIC Creating a schema to organize Delta tables for the fraud detection project.

# COMMAND ----------

spark.sql("""
CREATE SCHEMA IF NOT EXISTS workspace.fraud_db
""")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5.2: Write Data to Bronze Delta Table
# MAGIC
# MAGIC In this step, the raw transaction data along with ingestion metadata is stored as a Delta Lake table.

# COMMAND ----------

bronze_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.fraud_db.bronze_transactions")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6: Verify Bronze Delta Table
# MAGIC
# MAGIC In this step, we validate the Bronze Delta table by reading the stored data.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.fraud_db.bronze_transactions;