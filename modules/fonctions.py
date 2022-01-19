import os
import json
from time import sleep
from . import data

dossier_actuel = os.getcwd()
dossier_donnees = os.path.join(dossier_actuel, "data")

# Récuperation des différentes données
recuperation_clients = data.get_data(dossier_donnees, "list_clients")
recuration_produits = data.get_data(dossier_donnees, "list_product")
recuration_historiques = data.get_data(dossier_donnees, "list_history")

def ravitaillement():
    continuer = None
    while continuer != "":
        print(" ---------- Bienvenue dans ravitaillement  ----------")
    
        nom_produit = input("Veuillez entrer le nom du produit: ").lower()
        if nom_produit:
        
            # On verifie que l'utilisateur rentre bien un chiffre
            try:
                quantite_produit = int(input("Veuillez entrer la quantité: "))
            except ValueError:
                print("Vous devez saisir un nombre entre entier")
                continue
            else:
                
                if quantite_produit < 0:
                    print("Veuillez entrer une quantité supérieur à 0")
                    sleep(2)
                else:
                    # Création de l'instance qui va representer un produit
                    instance_produit = {"nom_produit": nom_produit, "quantite_produit": quantite_produit}  
    
                    if not recuration_produits:
                        recuration_produits.append(instance_produit)
                        print("Vous venez d'ajouter un nouveau produit")
                        data.recording_data(recuration_produits, dossier_actuel, "data", "list_product")
                        sleep(2)
                    else:
                        produit_existe = False
                        # On vérifie que le produit existe
                        for produit in recuration_produits:  
                            if nom_produit == produit["nom_produit"]: 
                                produit_existe = True
                                break
                    
                        quantite_total = produit["quantite_produit"] + quantite_produit
                    
                        if produit_existe:
                            produit["quantite_produit"] += quantite_produit
                            print(f"Vous venez d'ajout au stock de {nom_produit} {quantite_produit} autres {nom_produit}, le nouveau stock est de: {quantite_total} {nom_produit}")
                            sleep(3)
                        else:
                            recuration_produits.append(instance_produit)
                            print("Vous venez d'ajouter un nouveau produit")
                            sleep(3)  
                            
                    # On enregistre la liste des produits
                    data.recording_data(recuration_produits, dossier_actuel, "data", "list_product")
            
            continuer = input("Voulez vous continuer a vous ravitaillez ? Si oui taper une lettre au hasard, sinon taper entrer: ")
        else:
             print("Vous avez rien entré comme nom de produit")

def ajout_client():
    print(" ---------- Bienvenue dans ajouter un client  ----------")
        
    continuer = None
    while continuer != "":
        nom_client = input("Veuillez entrer le nom du client: ").lower()
        email_client = input("Veuillez entrer l'addresse mail du client: ").lower()
        
        if not nom_client or not email_client:
            print("Il a eu une erreur au niveau de la saisi de vôtre nom ou de l'addresse e-mail")
        else:
            # Création de l'instance qui va representer un client
            instance_client = {"nom": nom_client, "email": email_client}
            
            if not recuperation_clients:
                recuperation_clients.append(instance_client)
                print("Vous venez d'ajouter un nouveau client")
                sleep(2)
            else:
                client_existe = False
                for client in recuperation_clients:
                    if client["email"] == email_client:
                        client_existe = True
                        break
                
                if client_existe:
                    print("Vous ne pouvez pas utiliser cette addresse mail cas un clients a déjà été enregistré avec cette addresse mail")
                    sleep(3)
                else:
                    recuperation_clients.append(instance_client)
                    print("Vous venez d'ajouter un nouveau client")
                    sleep(2)
                    
            data.recording_data(recuperation_clients, dossier_actuel, "data", "list_clients")

        continuer = input("Voulez vous ajouter un autre client ? Si oui taper une lettre au hasard, sinon taper entrer: ")
    
def livraison():
        print(" ---------- Bienvenue dans effectuer une livraisonnt  ----------")
        
        continuer = None
        while continuer != "":
            print("Pour effectuer une livraison vous devez renseigner vôtre addresse mail et la liste des produits")                  
            mail_livraison = input("Veuillez saisir vôtre addresse mail: ")
            produit_livraison = input("Veuillez entrer le nom du produit a livrer: ").lower()
            
            try:
                quantite_livraison = int(input("Veuillez entrer la quantite a livrer: "))
            except ValueError:
                print("Veuillez saisir un nombre entier")
                sleep(1)
            else:
                historique_livraison = {
                    "email": mail_livraison, 
                    "produit": produit_livraison, 
                    "quantite_livraison": quantite_livraison
                }    
        
                # On verifie que le mail, produit et la quantité demandé existe
                mail_existe = produit_existe = False
                
                for mail_client in recuperation_clients:
                    if mail_client["email"] == mail_livraison:
                        mail_existe = True
                        break
                    
                for produit in recuration_produits:
                    if produit["nom_produit"] == produit_livraison:
                        produit_existe = True
                        break
                            
                quantite_existe = True if produit["quantite_produit"] >= quantite_livraison else False
                                            
                if not mail_existe:
                    print("L'addresse email est incorrecte")
                    sleep(1)

                elif not produit_existe:
                    print("Le produit que vous avez demandé n'existe pas")
                    sleep(1)
                    
                elif not quantite_existe:
                    print("La quantité que vous avez demandé est superieur a celle qui existe en stock")
                    sleep(1.5)
                
                else:
                    recuration_historiques.append(historique_livraison)
                    produit["quantite_produit"] -= quantite_livraison
                    data.recording_data(recuration_historiques, dossier_actuel, "data", "list_history")
                    data.recording_data(recuration_produits, dossier_actuel, "data", "list_product")
                    print("Vous venez d'effectuer une livraison")
                    sleep(2)

                continuer = input("Voulez vous effectuer une autre livraison ? Si oui taper une lettre au hasard, sinon taper entrer: ")
    
def historique():
    print(" ---------- Bienvenue dans l'historique  ----------")

    template_historique = """
    {}
    {}: {}
    -------------------------
    """

    historique = {}
    for historique_client in recuration_historiques:
        try:
            historique[historique_client["email"]][historique_client["produit"]] += historique_client["quantite_livraison"]                
        except KeyError:
            try:
                historique[historique_client["email"]].setdefault(historique_client["produit"], historique_client["quantite_livraison"])
            except KeyError:
                historique.setdefault(historique_client["email"], {historique_client["produit"]: historique_client["quantite_livraison"]})
    
    # Cette boucle va nous permetre d'afficher les produits
    for client in historique:    
        for produit, valeur in historique[client].items():
            print(template_historique.format(client, produit, valeur))
            sleep(0.5)

def affiche_stock():
    
    template_stocke = """
    {}: {}
    ---------------------
    """
    print("Les différent stock de produit sont: ")
    sleep(0.5)

    for produit in recuration_produits:
        print(template_stocke.format(produit["nom_produit"], produit["quantite_produit"]))
        sleep(0.5)

def editer_produit():
    continuer = None
    while continuer != "":
        nom_produit = input("Veuillez entrer le nom du produit a editer: ").lower() 
            
        produit_existe = False
        for produit in recuration_produits:
            if nom_produit == produit["nom_produit"]:
                produit_existe = True
                break
                
        if produit_existe:
            ancient_nom_produit = produit["nom_produit"]
            nouveau_nom_produit = input("Voulez vous éditer le nom du produit ? Si oui entrer le nouveau nom sinon taper entrer: ").lower()
            
            if nouveau_nom_produit != "":
                produit["nom_produit"] = nouveau_nom_produit
                data.recording_data(recuration_produits, dossier_actuel, "data", "list_product")
                print(f"Vous venez d'éditer le nom du produit {ancient_nom_produit} en {nouveau_nom_produit}")
                sleep(3)
            
            try:
                nouvelle_quantité = int(input("Voulez vous éditer la quantité  du produit ? Si oui entrer la nouvelle quantité sinon taper entrer: "))
            except ValueError:
                print("Vous devez entrer un nombre entier comme valeur")
                continue
            else:
                produit["quantite_produit"] = nouvelle_quantité
            data.recording_data(recuration_produits, dossier_actuel, "data", "list_product")

        else:
            print("Le nom du produit que vous avez entrer est introuvable")
            sleep(2)
            
        continuer = input("Voulez vous editer le nom d'un autre produit ? Si oui taper une lettre au hasrd sinon taper entrer: ") 

def editer_client():
    continuer = None
    while continuer != "":  
        nom_client = input("Veuillez entrer le nom du client: ").lower()
        email_client = input("Veuillez entrer l'email du client: ").lower()
        
        infos_existe = email_existe = False
        for client in recuperation_clients:
            if nom_client == client["nom"] and email_client == client["email"]:
                infos_existe = email_existe = True
                break
            
        if infos_existe and email_client:
            ancient_nom = client["nom"]
            nouveau_nom = input("Veuillez entrer le nouveau nom: ").lower()
            client["nom"] = nouveau_nom
            data.recording_data(recuperation_clients, dossier_actuel, "data", "list_clients")
            print(f"Vous venez de editer le nom de {ancient_nom} en {nouveau_nom}")
            sleep(3)
            
        continuer = input("Voulez vous editer un autres nom d'un autre produit ? Si oui taper entrer sinon taper une lettre au hasrd: ")
    
def fin_programmme():
    pass