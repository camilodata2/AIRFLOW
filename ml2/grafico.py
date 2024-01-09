import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from load_file import df1

def null_matrix(df1: pd.DataFrame, save_path: str) -> sns.matrix.ClusterGrid:
    """Create a heatmap showing null values in the DataFrame and save it as an image.

    Args:
        df1 (pd.DataFrame): The input DataFrame.
        save_path (str): The path to save the heatmap image.
    """
    try:
        plt.figure(figsize=(8, 8))  # Set the figure size
        heatmap = sns.heatmap(df1.isnull(), yticklabels=False, cbar=False)
        plt.savefig(save_path)  # Save the heatmap as an image
        plt.close()  # Close the plot
        print(f"Heatmap saved at: {save_path}")  # Display the path in the console
    except Exception as e:
        print(f"No se ha podido graficar: {str(e)}")

# Usage example:
save_path = "heatmap.png"  # Path to save the heatmap image
null_matrix(df1, save_path)
