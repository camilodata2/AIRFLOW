import pandas as pd
from estraer import extract


def transform():
    """aca vamos hacer el proceso de transformacion de datos"""
    try:
        # No sobrescribas el argumento de entrada, ya que se espera un DataFrame
        df = "Iris.csv"

        # Iterar sobre las columnas
        for column in df.columns:
            # Manejar los valores nulos en cada columna
            df[column].fillna(value=df[column].mean(), inplace=True)

        # Luego de manejar los valores nulos, realiza la ordenación por nombre
        df = df.sort_values(
            by="SepalLengthCm"
        )  # Reemplaza 'Nombre' con el nombre de la columna adecuada

        return df
    except Exception as e:
        # Manejo de excepciones
        return f"Error en la transformación: {str(e)}"


if __name__ == "__main__":
    print(transform())
