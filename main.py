from time import sleep
import os
import json

stock_client = """
Nom produit: {}
Quantiter: {}

---------------------
"""

message_bienvenue = """
---------- Bienvenue dans le menu de gestion de stock ----------
1- Se ravitailler 
2- Ajouter un client 
3- Effectuer une livraison 
4- Voir l'historique des livraisons
5- Afficher mon stock 
6- Editer un produit 
7- Editer un client
8- Sortir
"""
print(message_bienvenue)

# Création du dossier qui va contenir les données importante du programme
# On récupere le chemin du fichier et on extrait le chemin du dossier parent
chemin_fichier = os.path.realpath(__file__)
chemin_repetoire = os.path.dirname(chemin_fichier)

# Création du dossier
dossier = os.path.join(chemin_repetoire, "donnees")

if not os.path.exists(dossier):
    os.makedirs(dossier)

    # Création des trois fichier qui von stocker les informations de l'utilisateur
    fichiers = ["liste_clients.json", "liste_produits.json", "liste_historiques.json"]
    for nom_fichier in fichiers:
        chemin_dossier = dossier + "/" + nom_fichier
        with open(chemin_dossier, "w") as fichier:
            pass

def enregistrement_donnees(donnees_enregistrer, fichier):
    """
    Cette fonction a pour bute d'enregistrer des données dans un fichier json     

    Args:
        donnees_enregistrer (str, int, bool, list, dict, tuple...): Ce paramétre prend tous sorte de type de données
        fichier (str): Ce paramétre prend le chemint du fichier json qui va stocker les données
    """
    
    chemin_dossier = dossier + "/" + fichier
    try:
        os.path.getsize(chemin_dossier)
    except OSError:
        print("Chemin introuvable ! Veuillez vérifiez le nom du fichier")
    else:     
        with open(chemin_dossier, "w") as f:
            json.dump(donnees_enregistrer, f, indent=4)
        
def recuperation_donnees(fichier):
    """
    Cette fonction a pour bute de récupérer les données dans un fichier json 

    Args:
        fichier (str): Ce paramétre prend le chemint du fichier json qui contient les données

    Returns:
        str, int, bool, list, dict, tuple...: La fonction nous retourne tout le contenue qui se trouve dans le fichier json
    """
    
    chemin_dossier = dossier + "/" + fichier
    try:
        os.path.getsize(chemin_dossier)
    except OSError:
        print("Chemin introuvable ! Veuillez vérifiez le nom du fichier")
    else:
        with open(chemin_dossier, "r") as f:
            if os.path.getsize(chemin_dossier) == 0:
                return []
            return json.load(f)

while True:
    # Récupération des données dans les fichiers json
    listes_produits = recuperation_donnees("liste_produits.json")
    listes_clients = recuperation_donnees("liste_clients.json")
    historiques = recuperation_donnees("liste_historiques.json")  
         
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
        
                        if not listes_produits:
                            listes_produits.append(instance_produit)
                            print("Vous venez d'ajouter un nouveau produit")
                            enregistrement_donnees(listes_produits, "liste_produits.json")
                            sleep(2)  
                        else:
                            produit_existe = False
                            # On vérifie que le produit existe
                            for produit in listes_produits:  
                                if nom_produit == produit["nom_produit"]: 
                                    produit_existe = True
                                    break
                        
                            quantite_total = produit["quantite_produit"] + quantite_produit
                        
                            if produit_existe:
                                produit["quantite_produit"] += quantite_produit
                                print(f"Vous venez d'ajout au stock de {nom_produit} {quantite_produit} autres {nom_produit}, le nouveau stock est de: {quantite_total} {nom_produit}")
                                sleep(3)
                            else:
                                listes_produits.append(instance_produit)
                                print("Vous venez d'ajouter un nouveau produit")
                                sleep(3)  
                                
                            # On enregistre la liste des produits
                            enregistrement_donnees(listes_produits, "liste_produits.json")
                
                continuer = input("Voulez vous continuer a vous ravitaillez ? Si oui taper une lettre au hasard, sinon taper entrer: ")
                
            else:
                print("Vous avez rien entré comme nom de produit")

    def ajout_client():
        print(" ---------- Bienvenue dans ajouter un client  ----------")
            
        continuer = None
        while continuer != "":
            
            nom_client = input("Veuillez entrer le nom du client: ").lower()
            email_client = input("Veuillez entrer l'addresse mail du client: ").lower()
            
            if nom_client == "" or email_client == "":
                print("Il a eu une erreur au niveau de la saisi de vôtre nom ou de l'addresse e-mail")
            else:
                # Création de l'instance qui va representer un client
                instance_client = {"nom": nom_client, "email": email_client}
                
                if not listes_clients:
                    listes_clients.append(instance_client)
                    print("Vous venez d'ajouter un nouveau client")
                    enregistrement_donnees(listes_clients, "liste_clients.json")
                    sleep(2)
                else:
                    client_existe = False
                    for client in listes_clients:
                        if client["email"] == email_client:
                            client_existe = True
                            break
                    
                    if client_existe:
                        print("Vous ne pouvez pas utiliser cette addresse mail cas un clients a déjà été enregistré avec cette addresse mail")
                        sleep(3)
                    else:
                        listes_clients.append(instance_client)
                        enregistrement_donnees(listes_clients, "liste_clients.json")
                        print("Vous venez d'ajouter un nouveau client")
                        sleep(2)

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
                    sleep(2)
                else:
                    historique_livraison = {
                        "email": mail_livraison, 
                        "produit": produit_livraison, 
                        "quantite_livraison": quantite_livraison
                    }    
            
                    # On verifie que le mail, produit et la quantité demandé existe
                    mail_existe = produit_existe = False
                    
                    for mail_client in listes_clients:
                        if mail_client["email"] == mail_livraison:
                            mail_existe = True
                            break
                        
                    for produit in listes_produits:
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
                        print(listes_produits[0]["quantite_produit"])
                        historiques.append(historique_livraison)
                        produit["quantite_produit"] -= quantite_livraison
                        enregistrement_donnees(historiques, "liste_historiques.json")
                        enregistrement_donnees(listes_produits, "liste_produits.json")
                        print("Vous venez d'effectuer une livraison")
                        sleep(2)
    
                    continuer = input("Voulez vous effectuer une autre livraison ? Si oui taper une lettre au hasard, sinon taper entrer: ")
        
    def historique():
        print(" ---------- Bienvenue dans l'historique  ----------")
  
        historique = {}
        for historique_client in historiques:
            try:
                historique[historique_client["email"]][historique_client["produit"]] += historique_client["quantite_livraison"]                
            except KeyError:
                try:
                    historique[historique_client["email"]].setdefault(historique_client["produit"], historique_client["quantite_livraison"])
                except KeyError:
                    historique.setdefault(historique_client["email"], {historique_client["produit"]: historique_client["quantite_livraison"]})
        
        # Cette boucle va nous permetre d'afficher les produits
        for client in historique:
            print(f"{client} ")
            sleep(0.5)
                
            for produit, valeur in historique[client].items():
                print(f"{produit} : {valeur}")
                sleep(0.5)

    def affiche_stock():
            print("Les différent stock de produit sont: ")
            sleep(0.5)

            for produit in listes_produits:
                print(stock_client.format(produit["nom_produit"], produit["quantite_produit"]))
                sleep(0.5)
        
    def editer_produit():
        continuer = None
        while continuer != "":
            nom_produit = input("Veuillez entrer le nom du produit a editer: ").lower() 
                
            produit_existe = False
            for produit in listes_produits:
                if nom_produit == produit["nom_produit"]:
                    produit_existe = True
                    break
                    
            if produit_existe:
                ancient_nom_produit = produit["nom_produit"]
                nouveau_nom_produit = input("Voulez vous éditer le nom du produit ? Si oui entrer le nouveau nom sinon taper entrer: ").lower()
                
                if nouveau_nom_produit != "":
                    produit["nom_produit"] = nouveau_nom_produit
                    enregistrement_donnees(listes_produits, "liste_produits.json")
                    print(f"Vous venez d'éditer le nom du produit {ancient_nom_produit} en {nouveau_nom_produit}")
                    sleep(3)
                
                try:
                    nouvelle_quantité = int(input("Voulez vous éditer la quantité  du produit ? Si oui entrer la nouvelle quantité sinon taper entrer: "))
                except ValueError:
                    print("Vous devez entrer un nombre entier comme valeur")
                    continue
                else:
                    if nouvelle_quantité != "":
                        produit["quantite_produit"] = nouvelle_quantité
                        enregistrement_donnees(listes_produits, "liste_produits.json")

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
            for client in listes_clients:
                if nom_client == client["nom"] and email_client == client["email"]:
                    infos_existe = email_existe = True
                    break
                
            if infos_existe and email_client:
                ancient_nom = client["nom"]
                nouveau_nom = input("Veuillez entrer le nouveau nom: ").lower()
                client["nom"] = nouveau_nom
                enregistrement_donnees(listes_clients, "liste_clients.json")
                print(f"Vous venez de editer le nom de {ancient_nom} en {nouveau_nom}")
                sleep(3)
                
            continuer = input("Voulez vous editer un autres nom d'un autre produit ? Si oui taper entrer sinon taper une lettre au hasrd: ")
        
    def fin_programmme():
        print("Fermeture du programme")
        exit()

    def erreur():
        print("Erreur")
        
    OPTIONS_MENU = {
        "1": ravitaillement,
        "2": ajout_client,
        "3": livraison,
        "4": historique,
        "5": affiche_stock,
        "6": editer_produit,
        "7": editer_client,
        "8": fin_programmme   
    }

    option = input("Veuillez choisir un option: ")
    OPTIONS_MENU.get(option, erreur)()
