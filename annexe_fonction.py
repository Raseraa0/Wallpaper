#!/usr/bin/env python3

"""Module de fonction annexe"""


import math as m
import matplotlib.pyplot as plt
import image_fonction 
import numpy as np


def graph(mini = 400, maxi = 800):
    """trace un graphique du nombre d'image utilisé en fonction du nombre d'image vraiment voulue"""
    liste_voulue = []
    liste_corrige = []
    largeur,hauteur = 1920,1080  #  720,1480 pour telephone

    for nb_image in range(mini,maxi):
        #Algo d'optimisation spatial
        air_total = largeur * hauteur
        air_image = air_total / nb_image
        cote_carre = m.floor(m.sqrt(air_image))
        nb_colonne = round(largeur / cote_carre)
        nb_ligne = round(hauteur / cote_carre)
        cote_carre = int(largeur / nb_colonne) +1
        nb_image_reel = nb_ligne * nb_colonne

        liste_voulue.append(nb_image)
        liste_corrige.append(nb_image_reel)

    plt.plot(liste_voulue,liste_voulue,linewidth=2,color="red",linestyle=":",label="Ligne Parfaite")
    plt.plot(liste_voulue,liste_corrige,linewidth=2,color="blue",label="Ligne Réél")
    plt.legend()
    plt.show()



def test(nb_image_voulue):
    """donne le nombre d'image réellement utilisé lorsque l'on
    rentre un certaine nombre d'image voulue"""
    largeur,hauteur = 1920,1080  #  720,1480 pour telephone

    air_total = largeur * hauteur
    air_image = air_total / nb_image_voulue
    cote_carre = m.floor(m.sqrt(air_image))
    nb_colonne = round(largeur / cote_carre)
    nb_ligne = round(hauteur / cote_carre)
    cote_carre = int(largeur / nb_colonne) +1
    nb_image_reel = nb_ligne * nb_colonne

    # for erreur_largeur in range(0,100):  #vise a reduire l'ecart entre image voulue et reel
    #    for erreur_hauteur in range(0,100):
    #        air_total = (largeur+erreur_largeur) * (hauteur+erreur_hauteur)
    #        air_image = air_total / nb_image_voulue
    #        cote_carre = m.floor(m.sqrt(air_image))
    #        nb_colonne = round((largeur+erreur_largeur) / cote_carre)
    #        nb_ligne = round((hauteur+erreur_hauteur) / cote_carre)
    #        cote_carre = int(largeur / nb_colonne) +1
    #        autre_nb_image_reel = nb_ligne * nb_colonne
    #        if abs(autre_nb_image_reel-nb_image_voulue)<abs(nb_image_reel-nb_image_voulue):
    #            nb_image_reel = autre_nb_image_reel

    return nb_image_reel


def doublon(nombre_image, seuil=30):
    """verifie s'il y a des doublons dans la liste d'image"""
    liste_image = image_fonction.import_img(nombre_image)

    liste_doublons = []

    for i in range(0,nombre_image):
        print("cmp: "+str(i)+"---")
        for j in range(i+1,nombre_image):


            if liste_image[i].size != liste_image[j].size:
                continue
            
            size = liste_image[i].size[0]
            tab1 = np.array(liste_image[i].image, dtype=np.int16)
            tab2 = np.array(liste_image[j].image, dtype=np.int16)

            err = 0
            for ligne in range(0,size):
                for colonne in range(0,size):
                    errtemp = abs(tab1[ligne,colonne,0] - tab2[ligne,colonne,0])
                    errtemp += abs(tab1[ligne,colonne,1] - tab2[ligne,colonne,1])
                    errtemp += abs(tab1[ligne,colonne,2] - tab2[ligne,colonne,2])
                    errtemp /= 3
                    err += errtemp
            err/=nombre_image

            if err < seuil:
                liste_doublons.append((i+1,j+1))


    for tup in liste_doublons:
        print("--------"+str(tup)+"--------")

def possible(mini = 600,maxi = 700):
    """regarde si une configuration est possible avec exactement le nombre d'image voulue"""
    liste_possible = []
    for nb_image in range(mini,maxi):
        if test(nb_image)==nb_image:
            liste_possible.append(nb_image)
    return liste_possible

print(doublon(669)) 
