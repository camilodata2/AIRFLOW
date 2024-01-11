import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
import missingno as msno
from load_file import df1

def tercer_grafico(df1: pd.DataFrame, save_path:str) -> msno.matrix:
    try:
        fig=plt.figure(figsize=(4,4))
        grafico=msno.matrix(df1)
        plt.savefig(save_path)
        plt.close()
        print(f"Heatmap saved at: {save_path}") 
    except Exception as e:
        print(f"No se ha podido graficar: {str(e)}")
# aca vamos a llamar a la funcio
save_path='matrix.png'
tercer_grafico(df1,save_path)


