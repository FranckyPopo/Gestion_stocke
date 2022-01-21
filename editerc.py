from cProfile import label
from http import client
from os import name
from pydoc import text
from tkinter import*
from turtle import heading, left

#
client = Tk()
client.title("Gestion De Stock")
client.geometry("800x800")
client.resizable(False,False)
heading = Label(client, text= "Editer Un Client", bg="skyblue",highlightbackground="black", highlightthickness= 2, font="Roboto 20").pack(pady=50, ipadx=300, ipady=10)

frame1 = Frame(client, highlightbackground="black", highlightthickness= 1)
frame1.pack(pady=60, padx=20)
name1 = Label(frame1, text="Nom: Jacques", font="Roboto 16")
email1 = Label(frame1, text="Email: jacques@yahoo.com", font="Roboto 16")
line1 = Label(frame1, text="-------------------------------")

name2 = Label(frame1,text="Nom: Jean", font="Roboto 16")
email2 = Label(frame1, text="Email: jean@gmail.com", font="Roboto 16")
line2 = Label(frame1, text="-------------------------------")

name3 = Label(frame1,text="Nom: ", font="Roboto 16")
email3 = Label(frame1, text="Email: ", font="Roboto 16")
line3 = Label(frame1, text="-------------------------------")

name4 = Label(frame1,text="Nom:", font="Roboto 16")
email4 = Label(frame1, text="Email:", font="Roboto 16")
line4 = Label(frame1, text="-------------------------------")

name5 = Label(frame1,text="Nom:", font="Roboto 16")
email5 = Label(frame1, text="Email:", font="Roboto 16")
line5= Label(frame1, text="-------------------------------")

name1.grid(row=0 , column=0, sticky='w')
email1.grid(row=1 , column=0,sticky='w')
line1.grid(row=2 , column=0,sticky='w')

name2.grid(row=3 , column=0, sticky='w')
email2.grid(row=4 , column=0,sticky='w')
line2.grid(row=5 , column=0,sticky='w')

name3.grid(row=6 , column=0, sticky='w')
email3.grid(row=7 , column=0,sticky='w')
line3.grid(row=8, column=0,sticky='w')

name4.grid(row=9 , column=0, sticky='w')
email4.grid(row=10 , column=0,sticky='w')
line4.grid(row=11 , column=0,sticky='w')

name5.grid(row=12 , column=0, sticky='w')
email5.grid(row=13 , column=0,sticky='w')
line5.grid(row=14 , column=0,sticky='w')


#Cre------------
def open():    
    top = Toplevel()
    top.title("Gestion Des Stock")
    top.resizable(False,False)
    top.geometry("800x800")
    heading1 = Label(top, text= "Modification Du Client ", bg="skyblue",highlightbackground="black", highlightthickness= 2, font="Roboto 20").pack(pady=50, ipadx=250, ipady=10)

    frame2 = Frame(top,highlightbackground="black", highlightthickness= 2)
    frame2.pack(pady=60)
    lbl1 = Label(frame2, text="Veuillez saisir l'ancien nom du client: ", font="Roboto 15")
    lbl2 = Label(frame2, text="Veuillez saisir l'ancien email du client: ", font="Roboto 15")
    lbl3 = Label(frame2, text="Veuillez saisir le nouveau nom du client: ", font="Roboto 15")
    lbl4 = Label(frame2, text="Veuillez saisir le nouveau email du client: ",font= "Roboto 15")

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
btn_accueil = Button(client,text="Retour à la page d'accueil", font= "Roboto 15", relief=FLAT, bg="skyblue", width=20, height=2 ).pack(pady= 30)

client.mainloop()