from asyncore import write
from cProfile import label
from cgitb import text
from email import header
from re import template
from tkinter import*
from turtle import right, width
import style

#C'est le titre de la page et la couleur de fond
afficher = Tk()
afficher.title("Gestion Des Stock")
afficher.configure(bg="#808080")
heading = Label(afficher, text= "Afficher Le Stock", bg="skyblue",highlightbackground="black", highlightthickness= 3, font="Roboto 20").pack(pady=30, ipadx=300, ipady=10)

#Création du cadre qui contiendra le nom du produit et la quantité du produit.
frame = Frame(afficher, highlightbackground="black", highlightthickness= 3)
frame.pack(pady=30, ipadx=250, ipady=350)

#Condition pour affiche chaque produit avec sa quantité
nom_produit = StringVar()
quantite_produit = StringVar()

# template_stocke = """
#     {}:{}
#     ---------------
#     """
# for produit in recuration_produits:
#     produit_label = Text(frame,"Produit: %s\nQuantité: %s\n--------------" % (nom_produit.get(),quantite_produit.get()))
    
#bouton pour revenir à la page d'accueil
btn = Button(afficher , text="Retour à la page d'accueil", font= "Roboto 17",relief=FLAT, bg="skyblue", width=20, height=3).pack(pady= 75)

afficher.mainloop()