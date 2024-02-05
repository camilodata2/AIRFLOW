from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {"owner": "juan", "retries": 5, "retry_delay": timedelta(minutes=5)}


# Define Python functions to be executed by operators
def greet():
    print("Hello World!")


def say_hello():
    print("Saying hello!")


def say_goodbye():
    print("Saying goodbye!")


# Define the DAG
with DAG(
    default_args=default_args,
    dag_id="our_first_pythonOperator",
    description="Awesome pythonOperator",
    start_date=datetime(2021, 10, 6),
    schedule_interval="@daily",
) as dag:
    # Define the PythonOperator tasks
    task_greet = PythonOperator(task_id="Greet", python_callable=greet)

    task_say_hello = PythonOperator(task_id="Say_Hello", python_callable=say_hello)

    task_say_goodbye = PythonOperator(
        task_id="Say_Goodbye", python_callable=say_goodbye
    )

    # Define the task dependencies using '>>'
    task_greet >> task_say_hello >> task_say_goodbye
