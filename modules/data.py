import os
import json


def recording_data(data, path: str, name_folder: str, name_file: str):
    """
    Cette fonctione va nous perméttre d'enregistrer des données dans un fichier json

    Args:
        path (str): Ce paramétre prend le chemin absolut de l'endroit d'ou nous allons crée nôtre dossier qui va contenir le ou les fichier(s) json, il faut traiter 
        le chemin comme une chaine brute en ajoutant r ou R devant la chaine du chemin
        name_file (str): Ce paramétre represente le nom du fichier json que nous allons crée
        name_folder (str): Ce paramétre prend en charge le nom du dossier où sera crée le fichier json
        data (str, int, bool...): Ce paramétre prend les données a sauvegarder dans le fichier json
    """
    if os.path.exists(path):
        folder = os.path.join(path, name_folder)
        os.makedirs(folder, exist_ok=True) 
        file = folder + "/" + name_file + ".json" 
        
        with open(file, "w") as f:
            json.dump(data, f, indent=4)         
    else:
        print("Veuillez vérifier le chemin que vous avez donné")

def get_data(path_folder: str, name_file: str):
    
    """
    Cette fonction va nous permetre de réuperer les données qui son dans un fichier json

    Args:
        path_folder (str): Ce paramétre est prend en charge le chemin qui méne au fichier qui contient nos données
        name_file (str): Ce paramétre prend en charge le nom du fichier que nous voulons selectionner
    Returns:
        [list]: Rétourne les données du fichier sinon une liste vide si le fichier ne contient rien
    """
    
    file = path_folder + "/" + name_file + ".json"

    if not os.path.isfile(file) or os.path.getsize(file) == 0:
        return [] 
    elif os.path.isfile(file):
        with open(file, "r") as f:
            content = json.load(f)
            return content
    elif not os.path.exists(path_folder):
        os.makedirs(path_folder)
        with open(file, "r") as f:
            content = json.load(f)
        return []
    else:
        print("Vérifie si le nom des chemins et si les fichiers ou dossiers existe")