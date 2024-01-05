import pandas as pd

from load import carga
from columns import eliminar_columnas

def cambiar_dato(df: pd.DataFrame) -> pd.DataFrame:
    titanic = pd.get_dummies(df, columns=['Sex'], drop_first=True)
    
    # Convertir valores booleanos a enteros (0 o 1)
    titanic['Sex_male'] = titanic['Sex_male'].astype(int)
    titanic.rename(columns={'Sex_male': 'Sex'}, inplace=True)
    titanic = titanic.dropna(subset=['Age'])
    
    if titanic.empty or titanic['Age'].isnull().any():
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error
    else:
        return titanic


# Cargar datos en un DataFrame utilizando la función carga del archivo load.py
df = carga('titanic.csv')

# Obtener el DataFrame modificado eliminando columnas
df_modificado = eliminar_columnas(df)

cambiar = cambiar_dato(df_modificado)
print(cambiar.head(5))
