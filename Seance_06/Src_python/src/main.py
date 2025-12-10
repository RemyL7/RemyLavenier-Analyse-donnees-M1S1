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
surfaces_tries = sorted(Surface_km2["Surface (km²)"].tolist(), reverse=True)
rangs = range(1, len(surfaces_tries) + 1)
plt.figure(figsize=(8, 6))
plt.plot(rangs, surfaces_tries, marker='o')
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

surfaces_log = conversionLog(surfaces_tries)
rangs = list(range(1, len(surfaces_log) + 1))
rangs_log = conversionLog(rangs)
plt.figure(figsize=(8, 6))
plt.plot(rangs, surfaces_log, marker='o')
plt.xlabel("Rang")
plt.ylabel("Surface (km²) en log")
plt.title("Loi rang–taille des surfaces log")
plt.grid(True)
plt.savefig("loi_rang_taille_log.png", dpi=300)

"""
COMMENTAIRE :
Oui, il est possible de faire un test sur les rangs.
Par exemple, on peut utiliser des tests non paramétriques qui ne dépendent pas de la distribution des valeurs et qui utilisent les rangs directement :
1. Test de Spearman : pour mesurer la corrélation entre deux séries de rangs.
2. Test de Kendall : autre test de corrélation basé sur les rangs.
3. Test de Wilcoxon ou Mann–Whitney : pour comparer deux échantillons indépendants ou appariés sur leurs rangs.

Dans le cadre de la loi rang–taille, on peut par exemple tester si les rangs observés
suivent une distribution théorique (ex: Zipf) en comparant les rangs attendus et observés.
Cela reste un test sur les rangs, même si ce n’est pas un test classique "paramétrique".
"""
# Partie sur le monde
monde = pd.DataFrame(ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))
Etat = monde[["État"]]
Pop_2007 = monde[["Pop 2007"]]
Pop_2025 = monde[["Pop 2025"]]
densite_2007 = monde[["Densité 2007"]]
deniste_2025 = monde[["Densité 2025"]]


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



#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().






#Partie sur les populations des États du monde
#Source. Depuis 2007, tous les ans jusque 2025, M. Forriez a relevé l'intégralité du nombre d'habitants dans chaque États du monde proposé par un numéro hors-série du monde intitulé États du monde. Vous avez l'évolution de la population et de la densité par année.
monde = pd.DataFrame(ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))

#Attention ! Il va falloir utiliser des fonctions natives de Python dans les fonctions locales que je vous propose pour faire l'exercice. Vous devez caster l'objet Pandas en list().
"""

