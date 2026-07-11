# Credit Card Fraud Detection Data Pipeline using Databricks

## Project Overview

This project implements an end-to-end data engineering pipeline for detecting suspicious credit card transactions using Databricks, PySpark, and Delta Lake.

The pipeline follows the Medallion Architecture approach:
- Bronze Layer for raw data ingestion
- Silver Layer for data cleaning and transformation
- Gold Layer for fraud detection analytics and business insights

---

## Architecture

CSV Files  
↓  
Bronze Layer  
↓  
Silver Layer  
↓  
Gold Layer  
↓  
SQL Analysis & Dashboard

---

## Technologies Used

- Databricks
- Apache Spark
- PySpark
- Delta Lake
- SQL
- Unity Catalog

---

## Medallion Architecture Implementation

### Bronze Layer

Purpose:
- Store raw transaction data
- Preserve original data
- Add ingestion metadata

Table:

`workspace.fraud_db.bronze_transactions`

Features:
- Raw data ingestion
- Source tracking
- Batch identification

---

### Silver Layer

Purpose:
- Improve data quality
- Clean and validate data

Transformations:
- Duplicate removal
- Null value validation
- Data type validation

Table:

`workspace.fraud_db.silver_transactions`

---

### Gold Layer

Purpose:
Create business-ready fraud analytics tables.

Tables:

`gold_fraud_alerts`

Contains:
- Transaction details
- Risk score
- Risk level


`gold_customer_risk_profile`

Contains:
- Customer transaction summary
- Average transaction amount
- High-risk transaction count

---

## Fraud Detection Logic

Risk Score Rules:

| Condition | Risk Score | Risk Level |
|---|---|---|
| Amount > 50000 | 90 | HIGH |
| Amount > 10000 | 50 | MEDIUM |
| Otherwise | 10 | LOW |

---

## SQL Analysis

Implemented analysis:

- High-risk transaction identification
- Top risky customers
- Risk distribution analysis
- Location-wise fraud analysis
- High-value suspicious transactions

---

## Dashboard Insights

Dashboard provides:

- Total transaction count
- High-risk transaction count
- Risk category distribution
- Customer risk analysis
- Location-based fraud patterns

---

## Project Workflow

1. Ingest raw CSV files into Bronze layer
2. Clean and validate data in Silver layer
3. Apply fraud detection rules in Gold layer
4. Generate SQL-based business insights
5. Create dashboard visualizations

---

## Author

Bhumika Maheshwari
