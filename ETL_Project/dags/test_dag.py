import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from ETL.load.load_to_mysql import load_data
from ETL.extract.extract_api import extract_data

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='bash_call_python_file',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    def extract_task(**kwargs):
        data = extract_data()
        kwargs['ti'].xcom_push(key='extracted_data', value=data)

    def load_task(**kwargs):
        data = kwargs['ti'].xcom_pull(key='extracted_data', task_ids='extract_task')
        if data:
            load_data(data)

    extarct = PythonOperator(
        task_id='extract_task',
        python_callable=extract_task,
        provide_context=True,
    )

    load = PythonOperator(
        task_id='load_task',
        python_callable=load_task,
        provide_context=True,
    )

    extarct >> load