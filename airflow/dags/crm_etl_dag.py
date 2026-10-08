from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="crm_etl",
    start_date=datetime(2026, 10, 7),
    schedule=None,
    catchup=False,
    tags=["CRM", "ETL"],
) as dag:

    load_raw_data = BashOperator(
        task_id="load_to_ods",
        bash_command="python /usr/local/airflow/crm_etl/scripts/load_to_ods.py",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=(
            "cd /usr/local/airflow/crm_etl/crm_warehouse && "
            "dbt run --profiles-dir ."
        ),
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=(
            "cd /usr/local/airflow/crm_etl/crm_warehouse && "
            "dbt test --profiles-dir ."
        ),
    )

    load_raw_data >> dbt_run >> dbt_test