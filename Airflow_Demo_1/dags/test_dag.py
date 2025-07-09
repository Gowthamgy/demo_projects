from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

# Define DAG
with DAG(
    dag_id='hello_scrapy_pipeline',
    default_args=default_args,
    schedule_interval=None,  # Manual trigger or set cron as needed
    catchup=False,
    tags=['example'],
) as dag:

    # Task 1: Python print Hello
    def print_hello():
        print("Hello from Airflow! welcome to the world of data pipelines.")

    task_hello = PythonOperator(
        task_id='task_hello',
        python_callable=print_hello
    )

    # Task 2: Run Scrapy spider via bash command
    task_scrapy = BashOperator(
        task_id='task_scrapy',
        bash_command='cd /opt/airflow/works && export PYTHONPATH=$(pwd) && scrapy crawl test'
    )

    task_show = BashOperator(
        task_id='task_show',
        bash_command='cd /opt/airflow/tested && export PYTHONPATH=$(pwd) && python viewall_record.py'
    )

    task_top5_salary = BashOperator(
        task_id='task_top5_salary',
        bash_command='cd /opt/airflow/tested && export PYTHONPATH=$(pwd) && python high_salary.py'
    )

    # Task sequence: task_hello >> task_scrapy
    task_hello >> task_scrapy >> task_show >> task_top5_salary
