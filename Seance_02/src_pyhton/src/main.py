#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import os

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
print(f"Nombre de lignes : {nb_lignes}")
print(f"Nombre de colonnes : {nb_colonnes}")

# Question 7 : faire une liste des types de variables des colonnes et l'afficher
print("Types de données Python par colonne :")
for colonne in contenu.columns:
    premier_non_null = contenu[colonne].dropna().iloc[0] if contenu[colonne].dropna().size > 0 else None
    type_python = type(premier_non_null).__name__ if premier_non_null is not None else "NoneType"
    print(f"{colonne} : {type_python}")

# Question 8 : afficher les noms des colonnes
print ("\nNoms des colonnes :")
print(contenu.head(0))

# Questions 9 & 10 : sommes des colonnes
effectifs = []

for colonne in contenu.columns:
    if contenu[colonne].dtype in ['int64', 'float64']:
        total = contenu[colonne].sum()
        effectifs.append((colonne, total))
    else:
        # Si ce n’est pas une colonne numérique, on ne fait rien
        effectifs.append((colonne, "non quantitatif"))

print("Sommes (effectifs) des colonnes :")
for nom_colonne, valeur in effectifs:
    print(f"{nom_colonne} : {valeur}")

# Question 11 : créer des diagrammes pour chaque département
os.makedirs("graph_departements", exist_ok=True)

for dept in contenu["Libellé du département"].unique():
    data_dept = contenu[contenu["Libellé du département"] == dept]

    inscrits = data_dept["Inscrits"].sum()
    votants = data_dept["Votants"].sum()

    plt.figure()
    plt.bar(["Inscrits", "Votants"], [inscrits, votants], color=["skyblue", "lightgreen"])
    plt.title(f"Libellé du département : {dept}")
    plt.ylabel("Nombre de personnes")
    plt.xlabel("Catégorie")

    dept = dept.replace("/", "_")
    fichier = f"graph_departements/diagramme_{dept}.png"
    plt.savefig(fichier)
    plt.close()

    print(f"Diagramme créé pour le département {dept} → {fichier}")

print("\nTous les graphiques ont été générés dans le dossier 'graph_departements'.")

# # Question 12 : créer des diagrammes circulaires pour chaque département
os.makedirs("graph_rond_departements", exist_ok=True)

col_dept = "Libellé du département"
col_blancs = "Blancs"
col_nuls = "Nuls"
col_exprimes = "Exprimés"
col_abstention = "Abstentions"

for dept in contenu[col_dept].unique():
    data_dept = contenu[contenu[col_dept] == dept]

    blancs = data_dept[col_blancs].sum()
    nuls = data_dept[col_nuls].sum()
    exprimes = data_dept[col_exprimes].sum()
    abstentions = data_dept[col_abstention].sum()

    valeurs = [blancs, nuls, exprimes, abstentions]
    labels = ["Blancs", "Nuls", "Exprimés", "Abstentions"]

    plt.figure()
    plt.pie(valeurs, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f"Répartition des votes - Département {dept}")

    dept = dept.replace("/", "_")
    nom_fichier = f"graph_rond_departements/pie_{dept}.png"
    plt.savefig(nom_fichier)
    plt.close()

    print(f"Diagramme circulaire créé pour {dept} → {nom_fichier}")

print("\nTous les diagrammes circulaires sont dans le dossier 'graph_rond_departements'.")

# Question 13 : histogramme
col_inscrits = "Inscrits"
df = contenu.dropna(subset=[col_inscrits])
plt.figure(figsize=(8, 6))
plt.hist(contenu[col_inscrits], bins=20, edgecolor='black', color='skyblue')
plt.title("Histogramme de la distribution des inscrits")
plt.xlabel("Nombre d’inscrits")
plt.ylabel("Fréquence (nombre de départements)")
plt.savefig("histogramme_inscrits.png")
plt.show()

print("\nHistogramme créé et enregistré sous 'histogramme_inscrits.png'")

print(contenu.columns)

# Question Bonus : diagrammes circulaires
os.makedirs("graph_rond_departements_voix", exist_ok=True)

col_dept = "Libellé du département"
col_ARTHAUD = "Voix"
col_ROUSSEL = "Voix.1"
col_MACRON = "Voix.2"
col_LASSALLE = "Voix.3"
col_LE_PEN = "Voix.4"
col_ZEMMOUR = "Voix.5"
col_MELENCHON = "Voix.6"
col_HIDALGO = "Voix.7"
col_JADOT = "Voix.8"
col_PECRESSE = "Voix.9"
col_POUTOU = "Voix.10"
col_DUPONT_AIGNAN = "Voix.11"

for dept in contenu[col_dept].unique():
    data_dept = contenu[contenu[col_dept] == dept]

    Arthaud = data_dept[col_ARTHAUD].sum()
    Roussel = data_dept[col_ROUSSEL].sum()
    Macron = data_dept[col_MACRON].sum()
    Lassalle = data_dept[col_LASSALLE].sum()
    Le_Pen = data_dept[col_LE_PEN].sum()
    Zemmour = data_dept[col_ZEMMOUR].sum()
    Melenchon = data_dept[col_MELENCHON].sum()
    Hidlago = data_dept[col_HIDALGO].sum()
    Jadot = data_dept[col_JADOT].sum()
    Pecresse = data_dept[col_PECRESSE].sum()
    Poutou = data_dept[col_POUTOU].sum()
    Dupont_aignan = data_dept[col_DUPONT_AIGNAN].sum()

    valeurs = [Arthaud, Roussel, Macron, Lassalle, Le_Pen, Zemmour, Melenchon, Hidlago, Jadot, Pecresse, Poutou, Dupont_aignan]
    labels = ["Arthaud", "Roussel", "Macron", "lassalle", "Le Pen", "Zemmour", "Melenchon", "Hidlago", "Jadot", "Pecresse", "Poutou", "Dupont-Aignan"]

    plt.figure()
    plt.pie(valeurs, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f"Répartition des votes - Département {dept}")

    dept = dept.replace("/", "_")
    nom_fichier = f"graph_rond_departements_voix/pie_{dept}.png"
    plt.savefig(nom_fichier)
    plt.close()

    print(f"Diagramme circulaire créé pour {dept} → {nom_fichier}")

print("\nTous les diagrammes circulaires sont dans le dossier 'graph_rond_departements'.")

# Question bonus 2 : diagramme circulaire des voix pour l’ensemble de la France
colonnes_choisies = ["Voix", "Voix.1", "Voix.2", "Voix.3", "Voix.4", "Voix.5", "Voix.6", "Voix.7", "Voix.8", "Voix.9", "Voix.10", "Voix.11"]

sommes = {}
for colonne in colonnes_choisies:
    total = contenu[colonne].sum()
    sommes[colonne] = total

labels = ["Arthaud", "Roussel", "Macron", "lassalle", "Le Pen", "Zemmour", "Melenchon", "Hidlago", "Jadot", "Pecresse", "Poutou", "Dupont-Aignan"]
valeurs = list(sommes.values())

plt.figure(figsize=(8, 8))
plt.pie(valeurs, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Diagramme circulaire des voix pour l’ensemble de la France")
plt.savefig("Diagramme circulaire des voix pour l’ensemble de la France.png")
plt.show()

print("Diagramme circulaire enregistré sous 'Diagramme circulaire des voix pour l’ensemble de la France.png'")
