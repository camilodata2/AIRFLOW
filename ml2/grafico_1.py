import pandas as pd
import matplotlib.pyplot as plt
from load_file import df1

def grafico_income(df: pd.DataFrame, save_path: str) -> plt.pie:
    """
    Create a pie chart showing income distribution.

    Args:
        df (pd.DataFrame): The input DataFrame.
        save_path (str): The path to save the pie chart image.

    Returns:
        plt.pie: The pie chart showing income distribution.
    """
    try:
        fig = plt.figure(figsize=(4, 4))  # Corrected figure creation
        income = df['income'].value_counts(normalize=True)
        pie_chart = income.plot.pie(autopct='%1.1f%%', textprops={'size': 'smaller'}, radius=0.5)
        plt.savefig(save_path)
        plt.close()
        return pie_chart
    except Exception as e:
        return f"No se pudo graficar: {str(e)}"

# Usage example:
save_path = "pie.png"  # Path to save the pie chart image
grafico_income(df1, save_path)
