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

from cProfile import label
from textwrap import fill
from tkinter import *
from random import *
from functools import partial

#########################################
# constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600

#########################################
# variables globales

        "Cases de la grille"
cases = []

        "constante de proportionnalité"
n = 50


        "configuration du canevas stockée dans une liste a deux dimensions"
config_courante = []


        " placement/orientation de la fourmi "
x_fourmi = 0 
y_fourmi = 0 


        " position de la tête "
position_tete_fourmi = 0 


        " pause"
var_pause = False
boutton_pause = 0 

        "constante de vitesse de mouvement"
vitesse = 1000
#########################################
# fonctions

def fourmi_de_langton(n):
    '''Fonction intermédiaire pour lancer le programme fourmi de langton'''
    configuration_courante_vide(n)

def configuration_courante_vide(n):
    '''Initialise la configuration conrante vide du jeu '''
    global config_courante
    global cases

    for i in range(n):
        config_courante.append([0 for x in range(n)])

    grille(n)


def grille(n):
    '''Fonctions qui affiche la grille pour y visualiser les mouvments de la fourmi'''
    c = HAUTEUR / n
    global cases
    for ligne in range(n):
        transit = []
        for colonne in range(n):
            transit.append(
                canevas.create_rectangle(colonne * c + 2, ligne * c + 2, (colonne + 1) * c + 2, (ligne + 1) * c + 2))
        cases.append(transit)

    maj_grille(n)


def maj_grille(n):
    '''Fonction qui met à jour la grille en fonction de la configuration courante au sein du jeu'''
    for ligne in range(n):
        for colonne in range(n):
            if config_courante[ligne][colonne] == 0:
                canevas.itemconfigure(cases[ligne][colonne], fill='white', )   # fond blanc du jeu afin de visualiser les mouvements de la fourmi
            if config_courante[ligne][colonne] == 1:
                canevas.itemconfigure(cases[ligne][colonne], fill='black', )  # case noir representant le mouvement de la fourmi

#########################################
# partie principale


# création des widgets
fenetre = Tk()
fenetre.title("Projet 1 : Fourmi de Langton")
canevas = Canvas(fenetre, height=HAUTEUR, width=LARGEUR, bg="snow")

boutton_haut = Button(fenetre, text="Haut", width=8, height=3, bg="white",      #choix de l'orientation de la tete vers le haut 
                               fg="black", command=partial(haut))
boutton_bas = Button(fenetre, text="Bas", width=8, height=3, bg="white",        #choix de l'orientation de la tete vers le bas 
                               fg="black", command=partial(bas))
boutton_gauche = Button(fenetre, text="Gauche", width=8, height=3, bg="white",  #choix de l'orientation de la tete vers la gauche 
                               fg="black", command=partial(gauche))
boutton_droite = Button(fenetre, text="Droite", width=8, height=3, bg="white",  #choix de l'orientation de la tete vers la droite 
                               fg="black", command=partial(droite))
texte_tete = Label(fenetre, text='Dirigez la tête') 

boutton_pause = Button(fenetre, text="Pause", width=18, height=3, bg="white",
                               fg="black", command=pause)
boutton_x2 = Button(fenetre, text="Vitesse x2", width=8, height=2, bg="white",
                               fg="black", command=augmenter_vitesse) 
boutton_div2 = Button(fenetre, text="Vitesse /2", width=8, height=2, bg="white",
                               fg="black", command=reduire_vitesse)
boutton_avance = Button(fenetre, text="Next", width=8, height=2, bg="white",
                               fg="black", command=deplacement_une_fois)

# placement des widgets

canevas.grid(column=1, row=0, columnspan=2, rowspan=5, padx=3, pady=3)
boutton_haut.grid(column=4, row=1, padx=10, pady=10)
boutton_bas.grid(column=4, row=3, padx=10, pady=10)
boutton_gauche.grid(column=3, row=2, padx=10, pady=10)
boutton_droite.grid(column=5, row=2, padx=10, pady=10)
texte_tete.grid(column=4, row=2)
boutton_pause.grid(column=4,columnspan=5, row=0, padx=10, pady=10)                        
boutton_x2.grid(column=4, row=1, padx=10, pady=10)
boutton_div2.grid(column=5, row=1, padx=10, pady=10)                            
boutton_avance.grid(column=5, row=2, padx=10, pady=10)


# boucle principale

fenetre.mainloop()
