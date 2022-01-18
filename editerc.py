from cProfile import label
from tkinter import*
from turtle import right, width
import style

editerc = Tk()
editerc.title("Gestion Des Stock")
editerc.configure(bg="#808080")

frame = LabelFrame(editerc, text="Editer Un Client", bg="white",font="Roboto 20", pady=250, padx=150)
frame.pack(padx=50, pady=100)



btn = Button(frame, text="Retour à la page d'accueil", relief=FLAT, bg="skyblue").grid(row=5, column=1)

editerc.mainloop()