import pandas as pd
from load import carga

# Cargar datos en un DataFrame utilizando la función carga del archivo load.py
df = carga('titanic.csv')

# Definir la función para eliminar columnas
def eliminar_columnas(df:pd.DataFrame) -> pd.DataFrame:
    columnas_a_eliminar = ['Name', 'Ticket', 'Fare', 'Embarked', 'Cabin']
    df_sin_columnas = df.drop(columns=columnas_a_eliminar, errors='ignore')
    return df_sin_columnas

# Llamar a la función para eliminar las columnas
df_modificado = eliminar_columnas(df)
print(df_modificado.info())  # Mostrar las primeras filas del DataFrame modificado
