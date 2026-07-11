# Databricks notebook source
# MAGIC %md
# MAGIC # Silver Layer - Data Cleaning and Transformation
# MAGIC
# MAGIC This notebook performs data cleaning and transformation on the Bronze Delta table.
# MAGIC
# MAGIC The Silver layer improves data quality by:
# MAGIC - Removing duplicate records
# MAGIC - Handling missing values
# MAGIC - Validating data types
# MAGIC - Preparing clean data for business analysis

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: Read Bronze Delta Table
# MAGIC
# MAGIC In this step, we read the raw transaction data stored in the Bronze Delta layer.

# COMMAND ----------

silver_df = spark.read \
    .format("delta") \
    .table("workspace.fraud_db.bronze_transactions")

# COMMAND ----------

display(silver_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: Remove Duplicate Records
# MAGIC
# MAGIC Duplicate records can affect transaction analysis and fraud detection results.

# COMMAND ----------

silver_df = silver_df.dropDuplicates()

# COMMAND ----------

display(silver_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3: Handle Missing Values
# MAGIC
# MAGIC Missing values can impact data quality and downstream fraud analysis.

# COMMAND ----------

from pyspark.sql.functions import col, count, when

display(
    silver_df.select(
        [
            count(when(col(c).isNull(), c)).alias(c)
            for c in silver_df.columns
        ]
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4: Validate Data Types
# MAGIC
# MAGIC Correct data types are important for accurate calculations and analysis.

# COMMAND ----------

silver_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5: Write Data to Silver Delta Table
# MAGIC
# MAGIC In this step, the cleaned and validated transaction data is stored as a Silver Delta table.

# COMMAND ----------

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.fraud_db.silver_transactions")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6: Verify Silver Delta Table
# MAGIC
# MAGIC In this step, we validate the Silver Delta table after applying data cleaning and transformation rules.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.fraud_db.silver_transactions;