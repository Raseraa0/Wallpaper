#!/usr/bin/env python3

"""Module de fonction lié a la création d'image"""

import colorsys as clr
from resizeimage import resizeimage
import numpy as np
#import random as rdm
#import math as m
from PIL import Image



def create_background(size): # size de type (longueur,largeur)
    """crée le background"""
    background = Image.new("RGB", size, color="black")
    return background




class Im:
    """classe d'image, avec plusieur fonction utile"""
    def __init__(self,image):
        self.image = image
        self.size = image.size
        self.average_rgb = None
        self.average_hsv = None

    def __repr__(self):
        return f"Taille : {self.size}"

    def resize(self,new_size):
        """permet de resize l'image"""
        self.image = resizeimage.resize_contain(self.image,new_size)
        self.size = new_size

    def average_color(self):
        """permet de définir la couleur moyenne de l'image"""
        tableau_rgb = np.array(self.image)
        cote =self.size[0]
        taux_r = 0
        taux_g = 0
        taux_b = 0
        for ligne in range(cote):
            for colonne in range(cote):
                taux_r += tableau_rgb[ligne,colonne,0]
                taux_g += tableau_rgb[ligne,colonne,1]
                taux_b += tableau_rgb[ligne,colonne,2]
        taux_r /= cote**2
        taux_g /= cote**2
        taux_b /= cote**2
        self.average_rgb = (taux_r,taux_g,taux_b)
        self.average_hsv = clr.rgb_to_hsv(taux_r,taux_g,taux_b)


def import_img(nb_image):
    """permet d'importer les images"""
    liste_image = []
    for i in range(1,nb_image+1):
        name = "im/im"+str(i)+".jpg"
        image = Im(Image.open(name))
        liste_image.append(image)
    return liste_image   # List_img[3] renvoie im4 car les image commence a im1

def tri_couleur(liste_image,mode):
    """peremte de trier les image en fonction du hsv"""
    if mode == "C" or mode==0:
        mode = 0
    elif mode == "S" or mode == 1:
        mode = 1
    elif mode == "L" or mode == 2:
        mode = 2
    else:
        print("Il faut mettre C (couleur), S (saturation) ou L (luminosité")
    for i in range(1,len(liste_image)):
        hsv_ref =liste_image[i].average_hsv[mode]
        image_ref=liste_image[i]
        j = i-1
        while liste_image[j].average_hsv[mode] > hsv_ref and j >=0:
            liste_image[j+1] = liste_image[j]
            j-=1
        liste_image[j+1] = image_ref

