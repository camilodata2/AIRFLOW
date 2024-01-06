import pandas as pd
from change_future import cambiar
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

#Importamos las librerias necesarias para la creacion del modelo
def DT_model(**kwargs):
    """
    Funcion que se encargadra de entrenar el model

    """
    X = cambiar.drop("Survived", axis = 1)
    y = cambiar.Survived


     #30% para test y 70% para train
    X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size = 0.30, random_state = 00000)
    
    
      #Creacion del modelo
    tree = DecisionTreeClassifier(max_depth=2, random_state = 00000)
    
      #Entrenamiento
    tree.fit(X_train,y_train)
    
      #Calculo de las predicciones en Train y Test
    y_train_pred = tree.predict(X_train)
    y_test_pred = tree.predict(X_test)
    
      #Calculo el accuracy en Train
    train_accuracy = accuracy_score(y_train,y_train_pred)
    
      #Calculo el accuracy en Test
    test_accuracy = accuracy_score(y_test,y_test_pred)
    
    print('El accuracy en train es:', train_accuracy)
    print('El accuracy en test es:', test_accuracy)
    ti = kwargs['ti']
    ti.xcom_push(key='DT_model', value="Accuracy en train:" + str(train_accuracy) + ", Accuracy en test:" + str(test_accuracy))
