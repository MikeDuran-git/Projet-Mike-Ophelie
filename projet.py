
# ici on écrit notre code.

"""Utilisez read_csv pour lire les données
1-Affichez le tableau des données 
2-Affichez le nom de chaque "colums"
MIKE 3-Affichez les 10 première lignes, les 10 dernière et les lignes entre 100, 120.
4-Afficher le type de chaque "colums".
5- Remplacer les espaces par _ dans les noms des colonnes.
MIKE 6-affichez les informations de cette base de données (mean, min , max).
MIKE 7- Enlevez  les colonnes "Autres transports" et "Autres transports international"""

# ici on écrit notre code
import pandas as pd

raw_data=pd.read_csv("IGT - Pouvoir de réchauffement global - IGT - Pouvoir de réchauffement global.csv")

#on enleve les Nan Values
dataframe=raw_data.dropna("index")

# afficher le dataframe
print(dataframe)

# afficher le nom de chaque colonne
print(dataframe.colums)

# afficher le type de chaque colonne
print(dataframe.dtypes)

# remplacer les espaces par _ dans les noms des colonnes
dataframe = dataframe.columns.str.replace('INSEE commune', 'INSEE_commune')
dataframe = dataframe.columns.str.replace('Autres transports', 'Autres_transports')
dataframe = dataframe.columns.str.replace('CO2 biomasse hors-total', 'CO2_biomasse_hors-total')
dataframe = dataframe.columns.str.replace('Industrie hors-énergie', 'Industrie_hors-énergie')

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
print(afficher_10_premieres(dataframe))

# afficher les 10 dernières ligne
print(afficher_10_dernieres(dataframe))

# afficher la moyenne
print(getMean(dataframe))

# afficher les valeurs minimum
print(getMin(dataframe))

#afficher les valeurs maximum
print(getMax(dataframe))

#on enlevel les columns 'Autres transports international' et 'Autres transports'
print(enlever_columns(dataframe))


