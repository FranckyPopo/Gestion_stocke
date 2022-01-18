from cProfile import label
from tkinter import*
from turtle import right, width
import style

graphics = Tk()
graphics.title("Gestion Des Stock")
graphics.configure(bg="#808080")

frame = LabelFrame(graphics, text="Afficher Le Stock", bg="white",font="Roboto 20", pady=250, padx=150)
frame.pack(padx=50, pady=100)

btn = Button(frame, text="Retour à la page d'accueil", relief=FLAT, bg="skyblue").grid(row=5, column=1)

graphics.mainloop()