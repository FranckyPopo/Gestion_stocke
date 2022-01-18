from cProfile import label
from cgitb import text
from email import header
from tkinter import*
from turtle import right, width
import style

afficher = Tk()
afficher.title("Gestion Des Stock")
afficher.configure(bg="#808080")

heading = Label(afficher, text= "Afficher Le Stock", bg="skyblue",highlightbackground="black", highlightthickness= 3, font="Roboto 20").pack(pady=50, ipadx=300, ipady=10)

frame = Frame(afficher, highlightbackground="black", highlightthickness= 3)
frame.pack(pady=50, ipadx=100, ipady=200)

liste = Label(frame, text="La liste Des Produits", font="Roboto 20",).grid(row=0, column=0)

btn = Button(frame, text="Retour à la page d'accueil", relief=FLAT, bg="skyblue", width=20, height=3)

afficher.mainloop()