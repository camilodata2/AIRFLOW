from airflow import DAG 
from airflow.sensors.python_sensor import PythonSensor
from datetime import datetime, timedelta

def load_file(file):
    """Print the content of a file."""
    with open(file) as f:
        print("Content of %s:"% file ,f.read())
default_args={
    'owner': 'airflow',
    'start_date': timedelta(minutes=2),
    }

with DAG (
    dag_id='pythonsensonr operator ',
    description='firsty pythonSenssor',
    start_date =datetime(2016,9,1),
    default_args=default_args,
    schedule_interval= '@daily',
    concurrency=20) as dag:
    ti =PythonSensor(
        task_id='sensor_file',
        python_callable=load_file,
        #poke_interval=20,
        mode="reschedule",
        op_kwargs={'file': 'ruta_de_archivo'},
        catchup=False,

    )

    ti


