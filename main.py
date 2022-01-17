import tkinter, tkinter.font
from modules import fonctions, disign

windown = tkinter.Tk()
windown.geometry("400x400")
windown.title("GESTION DE STOCKS")

font_bouton = tkinter.font.Font(family="Arial", size="12", weight="bold")

bnt_ravitalement = tkinter.Button(windown, text="Ravitailement", **disign.disign_bouton)
bnt_ravitalement["font"] = font_bouton
bnt_ravitalement.pack()

bnt_ajouter_client = tkinter.Button(windown, text="Ajouter un client", **disign.disign_bouton)
bnt_ajouter_client["font"] = font_bouton
bnt_ajouter_client.pack()

bnt_livraison= tkinter.Button(windown, text="Effectuer une livraison", **disign.disign_bouton)
bnt_livraison["font"] = font_bouton
bnt_livraison.pack()

bnt_historique = tkinter.Button(windown, text="Voir l'historique des livraisons", **disign.disign_bouton)
bnt_historique["font"] = font_bouton
bnt_historique.pack()

bnt_afficher_stock= tkinter.Button(windown, text="Afficher le stock", **disign.disign_bouton)
bnt_afficher_stock["font"] = font_bouton
bnt_afficher_stock.pack()

bnt_editer_produit= tkinter.Button(windown, text="Editer un produit", **disign.disign_bouton)
bnt_editer_produit["font"] = font_bouton
bnt_editer_produit.pack()

bnt_editer_client= tkinter.Button(windown, text="Editer un client", **disign.disign_bouton)
bnt_editer_client["font"] = font_bouton
bnt_editer_client.pack()



windown.mainloop()