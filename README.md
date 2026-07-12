# Real-Time Credit Card Fraud Risk Scoring Pipeline

## Overview

This project implements an end-to-end credit card fraud risk scoring pipeline using Databricks, Apache Spark, and Delta Lake.

The pipeline follows the Medallion Architecture approach (Bronze, Silver, and Gold layers) to ingest raw transaction data, clean and transform data, generate fraud risk scores, and create analytical datasets for fraud monitoring.

---

## Architecture

```
Raw Transaction Data
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

## Technologies Used

- Databricks
- Apache Spark (PySpark)
- Delta Lake
- SQL
- Unity Catalog
- GitHub

---

## Project Structure

```
Credit-Card-Fraud-Risk-Scoring-Pipeline

│
├── notebooks
│
├── data
│
├── results
│
└── README.md
```

### Folder Description

**notebooks**
- Contains Databricks notebooks and SQL scripts used for data ingestion, transformation, fraud detection, and analysis.

**data**
- Contains raw input datasets used for the fraud detection pipeline.

**results**
- Contains output screenshots, analysis results, and dashboard visualizations.

**README.md**
- Contains project documentation and implementation details.

---

## Data Pipeline

### Bronze Layer

The Bronze layer is responsible for ingesting raw transaction data and storing it in Delta Lake format.

Operations performed:
- Load raw CSV transaction data
- Validate schema
- Add metadata columns
- Create Bronze Delta table

---

### Silver Layer

The Silver layer performs data cleaning and transformation to prepare analytics-ready data.

Operations performed:
- Remove duplicate records
- Handle missing values
- Join transaction data with customer profile information
- Perform data transformations

---

### Gold Layer

The Gold layer creates business-ready datasets for fraud analysis.

Operations performed:
- Calculate fraud scores
- Generate risk categories
- Create customer risk profiles
- Prepare analytical tables

Gold datasets:
- Fraud Alerts
- Customer Risk Profile

---

## SQL Analysis

SQL queries are used to generate insights from Gold layer data.

Analysis includes:

- Fraud distribution by risk level
- High-value suspicious transactions
- Top fraud merchants
- Customer risk analysis
- Fraud trends

---

## Dashboard

A fraud monitoring dashboard is created using Gold layer datasets.

Dashboard visualizations include:

- Fraud alerts distribution by risk level
- Fraud amount analysis
- Top fraud merchants
- Customer risk profile
- Fraud trends over time

---

## Key Features

- End-to-end Data Engineering pipeline
- Medallion Architecture implementation
- Delta Lake based data storage
- Spark-based data processing
- Fraud risk scoring logic
- Analytics-ready datasets

---

## Results

The pipeline successfully transforms raw transaction data into structured datasets for fraud detection analysis and visualization.

Dashboard screenshots and output results are available in the results folder.

---

## Future Improvements

- Implement real-time streaming ingestion
- Add machine learning based fraud prediction
- Integrate advanced BI tools
- Add automated data quality monitoring

---

## Author

Bhumika Maheshwari
