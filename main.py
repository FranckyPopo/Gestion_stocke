import tkinter
from modules import fonctions, disingn

windown = tkinter.Tk()
windown.geometry("480x380")
windown.title("Gestion de stock")

#frame_principale = tkinter.Frame(windown, width=100)

bnt1 = tkinter.Button(windown, text="1", **disingn.bnt_principale).grid(row=0, column=0)
bnt2 = tkinter.Button(windown, text="2", **disingn.bnt_principale).grid(row=1, column=0)
bnt3 = tkinter.Button(windown, text="3", **disingn.bnt_principale).grid(row=2, column=0)
bnt4 = tkinter.Button(windown, text="4", **disingn.bnt_principale).grid(row=3, column=0)
bnt5 = tkinter.Button(windown, text="5", **disingn.bnt_principale).grid(row=4, column=0)
bnt6 = tkinter.Button(windown, text="6", **disingn.bnt_principale).grid(row=5, column=0)

#frame_principale.pack(expand="yes")
windown.mainloop()