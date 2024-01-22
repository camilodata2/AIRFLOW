from airflow.models.baseoperator import BaseOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook  # Import PostgresHook
from airflow.utils.decorators import apply_defaults

# Declare fields that can be templated
template_fields = ("pre_sql", "s3_bucket", "s3_key", "copy_options")
template_ext = (".hql", ".sql")

class RedshiftOperator(BaseOperator):  
    @apply_defaults
    def __init__(self, table_name: str, s3_bucket: str, s3_key: str, s3_credentials: str, redshift_conn_id: str,
                 copy_options=None, pre_sql=None, *args, **kwargs) -> None:  # Add default values
        super().__init__(*args, **kwargs)
        self.table_name = table_name  # Fix variable name
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.s3_credentials = s3_credentials
        self.redshift_conn_id = redshift_conn_id
        self.copy_options = copy_options  # Store copy_options
        self.pre_sql = pre_sql  # Store pre_sql

    def execute(self, context):
        try:
            self.redshift_hook = PostgresHook(postgres_conn_id=self._redshift_conn_id)  # Fix variable name

            copy_query = f"""
            COPY {self._table_name}
            FROM 's3://{self._s3_bucket}/{self._s3_key}'
            WITH CREDENTIALS '{self._s3_credentials}'
            {self._copy_options}
            """

            if self._pre_sql:
                self.log.info("Pre SQL: %s" % self._pre_sql)
                self.redshift_hook.run(self._pre_sql)

            self.log.info("Running Query: %s" % copy_query)
            self.redshift_hook.run(copy_query)  # Fix variable name

            print('Se ha realizado con éxito las operaciones requeridas')  # Fix print statement

        except Exception as e:
            self.log.error("Error al ejecutar la consulta: %s" % str(e))
            