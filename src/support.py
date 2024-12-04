import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import support as src
from sklearn.model_selection import train_test_split
from sklearn import metrics

def visual_categ(df):

    """
    Def:
        Calcula la distribución de las variables categóricas.

    Args:
        df: un dataframe de pandas.
    
    """

    col_categ = df.select_dtypes(include="object").columns
    num_col_categ = len(df.select_dtypes(include="object").columns)
    colors = ["green", "skyblue", "purple"]

    fig, axes = plt.subplots(nrows= (2 if num_col_categ >= 4 else 1), ncols= num_col_categ, figsize = (30,10))

    axes = axes.flat


    for i, column in enumerate(col_categ):

        value_counts = df[column].value_counts()
        axes[i].bar(value_counts.index, value_counts.values, color = colors[i])
        axes[i].set_title(column)
        axes[i].tick_params(axis = "y", labelsize = 20)
        axes[i].tick_params(axis = "x", labelsize = 20, rotation=-45)


def reorganizar(df, columna, name, ajuste):
    """
    Def:
        Agrupa categorías con muy pocos valores para evitar ruido.

    Args:
        df: el dataframe de pandas.
        columna: columna categórica que queremos agrupar
        name: valor que asignamos a las categorías mínimas (i.e.: "otros").
        ajuste: porcentaje de esa categoría respecto al conjunto de los datos.
        
        """
    
    for value in df[columna].unique():
        dicc_replace = {}
        if float(df[df[columna] == value].count()[0]) / df.shape[0] *100 < ajuste:
            dicc_replace[value] = name
            df[columna] = (
                df[columna]
                .map(dicc_replace)).fillna(df[columna])
            

 
def train_val_test_split(df, rstate=42, shuffle=True, stratify=None):

    """
    Def:
        Dividimos el conjunto de datos en entrenamiento, validacióno y prueba.
    
    Args:
        df: un dataframe de pandas
    """

    strat = df[stratify] if stratify else None
    train_set, test_set = train_test_split(
        df, test_size=0.4, random_state=rstate, shuffle=shuffle, stratify=strat)
    strat = test_set[stratify] if stratify else None
    val_set, test_set = train_test_split(
        test_set, test_size=0.5, random_state=rstate, shuffle=shuffle, stratify=strat)
    return (train_set, val_set, test_set)



def remove_labels(df, label_name):

    """
    Def:
        Separamos las características de la variable respuesta.

    Args:
        df: un dataframe de pandas.
        label_name: nombre de la columna de la variable respuesta.
    """

    X = df.drop(label_name, axis=1)
    y = df[label_name].copy()
    return (X, y)
