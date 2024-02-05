from airflow import DAG
from airflow.sensors.python_sensor import PythonSensor
from datetime import datetime, timedelta
import os


def load_file(file_path):
    """Print the content of a file."""
    # with open(file) as f:
    #    print("Content of %s:"% file ,f.read())
    return True if os.path.exists(file_path) else False


default_args = {
    "owner": "airflow",
    "start_date": timedelta(minutes=2),
}

with DAG(
    dag_id="pythonsensonr operator ",
    description="firsty pythonSenssor",
    start_date=datetime(2016, 9, 1),
    default_args=default_args,
    schedule_interval="@daily",
    concurrency=20,
) as dag:
    ti = PythonSensor(
        task_id="sensor_file",
        python_callable=load_file,
        mode="reschedule",
        timeout=600,  # seconds
        poke_interval=60,  # seconds
        retries=3,
        op_kwargs={"file_path": "/home/camilo/airflow/adult.csv"},
        catchup=False,
    )

    ti
