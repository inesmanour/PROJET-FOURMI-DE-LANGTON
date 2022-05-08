# PROJET-FOURMI-DE-LANGTON
GROUPE LDDBI

INES MANOUR

LAURA LEFEVRE

ADAM KEDDIS

###############################################################################

Lien du GitHub : https://github.com/uvsq22103405/PROJET-FOURMI-DE-LANGTON.git

-Présentation de la fourmi de Langton :
    La Fourmi de Langton est un automate cellulaire compose d’une grille a deux dimensions et d’une fourmi. L'objectif de ce projet est d'implémenter une interface graphique à l'aide de la bibliothèque Tkinter permettant d'afficher le comportement de cet automate.

-Composantes :
    - Une grille composée de cases pouvant être soit blanche soit noire. La grille a la propriété d'etre un tore, c'est à dire que si la foumi sort en bas, elle réaparaît en haut, si elle sort a droite, elle resort a gauche et vice versa.
    - La fourmi possède une position sur la grille et une orientation.

-Regles de base et deroulement d'une etape :
    - Si la fourmi se trouve sur une case noire, elle tourne de 90° vers la gauche, change la couleur de la case en blanc et avance d'une case
    - Si la fourmi se trouve sur un case blanche, elle tourne de 90° vers la droite, change la couleur de la case en noir et avance d'une case


-Notice d'utilisation lors de l'execution du programme :
    Lorsque l'on execute le programme, une interface graphique s'ouvre ("Projet 2 : Fourmi de Langton"). 
    
    Au centre de la fenetre se trouve la grille avec n cases (30 par defaut), en bas a droite un bouton quitter pour fermer la fenetre et sur la gauche un bouton pour creer une fourmi.
    
    Lorsque l'on clique sur "Creer une fourmi", le programme positionne aleatoirement une fourmi dans la grille (symbolise par une case noire) et des boutons avec des fleches s'affichent. Ces boutons permettent a l'utilisateur de choisir l'orientation de la fourmi (haut, bas, gauche, droite).
    
    Apres avoir choisi l'orientation de la fourmi, en haut a gauche est affiche l'orientation choisi par l'utilisateur et differents boutons/widgets apparaissent : 
        - Bouton Play : permet de lancer l'automate de la fourmi de langton de maniere automatique
        - Bouton Pause : permet de mettre l'automate en pause
        - Bouton Next : permet de passer les etapes de l'automate une a une
        - Bouton Retour : permet de revenir en arriere dans les etapes (en cours developpemment, fonction pas totalement fonctionnelle)
        - Bouton Sauvegarde : permet de sauvegarder une partie de jeu dans un fichier .txt sous le nom de sauvegarde.txt
        - Bouton Load : permet de charger une partie de jeu enregistre sous le nom de sauvegarde.txt
        - Bouton Quitter : permet de quitter le jeu en fermant la fenetre
        - Scale Temps d'execution (ms) : permet de choisir le temps entre les differentes etapes et donc de regler la vitesse d'execution (de 0 ms a 500 ms)


-Explications et details du programme en lui-meme :

    *Structure generale :
        Le code est structuré par une entete (nom projet, noms etudiants, filliere) et par 5 parties :
            - IMPORT DES LIBRAIRIES : import des differentes librairies utilisees dans le programme et necessaire a son bon fonctionnement

            - VARIABLES GLOBALES : creation des differentes variables globales du programme qui seront modifies lors des differents appels de fonctions

            - DEFINITION DES FONCTIONS : definitions des differentes fonctions du programme

            - CREATION ET PLACEMENT DES WIDGETS : creation et placement des differents widgets du programme : fenetre, canevas, font, boutons, labels, scale

            - BOUCLE PRINCIPALE : partie permettant le lancement du programme avec l'appelle de la fonction principale "jeu_Fourmi()" ainsi que la fonction .mainloop() pour    lancer l'interface graphique de Tkinter

    *Informations sur les variables globales modifiables par l'utilisateur :
        - La largeur et la hauteur du canevas peuvent etre modifiees. 
        Recomendation : garder les valeurs par defauts (700x700) pour garantir un affichage correct des widgets. 

        - La constante de proportionnalite n a pour valeur par defaut n=30, cela signifie que la grille sera de 30x30. Cette constante peut etre modifiee ce qui permettra d'avoir un plus grand ou un moins grand nombre de cases dans la grille. 
        Attention : plus n est grand plus le programme sera "gourmand" et risque d'avoir du mal a fonctionner. 


    *Details et explications des fonctions :
        - jeu_Fourmi(): 
            Cette fonction est la fonction principale du jeu. Elle est appellee lors de l'execution du programme et permet le lancement du jeu.
            Dans cette fonction, on appelle une premiere fonction qui permet de cacher les widgets qui ne doivent pas encore etre affiches.
            Ensuite, on appelle une fonction permettant de la creation d'une configuration courante vide (liste imbriquees remplies de n 0)
                -> Cette fonction est automatiquement appelee lors de l'execution du programme.

        - widget_a_cacher(): 
            Cette fonction est la premiere fonction appellee par la fonction jeu_Fourmi(). C'est elle qui permet de cacher les widgets lors de l'execution du programme. Les widgets caches sont des widgets comme play, next, etc. qui seront utiles lors du jeu (apres avoir creer une fourmi et choisi son orientation). Pour cacher ces differents widgets, on appelle dans cette fonction une autre fonction qui a la fonctionnalite de cacher n'importe quel widget envoye en parametre.
                -> Cette fonction est automatiquement appelee lors de l'execution du programme.

        - configuration_courante_vide():
            Cette fonction est appelee par jeu_Fourmi() etpermet la creation d'une configuration courante vide, c'est a dire, une liste a deux dimensions representant une matrice avec n lignes et n colonnes. On modifie donc la variable globale configuration_courante en ajoutant n fois des listes de n 0.
            Apres avoir cree notre configuration courante vide, on appelle une fonction permettant d'initialiser une grille proportionnelle a la taille de la configuration courante en se servant de cette variable globale.
                -> Cette fonction est automatiquement appelee lors de l'execution du programme.

        - init_grille():
            Cette fonction est appelee par configuration_courante_vide() et permet de creer une grille representative de la configuration courante et proportionnelle a celle-ci. On se sert d'une variable globale "cases" ou on y ajoute les differentes cases crees par cette fonction.
                -> Cette fonction est automatiquement appelee lors de l'execution du programme.

         - maj_grille(): 
            Cette fonction est appelee par differentes fonctions. Elle permet de mettre a jour la grille en se basant sur la configuration courante qui est modifie lors du jeu. En effet, lorsque la configuration courante est modifie, c'est a dire lorsque des 0 sont remplaces par des 1 ou inversement, cette fonction est appelee pour permettre l'affichage dans l'interface graphique des modifications faites. On parcours la configuration courante, si on a un 0, alors la case s'affiche blanche, si on a un 1, la case s'affiche noir. 
                -> Cette fonction est automatiquement appelee par differentes fonctions du programme (creation_fourmi, deplacement, load, retour).

            Idee a approfondir : Cette fonctionnalite du programme pourrait etre optimiser en trouvant une autre methode permettant de ne pas avoir a parcourir entierement la configuration courante. On pourrait par exemple utiliser les coordonnees de la fourmi et modifier directement cette valeur plutot que de parcourir entierement la configuration courante.

        - creation_fourmi():
            Cette fonction de creer une fourmi et de la placer de maniere aleatoire sur la grille.
            On commence par attribuer des coordonnees aleatoires entre 0 et n-1, grace a la methode randint de la librairie random. Apres cette etape, nous avons nos coordonnees et nous pouvons donc modifier la configuration courante en ajouter un 1 aux nouvelles coordonnees de la fourmi, ce qui symbolisera la fourmi par une case noire. On appelle maj_grille() pour mettre la grille a jour.
            Ensuite, la fonction appelle une autre fonction permettant de cacher le bouton qui permet de creer une fourmi.
            Pour terminer, on appelle une fonction qui permet d'afficher un lot de fleche pour choisir l'orientation de la fourmi creee.
                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton "bouton_creer_fourmi".

        - hide(widget, presence:bool):
            Cette fonction est la fonction permettant d'afficher ou de cacher n'importe quel widget donne en parametre. Le parametre presence permet quant a lui de dire a la fonction si le widget en question est affiche ou non et donc de lui dire s'il doit le cacher ou l'afficher. 
            Si le parametre presence est sur True, cela signifie qu'il est affiche et donc que la fonction a pour objectif de le cacher en gardant en memoire les options de grilles. C'est a dire que l'on peu cacher et afficher autant de fois que l'on veut le widget, ces options comme sa position ne seront pas perdus mais gardes en memoire. Pour faire cela, on utilise la fonction .grid_remove(). 
            A contrario, si le parametre presence est sur False, il est donc cache de l'interface graphique et cette fonction va permettre de l'afficher en utilisant simplement la fonction .grid().
                -> Cette fonction est appelee par la fonction widget_a_cacher(), widget_a_afficher() et creation_fourmi().

        - affiche_fleche():
            Cette fonction permet simplement d'afficher les boutons fleches et le label associe. Ces boutons vont permettre a l'utilisateur de choisir l'orientation de la fourmi creer par ce dernier. Le label associe est un label permettant de dire a l'utilisateur de choisir l'orientation de la fourmi.
            Pour ce faire, on appelle la fonction hide() avec le parametre de presence sur False pour permettre a la fonction d'afficher les widgets.
                -> Cette fonction est automatiquement appelee par la fonction creation_fourmi

        - cache_fleche(): 
            Cette fonction permet simplement de cacher les boutons fleches et le label associe. En effet, apres le choix de l'orientation par l'utilisateur, il faut cacher les  boutons fleches et le label associe pour afficher ensuite ceux necessaires au jeu. 
            Pour ce faire, on appelle de nouveau la fonction hide() mais avec le parametre de presence sur True pour permettre a la fonction de cacher ces widgets.
                -> Cette fonction est automatiquement appelee par la fonction orientation_fourmi().

        - changement_txt(label, txt_modif:str): 
            Cette fonction permet de changer le texte d'un label. On passe en parametre le label a modifier ainsi que le texte que l'on veut mettre (une chaine de caractere est attendue).
            Pour ce faire, on utilise la fonction .configure() avec le texte passe en parametre de la fonction.
                -> Cette fonction est automatiquement appelee par la fonction orientation_fourmi().

        - widget_a_afficher():
            Cette fonction permet d'afficher les differents widgets necessaires au jeu.
            Pour ce faire, on a de nouveau recours a la fonction hide avec comme parametre de presence False pour pouvoir les afficher.
            On affiche un label de texte informatif qui permettra d'ecrire l'orientation choisi par l'utilisateur et les differents boutons : next, play, pause, save, load, retour et le scale vitesse.
                -> Cette fonction est automatiquement appelee par la fonction orientation_fourmi().
            
        - orientation_fourmi(direction:str):
            Cette fonction permet d'attribuer l'orientation de depart a la fourmi choisi par l'utilisateur.
            On commence par cacher les fleches et le label en appellant la fonction cache_fleche et on affiche les differents widgets necessaires en appellant la fonction widget_a_afficher(). 
            Cette fonction a pour parametre la direction choisi par l'utilisateur. En effet, en fonction du bouton sur lequel l'utilisater aura clique, ce parametre va varier entre : "haut", "bas", "gauche" et "droite".
            Ainsi, en fonction de l'orientation, on va appeller la fonction changement_txt pour modifier le label txt_informatif pour ecrire et afficher l'orientation choisie.
                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur les boutons fleches.
        
        - deplacement():
            Cette fonction est la fonction permettant le deplacement de la fourmi.

            Tout d'abord, la fonction doit verifier si la variable globale pause est sur False ou non. Si elle est sur False, cela signifie que le programme ne doit pas etre en pause. Ainsi, on demarre l'automate. En fonction de l'orientation de la fourmi, on va modifier les positions de la fourmi en fonction de son orientation, ensuite on appelle une fonction qui va verifier les coordonnees de la fourmi pour savoir si elle est a proximite d'un cote et donc devoir changer de cote car la grille a la fonctionnalite d'etre un tore comme dit precedemment. Ensuite, on modifie la variable globale de l'orientation et en fonction de la couleur de la case sur laquelle la fourmi se trouve et on modifie la couleur de cette derniere. Cette methode fonctionne puisque lorsque l'on creer un fourmi, on la place aleatoirement sur la grille en la representant par une case noir, lors de cette etape c'est l'utilisateur qui choisi l'orientation et donc n'est pas defini en fonction de la couleur de la case. Cela explique pourquoi la premiere etape est l'avancement d'une case par la fourmi. 
            
            Apres avoir effectuer le deplacement, on met a jour la grille en appellant la fonction maj_grille().
            
            Ensuite, on regarde si la variabe globale auto est sur True. Si elle est sur True, alors cela signifie que le programme doit s'executer de maniere automatique. 
            
            Ainsi, on rappelle la fonction deplacement de maniere automatique grace a la methode .after(). On passe en premier parametre la vitesse d'execution que l'on recupere grace au scale place sur l'interface graphique par un .get(). En second parametre on met la fonction deplacement qui permet de rappeller notre fonction de maniere automatique. L'utilisateur peut donc regler en temps reel la temps d'execution entre les differents deplacements de la fourmi.
                -> Cette fonction est automatiquement appelee par la fonction next() et automate().

        - verif_coordonnee():
            Cette fonction permet de verifier les coordonnees de la fourmi lors de ses deplacements. C'est cette fonction qui permet de remplir la condition associe a la grille qui dit que c'est un tore. Ainsi, lorsque la fourmi est colle au cote :
                - haut ; la fonction va modifier sa coordonnee y en la passant en bas de la grille (y=n-1).
                - bas ; la fonction va modifier sa coordonnee y en la passant en haut de la grille (y=0)
                - gauche ; la fonction va modifier sa coordonnee x en la passant a droite de la grille (x=n-1)
                - droite ; la fonction va modifier sa coordonnee x en la passant a gauche de la grille (x=0)

                -> Cette fonction est automatiquement appellee par la fonction deplacement.
        
        - automate():
            Cette fonction permet d'activer le deplacement automatique de la fourmi et donc de lancer l'automate associe au jeu.

            Pour ce faire, on passe la variable pause en False pour etre sur quelle soit bien sur False (variable pouvant etre modifier lorsque l'utilisateur clique sur le bouton pause). Si on ne met pas cette variable sur False, alors le deplacement ne pourra pas se faire dans la fonction deplacement.

            On passe la fonction auto en True, pour que lors de l'appel de la fonction deplacement, on puisse rentrer dans le if permettant le rappeller de maniere automatique la fonction deplacement.

            On appelle ensuite la fonction deplacement(). La variable pause mise sur False et le mode auto sur True, la fonction deplacement() sera appellee de maniere automatique et il sera alors possible de voir sur l'interface graphique le deplacement de la fourmi.
                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Play.

        - pause():
            Cette fonction permet de mettre l'automate en pause.

            Pour ce faire, la fonction modifie simplement la variable pause en True. Ainsi, dans la fonction deplacement, la variable pause sera sur True et l'automate s'arretera.

                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Pause.

        - next():
            Cette fonction permet de passer les etapes du programme une a une.

            Pour ce faire, si la variable pause est sur True, on la passe en False pour permettre le deplacement lors de l'appel de la fonction deplacement(). Ensuite, si la variable auto est sur True, on la passe en False pour s'assurer que dans l'appel de la fonction deplacement, elle ne sera pas rappellee de maniere automatique.
            Apres avoir verifier et modifier si necessaire les variables globales pause et auto on peut appeller la fonction deplacement pour permettre un seul deplacement.
                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Next.
            
        - save(): 
            Cette fonction permet de sauvegarder une partie en cours dans un fichier texte sous le nom de "sauvegarde.txt".

            La fonction commence par ouvrir le fichier sauvegarde.txt en fonction 'write' pour permettre l'ecriture dans le fichier. Si celui-ci n'existe pas, alors il est automatiquement cree.

            Ainsi, par le biais d'une boucle, on ecrit chaque element de la configuration courante dans le fichier txt en y ajoutant un retour a la ligne a chaque fois. On oublie pas de convertir le 0 ou le 1 de la configuration courante en chaine de caractere pour qu'il puisse etre ecrit dans le fichier .txt.

            On ecrit ensuite a la fin, l'un apres l'autre : la position y, la position x et la variable orientation. 
            Ainsi, il sera facile de recupere ses informations essentielles pour pourvoir ensuite charger une partie.

            On n'oublie pas ensuite de fermer le fichier avec .close().

            Attention : le fichier sera sauvegarder dans le dossier courant (celui ou vous vous trouvez au niveau du terminal)

                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Sauvegarde.
        
        - load():
            Cette fonction permet de charger une partie sauvegardee sous le nom de "sauvegarde.txt".

            La fonction commence par ouvrir le fichier sauvegarde.txt en mode lecture ("read"). 

            Ainsi, par le biais d'une boucle, on recupere les valeurs du fichier .txt en convertissant les element en int. On modifie la configuration courante avec la valeur recuperer et donc recuperer la configuration courante voulu sauvegarder prealablement.

            On stocke ensuite dans une variable les derniers elements restants (les positions et l'orientation). On a donc une liste a compose de trois elements : y_fourmi, x_fourmi, variable_orientation. 
            On peut ensuite grace aux indices de ces elements, les recuperer et modifier nos variables globales avec les bonnes valeurs. 

            On n'oublie pas ensuite de fermer le fichier acec .close().

            Pour finir, on met a jour la grille pour afficher la configuration courante sauvegardee.

            Attention : si vous ne vous trouvez pas dans le fichier ou sauvegarde.txt a ete cree, la fonction ne fonctionnera pas. Pour ce faire, utiliser la fonction cd suivi du chemin vers le fichier .txt dans le terminal.

                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Load.

        - retour():
            Cette fonction permet de retourner en arriere dans les etapes du jeu.

            La fonction regarde la couleur de la case sur lequel se trouve la fourmi. Si c'est 1 (noir), la case est remise en blanche (0), et inversement, si c'est 0, la case est remise en noir (1). Ensuite, en fonction de l'orientation de la fourmi il est possible de retrouver l'enchainement des etapes et donc de remonter dans ces dernieres.

            La fonction appelle la fonction maj_grille a chaque etape rembobinee.

            Information : Cette fonction n'est pas encore fonctionnelle, elle est en developpement mais nous n'avons pas encore reussi a la faire fonctionner

                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Retour.

        - fermer_fenetre():
            Cette fonction permet de fermer la fenetre et donc de quitter le jeu.

            Pour ce faire, on appelle simplement la fonction propre a Tkinter : .destroy().

                -> Cette fonction est automatiquement appelee lorsque l'utilisateur clique sur le bouton Quitter.

    
    * Informations sur la partie de la creation des widgets et les placements :
        Cette partie est aussi structure en differentes 2 sous-parties (Creation, Placement), elles-memes structurees en plusieurs sous-parties :

        Partie Creation :
            - Widgets principaux : Creation de la fenetre, creation du canevas pour l'affichage de la grille et ajout du titre

            - Creation d'une police de "base" : Police d'ecriture utilisee a chaque fois (caractere en gras, type Helvetica et de taille 12)

            - Creation des Boutons : tous les boutons sont nommes de la meme maniere : bouton_nomDuBouton
                nomDesBoutons : creer_fourmi, play, next, pause, haut, bas, droit, gauche, save, load, retour, quitter

                Les boutons associes aux fleches (haut, bas, droit, gauche) pour le choix de l'orientation ont la specificite d'afficher une image a la place des caracteres. Pour ce faire, une partie est dedie au chargement des images. On creer donc 4 variables dans lequel on stocke l'image grace a la methode propre a Tkinter : PhotoImage. Dans cette methode, on doit mettre le chemin vers l'image a charger. Il ne faut donc pas oublier d'avoir ces 4 images dans le dossier et modifier le chemin pour que l'affichage fonctionne correctement. Le resultat a l'affichage doit etre 4 fleches avec les differentes orientations.
                De plus, lors de la creation des boutons fleches, pour pouvoir appeller la fonction orientation (lorsque l'on clique dessus) avec le parametre qu'il faut, on passe une fonction lambda avec l'orientation associee. 
            
            - Creation des labels : creation de 2 labels :
                - txt_orientation : demande a l'utilisateur de choisir l'orientation de la fourmi
                - txt_informatif  : affiche l'orientation choisie par l'utilisateur

            - Creation de scale : creation d'un scale pour permettre a l'utilisateur de choisir le temps d'execution des deplacements de la fourmi, donc de choisir la vitesse  de celui-ci. Le scale va de 0 a 500, ces variables peuvent etre modifiees.

        Partie Placement :
            - Canevas : On place le canevas au centre de la fenetre

            - Boutons : Les boutons sont places autour du canevas et on ajoute un padx de 5 pour eviter qu'ils ne soient colles au canevas. 

            - Labels : Les labels sont places sur le cote gauche de la fenetre et on ajoute un padx de 10 pour eviter qu'ils ne soient colles au canevas.

            - Scale : Le scale est place sous le canevas et donc sous la grille en position horizontale.


Signature : Ce programme a ete realise par Ines MANOUR, Laura LEFEVRE et Adam KEDDIS ; etudiants a l'UVSQ en LDDBI ; dans le cadre d'un projet du module IN200.
            08/05/2022
