# Créé par Laura, le 29/04/2022 en Python 3.7
from tkinter import *
from random import randint
from tkinter.font import Font

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600

#########################################
# VARIABLES GLOBALES

#Cases de la grille
cases = []

#constante de proportionnalité
n = 30

#configuration du canevas stockée dans une liste a deux dimensions
config_courante = []

#position et orientation de la fourmie
x_fourmi = 0
y_fourmi = 0
variable_orientation = ""


#Variable pour gerer le temps
var_pause = False


def jeu_Fourmi():
    '''Fonction intermédiaire permettant le lancement du jeu'''
    hide(bouton_haut, True)
    hide(bouton_bas, True)
    hide(bouton_droit, True)
    hide(bouton_gauche, True)
    hide(txt_orientation, True)
    hide(txt_informatif, True)
    hide(bouton_next, True)
    hide(bouton_play, True)
    hide(bouton_pause, True)
    hide(scale_vitesse, True)
    hide(bouton_save, True)
    hide(bouton_load, True)
    hide(bouton_retour, True)
    configuration_courante_vide()

def configuration_courante_vide():
    '''Initialise la configuration conrante vide du jeu '''
    global config_courante, n

    for i in range(n):
        config_courante.append([0 for x in range(1, n+1)])

    return init_grille()

def init_grille():
    '''Fonctions qui permet la création d'une grille'''
    global cases

    c = HAUTEUR / n
    for ligne in range(n):
        transit = []
        for colonne in range(n):
            transit.append(canevas.create_rectangle(colonne * c + 2, ligne * c + 2, (colonne + 1) * c + 2, (ligne + 1) * c + 2, fill="snow", outline="darkSeaGreen1"))
        cases.append(transit)

def maj_grille():
    '''Fonction qui met à jour la grille en fonction de la configuration courante au sein du jeu'''
    for ligne in range(n):
        for colonne in range(n):
            if config_courante[ligne][colonne] == 0:
                canevas.itemconfigure(cases[ligne][colonne], fill='snow')   #Changement de la couleur de la case en blanc
            if config_courante[ligne][colonne] == 1:
                canevas.itemconfigure(cases[ligne][colonne], fill='black')  #Changement de la couleur de la case en noir

def creation_fourmi():
    '''Fonction permettant le placement aléatoire d'une fourmi et pour aller plus loin, permet de choisir l'orientation de la fourmi'''
    global config_courante, x_fourmi, y_fourmi

    x_fourmi = randint(0,n-1)
    y_fourmi = randint(0,n-1)

    config_courante[y_fourmi][x_fourmi] += 1
    
    bouton_creer_fourmi.destroy()

    affiche_fleches()
    maj_grille()

def hide(widget, v):
    '''Fonction permettant de cacher ou d'afficher un widget'''
    if v == True :
        widget.grid_remove()
    else :
        widget.grid()

def affiche_fleches():
    '''Fonction permettant de d'afficher les flèches avec le label attribué pour choisir l'orientation de la fourmi'''
    hide(txt_orientation, False)
    hide(bouton_haut, False)
    hide(bouton_bas, False)
    hide(bouton_droit, False)
    hide(bouton_gauche, False)

def changement_txt(label, txt_modif:str):
    '''Fonction permettant de changer le texte d'un label'''
    label.configure(text=txt_modif) 

def orientation_fourmi(direction:str):
    '''Fonction permettant d'attribuer l'orientation choisi par l'utilisateur à la fourmi'''
    global variable_orientation
    
    #On cache les boutons des fleches et le label associé après la sélection de l'orientation
    hide(bouton_haut, True)
    hide(bouton_bas, True)
    hide(bouton_droit, True)
    hide(bouton_gauche, True)
    hide(txt_orientation, True)

    #On affiche les boutons necessaires a la suite du jeu
    hide(txt_informatif, False)
    hide(bouton_next, False)
    hide(bouton_play, False)
    hide(bouton_pause, False)
    hide(scale_vitesse, False)
    hide(bouton_save, False)
    hide(bouton_load, False)
    hide(bouton_retour, False)

    #appelle la fonction changement_txt en fonction de l'orientation choisie par l'utilisateur
    if direction == "haut":
        changement_txt(txt_informatif, "La fourmi démarre\n par le haut")
        variable_orientation = "haut"
    elif direction == "bas":
        changement_txt(txt_informatif, "La fourmi démarre\n par le bas")
        variable_orientation = "bas"
    elif direction == "droite":
        changement_txt(txt_informatif, "La fourmi démarre\n par la droite")
        variable_orientation = "droite"
    else :
        changement_txt(txt_informatif, "La fourmi démarre\n par la gauche")
        variable_orientation = "gauche"

    return

def deplacement(x:str):
    ''' Fonction permettant le déplacement de la fourmi en fonction du choix de l'orientation par l'utilisateur'''
    global x_fourmi, y_fourmi, config_courante, variable_orientation, vitesse, scale_vitesse
    
    
    if var_pause == False :
        if variable_orientation == "haut":
            y_fourmi -= 1
            verif_coordonnee()
            if config_courante[y_fourmi][x_fourmi] == 0:
                config_courante[y_fourmi][x_fourmi] += 1
                variable_orientation = "droite"
            else:
                config_courante[y_fourmi][x_fourmi] -= 1
                variable_orientation = "gauche"
                
        elif variable_orientation == "bas":
            y_fourmi += 1
            verif_coordonnee()
            if config_courante[y_fourmi][x_fourmi] == 0:
                config_courante[y_fourmi][x_fourmi] += 1
                variable_orientation = "gauche"
            else :
                config_courante[y_fourmi][x_fourmi] -= 1
                variable_orientation = "droite"

        elif variable_orientation == "droite":
            x_fourmi += 1
            verif_coordonnee()
            if config_courante[y_fourmi][x_fourmi] == 0:
                config_courante[y_fourmi][x_fourmi] += 1
                variable_orientation = "bas"
            else :
                config_courante[y_fourmi][x_fourmi] -= 1
                variable_orientation = "haut"

        elif variable_orientation == "gauche":
            x_fourmi -= 1
            verif_coordonnee()
            if config_courante[y_fourmi][x_fourmi] == 0:
                config_courante[y_fourmi][x_fourmi] += 1
                variable_orientation = "haut"
            else :
                config_courante[y_fourmi][x_fourmi] -= 1
                variable_orientation = "bas"
        maj_grille()
        if x == "automate":
            canevas.after(scale_vitesse.get(), lambda:deplacement("automate"))
    return 

def verif_coordonnee():
    '''Fonction permettant de modifier les coordonnees si la fourmi doit changer de cote'''
    global x_fourmi, y_fourmi

    if y_fourmi < 0: 
            y_fourmi = n-1

    if y_fourmi > n-1:
            y_fourmi = 0

    if x_fourmi > n-1:
            x_fourmi = 0

    if x_fourmi < 0:
            x_fourmi = n-1

def automate():
    '''Fonction activant l'automate'''
    global var_pause
    var_pause = False
    deplacement("automate")

def pause():
    '''Fonction permettant d'arreter l'automate'''
    global var_pause

    var_pause = True

def save():
    '''Sauvegarde la partie en cours'''
    fic = open("sauvegarde.txt", 'w')
    for i in range(n):
        for j in range(n):
            fic.write(str(config_courante[i][j]) + "\n")
    fic.write(str(y_fourmi) + '\n')
    fic.write(str(x_fourmi) + '\n')
    fic.write(variable_orientation)
    fic.close()

def load():
    '''Fonction permettant de charger une partie sauvegardee'''
    global config_courante, x_fourmi, y_fourmi, variable_orientation

    fic = open("sauvegarde.txt", 'r')

    for i in range(n):
        for j in range(n):
            val = int(fic.readline())
            config_courante[i][j] = val
    
    lignes = fic.readlines()
    x_fourmi = int(lignes[1])
    y_fourmi = int(lignes[0])
    variable_orientation = lignes[2]
    fic.close()
    return maj_grille()

def retour(): #ENCORE EN PHASE DE DVPT
    '''Fonction qui permet de revenir d'une etape en arriere'''
    global config_courante, x_fourmi, y_fourmi

    if config_courante[y_fourmi][x_fourmi] == 1 : #si c'est noir
        config_courante[y_fourmi][x_fourmi] = 0 #on remet la case en blanc
        if variable_orientation == "gauche":
            y_fourmi -= 1
            variable_orientation = "bas"
        if variable_orientation == "droite":
            y_fourmi += 1
            variable_orientation = "bas"
        if variable_orientation == "haut":
            x_fourmi += 1
            variable_orientation = "gauche"
        if variable_orientation == "droite":
            x_fourmi -= 1
            variable_orientation = "droite"
    else :
        config_courante[y_fourmi][x_fourmi] = 1 #on remet la case en noir
        if variable_orientation == "gauche":
            y_fourmi += 1
            variable_orientation = "bas"
        if variable_orientation == "droite":
            y_fourmi -= 1
            variable_orientation = "bas"
        if variable_orientation == "haut":
            x_fourmi -= 1
            variable_orientation = "gauche"
        if variable_orientation == "bas":
            x_fourmi += 1
            variable_orientation = "droite"
    maj_grille()

#########################################
###PARTIE PRINCIPALE

##Creation des Widgets
fenetre = Tk()
canevas = Canvas(fenetre, height=HAUTEUR, width=LARGEUR, highlightthickness=4, highlightbackground="ForestGreen")

font_base = Font(family='Helvetica', size=12, weight='bold') #création d'une police de base avec mise en gras du texte

#Boutons

bouton_creer_fourmi = Button(fenetre, text="Creer une fourmi", font=font_base, width=15, height=3, bg="darkSeaGreen1", fg="forest green", command=creation_fourmi)

    #Bouton play pour lancer le jeu de manière automatique
bouton_play = Button(fenetre, text="Play", font=font_base, width=10, height=3, command=automate)

    #Bouton next pour passer les étapes une à une
bouton_next = Button(fenetre, text="Next", font=font_base, width=10, height=3, command=lambda:deplacement("not automate"))

    #Bouton pause pour mettre le jeu en pause
bouton_pause = Button(fenetre, text="Pause", font=font_base, width=10, height=3, command=pause)

    #Chargement des images pour les boutons fleches
im_haut = PhotoImage(file = r"C:\Users\Laura.DESKTOP-OMQOELF\Documents\cours\Université\in200\Projet fourmi\PROJET-FOURMI-DE-LANGTON\fleche_haut.png")
im_bas = PhotoImage(file = r"C:\Users\Laura.DESKTOP-OMQOELF\Documents\cours\Université\in200\Projet fourmi\PROJET-FOURMI-DE-LANGTON\fleche_bas.png")
im_droite = PhotoImage(file = r"C:\Users\Laura.DESKTOP-OMQOELF\Documents\cours\Université\in200\Projet fourmi\PROJET-FOURMI-DE-LANGTON\fleche_droite.png")
im_gauche = PhotoImage(file = r"C:\Users\Laura.DESKTOP-OMQOELF\Documents\cours\Université\in200\Projet fourmi\PROJET-FOURMI-DE-LANGTON\fleche_gauche.png")

    #Bouton fleches
bouton_haut = Button(fenetre, image = im_haut, borderwidth=3, command= lambda : orientation_fourmi("haut"))
bouton_bas = Button(fenetre, image = im_bas, borderwidth=3, command= lambda : orientation_fourmi("bas"))
bouton_droit = Button(fenetre, image = im_droite, borderwidth=3, command= lambda : orientation_fourmi("droite"))
bouton_gauche = Button(fenetre, image = im_gauche, borderwidth=3, command= lambda : orientation_fourmi("gauche"))

    #Bouton sauvegarde
bouton_save = Button(fenetre, text="Sauvegarde", font=font_base, width=10, height=3, command=save)

    #Bouton load
bouton_load = Button(fenetre, text="Load", font=font_base, width=10, height=3, command=load)

    #Bouton retour
bouton_retour = Button(fenetre, text="Retourne", font=font_base, width=10, height=3, command=retour)

#Labels
txt_orientation = Label(text="Choisir l'orientation\n de la fourmi :", font=font_base, width=15, height=3, bg="darkSeaGreen1", fg="forest green", padx=15)
txt_informatif = Label(text="", font=font_base, width=15, height=3, bg="darkSeaGreen1", fg="forest green", padx=15)

#Scale pour la vitesse
scale_vitesse = Scale(fenetre, orient='horizontal', from_=0, to=500, tickinterval=100, length=400, label='Vitesse')

##Placement des widgets

#Placement du canevas
canevas.grid(column=3, row=0, rowspan=4, columnspan=4)

#Placement des boutons

    #bouton pour creer une fourmi
bouton_creer_fourmi.grid(column=0, row=1, columnspan=2, rowspan=2, padx=5)

    #bouton pour choisir l'orientation
bouton_bas.grid(column =1, row = 1, rowspan=2, sticky="s")
bouton_haut.grid(column =1, row = 2, rowspan=2, sticky="n")
bouton_droit.grid(column =2, row = 2)
bouton_gauche.grid(column =0, row = 2)

    #Bouton play
bouton_play.grid(column=1, row=1)

    #Bouton next
bouton_next.grid(column=1, row=3)

    #Bouton pause
bouton_pause.grid(column=1, row=2)

    #Bouton save
bouton_save.grid(column=10, row=1, padx=5)

    #Bouton load
bouton_load.grid(column=10, row=2, padx=5)

    #Bouton retour
bouton_retour.grid(column=10, row=3, padx=5)

#Placement des labels

    #label demandant de choisir l'orientation
txt_orientation.grid(column=0, row=1, columnspan=3, padx=10)

    #label qui affiche l'orientation pour la fourmi choisi par l'utilisateur 
txt_informatif.grid(column=0, row=0, columnspan=3, padx=10)

#Placement des scales
scale_vitesse.grid(column=4, row =5)


###BOUCLE PRINCIPALE
jeu_Fourmi()
fenetre.mainloop()
