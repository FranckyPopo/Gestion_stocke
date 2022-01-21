from cProfile import label
from http import client
from os import name
from pydoc import text
from tkinter import*
from turtle import heading, left

#C'est le titre de la page et la couleur de fond
editerp = Tk()
editerp.title("Gestion De Stock")
editerp.geometry("800x800")
editerp.resizable(False,False)
heading = Label(editerp, text= "Editer Un Produit", bg="skyblue",highlightbackground="black", highlightthickness= 2, font="Roboto 20").pack(pady=50, ipadx=300, ipady=10)

frame1 = Frame(editerp, highlightbackground="black", highlightthickness= 1)
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


#Cre------------
def open():    
    top = Toplevel()
    top.title("Gestion Des Stock")
    top.resizable(False,False)
    top.geometry("800x800")
    heading1 = Label(top, text= "Modification Du Produit", bg="skyblue",highlightbackground="black", highlightthickness= 2, font="Roboto 20").pack(pady=50, ipadx=250, ipady=10)

    frame2 = Frame(top,highlightbackground="black", highlightthickness= 2)
    frame2.pack(pady=60)
    lbl1 = Label(frame2, text="Veuillez saisir l'ancien nom du produit: ", font="Roboto 15")
    lbl2 = Label(frame2, text="Veuillez saisir l'ancien quantite du produit: ", font="Roboto 15")
    lbl3 = Label(frame2, text="Veuillez saisir le nouveau nom du produit: ", font="Roboto 15")
    lbl4 = Label(frame2, text="Veuillez saisir le nouvelle quantite du produit: ",font= "Roboto 15")

    entry1 = Entry(frame2)
    entry2 = Entry(frame2)
    entry3 = Entry(frame2)
    entry4 = Entry(frame2)

    btn_enregister = Button(frame2 , text="  Enregistrer  ", font= "Roboto 15" , relief=FLAT, bg="skyblue", width=10, height=2)

    lbl1.grid(row=0 , column=0, sticky='w')
    lbl2.grid(row=2 , column=0,sticky='w')
    lbl3.grid(row=4 , column=0,sticky='w')
    lbl4.grid(row=6 , column=0,sticky='w')

    entry1.grid(row=1 , column=0, sticky='w')
    entry2.grid(row=3 , column=0, sticky='w')
    entry3.grid(row=5 , column=0, sticky='w')
    entry4.grid(row=7 , column=0, sticky='w')

    btn_enregister.grid(row=8, columnspan=1, sticky='NSEW')

btn_editer = Button(frame1, command=open, text="  Editer  ", font= "Roboto 15", relief=FLAT, bg="skyblue", width=10, height=2, highlightthickness=1)
btn_editer.grid(row=15, columnspan=1, sticky='NSEW')
btn_accueil = Button(editerp,text="Retour à la page d'accueil", font= "Roboto 15", relief=FLAT, bg="skyblue", width=20, height=2 ).pack(pady= 30)

editerp.mainloop()