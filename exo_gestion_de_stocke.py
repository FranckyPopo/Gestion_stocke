from time import sleep

print("---------- Bienvenue dans le menu de gestion de stock ----------")

# Création des dictionnaires qui va contenir tout les produits et clients
listes_produits = []
listes_clients = []
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
                        
                        # On vérifie que le produit existe
                        for produit in listes_produits:  
                            produit_existe = True if nom_produit == produit["nom_produit"] else False
                    
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
                
                for client in listes_clients:
                    client_existe = True if client["email"] == email_client else False
                
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
            
    # elif option == 3:
    #     print("Pour affectuer une livraison vous devez entrer le nom du produit ainsi que la quantité")
        
    #     while True:
    #         email_livraison = input("Veuillez entrer vôtre addresse email pour effectuer la livraison: ")
            
    #         if email_livraison in listes_clients.values():
                
    #             produit_livraison = input("Veuillez entrer le nom du produit a livrer : ").lower()
                
    #             if produit_livraison in listes_produits.keys():
                                
    #                 On vérifie que l'utilisateur ne saisise pas autres choses que des chiffres 
    #                 try:
    #                     quantite_produit_livraison = int(input("Veuillez entrer la quantité du produit a livrer: ")) 

    #                 except ValueError:
    #                     print("Vous de devez saisir un nombre entier comme quantité du produit a livrer")

    #                 else: 
    #                     On verifie la quantité de la livraison
    #                     if listes_produits[produit_livraison] >= quantite_produit_livraison:
    #                         listes_produits[produit_livraison] -= quantite_produit_livraison      

    #                         Cette gérer l'historique de livrason
    #                         On recupere l'index de notre client
    #                         index = liste_emails.index(email_livraison)
                            
    #                         On ajoute la livraison a l'historique de livraison
    #                         historique_client = {"mail": email_livraison, "liste_produits_livre": {produit_livraison: quantite_produit_livraison}}
                            

    #                         On gére l'ajout des historiques
    #                         if (bool(historiques) == False):
    #                             print("condition 1")
    #                             historiques.append(historique_client)
                                
    #                         elif bool(historiques):
    #                             if email_livraison not in liste_emails:
                                  
    #                                 historiques.append(historique_client)  
                                
    #                         On gére l'ajout et mise a jour d'un nouveau produit
    #                         if produit_livraison not in historiques[index]["liste_produits_livre"].keys():
    #                             historiques[index]["liste_produits_livre"][produit_livraison] = quantite_produit_livraison
                                
    #                         elif produit_livraison in historiques[index]["liste_produits_livre"].keys():
    #                             historiques[index]["liste_produits_livre"][produit_livraison] += quantite_produit_livraison
                            
                            
                                                                                          
    #                         print(historiques)
                                    
    #                         continuer = input("Voulez vous effectuer un autres livraison ? : ").upper()
    #                         if continuer == "":
    #                             sleep(3)
    #                             print("Felicitation vôtre livraison a bien été effectué")
    #                             break
                            
    #                     else:
    #                         print("La quantité du produit en stocke est inférieur a celle demandé")
    #                         break
                        
    #             else:
    #                 print("Le produit n'est pas en stock")
    #                 break
                                     
    #         else:
    #             print("Cette addresse mail n'est pas associé a un client, veuillez enregistrer cette addresse mail en tan que client")    
    #             sleep(3)
    #             break
    
    # elif option == 4:
    #     pass
    
