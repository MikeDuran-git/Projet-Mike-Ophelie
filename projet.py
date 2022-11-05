# ici on écrit notre code
import pandas as pd

raw_data=pd.read_csv("IGT - Pouvoir de réchauffement global - IGT - Pouvoir de réchauffement global.csv")

#on enleve les Nan Values
df=raw_data.dropna("index")

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
    return dataframe.drop(['Autres transports international','Autres transports'],axis=1)


# afficher les 10 prem lignes
print(afficher_10_premieres(df))

# afficher les 10 dernières ligne
print(afficher_10_dernieres(df))

# afficher la moyenne
print(getMean(df))

# afficher les valeurs minimum
print(getMin(df))

#afficher les valeurs maximum
print(getMax(df))

#on enlevel les columns 'Autres transports international' et 'Autres transports'
print(enlever_columns(df))


