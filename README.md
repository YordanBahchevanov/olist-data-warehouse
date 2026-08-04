# Olist Data Warehouse | PostgreSQL Data Engineering Project

## Overview

This project is an end-to-end Data Engineering portfolio project that demonstrates how to build a modern Data Warehouse using PostgreSQL, Docker, Python, and SQL.

The project is based on the **Brazilian Olist E-Commerce Dataset** from Kaggle, but extends it by simulating real-world data quality issues before loading the data into a multi-layer Data Warehouse.

The objective is not only to build a Data Warehouse, but also to demonstrate data ingestion, data quality management, ETL development, and analytical modeling using a Bronze → Silver → Gold architecture.

---

# Project Architecture

```
Kaggle Olist Dataset
        │
        ▼
 Original CSV Files
        │
        ▼
 Python Dirty Data Generator
        │
        ▼
   Messy CSV Files
        │
        ▼
 Python ETL Loader
        │
        ▼
 PostgreSQL Data Warehouse
        │
 ┌──────┼──────┐
 │      │      │
 ▼      ▼      ▼
Bronze Silver Gold
        │
        ▼
     Power BI
```

---

# Technologies

* PostgreSQL 16
* pgAdmin 4
* Docker & Docker Compose
* Python 3.12
* Pandas
* NumPy
* SQL
* Git & GitHub
* Power BI
* Draw.io

---

# Data Source

Dataset:

**Brazilian Olist E-Commerce Dataset**

The original dataset contains information about:

* Customers
* Orders
* Order Items
* Payments
* Products
* Sellers
* Reviews
* Geolocation
* Product Categories

---

# Project Structure

```
olist-data-warehouse/
│
├── datasets/
│   ├── original/
│   └── messy/
│
├── docs/
│
├── powerbi/
│
├── scripts/
│   ├── config.py
│   ├── dirty_data.py
│   ├── logger.py
│   ├── make_data_messy.py
│   └── utils.py
│
├── sql/
│   ├── init/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

# Data Warehouse Architecture

## Bronze Layer

Stores raw imported data exactly as received.

Characteristics:

* No business transformations
* Minimal validation
* Historical copy of the source data

---

## Silver Layer

Stores cleaned and standardized data.

Typical operations:

* Remove duplicates
* Handle missing values
* Standardize text
* Correct data quality issues
* Validate dates
* Apply business rules

---

## Gold Layer

Business-ready analytical model.

Contains:

* Fact tables
* Dimension tables
* Star Schema
* Reporting objects
* KPI calculations

---

# Data Quality Simulation

Unlike the original dataset, this project intentionally introduces realistic data quality problems before ingestion.

Current issues include:

* Missing values
* Duplicate rows
* Extra whitespace
* Uppercase inconsistencies
* Negative numeric values
* Invalid chronological dates
* Future dates
* Missing delivery dates
* Unrealistic delivery durations

The purpose is to simulate production ETL scenarios where incoming data is rarely perfect.

---

# Docker Environment

The project runs entirely inside Docker.

Services:

* PostgreSQL
* pgAdmin

Database initialization is automated using PostgreSQL initialization scripts located in:

```
sql/init/
```

Schemas are automatically created during the first database initialization.

---

# Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/YordanBahchevanov/olist-data-warehouse.git
cd olist-data-warehouse
```

---

## 2. Create the environment file

Copy the example configuration:

```bash
cp .env.example .env
```

Edit the values if necessary.

---

## 3. Start Docker

```bash
docker compose up -d
```

Docker will automatically:

* create the PostgreSQL database
* execute initialization scripts
* create Bronze, Silver and Gold schemas

---

## 4. Open pgAdmin

```
http://localhost:5050
```

Login using the credentials from your `.env` file.

---

## 5. Register PostgreSQL Server

Connection settings:

Host

```
postgres
```

Port

```
5432
```

Database

```
olist_dwh
```

Username

```
<POSTGRES_USER>
```

Password

```
<POSTGRES_PASSWORD>
```

---

# ETL Workflow

1. Download original dataset
2. Generate messy dataset
3. Load raw data into Bronze
4. Clean and standardize in Silver
5. Build analytical model in Gold
6. Create Power BI dashboards

---

# Future Improvements

* Automated ETL pipeline
* Incremental loading
* Data validation framework
* Logging and monitoring
* Unit tests
* Airflow orchestration
* CI/CD with GitHub Actions
* Data quality reports
* dbt transformations

---

# Learning Goals

This project demonstrates practical experience with:

* Docker
* PostgreSQL
* SQL
* Python
* ETL Development
* Data Cleaning
* Data Warehouse Design
* Star Schema Modeling
* Git
* GitHub
* Power BI

---

# License

This project is intended for educational and portfolio purposes.

The original Olist dataset belongs to its respective authors and is publicly available on Kaggle.
