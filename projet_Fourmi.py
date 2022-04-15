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

# Cases de la grille
cases = []
# constante de proportionnalité
n = 50
# configuration du canevas stockée dans une liste a deux dimensions
config_courante = []
# placement de la fourmi 
x_fourmi = 0 
y_fourmi = 0 
# position de la tête 
position_tete_fourmi = 0 
# pause 
var_pause = False
boutton_pause = 0 
#########################################
# fonctions
def fourmi_de_langton(n):
    '''Fonction intermédiaire pour lancer le programme tas de sable'''
    configuration_courante_vide(n)




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
                canevas.itemconfigure(cases[ligne][colonne], fill='white', )  # white pour 0 grain
            if config_courante[ligne][colonne] == 1:
                canevas.itemconfigure(cases[ligne][colonne], fill='black', )  # noir pour 1 grain




def placement_fourmi():
    ''' Fonction qui initialise une configuration aléatoire : ajoute entre 0 et n grains de sable à chaque case'''
    global config_courante, n, x_fourmi, y_fourmi, boutton_bas, boutton_droite, boutton_gauche, boutton_haut, texte_tete
    x_fourmi = randint(0,n-1)
    y_fourmi = randint(0,n-1)
    config_courante[y_fourmi][x_fourmi] += 1 
    boutton_creer_fourmi.destroy()
    boutton_haut = Button(fenetre, text="Haut", width=8, height=3, bg="white",
                               fg="black", command=partial(haut))
    boutton_bas = Button(fenetre, text="Bas", width=8, height=3, bg="white",
                               fg="black", command=partial(bas))
    boutton_gauche = Button(fenetre, text="Gauche", width=8, height=3, bg="white",
                               fg="black", command=partial(gauche))
    boutton_droite = Button(fenetre, text="Droite", width=8, height=3, bg="white",
                               fg="black", command=partial(droite))
    texte_tete = Label(fenetre, text='Dirigez la tête')
    boutton_haut.grid(column=4, row=1, padx=10, pady=10)
    boutton_bas.grid(column=4, row=3, padx=10, pady=10)
    boutton_gauche.grid(column=3, row=2, padx=10, pady=10)
    boutton_droite.grid(column=5, row=2, padx=10, pady=10)
    texte_tete.grid(column=4, row=2)
    maj_grille(n)

def haut():
    global x_fourmi, y_fourmi, config_courante, position_tete_fourmi, boutton_pause
    position_tete_fourmi = haut
    boutton_pause = Button(fenetre, text="Pause", width=18, height=3, bg="white",
                               fg="black", command=pause)
    boutton_pause.grid(column=4, row=0, padx=10, pady=10)
    boutton_haut.destroy()
    boutton_bas.destroy()
    boutton_gauche.destroy()
    boutton_droite.destroy()
    texte_tete.destroy()
    texte_haut = Label(fenetre, text='La tête a commencé en haut')
    texte_haut.grid(column=0, row=0, padx=10, pady=10)
    if config_courante[y_fourmi][x_fourmi] == 0:
        config_courante[y_fourmi][x_fourmi] += 1 
    maj_grille(n)
    deplacement()

def bas():
    global x_fourmi, y_fourmi, config_courante, position_tete_fourmi, boutton_pause
    position_tete_fourmi = bas
    boutton_pause = Button(fenetre, text="Pause", width=18, height=3, bg="white",
                               fg="black", command=pause)                          
    boutton_pause.grid(column=4, row=0, padx=10, pady=10)
    boutton_haut.destroy()
    boutton_bas.destroy()
    boutton_gauche.destroy()
    boutton_droite.destroy()
    texte_tete.destroy()
    texte_bas = Label(fenetre, text='La tête a commencé en bas')
    texte_bas.grid(column=0, row=0, padx=10, pady=10)
    if config_courante[y_fourmi][x_fourmi] == 0:
        config_courante[y_fourmi][x_fourmi] += 1 
    maj_grille(n)
    deplacement()

def gauche():
    global x_fourmi, y_fourmi, config_courante, position_tete_fourmi, boutton_pause
    position_tete_fourmi = gauche
    boutton_pause = Button(fenetre, text="Pause", width=18, height=3, bg="white",
                               fg="black", command=pause)
    boutton_pause.grid(column=4, row=0, padx=10, pady=10)
    boutton_haut.destroy()
    boutton_bas.destroy()
    boutton_gauche.destroy()
    boutton_droite.destroy()
    texte_tete.destroy()
    texte_gauche = Label(fenetre, text='La tête a commencé à gauche')
    texte_gauche.grid(column=0, row=0, padx=10, pady=10)
    if config_courante[y_fourmi][x_fourmi] == 0:
        config_courante[y_fourmi][x_fourmi] += 1 
    maj_grille(n)
    deplacement()

def droite():
    global x_fourmi, y_fourmi, config_courante, position_tete_fourmi, boutton_pause
    position_tete_fourmi = droite
    boutton_pause = Button(fenetre, text="Pause", width=18, height=3, bg="white",
                               fg="black", command=pause)
    boutton_pause.grid(column=4, row=0, padx=10, pady=10)
    boutton_haut.destroy()
    boutton_bas.destroy()
    boutton_gauche.destroy()
    boutton_droite.destroy()
    texte_tete.destroy()
    texte_droite = Label(fenetre, text='La tête a commencé à droite')
    texte_droite.grid(column=0, row=0, padx=10, pady=10)
    if config_courante[y_fourmi][x_fourmi] == 0:
        config_courante[y_fourmi][x_fourmi] += 1 
    maj_grille(n)
    deplacement()

def deplacement():
    global x_fourmi, y_fourmi, config_courante, position_tete_fourmi, launch
    launch = canevas.after(200, deplacement)
    if position_tete_fourmi == haut:
        y_fourmi -= 1
        tore()
        if config_courante[y_fourmi][x_fourmi] == 0:
            config_courante[y_fourmi][x_fourmi] += 1
            position_tete_fourmi = droite
            maj_grille(n)
            return
        elif config_courante[y_fourmi][x_fourmi] == 1:
            config_courante[y_fourmi][x_fourmi] -= 1
            position_tete_fourmi = gauche
            maj_grille(n)
            return
    elif position_tete_fourmi == bas:
        y_fourmi += 1
        tore()
        if config_courante[y_fourmi][x_fourmi] == 0:
            config_courante[y_fourmi][x_fourmi] += 1
            position_tete_fourmi = gauche
            maj_grille(n)
            return
        elif config_courante[y_fourmi][x_fourmi] == 1:
            config_courante[y_fourmi][x_fourmi] -= 1
            position_tete_fourmi = droite
            maj_grille(n)
            return
    elif position_tete_fourmi == droite:
        x_fourmi += 1
        tore()
        if config_courante[y_fourmi][x_fourmi] == 0:
            config_courante[y_fourmi][x_fourmi] += 1
            position_tete_fourmi = bas
            maj_grille(n)
            return
        elif config_courante[y_fourmi][x_fourmi] == 1:
            config_courante[y_fourmi][x_fourmi] -= 1
            position_tete_fourmi = haut   
            maj_grille(n)
            return     
    elif position_tete_fourmi == gauche:
        x_fourmi -= 1
        tore()
        if config_courante[y_fourmi][x_fourmi] == 0:
            config_courante[y_fourmi][x_fourmi] += 1
            position_tete_fourmi = haut
            maj_grille(n)
            return
        elif config_courante[y_fourmi][x_fourmi] == 1:
            config_courante[y_fourmi][x_fourmi] -= 1
            position_tete_fourmi = bas
            maj_grille(n)
            return 


def pause():
    global launch, var_pause, boutton_pause
    var_pause = not var_pause
    if var_pause == True :
        canevas.after_cancel(launch)
        boutton_pause.config(text="Démarrer")
    else:
        launch = canevas.after(500, deplacement)  
        boutton_pause.config(text="Pause")


def tore():
    global x_fourmi, y_fourmi, n
    if x_fourmi > n-1:
        x_fourmi = 0 
        return
    elif x_fourmi < 0:
        x_fourmi = n-1
        return
    elif y_fourmi > n-1:
        y_fourmi = 0 
        return
    elif y_fourmi < 0:
        y_fourmi = n-1
        return
    

#########################################
# partie principale


# création des widgets
fenetre = Tk()
fenetre.title("Projet 1 : Fourmi de Langton")
canevas = Canvas(fenetre, height=HAUTEUR, width=LARGEUR, bg="snow")
boutton_creer_fourmi = Button(fenetre, text="Créer fourmi ", width=18, height=3, bg="white",
                               fg="black", command=partial(placement_fourmi))

# placement des widgets
canevas.grid(column=1, row=0, columnspan=2, rowspan=5)
boutton_creer_fourmi.grid(column=0, row=0, padx=10, pady=10)

# boucle principale
fourmi_de_langton(n)
fenetre.mainloop()