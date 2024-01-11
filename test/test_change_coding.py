import pandas as pd
import pytest
from ml.load import carga
from ml.change_future import cambiar_dato
from ml.columns import eliminar_columnas

def test_cambiar_dato():
    try:
        
        # Cargar datos en un DataFrame utilizando la función carga del archivo load.py
        df = carga('titanic.csv')
        df_modificado = eliminar_columnas(df)
        resultado = cambiar_dato(df_modificado)
        assert isinstance(resultado, pd.DataFrame)
        assert not resultado.empty
        assert not resultado['Age'].isnull().any()

    except Exception as e:
        pytest.fail(f"Error en la prueba: {e}")
