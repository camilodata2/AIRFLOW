import pytest
import pandas as pd
from ml.load import carga

def test_ml_load():
    """Testa la funcion de carga del archivo csv"""
    try:
        df = carga('titanic.csv')
        assert isinstance(df, pd.DataFrame)
        assert not df.empty
    except Exception as e:
        pytest.fail(f"Error in load test: {e}")


    