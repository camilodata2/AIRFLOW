#aca vamos hacer la carga del archivo
import pandas as pd

def carga(url:str) -> pd.DataFrame:
    """Cargar el archivo de datos"""
    try:
        df = pd.read_csv(url, delimiter=',')
        return df
    except FileNotFoundError:
        print("El archivo no se encuentra en la carpeta actual")

#print(carga('titanic.csv').head(5))
#carga('titanic.csv').info()
print(carga('titanic.csv').isnull())
