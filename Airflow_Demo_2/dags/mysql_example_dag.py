import os
import sys
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from scrapy.utils.project import get_project_settings
from scrapy.spiderloader import SpiderLoader

# Allow Python to find your 'scraper' project
sys.path.append('/opt/airflow')

# Scrapy project root directory inside container
SCRAPY_PROJECT_PATH = '/opt/airflow/scraper'

# Point to Scrapy settings
os.environ['SCRAPY_SETTINGS_MODULE'] = 'scraper.settings'
settings = get_project_settings()

# Load all available spiders dynamically
loader = SpiderLoader(settings)
SPIDERS = loader.list()

print(f"Detected spiders: {SPIDERS}")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Create one DAG per spider dynamically
for spider_name in SPIDERS:

    with DAG(
        dag_id=f"scrapy_{spider_name}_dag",
        default_args=default_args,
        description=f"Run Scrapy Spider: {spider_name}",
        schedule_interval=None,  # Manual trigger; use cron if needed
        start_date=datetime(2024, 1, 1),
        catchup=False,
        tags=["scrapy"],
    ) as dag:

        crawl_task = BashOperator(
            task_id=f"crawl_{spider_name}",
            bash_command=(
                f"export PYTHONPATH=/opt/airflow && "
                f"cd {SCRAPY_PROJECT_PATH} && "
                f"scrapy crawl {spider_name}"
            ),
        )

        globals()[f"scrapy_{spider_name}_dag"] = dag
