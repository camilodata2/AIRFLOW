from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from random import uniform


def training_model(ti):
    accuracy = uniform(0.1, 12.15)
    print(f"The model accuracy is: {accuracy}")
    ti.xcom_push(key="model accuracy", value=accuracy)


def choose_best_model(ti):
    accuracies = ti.xcom_pull(
        key="model accuracy",
        task_ids=["training_model_A", "training_model_B", "training_model_C"],
    )
    print(f"The accuracies are: {accuracies}")


default_args = {
    "owner": "airflow",
    "start_date": datetime(2015, 8, 2),
    "email": ["palvis253@gmail.com"],
}

with DAG(
    default_args=default_args,
    dag_id="our_first_xcom2",
    description="We are making an XCom and choosing the best ML model",
    start_date=datetime(2021, 10, 6),
    catchup=False,
    schedule_interval="@daily",
) as dag:
    downloading_data = BashOperator(
        task_id="downloading_data",
        bash_command='echo "Downloading Data"',
        do_xcom_push=False,
    )

    training_model_task = [
        PythonOperator(
            task_id=f"training_model_{i}",
            python_callable=training_model,
            provide_context=True,
            dag=dag,
        )
        for i in ["A", "B", "C"]
    ]

    choose_model = PythonOperator(
        task_id="choose_model",
        python_callable=choose_best_model,
        provide_context=True,
        dag=dag,
    )

    downloading_data >> training_model_task >> choose_model
