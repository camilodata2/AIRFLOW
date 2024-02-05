from datetime import timedelta, datetime
from airflow.decorators import dag, task
from airflow.utils.edgemodifier import Label
from custom.sensor import AvailableDataSensor

default_args = {
    "owner": "Camilo",
    "depends_on_past": False,  # Cambié 'depends_on_false' a 'depends_on_past'
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


@dag(
    default_args=default_args,
    schedule_interval="*/10 * * * *",  # cada 10 minutos
    description="This helps us check available data on redshift",
    start_date=datetime(2021, 9, 7),
    tags=["check", "available"],
)
def check_available_data(task_id: str) -> None:
    @task(task_id=task_id)
    def _check() -> None:
        return AvailableDataSensor(
            task_id="available_data_on_redshift",
            start_date="{{ds}}",
            end_date="{{next_ds}}",
            redshift_conn_id="",  # Coloca aquí el ID de la conexión de Redshift
        )

    check_task = _check()  # Llamada a la función _check
    check_task.set_upstream(Label("Start"))  # Configuración de upstream
    check_task.set_downstream(Label("End"))  # Configuración de downstream
