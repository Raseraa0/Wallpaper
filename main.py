#!/usr/bin/env python3

"""le main, tout simplement"""
import math as m
from PIL import ImageEnhance
import image_fonction as i
import placement_fonction as p
import affichage as aff
#import annexe_fonction as a
#import random as rdm


def main():
    """main, tout simplement"""

    aff.primaire("Début de programme de génération")

    while 1:
        securite = aff.securite()#juste au cas ou je miss click
        if securite == "o":
            break
        elif securite == "n":
            raise KeyboardInterrupt

    aff.primaire("Calcul du nombre d'images")

    size_background = (1920,1080)
    # size_background = (720,1480)
    background = i.create_background(size_background)

    #########################
    nb_image_voulue = 650   # afin d'éviter tout bug, vaut mieux mettre des ici le bon nombre d'images
    #########################

    aff.information([f"Taille de l'écran : {aff.to_bold(size_background)}",
                        f"Nombre d'images voulues : {aff.to_bold(nb_image_voulue)}"])

    largeur,hauteur = background.size

    air_total = largeur * hauteur
    air_image = air_total / nb_image_voulue
    cote_carre = m.floor(m.sqrt(air_image))
    nb_colonne = round(largeur / cote_carre)
    nb_ligne = round(hauteur / cote_carre)
    cote_carre = int(largeur / nb_colonne) +1
    nb_image_reel = nb_ligne * nb_colonne

    # for erreur_largeur in range(0,100):  #vise a reduire l'ecart entre image voulue et reel
    #     for erreur_hauteur in range(0,100):
    #         air_total = (largeur+erreur_largeur) * (hauteur+erreur_hauteur)
    #         air_image = air_total / nb_image_voulue
    #         cote_carre = m.floor(m.sqrt(air_image))
    #         nb_colonne = round((largeur+erreur_largeur) / cote_carre)
    #         nb_ligne = round((hauteur+erreur_hauteur) / cote_carre)
    #         cote_carre = int(largeur / nb_colonne) +1
    #         autre_nb_image_reel = nb_ligne * nb_colonne
    #         if abs(autre_nb_image_reel-nb_image_voulue)<abs(nb_image_reel-nb_image_voulue):
    #             nb_image_reel = autre_nb_image_reel



    taille = (cote_carre,cote_carre)
    marge_largeur = largeur -  nb_colonne * cote_carre
    marge_hauteur = hauteur - nb_ligne * cote_carre
    marge = (marge_largeur,marge_hauteur)


    aff.information(f"Après optimisation, il y aura {aff.to_bold(nb_image_reel)} images ")
    
    aff.primaire("Redimensionnement des images et calcul des RGB")

    liste_image = i.import_img(nb_image_reel)
    for image in liste_image:
        image.resize(taille)
        image.average_color()


    # Ajout du rgb
    with open("dataBefore.txt",'r') as f:
        lignes = f.readlines()
    for index in range(nb_image_reel):
        lignes[index] = lignes[index].strip() + f"\t{liste_image[index].average_rgb}\n"
    
    aff.primaire("Ajout au data.txt trié par RGB")

    p.tri(lignes,liste_image)

    with open("data.txt",'w') as f:
        f.writelines(lignes)
    
    liste_mode = ["C","S","L"]
    liste_organisation =["C","CR","H","B","G","D"]
    numero = 0
    
    aff.primaire("Génération des fonds d'écrans")

    total = len(liste_mode)*len(liste_organisation)
    cpt = 0
    for mode in liste_mode:
        i.tri_couleur(liste_image, mode)
        for organisation in liste_organisation:

            tableau_index = p.organisation_index(nb_ligne,nb_colonne,organisation)
            
            p.placement(tableau_index,liste_image,background,marge)

            pour_luminosite = ImageEnhance.Brightness(background)
            background = pour_luminosite.enhance(0.6)

            numero+=1
            background_name = f"END/Wallpaper{numero}.png"
            # bg_name = "ENDphone/Wallpaper"+str(num)+".png"

            background.save(background_name)

            cpt+=1
            aff.information(f"image {cpt}/{total} terminée ")

    aff.final("Génération terminée avec succès")

if __name__ =="__main__":
    main()
    