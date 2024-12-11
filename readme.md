# Predicción de fraude

## Descripción del proyecto

Este proyecto tiene como objetivo clasificar personas de riesgo o no a la hora de dar un préstamo. Utilizando la BBDD [UC Irvine](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data) se trata de crear un modelo de datos que permita predecir si una nueva persona será considerada de riesgo para conceder una línea de crédito, permitiendo a la empresa reducir el número de deudores.

## Proceso del proyecto
### Análisis Exploratorio de Datos
En primer lugar, se ha realizado una exploración de los datos separando entre variable respuesta, variables categóricas y variables numéricas. 
1. **Variable respuesta**: Hay un **desbalanceo moderado** (70%-30%) que habrá que tener en cuenta a la hora de medir el rendimiento de los modelos aplicados.
2. **Variables numéricas**:
    1. Encontramos variables numéricas como "Installment_commitment" o "residence_size" que pueden ser consideradas categóricas ya que aunque son valores numéricos se pueden tratar como variables categóricas.
    2. encontramos variables numéricas como "Installment_commitment" o "residence_sice" que pueden ser consideradas categóricas ya que aunque son valores numéricos se pueden tratar como variables categóricas.
    3. Respecto a las variables numéricas restantes, vemos que hay un sesgo claro hacia la derecha, donde encontramos usando el violinplot outliers tanto en la clase positiva como negativa. Habrá que valorar hacer análisis eliminando outliers.
    4. Con el mapa de calor vemos que las variables no tienen una relación extremadamente directa (a priori no las eliminaremos).
3. **Variables categóricas**: 
    1. Vemos que hay variables con clases con una pequeña representación, lo que puede generar ruido al hacer el modelo. Se puede analizar el modelo en el caso de que se agrupen esas clases minoritario.
    2. Item 3b

### Preparación del conjunto de datos
Una vez analizados los datos pasamos a dividir el conjunto de datos y preparar el conjunto de entrenamiento utilizando un pipeline resolviendo los posibles nulos que puedan añadirse en un futuro a este conjunto de entrenamiento con la mediana mediante "Simple Imputer" y normalizando usando "Robust Scaler".

Para las variables categóricas utilizamos un Pipeline usando OneHotEncoder para codificar las variables.

### Entrenamiento del algoritmo
Al ser un problema de clasificación binaria comenzamos entrenando un modelo de Regresión Logística para ver como se comporta el modelo con estos datos.

### Entrenamiento con otros modelos