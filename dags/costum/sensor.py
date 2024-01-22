from airflow.sensors.base import BaseSensorOperator
from airflow.utils.decorators import apply_defaults
from airflow.providers.postgres.hooks.postgres import PostgresHook 
class AvailableDataSensor(BaseSensorOperator):
    def __init__(self, redshift_conn_id:str,start_date="{{ds}}",end_date="{{nex_ds}}",**kwargs):
        super.__init__(**kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.start_date=start_date
        self.end_date=end_date
        @apply_defaults
        def poke(self,context) -> None:
            hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
            try:
                next(
                    hook.get_rating(
                        start_date=self.start_date,
                        end_date=self.end_date,
                        batch_size=1
                    )
                )
                self.log.info(
                    "Data available for the date range %s to %s",
                    self.start_date,
                    self.end_date)
                return True
            except StopIteration:
                self.log.warning("No data found for the date range %s to %s ",
                self.start_date,
                self.end_date)
                return False
            finally:
                # Close connection if it was opened by this operator
                hook.close()

                


          