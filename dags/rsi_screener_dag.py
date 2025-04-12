from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import pendulum

# Set timezone to CST (America/Chicago)
local_tz = pendulum.timezone("America/Chicago")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="rsi_screener_email_dag",
    default_args=default_args,
    description="Run RSI screener and email report daily",
    schedule_interval="0 9 * * 1-5",  # Mon–Fri at 9:00AM CST
    start_date=datetime(2025, 4, 11, tzinfo=local_tz),
    catchup=False,
    tags=["rsi", "email", "finance"],
) as dag:

    run_script = BashOperator(
        task_id="run_rsi_script",
        bash_command="/usr/local/bin/python3.11 /Users/ajaymangla/airflow/scripts/rsi_screener_email.py"
    )
