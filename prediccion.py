import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# Nombre del .csv: 2_IrisSpecies.csv
df = pd.read_csv("PedroMartinPerez/iris.csv")

# Modifico en: 0-1-2 (en este caso) para la salida:
# Y se lo asigno a la propia columna.
df.species = df.species.map({"setosa": 0, "versicolor": 1, "virginica": 2})

#X es “Input=entrada”, la información a proporcionar,
#y es “Output=salida”, la información a predecir
X = df.drop("species", axis=1)

y = df["species"]

# separo:
# 80% para train (entrenamiento): 80% de 150 = 120
# 20% para test (prueba) : 20% de 150 = 30
# test_size=0.80 indica el 80%
# random_state=0 sirve para obtener siempre el mismo resultado
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.80, random_state=0)

# NOTA:
# En aquellos casos que hubiera problema al entrenar con los algoritmos:
# 1 típica forma de solucionarlo es:
# X_train = X_train.values
# y_train = y_train.values
# X_test = X_test.values
# y_test = y_test.values

#Clasificador elegido: DecisionTreeClassifier 
clf = DecisionTreeClassifier()

#Entrenamos con los datos de entreno
clf.fit(X_train, y_train)
#Intentamos predecir y_test
y_pred = clf.predict(X_test)

#Comprobamos la precisión de nuestra predicción siendo 1 el 100% y 0 el 0%
acc = accuracy_score(y_test, y_pred)

print(acc)
def predecir(datos):
    res = clf.predict(datos)
    if res == 0:
        return "setosa"
    if res == 1:
        return "versicolor"
    if res == 2:
        return "virginica"
    else:
        return "Error en la predicción"