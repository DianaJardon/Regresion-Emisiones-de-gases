## Emisión de Gases de Efecto Invernadero a nivel Nacional del 2017 al 2019

<span style="color: cyan">Implementación de un modelo regresion lineal para hacer el pronosticp de emisiones 2019</span>

1. Un modelo de regresión lineal es un modelo estadístico que se utiliza para entender la relación entre una variable dependiente (también conocida como variable de respuesta o variable objetivo) y una o más variables independientes (también conocidas como variables predictoras o características). El objetivo principal de la regresión lineal es modelar esta relación de una manera que permita predecir el valor de la variable dependiente basándose en los valores de las variables independientes.
   
   
  ![Regresion](img/1.png)

2. El presente código realiza un análisis de regresión lineal para predecir las emisiones de gases de efecto invernadero en 2019 (variable objetivo) basado en las emisiones en 2017 y 2018 (características o variables independientes). 

* Carga de datos: Los datos se cargan desde un archivo CSV llamado 'Emisiones.csv' utilizando Pandas. La codificación 'latin-1' se especifica para asegurar que los caracteres especiales se manejen correctamente.

* Preparación de datos: Se crea un DataFrame llamado emisionDataFrame directamente desde el archivo CSV. Las características y la variable objetivo se seleccionan del DataFrame.

* División de datos: Los datos se dividen en conjuntos de entrenamiento y prueba. Se separa el 4% de los datos para el conjunto de prueba y el 96% para el conjunto de entrenamiento.

* Entrenamiento del modelo: Se crea un modelo de regresión lineal utilizando la clase LinearRegression de Scikit-Learn y se entrena utilizando los datos de entrenamiento (X_train y Y_train).

* Evaluación del modelo: Se realizan predicciones tanto en el conjunto de entrenamiento como en el conjunto de prueba utilizando el modelo entrenado. Se calcula el error cuadrático medio (MSE) para evaluar el rendimiento del modelo en ambos conjuntos de datos.

* Resultados: Los valores de MSE se imprimen en la consola para evaluar la calidad del modelo. Además, se crea un DataFrame llamado df_predicciones que contiene las predicciones y los valores reales del conjunto de prueba, y se muestran las primeras 10 filas de este DataFrame para inspeccionar las predicciones.

En resumen, el modelo utiliza las emisiones de gases de efecto invernadero en 2017 y 2018 para predecir las emisiones en 2019, y se evalúa su rendimiento utilizando el error cuadrático medio.