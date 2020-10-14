import tkinter as tk
import time
import tkinter.font as tkFont
from tkinter import *


def Canva():
    Damier = tk.Tk()
    Damier.title("Jeu de Dame")
    SW = Damier.winfo_screenwidth()
    SH = Damier.winfo_screenheight()
    Canva = tk.Canvas(Damier, width=SW*0.42, height=SH*0.7, bg="ivory")
    Canva.pack()
    return Canva, Damier, SW, SH

def CreationDamier(gui, SW, SH):
    a = range(int(SH*0.1), int(SH*0.6), int(SW*0.03))
    b = range(int(SH*0.1), int(SH*0.6), int(SW*0.03))
    compteur1 = 1
    compteur2 = 1
    coordonnees=[]
    for i in a:
        if compteur1%2 == 0:
            for j in b:
                if compteur2 % 2 == 0:
                    z = int(SW * 0.03)
                    gui.create_rectangle(i, j, i+int(SW*0.03), j+int(SW*0.03), fill="white", outline="black")
                    coordonnees.append([i, j, i+z, j+z, 0])
                else:
                    z = int(SW * 0.03)
                    gui.create_rectangle(i, j, i+int(SW*0.03), j+int(SW*0.03), fill="black", outline="black")
                    coordonnees.append([i, j, i+z, j+z, 0])
                compteur2 += 1
            compteur1 += 1
        else:
            for j in b:
                if compteur2 % 2 == 0:
                    z = int(SW * 0.03)
                    gui.create_rectangle(i, j, i+int(SW*0.03), j+int(SW*0.03), fill="black", outline="black")
                    coordonnees.append([i, j, i+z, j+z, 0])
                else:
                    z = int(SW * 0.03)
                    gui.create_rectangle(i, j, i+int(SW*0.03), j+int(SW*0.03), fill="white", outline="black")
                    coordonnees.append([i, j, i+z, j+z, 0])
                compteur2 += 1
            compteur1 += 1

    return coordonnees


def creerpion(gui, SW, SH):
    Coord = CreationDamier(gui, SW, SH)
    for i in range(0, 10):
        if i%2 != 0:
            for j in range(0, 3, 2):
                j = j + i * 10
                gui.create_oval(Coord[j][0], Coord[j][1], Coord[j][2], Coord[j][3], fill="Red")
                Coord[j][4] = 1
            for j in range(8, 10, 2):
                j = j + i * 10
                gui.create_oval(Coord[j][0], Coord[j][1], Coord[j][2], Coord[j][3], fill="Blue")
                Coord[j][4] = 2
        if i%2 == 0:
            for j in range(1, 3, 2):
                j = j + i * 10
                gui.create_oval(Coord[j][0], Coord[j][1], Coord[j][2], Coord[j][3], fill="Red")
                Coord[j][4] = 1
            for j in range(7, 10, 2):
                j = j + i * 10
                gui.create_oval(Coord[j][0], Coord[j][1], Coord[j][2], Coord[j][3], fill="Blue")
                Coord[j][4] = 2


def CompteurTemps(temps, gui, SW, SH):
    TexteStyle = tkFont.Font(family="Lucida Grande", size=20)
    gui.create_text((SW*0.21, SH*0.028), text=temps, font=TexteStyle)
    gui.create_rectangle(SW*0.16, 2, SH*0.455, 50, outline="black")

def Joueur1(joueur, gui, SW, SH):
    TexteStyle = tkFont.Font(family="Lucida Grande", size=15)
    gui.create_text((SW*0.02, SH*0.015), text=joueur, font=TexteStyle)
    gui.create_rectangle(SW*0.001, 2, SW*0.12, 50, outline="black")

def Joueur2(joueur, gui, SW, SH):
    TexteStyle = tkFont.Font(family="Lucida Grande", size=15)
    gui.create_text((SW*0.33, SH*0.015), text=joueur, font=TexteStyle)
    gui.create_rectangle(SW*0.30, 2, SW*0.42, 50, outline="black")


async def timer():
    minutes = 0
    while True:
        now = time.localtime(time.time())
        secondes = now[5]
        temps=[minutes, secondes]
        time.sleep(1)
        if secondes == 59:
            minutes += 1

def position(event):
    print("position du pointeur:", event.x, event.y)


def Start():
    Interface, Window, SW, SH = Canva()
    CompteurTemps("0:00", Interface, SW, SH)
    Joueur1("Hugo", Interface, SW, SH)
    Joueur2("Alexandre", Interface, SW, SH)
    CreationDamier(Interface, SW, SH)
    creerpion(Interface, SW, SH)

    Window.bind("<Button-1>", position)
    Window.bind("<ButtonRelease>", position)
    Window.mainloop()

Start()





