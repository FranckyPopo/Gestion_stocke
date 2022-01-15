from time import sleep
import os
import json
import data

dossier_actuel = os.getcwd()
dossier_donnees = os.path.join(dossier_actuel, "donnees")

# Récuperation des différente données
recuperation_clients =  data.get_data(dossier_donnees, "liste_clients")
recuration_produits = data.get_data(dossier_donnees, "liste_produits")
recuration_historiques = data.get_data(dossier_donnees, "liste_historiques")

