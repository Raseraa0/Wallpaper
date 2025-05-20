import os,sys
from io import BytesIO
from mutagen.id3 import ID3
from PIL import Image
import affichage as aff

###################################################################
# Code qui permet d'obtenir les tags
###################################################################

def showTags():
    from mutagen.id3 import ID3
    path = "/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_RZCT60LA1HY/Internal storage/Music/../Musique/Nocturnes vol1 - GVS/1 - CdG_.mp3"
    tags = ID3(path)
    print(tags)

###################################################################
# classe qui pemret de regrouper toute les données des musiques
###################################################################

class Musique:

    numero_image = None
    album = None
    artiste = None

    def __init__(self, numero_image = None, album = None, artiste = None ):
        self.numero_image = numero_image
        self.album = album
        self.artiste = artiste



def toData(liste_musique):
    with open("dataBefore.txt", 'w') as f:
        for musique in liste_musique:
            f.write(f"{musique.numero_image}\t{musique.album}\t{musique.artiste}\n")

###################################################################
# Code qui permet d'obtenir les informations correspondantes
###################################################################

# Permet d'obtenir l'image en fonction du tag
def getCover(tags):
    # Liste des clés possibles  

    possible_keys = ["APIC:", "APIC:cover", "APIC:\"Album cover\"", "APIC:front cover"]

    for key in possible_keys:
        if key in tags:
            return tags[key].data
        
    return None

# Permet d'obtenir le nom de l'album en fonction du tag
def getAlbum(tags):
    # Liste des clés possibles  
    possible_keys = ["TALB"]

    for key in possible_keys:
        if key in tags:
            return tags[key]
        
    return None

# Permet d'obtenir le nom de l'artiste en fonction du tag
def getArtist(tags):
    # Liste des clés possibles  
    possible_keys = ["TPE1", "TPE2"]

    for key in possible_keys:
        if key in tags:
            return tags[key]
        
    return None



###################################################################
# Liste des autres doublons
###################################################################

liste_autre_doublons = []
liste_autre_doublons.append("Ipseite")
liste_autre_doublons.append("Trone")
liste_autre_doublons.append("Rêves bizarres (feat. Damso)")
liste_autre_doublons.append("Princesse Diana")
liste_autre_doublons.append("Princesse Leïa")
liste_autre_doublons.append("Princesse Leïa")


###################################################################
# Code principal
###################################################################


def getAll():

    # Chemin qui permet d'acceder à l'endroit ou la playlist est stocké
    playlist_path = '/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_RZCT60LA1HY/Internal storage/Music/'

    # Liste des chemin des musiques dont la cover n'a pas été trouvée
    unfind = []
    
    # Liste des noms des albums 
    liste_album = []

    # Liste des musiques via la classe
    liste_musique = []

    aff.primaire("Début de la récupération d'image")

    # On ouvre le fichier qui contient tout les chemin de toute les musiques
    with open(playlist_path+'♡ .... ♡ (1).m3u') as file:

        # On skip la première ligne (contenue inutile)
        next(file)
        
        num = 1     # la numérotation commence à 1
        
        for line in file:

            print(num)      # on affiche le numero afin de voire la progression
            path = playlist_path + line.strip()     # on recupère le chemin absolue de la musique 
            tags = ID3(path)        # on recupère les tags de la musique

            # 
            new_musique = Musique()
            new_musique.numero_image = num

            ### On recupère le nom de l'album
            album = getAlbum(tags)

            ### On recupère le nom de l'artiste
            artiste = getArtist(tags)
            new_musique.artiste = artiste
            
            if album in liste_album:
                aff.warning(f"L'album {album} de {artiste} a été detecté en double (vérification automatique)",hard=1)
                continue    # on passe la suite si la cover existe deja 
            
            if album in liste_autre_doublons:
                aff.warning(f"L'album {album} de {artiste} a été detecté en double (vérification manuelle)",hard=0)
                continue

            liste_album.append(album)
            new_musique.album = album

            ### On recupère la cover de la musique
            pict = getCover(tags)

            if pict:
                im = Image.open(BytesIO(pict))
                im.save(f'/home/arthur/Documents/Perso/the_wallpaper/pythonVersion/im/im{num}.jpg')
                num += 1
                liste_musique.append(new_musique) 
            else:
                aff.warning(f"La cover de l'album n'a pas été trouvée :\n{path}",hard = 2)
                unfind.append(path)



    # # On affiche toute les image qui ne sont pas passé
    # if unfind:
    #     print("\033[91m\u25CF\033[0m ","Les images suivantes ne sont pas passées :\n")
    #     for path in unfind:
    #         print(path)
    # else:
    #     print("\033[92m\u25CF\033[0m ","Toute les images sont passées avec succès")

    toData(liste_musique)

    aff.final("Téléchargement des images terminé avec succès")


if __name__ == "__main__": 
    getAll()
