import tkinter
from modules import fonctions, disingn

windown = tkinter.Tk()
windown.geometry("500x400")
windown.title("Gestion de stock")
windown["bg"] = "#dedee1"

frame_principale = tkinter.Frame(windown, bg="#dedee1")

bnt1 = tkinter.Button(frame_principale, text="Se ravaitailler", command=fonctions.ravitaillement, **disingn.bnt_principale).pack(**disingn.bnt_pading)
bnt2 = tkinter.Button(frame_principale, text="Ajouter une client", **disingn.bnt_principale).pack(**disingn.bnt_pading)
bnt3 = tkinter.Button(frame_principale, text="Effectuer une livraison", **disingn.bnt_principale).pack(**disingn.bnt_pading)
bnt4 = tkinter.Button(frame_principale, text="Voir l'historiques des livraison", **disingn.bnt_principale).pack(**disingn.bnt_pading)
bnt5 = tkinter.Button(frame_principale, text="Afficher le stocke", **disingn.bnt_principale).pack(**disingn.bnt_pading)
bnt6 = tkinter.Button(frame_principale, text="Editer produit", **disingn.bnt_principale).pack(**disingn.bnt_pading)
bnt7 = tkinter.Button(frame_principale, text="Editer client", **disingn.bnt_principale).pack(**disingn.bnt_pading)

frame_principale.pack(expand="yes")
windown.mainloop()