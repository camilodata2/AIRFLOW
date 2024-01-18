from airflow.hooks.base_hook import BaseHook 
import requests
import logging

# vamos a crear un costum hook, para hacer un sistema de recomendacion de alimentos

class FoodHook(BaseHook):
   DEFAULT_HOST = "movielens"
   DEFAULT_SCHEMA = "http"
   DEFAULT_PORT = 5000
   def __init__(self,conn_id):
    super().__init__()
    self._conn_id= conn_id # es como si fuera una variable de instancia

    def get_conn(self):
        try:
            config=self.get_connection(self._conn_id)
            schema=self.DEFAULT_SCHEMA
            port=self.DEFAULT_PORT
            host=self.DEFAULT_HOST
    
            base_url=f'{schema}://{host}:{port}'
            session=request.Session()

    
            if config.loging:
                session.auth= (config.login,config.password)
                print('la conexion fue exitosa')
        except Exception as e:
            print (f'no se pudo establecer conexion:{str(e)}')

            return session