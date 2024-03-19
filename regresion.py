import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar los datos desde el archivo CSV  el latin -1 es para poder leer el archivo 
emision = pd.read_csv('DATA/Emisiones.csv', encoding='latin-1') 

# Crear un DataFrame directamente desde el archivo CSV
emisionDataFrame = pd.DataFrame(emision)

# Elegir las características y la variable objetivo
X = emisionDataFrame[['EMISIONES 2017', 'EMISIONES 2018']]  # Características (variables independientes)
Y = emisionDataFrame['EMISIONES 2019']  # Variable objetivo (variable dependiente)

# Dividir los datos en conjuntos de entrenamiento y prueba
# Se separan 4% para el conjunto de prueba y 96% para el conjunto de entrenamiento
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.96, random_state=5)

# Mostrar las formas de los conjuntos de entrenamiento y prueba
print(X_train.shape)  # Forma de X_train
print(X_test.shape)   # Forma de X_test
print(Y_train.shape)  # Forma de Y_train
print(Y_test.shape)   # Forma de Y_test

# Entrenar un modelo de regresión lineal
lin_model = LinearRegression()
lin_model.fit(X_train, Y_train)

# Realizar predicciones en el conjunto de entrenamiento y calcular MSE
y_train_predict = lin_model.predict(X_train)
MSE_train = mean_squared_error(Y_train, y_train_predict)
print("Entrenamiento: MSE =", MSE_train)

# Realizar predicciones en el conjunto de prueba y calcular MSE
y_test_predict = lin_model.predict(X_test)
MSE_test = mean_squared_error(Y_test, y_test_predict)
print("Pruebas: MSE =", MSE_test)

# Crear un DataFrame con las predicciones y los valores reales del conjunto de prueba
df_predicciones = pd.DataFrame({'valor_real': Y_test, 'prediccion': y_test_predict})
df_predicciones = df_predicciones.reset_index(drop=True)
df_predicciones.head(10)  # Mostrar las primeras 10 filas del DataFrame de predicciones
print(df_predicciones)
