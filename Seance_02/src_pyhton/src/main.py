#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt

# Question 4 : lecture du fichier CSV avec la méthode read_csv(...)
# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
# The CSV is located in the data/ directory inside the project.
csv_path = "data/resultats-elections-presidentielles-2022-1er-tour.csv"
with open(csv_path, "r", encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier)

# Question 5 : afficher sur le terminal le contenu du DataFrame
print(contenu)

# Question 6 : calculer le nombre de lignes et de colonnes et les afficher
nb_lignes = len(contenu)
nb_colonnes = len(contenu.columns)
print(f"\nNombre de lignes : {nb_lignes}")
print(f"Nombre de colonnes : {nb_colonnes}")

# Question 7 : 


# Question 8 : afficher les noms des colonnes
print("\nNoms des colonnes :")
# Mettre dans un commentaire le numéro de la question
# Question 1
# ...
