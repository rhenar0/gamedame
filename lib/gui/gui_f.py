import tkinter as tk
import time
import tkinter.font as tkFont
from tkinter import *

coordX = 0
coordY = 0

interface = { #On créer une table pour utiliser ces valeurs dans des fonctions ayant pour seul argument "event"
    "gui" : "null",
    "largeur" : "null",
    "hauteur" : "null",
    "coord" : "null",
    "xCaseDebut" : "[0,0]",
    "yCaseDebut" : "[0,0]",
    "typeCaseDebut" : "null",
    "xCaseFin": "[0,0]",
    "yCaseFin": "[0,0]",
    "typeCaseFin": "null",
    "couleurCase" : "null",
}

def Canva():
    """
    Fonction qui va générer notre fenêtre graphique globale qui va nous servir dans toute la suite du programme.

    :return: Canva : C'est la partie de la fenêtre que l'on "édite" dans la suite du programme.
             Damier : C'est la fenêtre dans toute sa globalité (contenant le titre, la "croix" pour fermer la fenêtre ...
             SW : SW pour Screen width, récupère la largeur d'écran.
             SH : SH pour Screen height, récupère la hauteur d'écran.

    """

    Damier = tk.Tk()
    Damier.title("Jeu de Dame")
    SW = Damier.winfo_screenwidth()
    SH = Damier.winfo_screenheight()
    Canva = tk.Canvas(Damier, width=SW*0.42, height=SH*0.7, bg="ivory")
    Canva.pack()
    return Canva, Damier, SW, SH

def CreationDamier(gui, SW, SH):
    """
    Fonction qui va non seulement délimiter les "bords" du damier mais également créer les cases blanches et noires de la
    bonne taille.

    :param gui: Interface graphique créée via tkinter.
    :param SW: SW pour Screen width, récupère la largeur d'écran.
    :param SH: SH pour Screen height, récupère la hauteur d'écran.

    :return: La fonction renvoie un tableau de coordonnées contenant dans l'ordre :
            - Les coordonnées x,y du coin supérieur gauche de la case dans les deux premiers emplacement de la liste
            - Les coordonnées x,y du coin inférieur droit de la cas dans le 3ème et 4ème emmplacement de la liste
            - Une valeur qui par défaut vaut 0 mais qui sera modifier par la suite pour faciliter le code
    """
    a = range(int(SH*0.1), int(SH*0.6), int(SW*0.03)) # Créer une liste servant par la suite à définir le nombre de colonnes
    b = range(int(SH*0.1), int(SH*0.6), int(SW*0.03)) # Créer une liste servant par la suite à définir le nombre de lignes
    # Ces listes utilisant SH et SW permettent à notre damier de s'adapter à la taille de l'écran de l'utilisateur.

    compteur1 = 1 # Nous sert par la suite a alterner les cases blanches et noires.
    compteur2 = 1 # Nous sert par la suite a alterner les cases blanches et noires.
    coordonnees=[]
    for i in a: # Définit donc colonnes par colonnes
        if compteur1%2 == 0: # On utilise la parité du compteur pour alterner d'une colonne à l'autre
            for j in b: # Définit donc lignes par lignes
                if compteur2 % 2 == 0: # On utilise la parité du compteur pour alterner d'une ligne à l'autre
                    z = int(SW * 0.03) # Variable servant à ne pas re-écrire inutilement la valeur
                    gui.create_rectangle(i, j, i+z, j+z, fill="white", outline="black") # Créer les cases
                    coordonnees.append([i, j, i+z, j+z, 0, True]) #Ajoute les coordonnées de la case comme décrit dans la présentation de la fonction
                else:
                    z = int(SW * 0.03)
                    gui.create_rectangle(i, j, i+int(SW*0.03), j+int(SW*0.03), fill="black", outline="black") # Créer les cases
                    coordonnees.append([i, j, i+z, j+z, 0, False]) # Ajoute les coordonnées de la case comme décrit dans la présentation de la fonction
                compteur2 += 1
            compteur1 += 1
        else:
            for j in b:
                if compteur2 % 2 == 0:
                    z = int(SW * 0.03)
                    gui.create_rectangle(i, j, i+z, j+z, fill="black", outline="black") # Créer les cases
                    coordonnees.append([i, j, i+z, j+z, 0, False]) # Ajoute les coordonnées de la case comme décrit dans la présentation de la fonction
                else:
                    z = int(SW * 0.03)
                    gui.create_rectangle(i, j, i+z, j+z, fill="white", outline="black") # Créer les cases
                    coordonnees.append([i, j, i+z, j+z, 0, True]) # Ajoute les coordonnées de la case comme décrit dans la présentation de la fonction
                compteur2 += 1
            compteur1 += 1

    return coordonnees


def creerpion(gui, SW, SH):
    """
    Comme ma fonction qui génères les cases au sein de mon damier les créer horizontalement de haut en bas puis répète l'opération
    de gauche à droite, ma fonction va alors créer les casesJetons de la même manière.

    :param gui: Interface graphique créée via tkinter.
    :param SW: SW pour Screen width, récupère la largeur d'écran.
    :param SH: SH pour Screen height, récupère la hauteur d'écran.

    :return: Aucune valeur de retour puisque la fonction créer des cases contenant un jeton (dernière valeur des listes
    du tableau Coord : 1 si jeton rouge 2 si jeton bleu) directement dans la fenêtre gui.
    """

    Coord = interface["coord"] # Récupères les coordonnées des cases du damier.
    for i in range(0, 10): # Afin de parcourir toutes les colonnes du damier

        if i%2 != 0: # Pour remplir les colonnes impaires
            for j in range(0, 3, 2): # Pour remplir le "haut" du damier
                j = j + i * 10 # Sert au programme à determiner combien de case il va remplir verticalement
                gui.create_oval(Coord[j][0], Coord[j][1], Coord[j][2], Coord[j][3], fill="Red")
                Coord[j][4] = 1
            for j in range(8, 10, 2): # Pour remplir le "bas" du damier
                j = j + i * 10 # Sert au programme à determiner combien de case il va remplir verticalement
                gui.create_oval(Coord[j][0], Coord[j][1], Coord[j][2], Coord[j][3], fill="blue")
                Coord[j][4] = 2

        if i%2 == 0: # Pour remplir les colonnes paires.
            for j in range(1, 3, 2): # Pour remplir le "haut" du damier
                j = j + i * 10 # Sert au programme à determiner combien de case il va remplir verticalement
                gui.create_oval(Coord[j][0], Coord[j][1], Coord[j][2], Coord[j][3], fill="red")
                Coord[j][4] = 1
            for j in range(7, 10, 2):# Pour remplir le "bas" du damier
                j = j + i * 10 # Sert au programme à determiner combien de case il va remplir verticalement
                gui.create_oval(Coord[j][0], Coord[j][1], Coord[j][2], Coord[j][3], fill="Blue")
                Coord[j][4] = 2


def CompteurTemps(temps, gui, SW, SH):
    """
    Fonction qui créer la délimitation de la fenêtre et servant à afficher le timer.

    :param temps: Récupèreras à terme le temps renvoyer par la fonction timer situé plus bas dans le code.
    :param gui: Interface graphique créée par tkinter.
    :param SW: SW pour Screen width, récupère la largeur d'écran.
    :param SH: SH pour Screen height, récupère la hauteur d'écran.

    :return: Rien car "écrit" directement dans la fenêtre graphique.
    """
    TexteStyle = tkFont.Font(family="Lucida Grande", size=20) # Définit le style de police dans la case.
    gui.create_text((SW*0.21, SH*0.028), text=temps, font=TexteStyle) # Affiche le texte (à terme le timer).
    gui.create_rectangle(SW*0.16, 2, SH*0.455, 50, outline="black") # Genère la bordure.

def Joueur1(joueur, gui, SW, SH):
    """
    Fonction qui creer la délimitation de la fenêtre et servant à afficher le Joueur1.

    :param joueur: Récupères le nom du premier joueur pour la partie.
    :param gui: Interface graphique créée par tkinter.
    :param SW: SW pour Screen width, récupère la largeur d'écran.
    :param SH: SH pour Screen height, récupère la hauteur d'écran.
    :return: Rien car "écrit" directement dans la fenêtre graphique.
    """
    TexteStyle = tkFont.Font(family="Lucida Grande", size=15) # Définit le style de police dans la case.
    gui.create_text((SW*0.02, SH*0.015), text=joueur, font=TexteStyle) # Affiche le texte (à terme le timer).
    gui.create_rectangle(SW*0.001, 2, SW*0.12, 50, outline="black") # Genère la bordure.

def Joueur2(joueur, gui, SW, SH):
    """
    Fonction qui créer la délimitation de la fenêtre et servant à afficher le Joueur2.

    :param joueur: Récupères le nom du deuxième joueur pour la partie.
    :param gui: Interface graphique créée par tkinter.
    :param SW: SW pour Screen width, récupère la largeur d'écran.
    :param SH: SH pour Screen height, récupère la hauteur d'écran.
    :return: Rien car "écrit" directement dans la fenêtre graphique.
    """
    TexteStyle = tkFont.Font(family="Lucida Grande", size=15) # Définit le style de police dans la case.
    gui.create_text((SW*0.33, SH*0.015), text=joueur, font=TexteStyle) # Affiche le texte (à terme le timer).
    gui.create_rectangle(SW*0.30, 2, SW*0.42, 50, outline="black") # Genère la bordure.


async def timer():
    """
    Fonction qui génère un timer affichant "minutes : secondes" permettant de savoir le temps depuis le début de la partie.

    :return: Pour l'instant rien mais retournera le temps (attente d'adaptation de la fonction pour la lancer en asynchrone
    par rapport a la fonction main du jeu.
    """
    minutes = 0
    while True:
        now = time.localtime(time.time())
        secondes = now[5]
        temps=[minutes, secondes]
        time.sleep(1)
        if secondes == 59:
            minutes += 1


def caseCorrespondanteDebut(event):
    """
    Fonction qui va nous donner le type et les coordonnées de la case sur laquelle on clique. Foncièrement cela va servir à savoir si on peut bouger notre pion
    et si on a survoler un pion pour le "manger"
    :param event:
    :return:
    """
    coordX = event.x
    coordY = event.y
    Coord = interface["coord"]
    for i in range(len(Coord)):
        if coordX >= Coord[i][0] and coordX <= Coord[i][2]:
            if coordY >= Coord[i][1] and coordY <= Coord[i][3]:
                interface["couleurCase"] = Coord[i][5]
                interface["typeCaseDebut"] = Coord[i][4]
                interface["xCaseDebut"] = [Coord[i][0], Coord[i][2]]
                interface["yCaseDebut"] = [Coord[i][1], Coord[i][3]]
                print(interface["typeCaseDebut"], interface["xCaseDebut"], interface["yCaseDebut"], interface["couleurCase"])

def caseCorrespondanteFin(event):
    """
    Fonction qui va nous donner le type et les coordonnées de la case sur laquelle on relache le clic.
    Foncièrement cela va servir à savoir si on peut bouger notre pion et si on a survoler un pion pour le "manger"
    :param event:
    :return:
    """
    coordX = event.x
    coordY = event.y
    Coord = interface["coord"]
    for i in range(len(Coord)):
        if coordX >= Coord[i][0] and coordX <= Coord[i][2]:
            if coordY >= Coord[i][1] and coordY <= Coord[i][3]:
                interface["typeCaseFin"] = Coord[i][4]
                interface["xCaseFin"] = [Coord[i][0], Coord[i][2]]
                interface["yCaseFin"] = [Coord[i][1], Coord[i][3]]
                print(interface["typeCaseFin"], interface["xCaseFin"], interface["yCaseFin"])

def deplacementPion(event):
    gui = interface["gui"]
    couleurCase = interface["couleurCase"]
    xCoordCaseDepart = [interface["xCaseDebut"][0], interface["xCaseDebut"][1]]
    yCoordCaseDepart = [interface["yCaseDebut"][0], interface["yCaseDebut"][1]]
    typeCaseDepart = interface["typeCaseDebut"]
    xCoordCaseArrivee = [interface["xCaseFin"][0], interface["xCaseFin"][1]]
    yCoordCaseArrivee = [interface["yCaseFin"][0], interface["yCaseFin"][1]]
    typeCaseArrive = interface["typeCaseFin"]
    print(typeCaseDepart, typeCaseArrive, couleurCase)
    if typeCaseArrive == 0:
        if couleurCase is True:
            print("j'ai compris")
        else:
            gui.create_rectangle(xCoordCaseDepart[0], yCoordCaseDepart[0], xCoordCaseDepart[1], yCoordCaseDepart[1], fill="black", outline="black")
            if typeCaseDepart == 1:
                gui.create_oval(xCoordCaseArrivee[0], yCoordCaseArrivee[0], xCoordCaseArrivee[1], yCoordCaseArrivee[1],
                                fill="red")
            else:
                gui.create_oval(xCoordCaseArrivee[0], yCoordCaseArrivee[0], xCoordCaseArrivee[1], yCoordCaseArrivee[1],
                                fill="blue")


def Start():
    Interface, Window, SW, SH = Canva() # On récupères les infos de la fenêtre créée
    interface["gui"] = Interface #On modifie les variables dans la table
    interface["largeur"] = SW
    interface["hauteur"] = SH
    CompteurTemps("0:00", interface["gui"], SW, SH)
    Joueur1("Hugo", interface["gui"], SW, SH)
    Joueur2("Alexandre", interface["gui"], SW, SH)
    interface["coord"] = CreationDamier(interface["gui"], SW, SH)
    creerpion(interface["gui"], SW, SH)# On lance la fonction qui crée les pions de base

    Window.bind("<Button-1>", caseCorrespondanteDebut) #Lance la fonction caseCorrespondante au clic droit de la souris
    Window.bind("<ButtonRelease>", caseCorrespondanteFin) #Lance la fonction caseCorrespondante au relachement du clic droit de la souris
    Window.bind("<Key>", deplacementPion)#Lance la fonction deplacementPion a l'appuie d'une touche
    Window.mainloop()

Start()





