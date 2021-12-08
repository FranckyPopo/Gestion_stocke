from time import sleep

print("---------- Bienvenue dans le menu de gestion de stock ----------")

# Création des dictionnaires qui va contenir tout les produits et clients
listes_produits = {}
listes_clients = {}

while True:
    print("1- Se ravitailler")
    print("2- Ajouter un client")
    print("3- Effectuer une livraison")
    print("4- Voir l'historique des livraisons")
    
    choix = int(input())

    if choix == 1:
        print("Pour vous raitaller vous devez entrer le nom du produit et la quantité")
        
        produit = input("Veuillez entrer le nom du produit: ").lower()
        quantité = int(input("Veuillez entrer la quantité: "))
        
        # On ajoute ou nous fesons la mise a jour du produit
        if listes_produits.get(produit):
            listes_produits[produit] += quantité
        else:
            listes_produits[produit] = quantité
        print(listes_produits)
            
    elif choix == 2:                    
        print("Pour ajouter un client vous devez entrer sont nom et une addresse mail unique")

        nom_client = input("Veuillez entrer le nom du client: ")
        email_client = input("Veuillez entrer l'addresse mail du client: ")
        
        # On vérifie que l'addresse email du client n'est pas utiliser pas un autres client 
        if email_client not in listes_clients.values():
            listes_clients[nom_client] = email_client
            print("Vous venez d'enregistrer un nouveau client")
            
            sleep(3)
        else:
            print("Imposible de vous enregistrer cas cette addresse mail a déja été utiliser pour un autres client")
            
    elif choix == 3:
        print("Pour affectuer une livraison vous devez entrer le nom du produit ainsi que la quantité")
        
        while True:
            email_livraison = input("Veuillez entrer vôtre addresse email pour effectuer la livraison: ")
            
            if email_livraison in listes_clients.values():
                produit_livraison = input("Veuillez entrer le nom du produit: ")
                
                if produit_livraison in listes_produits.keys():
                    
                    if bool(produit_livraison) == False:
                            print("Livraison effectué avec succès")
                            break
                    
                    # On vérifie que l'utilisateur ne saisise pas autres choses que des chiffres 
                    try:
                        quantite_produit_livraison = int(input("Veuillez entrer la quantité du produit a livrer: ")) 

                    except ValueError:
                        print("Vous de devez saisir un nombre entier comme quantité du produit a livrer")

                    else: 
                        
                        # On verifie la quantité de la livraison
                        if listes_produits[produit_livraison] > quantite_produit_livraison:
                            listes_produits[produit_livraison] -= quantite_produit_livraison
                        else:
                            print("La quantité du produit en stocke est inférieur a celle demandé")
                            break
                        
                else:
                    print("Le produit n'est pas en stocke")
                    break
                                     
            else:
                print("Cette addresse mail n'est pas associé a un client, veuillez enregistrer Cette addresse mail en tan que client")    
                sleep(3)
                break
        