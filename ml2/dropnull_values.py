import pandas as pd
from load_file import df1  # Asegúrate de tener cargado tu DataFrame

def eliminar_valores_faltantes(df1: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina filas con valores faltantes en un DataFrame.

    Args:
        df1 (pd.DataFrame): DataFrame a limpiar.

    Returns:
        pd.DataFrame: DataFrame sin filas que contengan valores faltantes.
    """
    try:
        df1_cleaned = df1.dropna(subset=['workclass', 'occupation', 'native.country'])
        return df1_cleaned
    except Exception as e:
        return f'Hubo un error: {str(e)}'

df11_sin_faltantes = eliminar_valores_faltantes(df1)
