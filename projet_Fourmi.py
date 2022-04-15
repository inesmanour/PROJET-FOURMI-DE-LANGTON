#Projet
#########################################
# informations liées au groupe
# groupe LDDBI
# LAURA LEFEVRE
# ADAM KEDDIS
# MANOUR INES
#
#########################################
# import des librairies

from tkinter import *
from random import *

#########################################
# constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600

#########################################
# variables globales

#########################################
# fonctions


#########################################
# partie principale


# création des widgets
fenetre = Tk()
fenetre.title("Projet 1 : Fourmi de Langton")
canevas = Canvas(fenetre, height=HAUTEUR, width=LARGEUR, bg="snow")


# placement des widgets
canevas.grid(column=1, row=0, columnspan=2, rowspan=5, padx=3, pady=3)


# boucle principale

fenetre.mainloop()