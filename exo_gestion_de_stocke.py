from time import sleep

print("---------- Bienvenue dans le menu de gestion de stock ----------")

# Création des dictionnaires qui von contenir tout les produits, clients et autres
listes_produits = {"pomme": 10, "carote": 50}
listes_clients = {"afri": "afri@gmail.com", "popo": "popo@gmail.com"}
liste_emails = ["afri@gmail.com", "popo@gmail.com"]
historiques = []

while True:
    print("1- Se ravitailler")
    print("2- Ajouter un client")
    print("3- Effectuer une livraison")
    print("4- Voir l'historique des livraisons")
    
    
    choix = int(input())

    if choix == 1:
        print("Pour vous raitaller vous devez entrer le nom du produit et la quantité")
        
        while True:
            produit = input("Veuillez entrer le nom du produit: ").lower()
            quantité = int(input("Veuillez entrer la quantité: "))
            
            # On ajoute ou nous fesons la mise a jour du produit
            if listes_produits.get(produit):
                listes_produits[produit] += quantité
            else:
                listes_produits[produit] = quantité
            print(listes_produits)
            
            continuer = input("Voulez vous continuer a ajouter des produits ? si taper une lettre au hasard sinon taper entrer: ").upper()
            if continuer == "":
                break
               
    elif choix == 2:                    
        print("Pour ajouter un client vous devez entrer sont nom et une addresse mail unique")

        while True:
            nom_client = input("Veuillez entrer le nom du client: ")
            email_client = input("Veuillez entrer l'addresse mail du client: ")
            
            # On vérifie que l'addresse email du client n'est pas utiliser pas un autres client 
            if email_client not in listes_clients.values():
                listes_clients[nom_client] = email_client
                print("Vous venez d'enregistrer un nouveau client")
                
                # On ajoute l'email
                liste_emails.append(email_client)
                                
                sleep(3)
            else:
                print("Imposible de vous enregistrer cas cette addresse mail a déja été utiliser pour un autres client")
                
            continuer = input("Voulez vous continuer a ajouter un client ? si taper une lettre au hasard sinon taper entrer : ").upper()
            if continuer == "":
                break
            
    elif choix == 3:
        print("Pour affectuer une livraison vous devez entrer le nom du produit ainsi que la quantité")
        
        while True:
            email_livraison = input("Veuillez entrer vôtre addresse email pour effectuer la livraison: ")
            
            if email_livraison in listes_clients.values():
                
                produit_livraison = input("Veuillez entrer le nom du produit a livrer : ").lower()
                
                if produit_livraison in listes_produits.keys():
                                
                    # On vérifie que l'utilisateur ne saisise pas autres choses que des chiffres 
                    try:
                        quantite_produit_livraison = int(input("Veuillez entrer la quantité du produit a livrer: ")) 

                    except ValueError:
                        print("Vous de devez saisir un nombre entier comme quantité du produit a livrer")

                    else: 
                        # On verifie la quantité de la livraison
                        if listes_produits[produit_livraison] >= quantite_produit_livraison:
                            listes_produits[produit_livraison] -= quantite_produit_livraison
                            
                            
                            index = liste_emails.index(email_livraison)

                            # On recupere l'index de notre client
                            # ce bout de code n'est pas utile, tu peut le supprimer si tu veux
                            if email_livraison in liste_emails:
                                print("l'index existe")
                                print(index)
                            
                            # On ajoute la livraison a l'historique de livraison
                            historique_client = {"mail": email_livraison, "liste_produits_livre": {produit_livraison: quantite_produit_livraison}}
                            
                            # On ajoute un etudiant s'il n'existe pas 

                            # On ajout ou mise a jour du produit selectionné 
                            if (bool(historiques) == False) or (email_livraison not in liste_emails):
                                print("condition 1")
                                historiques.append(historique_client)
                                
                            elif produit_livraison not in historiques[index]["liste_produits_livre"].keys():
                                print("condition 2")
                                historiques[index]["liste_produits_livre"][produit_livraison] = quantite_produit_livraison
                                
                            else:

                                pass
                                #historiques[i]["liste_produits_livre"][produit_livraison] += quantite_produit_livraison
                            
                            print(historiques)
                                    
                            continuer = input("Voulez vous effectuer un autres livraison ? : ").upper()
                            if continuer == "":
                                break
                            
                        else:
                            print("La quantité du produit en stocke est inférieur a celle demandé")
                            break
                        
                else:
                    print("Le produit n'est pas en stock")
                    break
                                     
            else:
                print("Cette addresse mail n'est pas associé a un client, veuillez enregistrer cette addresse mail en tan que client")    
                sleep(3)
                break
    
    elif choix == 4:
        pass
    
