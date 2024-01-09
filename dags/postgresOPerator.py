from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'airflow',
    'start_date': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v3',
    description='This is my first PostgresOperator',
    start_date=datetime(2023, 12, 28, 2),
    schedule_interval='@daily'
) as dag:
    task1 = PostgresOperator(
        task_id="checking_connection",
        postgres_conn_id="my_db",
        sql="""CREATE TABLE IF NOT EXISTS hola(
               id serial PRIMARY KEY,
               name VARCHAR(45) NOT NULL,
               age INT CHECK(age > 18 AND age < 99))"""
    )
    
    task2 = PostgresOperator(
        task_id="insert_data",
        postgres_conn_id="my_db",
        sql="""INSERT INTO hola(name, age) VALUES('Juan', 28)"""
    )

    task3 = PostgresOperator(
        task_id="delete_data",
        postgres_conn_id="my_db",
        sql="""DELETE FROM hola WHERE name = 'Juan'"""
    )

    task1 >> task2 >> task3
