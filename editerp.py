from cProfile import label
from cgitb import text
from email import header
from tkinter import*
from turtle import right, width
import style

editerp = Tk()
editerp.title("Gestion Des Stock")
editerp.configure(bg="#808080")

heading = Label(editerp, text= "Editer Un Produit", bg="skyblue",highlightbackground="black", highlightthickness= 3, font="Roboto 20").pack(pady=50, ipadx=300, ipady=10)

frame1 = Frame(editerp, width=100, height=100, highlightbackground="black", highlightthickness= 3)
frame2 = Frame(editerp, width=100, height=100, highlightbackground="black", highlightthickness= 3)
frame1.pack()
frame2.pack()



editerp.mainloop()