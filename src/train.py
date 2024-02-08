# src/train.py

import hydra
from omegaconf import DictConfig, OmegaConf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(config: DictConfig) -> None:
    X, y = load_dataset(config.data.dataset_path)

    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config.data.test_size, random_state=42)

    # Configuración del modelo
    if config.model.algorithm == "RandomForest":
        model = RandomForestClassifier(n_estimators=config.model.n_estimators, random_state=42)
    else:
        raise ValueError(f"Algoritmo no soportado: {config.model.algorithm}")

    # Entrenamiento del modelo
    model.fit(X_train, y_train)

    # Predicciones en el conjunto de prueba
    y_pred = model.predict(X_test)

    # Métrica de evaluación (omitiendo detalles para simplicidad)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Entrenamiento completado. Precisión: {accuracy}")

def load_dataset(dataset_path):
    with open(dataset_path,'r') as f:
        data = [l.strip().split(',') for l in f.readline()]
  

