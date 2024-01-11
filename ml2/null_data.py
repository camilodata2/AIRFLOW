import pandas as pd 
from load_file import df1
import numpy as np

def null_value(df: pd.DataFrame) -> pd.DataFrame:
    """
    
    """
    # Drop rows with any missing values
    try:
        valores=round((df1.isnull().sum() / df1.shape[0]) * 100, 2).astype(str) + ' %'
        return (f'porcentaje de elementons  Nan en: {valores}')
    except Exception as e:
        return (f'se ha producido un error en la carga del archivo:{valores}',str(e))
null_value(df1)