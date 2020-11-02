from tkinter import *

def rond (event): # Un argument est envoyé automatiquement à la fonction suite au can.bind(...), c'est
    x,y = event.x,event.y #une instance d'une classe qui fournit les coordonnées du clic dans le canvas
    #par le biais de ses attributs x et y (le nom event est donné à l'argument
    #conventionnellement
    can.create_oval(x-5,y-5,x+5,y+5, fill='red') #on crée un cercle de centre les coordonnées du clic dans notre Canvas "can"

fen = Tk()
can = Canvas(fen, width =200, height =150, bg="light yellow")
can.bind("<Button-1>", rond) #on lie le clic gauche à la fonction "rond"
can.pack()
chaine = Label(fen)
chaine.pack()

fen.mainloop()