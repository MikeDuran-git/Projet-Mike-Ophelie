# ici on écrit notre code
import pandas as pd

def afficher_10_premieres(dataframe):
    return dataframe.head(10)

def afficher_10_dernieres(dataframe):
    return dataframe.head(-10)

def getMean(dataframe):
    return dataframe.mean()

def getMin(dataframe):
    return dataframe.min()

def getMax(dataframe):
    return dataframe.max()

# 'Autres transports international' et 'Autres transports'
def enlever_columns(dataframe):
    return dataframe.drop(['Autres transports international','Autres transports'],axis=1).
