""" 
    ce script tourne en permanence : 
    il recherche des fichiers dans le repertoire
    path et il les copie dans une dropbox distante.
    Si tout se passe bien, il supprime les fichiers locaux.
"""

import os
import time
path="./images/"
def upload_files():
    if not os.path.exists(path):
        return
    dir_list = os.listdir(path)
    first_10 = dir_list[:10]
    for file_name in first_10:
        file_full_path = path + file_name
        print(file_full_path) 
        cmd = "./DropBox/Dropbox-Uploader/dropbox_uploader.sh upload " + file_full_path + " ."
        returnCode=os.system(cmd)
        # ne supprimer les fichiers que si la commande s'est bien deroulee
        if returnCode == 0:
            os.remove(file_full_path)
        else:
            print("Erreur lors de l'appel du script")
            print (returnCode)

            
if __name__ == "__main__":
    while True:
        print("Uploadingfile")
        upload_files()
        time.sleep(10)
