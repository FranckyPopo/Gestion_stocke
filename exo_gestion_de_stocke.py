from time import sleep

print("---------- Bienvenue dans le menu de gestion de stock ----------")

# Création des dictionnaires qui va contenir tout les produits et clients
listes_produits = [
    {"nom_produit": "orange", "quantite_produit": 10}, 
    {"nom_produit": "fraise", "quantite_produit": 10},
    {"nom_produit": "pomme", "quantite_produit": 15} 
]

listes_clients = [{"nom": "afri", "email": "afrifranck2003@gmail.com"}, {"nom": "popo", "email": "popo@gmail.com"}]
historiques = []

while True:
    print("1- Se ravitailler")
    print("2- Ajouter un client")
    print("3- Effectuer une livraison")
    print("4- Voir l'historique des livraisons")
  
    option = int(input("Veuillez choisir une option: "))

    if option == 1:
      
        while True:
        
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
                        sleep(3)  
                    else:
                        
                        produit_existe = False
                        # On vérifie que le produit existe
                        for produit in listes_produits:  
                            if nom_produit == produit["nom_produit"]: 
                                produit_existe = True
                                break
                    
                        quantite_total = produit["quantite_produit"] + quantite_produit
                    
                        if produit_existe:
                            print(f"Vous venez d'ajout au stock de {nom_produit} {quantite_produit} autres {nom_produit}, le nouveau stock est de: {quantite_total} {nom_produit}")
                            produit["quantite_produit"] += quantite_produit
                            sleep(3)
                        else:
                            listes_produits.append(instance_produit)
                            print("Vous venez d'ajouter un nouveau produit")
                            sleep(3)  
                
                continuer = input("Voulez vous continuer ? Si oui taper une lettre au hasard, sinon taper entrer: ")
                if not continuer:
                    break
            else:
                print("Vous avez rien entré comme nom de produit")
                                                 
    elif option == 2:                    
        while True:
            nom_client = input("Veuillez entrer le nom du client: ")
            email_client = input("Veuillez entrer l'addresse mail du client: ")
            
            # Création de l'instance qui va representer un client
            instance_client = {"nom": nom_client, "email": email_client}
            
            if not listes_clients:
                listes_clients.append(instance_client)
                print("Vous venez d'ajouter un nouveau client")
                sleep(3)
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

            continuer = input("Voulez vous continuer a ajouter des client ? Si oui taper une lettre au hasard, sinon taper entrer: ")
            if not continuer:
                break
                
            print(listes_clients)
            
    elif option == 3:
        
        while True:
            print("Pour effectuer une livraison vous devez renseigner vôtre addresse mail et la liste des produits")
                                 
            mail_livraison = input("Veuillez saisir vôtre addresse mail: ")
            produit_livraison = input("Veuillez entrer le nom du produit a livrer: ").lower()
            print(produit_livraison)
            
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
                    print("La quantité que vous avez demandé est superieur a celle qui existe,")
                    sleep(2)
                    continue
                else:
                    historiques.append(historique_livraison)
                    produits["quantite_produit"] -= quantite_livraison
                    print("Vous venez d'effectuer un livraison")
                    sleep(2)
  
                continuer = input("Voulez vous effectuer une autre livraison ? Si oui taper une lettre au hasard, sinon taper entrer: ")
                if not continuer:
                    break
                
                print(historiques)
                
    elif option == 4:
        pass