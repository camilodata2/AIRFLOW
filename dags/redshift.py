from dags.custom import RedshiftOperator
from datetime import timedelta, datetime
from airflow.decorators import dag, task
from airflow.utils.edgemodifier import Label

default_args = {
    'owner': 'Camilo',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=3),
}

@dag(
    default_args=default_args,
    schedule_interval='0 * * * *',
    start_date=datetime(2019, 8, 6),
    catchup=False,
)
def Redshift_Copy_Operator(task_id: str) -> None:
    @task(task_id=task_id, labels=['Tarea de copia de archivos a RedShift'])
    def copy_files_to_redshift():
        return RedshiftOperator(
            task_id='copy_to_redshift_op',
            table_name='mytable',
            s3_bucket='s3://mybucket',
            s3_key='{{ execution_date.strftime("%Y/%m/%d") }}/mytable_0001.avro.gz',
            redshift_conn_id='redshift_default',
            pre_sql='TRUNCATE mytable;'
        )

    s3_to_redshift = copy_files_to_redshift()
    Label('s3_to_reshift')