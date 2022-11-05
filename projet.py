# ici on écrit notre code.

"""Utilisez read_csv pour lire les données

1-Affichez le tableau des données 

2-Affichez le nom de chaque "colums"

3-Affichez les 10 première lignes, les 10 dernière et les lignes entre 100, 120.

4-Afficher le type de chaque "colums".

5- Remplacer les espaces par _ dans les noms des colonnes.

6-affichez les informations de cette base de données (mean, min , max).

7- Enlevez  les colonnes "Autres transports" et "Autres transports international"""

# fonction qui lit un fichier csv

data = pd.read_csv('fichier.csv')
