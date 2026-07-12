# Project Documentation

# Real-Time Credit Card Fraud Risk Scoring Pipeline

## 1. Project Overview

This project implements an end-to-end credit card fraud risk scoring pipeline using Databricks, Apache Spark, Delta Lake, and SQL.

The main objective of this project is to build a scalable data engineering pipeline that processes raw transaction data, performs data cleaning and transformation, identifies suspicious transactions, generates risk categories, and provides analytical insights through SQL analysis and dashboards.

The project follows the Medallion Architecture approach consisting of Bronze, Silver, and Gold layers.

---

# 2. Problem Statement

Financial institutions process a large number of transactions every day. Detecting suspicious transactions manually is difficult and time-consuming.

This project aims to create a data pipeline that:

- Ingests raw transaction data
- Cleans and transforms data
- Generates fraud risk scores
- Categorizes transactions based on risk levels
- Creates customer risk profiles
- Provides visualization and analytical insights

---

# 3. Technologies Used

| Technology | Purpose |
|------------|---------|
| Databricks | Cloud data processing platform |
| Apache Spark | Distributed data processing |
| PySpark | Data transformation and processing |
| Delta Lake | Reliable data storage |
| SQL | Data analysis and reporting |
| Unity Catalog | Data governance |
| GitHub | Version control and documentation |

---

# 4. Project Architecture

The project follows the Medallion Architecture:

```
Raw CSV Data
      |
      ↓
Bronze Layer
(Data Ingestion)
      |
      ↓
Silver Layer
(Data Cleaning & Transformation)
      |
      ↓
Gold Layer
(Fraud Detection & Analytics)
      |
      ↓
SQL Analysis & Dashboard
```

---

# 5. Implementation Details

## 5.1 Bronze Layer

## Objective

The Bronze layer is responsible for ingesting raw transaction data and storing it in Delta format.

## Work Implemented

- Loaded raw CSV transaction data into Databricks
- Created Spark DataFrames
- Validated incoming schema
- Added metadata columns:
  - ingestion timestamp
  - source file name
- Stored raw data as Delta tables

## Output

Bronze Delta Table:

```
bronze_transactions
```

---

# 5.2 Silver Layer

## Objective

The Silver layer prepares clean and structured data for further analysis.

## Work Implemented

- Removed duplicate records
- Handled missing values
- Performed data cleaning
- Joined transaction data with customer profile information
- Created analytics-ready transaction data

## Output

Silver Delta Table:

```
silver_transactions
```

---

# 5.3 Gold Layer

## Objective

The Gold layer creates business-level datasets for fraud analysis.

## Work Implemented

- Generated fraud scores using rule-based logic
- Created transaction risk categories
- Prepared customer-level risk profiles
- Created analytical datasets for reporting

## Gold Tables

### Gold Fraud Alerts

Contains:

- Transaction details
- Fraud score
- Risk level
- Merchant information
- Transaction amount


### Gold Customer Risk Profile

Contains:

- Customer information
- Spending behavior
- Customer risk category

---

# 6. SQL Analysis

SQL queries were created to analyze fraud patterns.

Analysis performed:

- Fraud distribution by risk level
- Fraud amount analysis
- Top fraud merchants
- Customer risk analysis
- Fraud trends over time

---

# 7. Dashboard Implementation

A fraud monitoring dashboard was created using Gold layer data.

Dashboard visualizations include:

- Fraud alerts distribution by risk level
- Fraud amount by risk category
- Top fraud merchants
- Customer risk profile
- Fraud trend analysis

The dashboard helps understand fraud patterns and identify high-risk areas.

---

# 8. Challenges Faced During Development

## Challenge 1: Delta Metadata Mismatch

### Problem

While updating Delta tables, metadata mismatch errors occurred because previous table schemas were stored in Delta metadata.

### Solution

- Removed old Delta tables
- Cleared conflicting metadata
- Recreated tables with updated schemas

---

## Challenge 2: Incorrect Schema During Data Ingestion

### Problem

During ingestion, unwanted columns appeared due to schema inference and checkpoint history.

Example:

```
home_location
avg_spend_per_day
preferred_category
```

### Solution

- Removed incorrect checkpoint files
- Cleaned ingestion paths
- Used controlled schema validation

---

## Challenge 3: Customer Risk Category Imbalance

### Problem

Initially, all customers were classified into the same risk category.

### Cause

Risk classification was based on maximum fraud score, which caused customers with one risky transaction to be marked as high risk.

### Solution

Risk classification logic was reviewed and adjusted to create meaningful customer categories.

---

# 9. Scope Limitations (Not Implemented)

The following features were not included in this project:

## Real-Time Streaming Pipeline

A complete streaming architecture using Kafka or Azure Event Hub was not implemented.

## Machine Learning Fraud Prediction

The project uses rule-based fraud scoring.

A machine learning model for fraud prediction was not developed.

## External Data Sources

External banking APIs or real-time transaction sources were not integrated.

## Production Deployment

The project was developed and tested in Databricks but was not deployed as a production system.

---

# 10. Project Results

The project successfully achieved:

- End-to-end fraud data pipeline implementation
- Medallion Architecture implementation
- Delta Lake based data storage
- Data cleaning and transformation
- Fraud score generation
- Risk classification
- Customer risk profiling
- SQL-based fraud analysis
- Dashboard visualization

The final pipeline converts raw transaction data into structured datasets that provide meaningful fraud insights.

---

# 11. Future Enhancements

Future improvements can include:

- Real-time transaction streaming
- Machine learning based fraud detection
- Automated data quality monitoring
- Advanced feature engineering
- Integration with BI tools like Power BI/Tableau
- Production deployment with monitoring

---

# 12. Conclusion

This project demonstrates the development of a scalable data engineering pipeline for credit card fraud analysis using modern cloud data technologies.

By implementing Bronze, Silver, and Gold layers, the pipeline efficiently transforms raw transaction data into business-ready datasets and provides insights through SQL analysis and dashboards.

---

# Author

Bhumika Maheshwari
