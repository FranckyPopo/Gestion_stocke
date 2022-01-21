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
afficher.geometry("800x800")
afficher.configure(bg="#808080")
heading = Label(afficher, text= "Afficher Le Stock", bg="skyblue",highlightbackground="black", highlightthickness= 3, font="Roboto 20").pack(pady=30, ipadx=300, ipady=10)

#Création du cadre qui contiendra le nom du produit et la quantité du produit.
frame1 = Frame(afficher, highlightbackground="black", highlightthickness= 1)
frame1.pack(pady=60, padx=20)

produit1 = Label(frame1, text="Produit: Mangue", font="Roboto 16")
quantite1 = Label(frame1, text="Quantite: 9", font="Roboto 16")
line1 = Label(frame1, text="-------------------------------")

produit2= Label(frame1,text="Produit: Pomme", font="Roboto 16")
quantite2 = Label(frame1, text="Quantite: 12", font="Roboto 16")
line2 = Label(frame1, text="-------------------------------")

produit3= Label(frame1,text="Nom: Banane ", font="Roboto 16")
quantite3= Label(frame1, text="Quantite: 34 ", font="Roboto 16")
line3 = Label(frame1, text="-------------------------------")

produit4 = Label(frame1,text="Produit :", font="Roboto 16")
quantite4 = Label(frame1, text="Quantite:", font="Roboto 16")
line4 = Label(frame1, text="-------------------------------")

produit5 = Label(frame1,text="Produit:", font="Roboto 16")
quantite5 = Label(frame1, text="Quantite:", font="Roboto 16")
line5= Label(frame1, text="-------------------------------")

produit1.grid(row=0 , column=0, sticky='w')
quantite1.grid(row=1 , column=0,sticky='w')
line1.grid(row=2 , column=0,sticky='w')

produit2.grid(row=3 , column=0, sticky='w')
quantite2.grid(row=4 , column=0,sticky='w')
line2.grid(row=5 , column=0,sticky='w')

produit3.grid(row=6 , column=0, sticky='w')
quantite3.grid(row=7 , column=0,sticky='w')
line3.grid(row=8, column=0,sticky='w')

produit4.grid(row=9 , column=0, sticky='w')
quantite4.grid(row=10 , column=0,sticky='w')
line4.grid(row=11 , column=0,sticky='w')

produit5.grid(row=12 , column=0, sticky='w')
quantite5.grid(row=13 , column=0,sticky='w')
line5.grid(row=14 , column=0,sticky='w')

#bouton pour revenir à la page d'accueil
btn = Button(afficher , text="Retour à la page d'accueil", font= "Roboto 17",relief=FLAT, bg="skyblue", highlightcolor="black", highlightthickness=2,  width=20, height=1).pack(pady= 75)

afficher.mainloop()