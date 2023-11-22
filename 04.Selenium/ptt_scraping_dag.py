
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Including the path of the original script so it can be imported
# sys.path.append('/path/to/your/script')

# Importing the user's script
import ptt_selenium

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['willismax.com@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ptt_scraping_dag',
    default_args=default_args,
    description='A simple DAG to scrape PTT data',
    schedule=timedelta(minutes=5),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

def scrape_task():
    ptt_selenium.main() # Assuming the main functionality is in a function called 'main'

scrape = PythonOperator(
    task_id='scrape_ptt',
    python_callable=scrape_task,
    dag=dag,
)

scrape
