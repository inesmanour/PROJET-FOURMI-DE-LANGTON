# PROJET-FOURMI-DE-LANGTON

README-Version Courte
###############################################################################

GROUPE LDDBI

INES MANOUR

LAURA LEFEVRE

ADAM KEDDIS

###############################################################################

Lien du GitHub : https://github.com/uvsq22103405/PROJET-FOURMI-DE-LANGTON.git

-Présentation de la fourmi de Langton :
    La Fourmi de Langton est un automate cellulaire compose d’une grille a deux dimensions et d’une fourmi. L'objectif de ce projet est d'implémenter une interface graphique à l'aide de la bibliothèque Tkinter permettant d'afficher le comportement de cet automate.


-Notice d'utilisation lors de l'execution du programme :
    Post condition au bon fonctionnement : 
        - Avoir telecharge le fichier projet_Fourmi.py
        - Avoir telecharge les 4 images : fleche_bas.png, fleche_haut.png, fleche_gauche.png, fleche_droite.png
        - Avoir modifier le chemin vers les images dans la creation des boutons (lignes 390 à 393)
        
    Boutons/widgets a disposition apres la creation de la fourmi et le choix de son orientation : 
        - Bouton Play : lancer l'automate de la fourmi de langton de maniere automatique
        - Bouton Pause : mettre l'automate en pause
        - Bouton Next : passer les etapes de l'automate une a une
        - Bouton Retour : revenir en arriere dans les etapes (en cours developpemment, fonction pas totalement fonctionnelle)
        - Bouton Sauvegarde : sauvegarder une partie de jeu dans un fichier sauvegarde.txt
        - Bouton Load : charger une partie de jeu enregistre sous le nom de sauvegarde.txt
        - Bouton Quitter : quitter le jeu en fermant la fenetre
        - Scale Temps d'execution (ms) : choisir le temps entre les differentes etapes

    Le programme est code de maniere a pouvoir jongler entre les boutons play, pause et next.


-Explications et details du programme en lui-meme :

    *Structure generale :
        Le code est structuré par une entete et par 5 grandes parties :
            - IMPORT DES LIBRAIRIES

            - VARIABLES GLOBALES 

            - DEFINITION DES FONCTIONS 

            - CREATION ET PLACEMENT DES WIDGETS

            - BOUCLE PRINCIPALE

    *Informations sur les variables globales modifiables par l'utilisateur :
        - Largeur, hauteur du canevas 
        Recommandation : garder les valeurs par defauts (700x700) pour garantir un affichage correct des widgets. 

        - Constante de proportionnalite n (valeur par defaut n=30)
        Attention : plus n est grand plus le programme sera "gourmand" et risque d'avoir du mal a fonctionner. 


    *Details et explications des fonctions :
        - jeu_Fourmi(): 
            Cette fonction est la fonction principale du jeu. Elle est appellee lors de l'execution du programme et permet le lancement du jeu.
                -> Cette fonction est automatiquement appelee lors de l'execution du programme.

        - widget_a_cacher(): 
            Cette fonction permet de cacher les widgets lors de l'execution du programme. 
                -> Cette fonction est automatiquement appelee lors de l'execution du programme.

        - configuration_courante_vide():
            Cette fonction permet la creation d'une configuration courante vide representant une matrice avec n lignes et n colonnes.
                -> Cette fonction est automatiquement appelee lors de l'execution du programme.

        - init_grille():
            Cette fonction permet de creer une grille representative de la configuration courante.
                -> Cette fonction est automatiquement appelee lors de l'execution du programme.

         - maj_grille(): 
            Cette fonction permet de mettre a jour la grille en se basant sur la configuration courante. 
                -> Cette fonction est automatiquement appelee par differentes fonctions du programme (creation_fourmi, deplacement, load, retour).

            Idee a approfondir : Cette fonctionnalite du programme pourrait etre optimisee en trouvant une autre methode permettant de ne pas avoir a parcourir entierement la configuration courante. On pourrait par exemple utiliser les coordonnees de la fourmi et modifier directement cette valeur plutot que de parcourir entierement la configuration courante.

        - creation_fourmi():
            Cette fonction permet de creer une fourmi et de la placer de maniere aleatoire sur la grille.
                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton "bouton_creer_fourmi".

        - hide(widget, presence:bool):
            Cette fonction permet d'afficher ou de cacher n'importe quel widget donne en parametre. Le parametre presence permet quant a lui de dire a la fonction si le widget en question est affiche ou non et donc de lui dire s'il doit le cacher ou l'afficher. 
                -> Cette fonction est appelee par la fonction widget_a_cacher(), widget_a_afficher() et creation_fourmi().

        - affiche_fleche():
            Cette fonction permet simplement d'afficher les boutons fleches et le label associe. Ces boutons vont permettre a l'utilisateur de choisir l'orientation de la fourmi.
                -> Cette fonction est automatiquement appelee par la fonction creation_fourmi

        - cache_fleche(): 
            Cette fonction permet simplement de cacher les boutons fleches et le label associe. 
                -> Cette fonction est automatiquement appelee par la fonction orientation_fourmi().

        - changement_txt(label, txt_modif:str): 
            Cette fonction permet de changer le texte d'un label. On passe en parametre le label a modifier ainsi que le texte que l'on veut mettre (une chaine de caractere est attendue).
                -> Cette fonction est automatiquement appelee par la fonction orientation_fourmi().

        - widget_a_afficher():
            Cette fonction permet d'afficher les differents widgets necessaires au jeu.
                -> Cette fonction est automatiquement appelee par la fonction orientation_fourmi().
            
        - orientation_fourmi(direction:str):
            Cette fonction permet d'attribuer l'orientation de depart a la fourmi choisi par l'utilisateur.
                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur les boutons fleches.
        
        - deplacement():
            Cette fonction est la fonction permettant le deplacement de la fourmi.
                -> Cette fonction est automatiquement appelee par la fonction next() et automate().

        - verif_coordonnee():
            Cette fonction permet de verifier les coordonnees de la fourmi lors de ses deplacements. C'est cette fonction qui permet de remplir la condition associe a la grille qui dit que c'est un tore.
                -> Cette fonction est automatiquement appellee par la fonction deplacement.
        
        - automate():
            Cette fonction permet d'activer le deplacement automatique de la fourmi et donc de lancer l'automate associe au jeu.
                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Play.

        - pause():
            Cette fonction permet de mettre l'automate en pause.
                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Pause.

        - next():
            Cette fonction permet de passer les etapes du programme une a une.
                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Next.
            
        - save(): 
            Cette fonction permet de sauvegarder une partie en cours dans un fichier texte sous le nom de "sauvegarde.txt".

            Attention : le fichier sera sauvegarde dans le dossier courant

                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Sauvegarde.
        
        - load():
            Cette fonction permet de charger une partie sauvegardee sous le nom de "sauvegarde.txt".

            Attention : vous devez vous trouvez dans le dossier ou le fichier sauvegarde.txt a ete sauvegarde

                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Load.

        - retour():
            Cette fonction permet de retourner en arriere dans les etapes du jeu.

            Information : Cette fonction n'est pas encore fonctionnelle, elle est en developpement mais nous n'avons pas encore reussi a la faire fonctionner

                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Retour.

        - fermer_fenetre():
            Cette fonction permet de fermer la fenetre et donc de quitter le jeu.
                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Quitter.

    
    * Informations sur la partie de la creation des widgets et les placements :
        Cette partie est aussi structure en 2 sous-parties (Creation, Placement), elles-memes structurees en plusieurs sous-parties :

        Partie Creation :
            - Widgets principaux : fenetre, canevas, titre

            - Creation d'une police de "base" : Police d'ecriture utilisee a chaque fois

            - Creation des Boutons : tous les boutons sont nommes de la meme maniere : bouton_nomDuBouton
                nomDesBoutons : creer_fourmi, play, next, pause, haut, bas, droit, gauche, save, load, retour, quitter

                Les boutons associes aux fleches (haut, bas, droit, gauche) pour le choix de l'orientation ont la specificite d'afficher une image a la place des caracteres. Pour ce faire, une partie est dedie au chargement des images. On creer donc 4 variables dans lequel on stocke l'image. Dans cette methode, on doit mettre le chemin vers l'image a charger. Il ne faut donc pas oublier d'avoir ces 4 images dans le dossier et modifier le chemin pour que l'affichage fonctionne correctement.
            
            - Creation des labels :
                - txt_orientation : demande a l'utilisateur de choisir l'orientation de la fourmi
                - txt_informatif  : affiche l'orientation choisie par l'utilisateur

            - Creation de scale : creation d'un scale pour permettre a l'utilisateur de choisir le temps d'execution des deplacements de la fourmi.

        Partie Placement :
            - Canevas : On place le canevas au centre de la fenetre

            - Boutons : Les boutons sont places autour du canevas

            - Labels : Les labels sont places sur le cote gauche de la fenetre

            - Scale : Le scale est place sous le canevas


Signature : Ce programme a ete realise par Ines MANOUR, Laura LEFEVRE et Adam KEDDIS ; etudiants a l'UVSQ en LDDBI ; dans le cadre d'un projet du module IN200.
            08/05/2022
