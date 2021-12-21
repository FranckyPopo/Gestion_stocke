historiques = [
    {"email": "afrifran@gmail.com", "product": "pomme", "quantity_product": 12},
    {"email": "afrifran@gmail.com", "product": "pomme", "quantity_product": 12},
    {"email": "afrifran@gmail.com", "product": "Viande", "quantity_product": 100},
    {"email": "afrifran@gmail.com", "product": "pomme", "quantity_product": 18},
    {"email": "afrifran@gmail.com", "product": "orange", "quantity_product": 2},
    {"email": "afrifran@gmail.com", "product": "orange", "quantity_product": 3},

    {"email": "popo@gmail.com", "product": "fraise", "quantity_product": 2},
    {"email": "popo@gmail.com", "product": "fraise", "quantity_product": 8},
    {"email": "popo@gmail.com", "product": "banane", "quantity_product": 12},
{"email": "popo@gmail.com", "product": "banane", "quantity_product": 3}
]

historique_totaux = []
output = []

# On ajoute les quantités de chaque produit associé au client
for item in historiques:
    if not historique_totaux:
        historique_totaux.append(item)

    else:
        for cached_item in historique_totaux:
            if item["email"] == cached_item["email"] and item["product"] == cached_item["product"]:
                cached_item["quantity_product"] += item["quantity_product"]
                break
        else:
            historique_totaux.append(item)

historique_totaux
# Create output list
# for item in added_products:
#     if not output:
#         d = {"email": item["email"], item["product"]:item["quantity_product"]}
#         output.append(d)

#     else:
#         for cached_item in output:
#             if item["email"] == cached_item["email"]:
#                 cached_item.update({item["product"]:item["quantity_product"]})
#                 break
#         else:
#             d = {"email": item["email"], item["product"]: item["quantity_product"]}
#             output.append(d)

# print(output)