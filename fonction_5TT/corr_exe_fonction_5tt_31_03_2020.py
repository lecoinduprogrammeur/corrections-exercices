# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Proposition de correction
Exercice sur les fonctions 5TT 31/03/2020
"""

# liste vide
inscrit = []
adresse = []

# input () 1
prenom = input("Votre prénom ? ").capitalize()
nom = input("Votre nom de famille ? ").capitalize()
age = int(input("Votre âge ? "))
metier = input("Votre profession ? ").lower()

print ("Votre adresse complète : ")

# input () 2
num = input("Votre numéro ? ")
rue_bvd_av = input("Votre rue - boulevard - avenue ? ")
cp = input("Votre code postal ? ")
ville_village = input("Votre ville ou village ? ")

# fonction
def inscription():
    inscrit.append(prenom)
    inscrit.append(nom)
    inscrit.append(age)
    inscrit.append(metier)
    adresse.append(num)
    adresse.append(rue_bvd_av)
    adresse.append(cp)
    adresse.append(ville_village)
    adresse_complete ="/".join(adresse)
    inscrit.append(adresse_complete)

# appel de la fonction et exécution
inscription()

# affichage du résultat final
print (inscrit)