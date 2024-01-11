import pandas as pd
from load_file import df1
from sklearn.preprocessing import LabelEncoder

def eliminar_valores_faltantes(df1: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina filas con valores faltantes en un DataFrame y realiza Label Encoding.

    Args:
        df1 (pd.DataFrame): DataFrame a limpiar.

    Returns:
        pd.DataFrame: DataFrame sin filas que contengan valores faltantes y con Label Encoding aplicado.
    """
    try:
        columns_with_nan = ['workclass', 'occupation', 'native-country']

        # Eliminar filas con valores faltantes
        df1 = df1.dropna(subset=columns_with_nan)

        # Realizar Label Encoding para columnas 'object'
        le = LabelEncoder()
        for col in df1.columns:
            if df1[col].dtype == 'object':
                df1.loc[:,col] = le.fit_transform(df1[col])
                # La función .loc[] de pandas. Aquí, ':' se refiere a todas las filas del DataFrame,
                #  y col es el nombre de la columna que se va a modificar.

        return df1

    except Exception as e:
        return f'Hubo un error: {str(e)}'

df1_sin_faltantes = eliminar_valores_faltantes(df1)
#print(df1_sin_faltantes)
