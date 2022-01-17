import tkinter, tkinter.font
from modules import fonctions, disign

windown = tkinter.Tk()
windown.geometry("480x400")
windown.minsize(480, 360)
windown.title("GESTION DE STOCKS")
windown["bg"] = "#DEDEE1"
frame = tkinter.Frame(windown, bg="#DEDEE1")

font_bouton = tkinter.font.Font(family="Arial", size="12", weight="bold")

bnt_ravitalement = tkinter.Button(frame, text="Ravitailement", **disign.disign_bouton)
bnt_ravitalement["font"] = font_bouton
bnt_ravitalement.pack(disign.padding_bouton)

bnt_ajouter_client = tkinter.Button(frame, text="Ajouter un client", **disign.disign_bouton)
bnt_ajouter_client["font"] = font_bouton
bnt_ajouter_client.pack(disign.padding_bouton)

bnt_livraison= tkinter.Button(frame, text="Effectuer une livraison", **disign.disign_bouton)
bnt_livraison["font"] = font_bouton
bnt_livraison.pack(disign.padding_bouton)

bnt_historique = tkinter.Button(frame, text="Voir l'historique des livraisons", **disign.disign_bouton)
bnt_historique["font"] = font_bouton
bnt_historique.pack(disign.padding_bouton)

bnt_afficher_stock= tkinter.Button(frame, text="Afficher le stock", **disign.disign_bouton)
bnt_afficher_stock["font"] = font_bouton
bnt_afficher_stock.pack(disign.padding_bouton)

bnt_editer_produit= tkinter.Button(frame, text="Editer un produit", **disign.disign_bouton)
bnt_editer_produit["font"] = font_bouton
bnt_editer_produit.pack(disign.padding_bouton)

bnt_editer_client= tkinter.Button(frame, text="Editer un client", **disign.disign_bouton)
bnt_editer_client["font"] = font_bouton
bnt_editer_client.pack(disign.padding_bouton)

frame.pack(expand="yes")
windown.mainloop()