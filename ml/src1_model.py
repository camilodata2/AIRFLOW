import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.accuracy import accuracy_score
from change_future import cambiar

def rf_model(**kwargs):
    """
    esta funcion creara un modelos de randoforest
    """
    X=cambiar.drop('Survived',axis=1)
    Y=cambiar.Survived
    #Se separan los datos en entrenamiento y testeo
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3, random_state=0000)
    #se crea el modelo con 100 arboles
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)
    #Calculo de las predicciones en Train y Test
    y_pred_train=clf.predict(X_train)
    y_pred_test=clf.predict(X_test)
    #Calculo el accuracy en Train
    train_accuracy = accuracy_score(y_train,y_train_pred)
    #Calculo el accuracy en Test
    test_accuracy = accuracy_score(y_test,y_test_pred)
    print('El accuracy en train es:', train_accuracy)
    print('El accuracy en test es:', test_accuracy)
    ti = kwargs['ti']
    ti.xcom_push(key='rf_model', value="Accuracy en train:" + str(train_accuracy) + ", Accuracy en test:" + str(test_accuracy))

