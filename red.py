# Importar las bibliotecas necesarias
import pandas as pd  # Para manipulación de datos
import numpy as np  # Para operaciones numéricas
from sklearn.model_selection import train_test_split  # Para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.preprocessing import StandardScaler  # Para normalizar características StandardScaler es útil para preprocesar datos antes de entrenar un modelo de aprendizaje automático
from tensorflow.keras.models import Sequential  # Para definir modelos de redes neuronales, en este caso son secuenciales linea de capas
from tensorflow.keras.layers import Dense  # Para definir capas densas en el modelo 
# salida=activacion(entradas⋅pesos+sesgo)  cada neurona está completamente conectada a todas las neuronas de la capa anterior y la siguiente

# Cargar el archivo CSV con la codificación Latin-1
data = pd.read_csv('DATA/Emisiones.csv', encoding='latin-1')  # Cargar datos del archivo CSV La codificación Latin-1, también conocida como ISO 8859-1

# Seleccionar características y variable objetivo
X = data[['EMISIONES 2017', 'EMISIONES 2018']].values  # Características: emisiones de 2017 y 2018
y = data['EMISIONES 2019'].values  # Variable objetivo: emisiones de 2019

# Normalizar características
scaler = StandardScaler()  # Crear un objeto StandardScaler
X = scaler.fit_transform(X)  # Normalizar las características

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo de red neuronal
model = Sequential([  # Inicializar un modelo secuencial
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),  # Capa de entrada con 64 neuronas y activación ReLU
    Dense(64, activation='relu'),  # Capa oculta con 64 neuronas y activación ReLU
    Dense(1)  # Capa de salida con una neurona para la predicción
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')  # Compilar el modelo con el optimizador Adam y MSE como función de pérdida

# Entrenar el modelo
model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)  # Entrenar el modelo con 100 épocas, tamaño de lote de 32 y mostrar información de progreso

# Evaluar el modelo en los datos de prueba
loss = model.evaluate(X_test, y_test)  # Calcular la pérdida en los datos de prueba
print(f'Loss en el conjunto de prueba: {loss}')  # Imprimir la pérdida en el conjunto de prueba

# Hacer predicciones para el año 2020
# Suponiendo que tienes los datos del año 2020 en una variable llamada X_2020
X_2020 = np.array([[...], [...]])  # Completa con tus datos del año 2020
X_2020 = scaler.transform(X_2020)  # Normalizar las características del año 2020
predictions = model.predict(X_2020)  # Hacer predicciones utilizando el modelo entrenado
print(f'Predicciones para el año 2020: {predictions}')  # Imprimir las predicciones para el año 2020

