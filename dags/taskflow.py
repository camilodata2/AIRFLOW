from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.decorators import dag, task

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

@dag(
    default_args=default_args, 
    schedule_interval=None, 
    catchup=False,
    dag_id='complex_taskflow_example')
def complex_taskflow_dag():

    @task()
    def download_data():
        # Simular la descarga de datos
        print("Downloading data...")
        return True  # Simular que la descarga fue exitosa

    @task()
    def process_data(data):
        # Simular el procesamiento de datos
        print(f"Processing data: {data}")
        if data:
            return "processed"
        else:
            return "failed"

    @task()
    def notify_success():
        # Simular notificación en caso de éxito
        print("Data processing succeeded. Notifying...")

    @task()
    def notify_failure():
        # Simular notificación en caso de fallo
        print("Data processing failed. Notifying...")

    download_task = download_data()
    process_task = process_data(download_task.output)
    success_notification = notify_success()
    failure_notification = notify_failure()

    # Dependencias condicionales
    download_task >> process_task
    process_task >> [success_notification, failure_notification]

dag = complex_taskflow_dag()
