# ici on écrit notre code.

"""Utilisez read_csv pour lire les données
1-Affichez le tableau des données 
2-Affichez le nom de chaque "colums"
MIKE 3-Affichez les 10 première lignes, les 10 dernière et les lignes entre 100, 120.
4-Afficher le type de chaque "colums".
5- Remplacer les espaces par _ dans les noms des colonnes.
MIKE 6-affichez les informations de cette base de données (mean, min , max).
MIKE 7- Enlevez  les colonnes "Autres transports" et "Autres transports international"""

# fonction qui lit un fichier csv
dataframe = pd.read_csv('IGT - Pouvoir de réchauffement global.csv.csv')

# afficher le dataframe
print(dataframe)

# afficher le nom de chaque colonne
print(dataframe.colums)

# afficher le type de chaque colonne
print(dataframe.dtypes)

# remplacer les espaces par _ dans les noms des colonnes
dataframe2 = dataframe.columns.str.replace('INSEE commune', 'INSEE_commune')
dataframe2 = dataframe.columns.str.replace('Autres transports', 'Autres_transports')
dataframe2 = dataframe.columns.str.replace('CO2 biomasse hors-total', 'CO2_biomasse_hors-total')
dataframe2 = dataframe.columns.str.replace('Industrie hors-énergie', 'Industrie_hors-énergie')

