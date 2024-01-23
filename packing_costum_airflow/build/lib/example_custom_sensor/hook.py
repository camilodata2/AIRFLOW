import os
import boto3
from airflow.hooks.base_hook import BaseHook

class RedshiftHook(BaseHook):
    def __init__(self, redshift_conn_id='redshift_default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.client = None

    def get_client(self):
        try:
            if self.client is not None:
                return self.client
                
                conn_params = self.get_connection(self.redshift_conn_id)
        
                aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID') or conn_params.login
                aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY') or conn_params.password

                self.client = boto3.client(
                    'redshift',
                    region_name=conn_params.extra_dejson.get('region_name', 'us-west-2'),
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                )
                return self.client
        except Exception as e:
            return f'we cant conect to Database:{str(e)}'

    def execute_query(self, query):

        client = self.get_client()
        response = client.execute_statement(
            ClusterIdentifier=conn_params.extra_dejson.get('cluster_identifier'),
            Database=conn_params.extra_dejson.get('dbname'),
            DbUser=conn_params.login,
            Sql=query,
        )
        return response

    def fetch_records(self, query):
        response = self.execute_query(query)
        return response.get('records', [])