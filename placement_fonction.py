#!/usr/bin/env python3

"""Module de fonction lié aux placement des images"""

#import image_fonction as i
#from resizeimage import resizeimage
import numpy as np
#import random as rdm
#import math as m
#from PIL import Image,ImageEnhance
#import colorsys as clr

#%%
def organisation_index(nb_ligne,nb_colonne,organisation):

    """permet d'organiser dans un tableau les image, disposé comme demandé """

    tableau_index = np.zeros((nb_ligne,nb_colonne),dtype=int)

    if organisation in ["C","CR"]:
        index =- 1
        compteur = 0
        for _ in range(nb_ligne + nb_colonne):
            colonne = compteur
            ligne = 0
            while colonne >= nb_colonne:
                colonne -= 1
                ligne += 1
            while colonne != -1 and ligne < nb_ligne:
                index += 1
                tableau_index[ligne,colonne] = index
                ligne += 1
                colonne -= 1
            compteur += 1

    elif organisation in  ["H","B"]:
        ligne = 0
        index = -1
        for _ in range(nb_ligne):
            colonne = 0
            for _ in range(nb_colonne):
                index += 1
                tableau_index[ligne,colonne] = index
                colonne += 1
            ligne += 1

    elif organisation in ["D","G"]:
        colonne = 0
        index = -1
        for _ in range(nb_colonne):
            ligne = 0
            for _ in range(nb_ligne):
                index += 1
                tableau_index[ligne,colonne] = index
                ligne += 1
            colonne += 1

    else:
        print("Il faut rentrer : C,CR,H,B,G ou D")

    if organisation in ["B","G","CR"]:
        tableau_index = abs(tableau_index-(nb_ligne*nb_colonne-1)) #pour inverser tout les index

    return tableau_index


def placement(tableau_index,liste_image,background,marge):
    """place les image sur le background"""

    decalage_largeur = int(marge[0]/2)
    decalage_hauteur = int(marge[1])  #a modifier si il y a des bordures

    nb_ligne,nb_colonne = tableau_index.shape
    cote_carre = liste_image[0].size[0]
    for ligne in range(nb_ligne):
        for colonne in range(nb_colonne):
            indice = tableau_index[ligne,colonne]
            placement_image = (
                        colonne * cote_carre + decalage_largeur ,
                        ligne * cote_carre + decalage_hauteur,
                        (colonne+1) * cote_carre + decalage_largeur,
                        (ligne+1) * cote_carre + decalage_hauteur)
            #print("oooooooo")
            #print(str(indice) + " et " + str(len(liste_image)))
            #print("oooooo \n")
            background.paste(liste_image[indice].image,placement_image)

def tri(lignes, liste_image):
    liste_saturation = [ image.average_hsv[2] for image in liste_image]

    for i in range(len(liste_saturation)):
        min_index = i
        for j in range(i+1, len(liste_saturation)):
            if liste_saturation[j] < liste_saturation[min_index]:
                min_index = j
        liste_saturation[i], liste_saturation[min_index] = liste_saturation[min_index], liste_saturation[i]
        lignes[i], lignes[min_index] = lignes[min_index], lignes[i]
