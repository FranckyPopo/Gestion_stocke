import tkinter
from modules import fonctions

windown = tkinter.Tk()
windown.geometry("400x400")

bnt = tkinter.Button(windown, text="Ravitaillement", command=fonctions.ajout_client).pack()

windown.mainloop()