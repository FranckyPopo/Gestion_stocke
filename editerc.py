from cProfile import label
from tkinter import*
from turtle import right, width
import style

editerc = Tk()
editerc.title("Gestion Des Stock")
editerc.configure(bg="#808080")

heading = Label(editerc, text= "Editer Un Client", bg="skyblue", highlightbackground="black", highlightthickness= 3, font="Roboto 20").pack(pady=50, ipadx=300, ipady=10)

frame = Frame(editerc, width=100, height=100, highlightbackground="black", highlightthickness= 3)
frame.pack(pady=50, ipadx=300, ipady=300)


editerc.mainloop()