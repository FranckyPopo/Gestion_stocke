import tkinter
from turtle import width
from modules import fonctions

windown = tkinter.Tk()
windown.geometry("720x480")

frame_principale = tkinter.Frame(windown)
bnt1 = tkinter.Button(frame_principale, text="Ravitailler", command=fonctions.ravitaillement, width=25).pack(pady=5)
bnt2 = tkinter.Button(frame_principale, text="Ajouter un client", command=fonctions.ajout_client, width=25).pack(pady=5)
bnt3 = tkinter.Button(frame_principale, text="Effectuer une livraison", command=fonctions.livraison, width=25).pack(pady=5)
bnt4 = tkinter.Button(frame_principale, text="Voir l'historisque des livraisons", width=25).pack(pady=5)
bnt5 = tkinter.Button(frame_principale, text="Afficher le stock", width=25).pack(pady=5)
bnt6 = tkinter.Button(frame_principale, text="Editer un produit", width=25).pack(pady=5)
bnt7 = tkinter.Button(frame_principale, text="Editer un client", width=25).pack(pady=5)
frame_principale.pack(expand="yes")

windown.mainloop()