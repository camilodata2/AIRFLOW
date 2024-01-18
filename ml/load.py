#aca vamos hacer la carga del archivo
import pandas as pd
import pytest

def carga(url:str) -> pd.DataFrame:
    """Cargar el archivo de datos"""
    try:
        df = pd.read_csv(url, delimiter=',')
        return df
    except FileNotFoundError:
        print("El archivo no se encuentra")
        return pd.DataFrame()

       

#print(carga('titanic.csv').head(5))
#carga('titanic.csv').info()
#print(carga('titanic.csv'))
#assert isinstance(carga('titanic.csv'),pd.DataFrame)
