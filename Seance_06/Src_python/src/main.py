#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math
import os

#Fonction pour ouvrir les fichiers
def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

#Fonction pour obtenir l'ordre défini entre deux classements (listes spécifiques aux populations)
def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element][1]])
    return classement

#Partie sur les îles
iles = pd.DataFrame(ouvrirUnFichier("./data/island-index.csv"))
surface = iles[["Surface (km²)"]]
nouveaux = pd.DataFrame({
    "Continent": [
        "Asie/Afrique/Europe",
        "Amérique",
        "Antarctique",
        "Australie"
    ],
    "Surface (km²)": [
        float(85545323),
        float(37856841),
        float(7768030),
        float(7605049)
    ]
})
Surface_km2 = pd.concat([surface, nouveaux], ignore_index=True)
print(Surface_km2)

# 4 : ordre décroissant des surfaces
#Fonction pour trier par ordre décroissant les listes (îles et populations)
def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

ordreDecroissant(Surface_km2.values.tolist())

# 5 : loi rang-taille
surfaces_triees = sorted(Surface_km2["Surface (km²)"].tolist(), reverse=True)
rangs = range(1, len(surfaces_triees) + 1)
plt.figure(figsize=(8, 6))
plt.plot(rangs, surfaces_triees, marker='o')
plt.xlabel("Rang")
plt.ylabel("Surface (km²)")
plt.title("Loi rang–taille des surfaces")
plt.grid(True)
plt.savefig("loi_rang_taille.png", dpi=300)


#Fonction pour convertir les données en données logarithmiques
def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

surfaces_log = conversionLog(surfaces_triees)
rangs = list(range(1, len(surfaces_log) + 1))
rangs_log = conversionLog(rangs)
plt.figure(figsize=(8, 6))
plt.plot(rangs_log, surfaces_log)
plt.xlabel("Rang")
plt.ylabel("Surface (km²) en log")
plt.title("Loi rang–taille des surfaces log")
plt.grid(True)
plt.savefig("loi_rang_taille_log.png", dpi=300)


print("Image générée : rang_taille_log.png\n")
"""
COMMENTAIRE :
Non. Les rangs ne sont pas des variables aléatoires : ce sont des valeurs
déterministes obtenues après un tri. Ils ne suivent donc pas une distribution
probabiliste permettant d’appliquer un test statistique (normalité, KS, etc.)
On ne peut tester que les valeurs (surfaces), jamais les rangs eux-mêmes.
"""
#Fonction pour obtenir le classement des listes spécifiques aux populations
def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop
# Partie sur le monde
monde = pd.DataFrame(ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))
colonnes_analyse = ["État", "Pop 2007", "Pop 2025", "Densité 2007", "Densité 2025"]
donnees = monde[colonnes_analyse]

etats = list(donnees["État"])
pop2007 = [float(x) for x in donnees["Pop 2007"]]
pop2025 = [float(x) for x in donnees["Pop 2025"]]
dens2007 = [float(x) for x in donnees["Densité 2007"]]
dens2025 = [float(x) for x in donnees["Densité 2025"]]

print(f"Nombre d'États : {len(etats)}\n")

#Etape 2.2 - Classement décroissant populations et densités 

ordre_pop2007 = ordrePopulation(pop2007, etats)
ordre_pop2025 = ordrePopulation(pop2025, etats)
ordre_dens2007 = ordrePopulation(dens2007, etats)
ordre_dens2025 = ordrePopulation(dens2025, etats)

print("Extrait classement Pop 2007 (5 premiers) :", ordre_pop2007[:5])
print("Extrait classement Densité 2007 (5 premiers) :", ordre_dens2007[:5],"\n")


comparaison_pop_dens = classementPays(ordre_pop2007, ordre_dens2007)
comparaison_pop_dens.sort() 

rangs_pop = []
rangs_dens = []

for element in comparaison_pop_dens:
    rangs_pop.append(element[0])
    rangs_dens.append(element[1])

print("Extrait rangs Pop 2007 :", rangs_pop[:10])
print("Extrait rangs Densité 2007 :", rangs_dens[:10],"\n")

#Etape 2.5 - Calcul corrélations rang
print("\nCorrélation de rang (Spearman) et concordance (Kendall) :")

from scipy.stats import spearmanr, kendalltau

spearman_coef, spearman_p = spearmanr(rangs_pop, rangs_dens)
kendall_coef, kendall_p = kendalltau(rangs_pop, rangs_dens)

print(f"Coefficient de corrélation de rang Spearman : {spearman_coef:.4f} (p-value = {spearman_p:.4f})")
print(f"Coefficient de concordance de rang Kendall : {kendall_coef:.4f} (p-value = {kendall_p:.4f})")

