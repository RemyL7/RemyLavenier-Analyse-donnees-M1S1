#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats
import numpy as np

#C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
#Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
#Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

#Par convention, on place les fonctions locales au début du code après les bibliothèques.
def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

#Théorie de l'échantillonnage (intervalles de fluctuation)
#L'échantillonnage se base sur la répétitivité.
# Question 1-3 : moyennes
donnees = pd.DataFrame(ouvrirUnFichier("./data/Echantillonnage-100-Echantillons.csv"))
moyennes = donnees.mean()
print(moyennes.round(0))

# Question 1-4 : fréquences
# 1-4.1 : échantillon
somme_moyennes = moyennes.sum()
frequences = moyennes / somme_moyennes
print("Somme des moyennes :", somme_moyennes.round(0))
print("Fréquences :\n",frequences.round(2))

#1-4.2 : population
moy_pop = pd.DataFrame(ouvrirUnFichier("./data/Echantillonnage-Population-reelle.csv"))
somme_pop = moy_pop.sum()
frequences_pop = (moy_pop / somme_pop)
frequences_pop = frequences_pop.squeeze()
frequences_pop.index = ["Pour", "Contre", "Sans opinion"]
print("Somme de la population :", somme_pop.round(0))
print("Fréquences de la population :\n", frequences_pop.round(2))  

#1-5 : intervalles de fluctuation
def intervalle_fluctuation(f, n, z=1.96):
    ecart_type = np.sqrt(f * (1 - f) / n)
    borne_inf = f - z * ecart_type
    borne_sup = f + z * ecart_type
    return round(borne_inf, 3), round(borne_sup, 3)
frequences_interv = [frequences]
n = 1000
intervales = {}
for modalite, f in frequences.items():
    intervales[modalite] = intervalle_fluctuation(f, n)
print(intervales)

def intervalle_fluctuation_pop(f, n, z=1.96):
    ecart_type = np.sqrt(f * (1 - f) / n)
    borne_inf = f - z * ecart_type
    borne_sup = f + z * ecart_type
    return round(borne_inf, 3), round(borne_sup, 3)
frequences_interv_pop = [frequences_pop]
n = 2185
intervales_pop = {}
for modalite, f in frequences_pop.items():
    intervales_pop[modalite] = intervalle_fluctuation_pop(f, n)
print(intervales_pop, "\n")







#Théorie de l'estimation (intervalles de confiance)
#2-1 : panda.iloc
premier_echantillon = donnees.iloc[0]
premier_echantillon_liste = list(premier_echantillon)
print(premier_echantillon_liste)

#2-2 : somme et fréquence de l'échantillon
somme_ech1 = sum(premier_echantillon_liste)
print("Somme du premier échantillon :", somme_ech1)

frequences_ech1 = [val / somme_ech1 for val in premier_echantillon_liste]
print("Fréquences du premier échantillon :", frequences_ech1)

#2-3 : intervalle de confiance
modalites = ["Pour", "Contre", "Sans opinion"]
def intervalle_confiance(f, n, z=1.96):
    ecart_type = np.sqrt(f * (1 - f) / n)
    borne_inf = f - z * ecart_type
    borne_sup = f + z * ecart_type
    return round(borne_inf, 3), round(borne_sup, 3)
ic_95 = {modalite: intervalle_confiance(f, n)
         for modalite, f in zip(modalites, frequences)}
print("Intervalle de confiance 95% :", ic_95, "\n")





#Théorie de la décision (tests d'hypothèse)
#La décision se base sur la notion de risques alpha et bêta.
#Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
#3-1 : test de Shapiro-Wilks
from scipy.stats import shapiro

data1 = pd.read_csv("./data/Loi-normale-Test-1.csv")
data2 = pd.read_csv("./data/Loi-normale-Test-2.csv")

stat1, p_value1 = shapiro(data1)
stat2, p_value2 = shapiro(data2)

print("Test Shapiro - Fichier 1")
print("Statistique =", round(stat1, 4), ", p-value =", round(p_value1, 4))
if p_value1 > 0.05:
    print("Distribution normale")
else:
    print("Distribution non normale")

print("\nTest Shapiro - Fichier 2")
print("Statistique =", round(stat2, 4), ", p-value =", round(p_value2, 4))
if p_value2 > 0.05:
    print("Distribution normale")
else:
    print("Distribution non normale")


