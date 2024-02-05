from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

default_args = {"owner": "juan", "retries": 5, "start_date": timedelta(minutes=2)}

with DAG(
    dag_id="our_first_dag_v3",
    description="This is my first BashOperator",
    start_date=datetime(2023, 12, 28, 2),
    schedule_interval="@daily",
) as dag:
    task1 = BashOperator(task_id="print_hello", bash_command='echo "Hello World!"')

    task2 = BashOperator(
        task_id="sleep",
        bash_command="echo hey, I am task two and will running after you",
    )
    task3 = BashOperator(
        task_id="fail",
        bash_command="echo hey, I am task three and will running after task 2,so I am exhausted",
    )

    task1 >> task2
    task1 >> task3

    # Creating a Dummy Operator to use as a parent task for other tasks
    dummy_task = DummyOperator(task_id="dummy_task")

    # Using the bitwise operator to set the order of execution for tasks
    dummy_task >> task1
