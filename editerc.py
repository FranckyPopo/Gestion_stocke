from http import client
from tkinter import*
from turtle import heading

#C'est le titre de la page et la couleur de fond
client = Tk()
client.title("Gestion Des Stock")
client.configure(bg="#808080")
heading = Label(client, text= "Editer Un Client", bg="skyblue",highlightbackground="black", highlightthickness= 3, font="Roboto 20").pack(pady=30, ipadx=300, ipady=10)

#Création du cadre qui contiendra le nom du produit et la quantité du produit.
frame1 = Frame(client, highlightbackground="black", highlightthickness= 3)
frame1.pack(pady=30, ipadx=250, ipady=350)



#Condition pour affiche chaque produit avec sa quantité
nom_produit = StringVar()
quantite_produit = StringVar()

btn = Button(client, text="Editer", font= "Roboto 15",relief=FLAT, bg="skyblue", width=12, height=2).pack(pady= 20)
btn = Button(client,text="Retour à la page d'accueil", font= "Roboto 17",relief=FLAT, bg="skyblue", width=20, height=2).pack(pady= 30)

client.mainloop()