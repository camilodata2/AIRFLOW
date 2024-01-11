import pandas as pd 
import numpy as np
def cargar_archivo(url:str) -> pd.DataFrame:
    try:
        data = pd.read_csv(url, delimiter=",")
        return data
    except Exception as e:
        return (f"los datos no se pudieron cargar: {data}",str(e))
df=cargar_archivo('adult.csv')
df1=df.replace('?',np.nan)
print(df1)

#print(df1['workclass'].isnull().sum())
#print(cargar_archivo('adult.csv').isin().sum())
#print(cargar_archivo('adult.csv').duplicated())
#print(cargar_archivo('adult.csv').shape)
