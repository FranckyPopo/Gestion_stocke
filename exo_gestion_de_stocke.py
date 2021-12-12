from time import sleep

print("---------- Bienvenue dans le menu de gestion de stock ----------")

# Création des dictionnaires qui va contenir tout les produits et clients
listes_produits = [{"nom_produit": "pomme", "quantité_produit": 5}]
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
            
            # On verifie que l'utilisateur rentre bien un chiffre
            try:
                quantité_produit = int(input("Veuillez entrer la quantité: "))
            except ValueError:
                print("Vous devez saisir un nombre entre entier")
            else:
     
                if bool(nom_produit):
                    
                    if bool(listes_produits) == False:
                        instance_produit = {"nom_produit": nom_produit, "quantité_produit": quantité_produit} 
                        listes_produits.append(instance_produit)
                        
                        print("Vous avez ajouter d'ajour un nouveau produit")
                        sleep(3)
                        
                    else:
                        i = 0
                        for produit in listes_produits:
                            i += 1
                            # On ajoute ou nous fesons la mise a jour du produit
                            if produit["nom_produit"] == nom_produit:
                                print(i)
                                listes_produits[i-1]["quantité_produit"] += quantité_produit
                            else:
                                
                                instance_produit = {"nom_produit": nom_produit, "quantité_produit": quantité_produit} 
                                listes_produits.append(instance_produit)
                                
                                print("Vous avez ajouter d'ajour un nouveau produit")
                            
                                sleep(3)
                        
                    print(listes_produits)
                    
                    continuer = input("Voulez vous continuer a ajouter des produits ? si oui taper une lettre au hasard sinon taper entrer: ")
                    
                    if continuer == "":
                        break
                else:
                    print("Vous devez saisir, un nom de produit")
               
    elif option == 2:                    
        print("Pour ajouter un client vous devez entrer sont nom et une addresse mail unique")

        while True:
            nom_client = input("Veuillez entrer le nom du client: ")
            email_client = input("Veuillez entrer l'addresse mail du client: ")
            
            #On vérifie que l'addresse email du client n'est pas utiliser pas un autres client 
            if email_client not in listes_clients.values():
                listes_clients[nom_client] = email_client
                print("Vous venez d'enregistrer un nouveau client")
                
                #On ajoute l'email
                #liste_emails.append(email_client)
                
                #On créé un nouvelle historique
                historique_client = {"mail": email_client, "liste_produits_livre": {None}}
                historiques.append(historique_client)
                                
                sleep(3)
            else:
                print("Imposible de vous enregistrer cas cette addresse mail a déja été utiliser pour un autres client")
                
            continuer = input("Voulez vous continuer a ajouter un client ? si taper une lettre au hasard sinon taper entrer : ").upper()
            if continuer == "":
                break
            
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
    
