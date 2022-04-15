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

from distutils.command.config import config
from glob import glob
from tkinter import *
from random import *
from functools import partial
from winreg import REG_OPENED_EXISTING_KEY

#########################################
# constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
# boucle avalanche
boucle = False
#########################################
# variables globales

# Cases de la grille
cases = []
# constante de proportionnalité
n = 50
# configuration du canevas stockée dans une liste a deux dimensions
config_courante = []


#########################################
# fonctions
def tas_de_sable(n):
    '''Fonction intermédiaire pour lancer le programme tas de sable'''
    configuration_courante_vide(n)
def verif_sable(n):
    global boucle
    for ligne in range(n):
        for colonne in range(n):
            if config_courante[ligne][colonne] > 3 :
                boucle = True
            else:
                boucle = False


def avalanche(n):
    '''Fonction qui lance l'avalanche'''
    global boucle
    for ligne in range(n):
        for colonne in range(n):
            if config_courante[ligne][colonne] > 3 and ligne != 1 and ligne != 49 and colonne != 1 and colonne != 49:
                config_courante[ligne][colonne] -= 4
                config_courante[ligne - 1 ][colonne] += 1
                config_courante[ligne + 1 ][colonne] += 1
                config_courante[ligne][colonne + 1] += 1
                config_courante[ligne][colonne - 1] += 1
                maj_grille(n)
            if config_courante[ligne][colonne] > 3 and ligne == 1 and colonne == 1 :
                config_courante[ligne][colonne] -= 2
                config_courante[ligne + 1 ][colonne] += 1
                config_courante[ligne][colonne + 1 ] += 1
                maj_grille(n)
            if config_courante[ligne][colonne] > 3 and ligne == 1 and colonne == 49 :
                config_courante[ligne][colonne] -= 2
                config_courante[ligne + 1][colonne] += 1
                config_courante[ligne][colonne - 1 ] += 1
                maj_grille(n)
            if config_courante[ligne][colonne] > 3 and ligne == 49 and colonne == 1 :
                config_courante[ligne][colonne] -= 2
                config_courante[ligne - 1 ][colonne] += 1
                config_courante[ligne][colonne + 1 ] += 1
                maj_grille(n)
            if config_courante[ligne][colonne] > 3 and ligne == 49 and colonne == 49 :
                config_courante[ligne][colonne] -= 2
                config_courante[ligne - 1][colonne] += 1
                config_courante[ligne][colonne - 1 ] += 1
                maj_grille(n)

            if config_courante[ligne][colonne] > 3 and ligne == 1 and colonne != 1 and colonne != 49:
                config_courante[ligne][colonne] -= 3
                config_courante[ligne + 1 ][colonne] += 1
                config_courante[ligne][colonne + 1 ] += 1
                config_courante[ligne][colonne - 1 ] += 1
                maj_grille(n)
            if config_courante[ligne][colonne] > 3 and ligne == 49 and colonne != 1 and colonne != 49:
                config_courante[ligne][colonne] -= 3
                config_courante[ligne - 1 ][colonne] += 1
                config_courante[ligne][colonne + 1 ] += 1
                config_courante[ligne][colonne - 1 ] += 1
                maj_grille(n)
            if config_courante[ligne][colonne] > 3 and colonne == 1 and ligne != 1 and ligne != 49:
                config_courante[ligne][colonne] -= 3
                config_courante[ligne + 1 ][colonne] += 1
                config_courante[ligne - 1 ][colonne] += 1
                config_courante[ligne][colonne + 1 ] += 1
                maj_grille(n)
            if config_courante[ligne][colonne] > 3 and colonne == 1 and ligne != 1 and ligne != 49:
                config_courante[ligne][colonne] -= 3
                config_courante[ligne + 1 ][colonne] += 1
                config_courante[ligne - 1 ][colonne] += 1
                config_courante[ligne][colonne - 1 ] += 1
                maj_grille(n)
def configuration_courante_vide(n):
    '''Initialise la configuration conrante vide'''
    global config_courante
    global cases

    for i in range(n):
        config_courante.append([0 for x in range(n)])

    grille(n)


def grille(n):
    '''Fonctions qui affiche la grille '''
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
    '''Fonction qui met à jour la grille en fonction de la configuration courante'''
    for ligne in range(n):
        for colonne in range(n):
            if config_courante[ligne][colonne] == 0:
                canevas.itemconfigure(cases[ligne][colonne], fill='black', outline='grey')  # noir pour 0 grain


            elif config_courante[ligne][colonne] == 1:
                canevas.itemconfigure(cases[ligne][colonne], fill='white', outline='grey')  # blanc pour 1 grain




def random_config(n):
    ''' Fonction qui initialise une configuration aléatoire : ajoute entre 0 et n grains de sable à chaque case'''
    global config_courante
    for ligne in range(n):
        for colonne in range(n):
            config_courante[ligne][colonne] = randint(0, 1)  # il faut écraser la variable et pas l'additionner !!!
    maj_grille(n)








#########################################
# partie principale


# création des widgets
fenetre = Tk()
fenetre.title("Projet 1 : Tas de sable")
canevas = Canvas(fenetre, height=HAUTEUR, width=LARGEUR, bg="snow")
boutton_random_config = Button(fenetre, text="Configuration aléatoire", width=17, height=3, bg="moccasin",
                               fg="black", command=partial(random_config, n))


# placement des widgets
canevas.grid(column=1, row=0, columnspan=2, rowspan=5, padx=3, pady=3)
boutton_random_config.grid(column=0, row=0, )


# boucle principale
tas_de_sable(n)
fenetre.mainloop()