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

    nom_fichier = f"graph_rond_departements/pie_{dept}.png"
    plt.savefig(nom_fichier)
    plt.close()

    print(f"Diagramme circulaire créé pour {dept} → {nom_fichier}")

print("\nTous les diagrammes circulaires sont dans le dossier 'graph_rond_departements'.")

# Question 13 : histogramme
col_inscrits = "Inscrits"

# 3️⃣ Vérifie qu'il n'y a pas de valeurs manquantes
df = contenu.dropna(subset=[col_inscrits])

# 4️⃣ Création de l’histogramme
plt.figure(figsize=(8, 6))
plt.hist(contenu[col_inscrits], bins=20, edgecolor='black', color='skyblue')

# 5️⃣ Mise en forme
plt.title("Histogramme de la distribution des inscrits")
plt.xlabel("Nombre d’inscrits")
plt.ylabel("Fréquence (nombre de départements)")

# 6️⃣ Sauvegarde dans un fichier image
plt.savefig("histogramme_inscrits.png")
plt.show()

print("✅ Histogramme créé et enregistré sous 'histogramme_inscrits.png'")

