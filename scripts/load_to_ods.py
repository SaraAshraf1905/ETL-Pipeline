import duckdb
from pathlib import Path


# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "raw"
DATABASE = PROJECT_DIR / "crm_warehouse" / "dev.duckdb"


# Connect to DuckDB
con = duckdb.connect(str(DATABASE))


# Create RAW schema
con.execute("CREATE SCHEMA IF NOT EXISTS raw")


# Load Accounts
con.execute(f"""
    CREATE OR REPLACE TABLE raw.accounts AS
    SELECT *
    FROM read_csv_auto('{DATA_DIR / "accounts.csv"}', header=True)
""")


# Load Products
con.execute(f"""
    CREATE OR REPLACE TABLE raw.products AS
    SELECT *
    FROM read_csv_auto('{DATA_DIR / "products.csv"}', header=True)
""")


# Load Sales Pipeline
con.execute(f"""
    CREATE OR REPLACE TABLE raw.sales_pipeline AS
    SELECT *
    FROM read_csv_auto('{DATA_DIR / "sales_pipeline.csv"}', header=True)
""")


# Load Sales Teams
con.execute(f"""
    CREATE OR REPLACE TABLE raw.sales_teams AS
    SELECT *
    FROM read_csv_auto('{DATA_DIR / "sales_teams.csv"}', header=True)
""")



print("Raw data loaded successfully!")

# Show the tables we created
tables = con.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'raw'
    ORDER BY table_name
""").fetchall()

print("\nRAW tables:")
for table in tables:
    print("-", table[0])


con.close()