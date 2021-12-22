from time import sleep

message_bienvenue = """
---------- Bienvenue dans le menu de gestion de stock ----------
1- Se ravitailler 
2- Ajouter un client 
3- Effectuer une livraison 
4- Voir l'historique des livraisons
5- Afficher mon stock 
6- Editer un produit 
7- Editer un un client
8- Sortir
"""
print(message_bienvenue)
  
# Création des dictionnaires qui von contenir tout les produits et clients
listes_produits = [
    # {"nom_produit": "orange", "quantite_produit": 10}, 
    # {"nom_produit": "fraise", "quantite_produit": 10},
    # {"nom_produit": "pomme", "quantite_produit": 15} 
]

listes_clients = [{"nom": "afri", "email": "afrifranck2003@gmail.com"}, {"nom": "popo", "email": "popo@gmail.com"}]
historiques = [
    # {"email": "afrifranck2003", "produit": "pomme", "quantite_livraison": 12},
    # {"email": "afrifranck2003", "produit": "viande", "quantite_livraison": 100},
    # {"email": "afrifranck2003", "produit": "pomme", "quantite_livraison": 18},
    # {"email": "afrifranck2003", "produit": "orange", "quantite_livraison": 2},
    # {"email": "afrifranck2003", "produit": "orange", "quantite_livraison": 3},

    # {"email": "popo@gmail.com", "produit": "fraise", "quantite_livraison": 2},
    # {"email": "popo@gmail.com", "produit": "fraise", "quantite_livraison": 8},
    # {"email": "popo@gmail.com", "produit": "banane", "quantite_livraison": 12},
    # {"email": "popo@gmail.com", "produit": "banane", "quantite_livraison": 3},  
]

stock_client = """
Nom produit: {}
Quantiter: {}

---------------------
"""

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
                        
                    # Création de l'instance qui va representer un produit
                    instance_produit = {"nom_produit": nom_produit, "quantite_produit": quantite_produit}  
                    
                    if not listes_produits:
                        listes_produits.append(instance_produit)
                        print("Vous venez d'ajouter un nouveau produit")
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
                print("Il a eu une erreur au niveau de la saisit de vôtre nom ou de l'addresse e-mail: ")
            else:
                # Création de l'instance qui va representer un client
                instance_client = {"nom": nom_client, "email": email_client}
                
                if not listes_clients:
                    listes_clients.append(instance_client)
                    print("Vous venez d'ajouter un nouveau client")
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
                        print("Vous venez d'ajouter un nouveau client")
                        sleep(3)

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
                mail_existe = produit_existe = quantite_existe = False
                
                for mail_client in listes_clients:
                    if mail_client["email"] == mail_livraison:
                        mail_existe = True
                        break
                    
                for produits in listes_produits:
                    if produits["nom_produit"] == produit_livraison:
                        produit_existe = True
                        break
                
                for quantite in listes_produits:    
                    if quantite["quantite_produit"] >= quantite_livraison:
                        quantite_existe = True
                        break
                    
                print(f"le variable produit existe a pour valeur: {produit_existe}")
                    
                if not mail_existe:
                    print("L'addresse email est incorrecte")
                    sleep(2)
                    continue

                elif not produit_existe:
                    print("Le produit que vous avez demandé n'existe pas")
                    sleep(2)
                    continue
                    
                elif not quantite_existe:
                    print("La quantité que vous avez demandé est superieur a celle qui existe")
                    sleep(2)
                    continue
                else:
                    
                    # On verifie que la quantité a livrer existe
                    if produits["quantite_produit"] > 0:
                        historiques.append(historique_livraison)
                        produits["quantite_produit"] -= quantite_livraison
                        print("Vous venez d'effectuer un livraison")
                        sleep(2)
                    else:
                        print("La quantité que vous avez démander est suppérieur a celle en stock")
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
                nouveau_nom_produit = input("Veuillez entrer le nouveau nom du produit: ").lower()
                produit["nom_produit"] = nouveau_nom_produit
                print(f"Vous venez de editer le nom du produit {ancient_nom_produit} en {nouveau_nom_produit}")
                sleep(3)
            else:
                print("Le nom du produit que vous avez entrer est introuvable")
            
            continuer = input("Voulez vous editer une le nom d'un autre produit ? Si oui taper entrer sinon taper une lettre au hasrd: ") 

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
    "8": exit
}

while True:
    option = input("Veuillez choisir un option: ")
    OPTIONS_MENU.get(option, erreur)()
