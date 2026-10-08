# CRM Sales ETL Pipeline

A data engineering project that builds an ETL pipeline for CRM Sales Opportunities data.

## Technologies

- Python
- DuckDB
- dbt
- Apache Airflow
- Astro
- SQL

## Pipeline

CSV Files
↓
Python
↓
DuckDB Raw Layer
↓
dbt Staging
↓
dbt Dimensions and Fact
↓
dbt Tests

## Airflow

The Airflow DAG contains three tasks:

1. load_to_ods
2. dbt_run
3. dbt_test

The tasks run sequentially to load, transform, and validate the data.

## Data Model

### Dimensions

- dim_account
- dim_product
- dim_sales_teams

### Fact

- fact_sales_pipelines

## Project Structure

- `data/` - Source CSV files
- `scripts/` - Python loading scripts
- `crm_warehouse/` - dbt project
- `airflow/` - Airflow DAG and configuration
- `docs/` - Schemas and project documentation
