from airflow import DAG 
from datetime import timedelta , datetime
from airflow.operators.python import PythonOperator
from ml.src_model import dt_model
from ml.src1_model import rf_model
from ml.load import carga
from ml.model_compare import compare_model
default_args={
    'owener':'camilo',
    'depends_on_past':'False',
    'start_date':timedelta(minutes=5),
    }
with DAG (
    dag_id='ml_dag',
    defautl_args=defautl_args,
    schedule_interval= '@daily',
    start_date=datetime(2015,8,9),
    catchup=False,
    description='This Machine Learning dag'
) as dag:
  task1 = PythonOperator(
      task_id='data_load',
      python_callable= carga,
  
  )
  task2 = PythonOperator(
      task_id='data_tree_model',
      python_callable=dt_model,
  )
  task3= PythonOperator(
      task3='data_rando_forest_model',
      python_callable=rf_model,
  )
  task4 = PythonOperator(
      task_id = 'compare_models',
      python_callable=compare_model
  )
#los tasks se ejecutan en el orden que los definimos
task1 >> [task2,task3] >> task4


