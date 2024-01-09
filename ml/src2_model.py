import pandas as pd 
from sklearn import svm
from sklearn.model_selection import train_test_split
from change_future import cambiar
from sklearn.metrics import accuracy_score


def svm_model(**kwargs):
    """_summary_
    esta es una funcion donde voy a evaluar el modelo svm o bien llamado maquina de soporte vectorial
    que es un algoritmo no supervisado, por lo tanto se utiliza para 
    clasificacion y regresion. En este caso vamos a utilizarlo como clasicador

    """
    X=cambiar.drop('Survived', axis=1)
    Y=cambiar.Survived
    #Se divide la informacion en entrenamiento y testeo
    X_train,X_test,y_train,y_test = train_test_split(X,y, random_state=000 , test_size=30)
    model=svm.SVC()
    model.fit(X_train,y_train)
    y_pred_train=model.predict(X_train)
    y_pred_test=model.predict(X_test)
    #Calculo el accuracy en Train
    train_accuracy = accuracy_score(y_train,y_train_pred)
    #Calculo el accuracy en Test
    test_accuracy = accuracy_score(y_test,y_test_pred)
    print('El accuracy en train es:', train_accuracy)
    print('El accuracy en test es:', test_accuracy)
    ti = kwargs['ti']
    ti.xcom_push(key='rf_model', value="Accuracy en train:" + str(train_accuracy) + ", Accuracy en test:" + str(test_accuracy))

