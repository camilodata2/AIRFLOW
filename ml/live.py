import pandas as pd
from load import carga
from columns import eliminar_columnas

def sobrevivientes(df:pd.DataFrame) -> pd.DataFrame:
    mujeres_sobrevivientes = df.loc[(df['Sex'] == 'female') & (df['Survived'] == 1)].shape[0]
    hombres_sobrevivientes=df.loc[(df['Sex']=='male') & (df['Survived']==0)].shape[0]
    if mujeres_sobrevivientes > 0 and hombres_sobrevivientes > 0:
        return { 
            f'La cantidad de mujeres sobrevivientes es: {round(mujeres_sobrevivientes)}',
            f'la porsion de hombre sobreviventes son: {round(hombres_sobrevivientes)}'
        }
    else:
        return 'No sobrevivió ninguna mujer'

# Cargar datos en un DataFrame utilizando la función carga del archivo load.py
df = carga('titanic.csv')

# Obtener el DataFrame modificado eliminando columnas
df_modificado = eliminar_columnas(df)

# Usar el DataFrame modificado en la función sobrevivientes
resultado_sobrevivientes = sobrevivientes(df_modificado)
print(resultado_sobrevivientes)
