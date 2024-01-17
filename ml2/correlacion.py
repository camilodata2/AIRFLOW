import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt 
from valores_nulos import df1_sin_faltantes

def matrix_De_correlacion(df1_sin_faltantes: pd.DataFrame, save_path: str) -> sns.heatmap:
    """Genera y guarda un heatmap de la matriz de correlación.

    Args:
        df1 (pd.DataFrame): DataFrame con los datos.
        save_path (str): Ruta para guardar la imagen.
    """
    try:
        plt.figure(figsize=(8, 8))
        heatmap = sns.heatmap(df1_sin_faltantes.corr(), annot=True, fmt=".0%")
        plt.savefig(save_path)
        plt.close()
        print(f"Heatmap guardado en: {save_path}")
    except Exception as e:
        print(f'Error al generar el heatmap: {str(e)}')

save_path = 'corr.png'
matrix_De_correlacion(df1_sin_faltantes, save_path)
