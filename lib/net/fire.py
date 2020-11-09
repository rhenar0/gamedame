from firebase import Firebase
import uuid

firebaseConfig = {
    "apiKey" : "AIzaSyDFTe3lK1bJ7eqe5oF54vXq2ojpFWau718",
    "authDomain" : "gamedame-5e274.firebaseapp.com",
    "databaseURL" : "https://gamedame-5e274.firebaseio.com",
    "projectId" : "gamedame-5e274",
    "storageBucket" : "gamedame-5e274.appspot.com",
    "messagingSenderId" : "359814504023",
    "appId" : "1:359814504023:web:14012c2c5dbdfebd51cd12",
    "measurementId" : "G-3EB4S3TVKL"
}

firebase = Firebase(firebaseConfig)

db = firebase.database()


#
#
#Récupération données dans la base de donnée
#
#

#Fonction qui permet de retourner les données de configuration d'une partie se trouvant sur une DB Firebase

def getstatus(cube):
    """
    Obtiens le status de la configuration de l'instance.
    :param cube: Nom de l'instance
    :return: Retourne le status de la configuration de l'instance
    """

    data = db.child(cube).child("config").get().each()
    return data

def getstatus_pone(cube):
    """
    Permet de connaître si le joueur un est défini et de connaître ses paramètres.
    :param cube: Nom de l'instance ["cubone"]
    :return: Retourne le status de pone
    """

    k = "null"
    data = db.child(cube).child("config").get().each()
    for i in data:
        if i.key() == "pone_defined":
            k = i.val()
    return k

#Fonction de récupération des identifiants et status joueur

def ply_get_id(cube, player):
    """
    Permet en définissant la cible (Joueur un ou joueur deux) de récupérer un identifiant unique.
    :param cube: Nom de l'instance ["cubone"]
    :param player: Cible le joueur ["ply_one"]
    :return: Retourne l'identifiant unique
    """

    k = "null"
    data = db.child(cube).child("players").child(player).get().each()
    for i in data:
        if i.key() == "id":
            k = i.val()
    return k

def ply_get_pseudo(cube, player):
    """
    Permet en définissant la cible (Joueur un ou joueur deux) de récupérer un pseudo.
    :param cube: Nom de l'instance ["cubone"]
    :param player: Cible le joueur ["ply_one"]
    :return: Retourne le pseudo
    """

    k = "null"
    data = db.child(cube).child("players").child(player).get().each()
    for i in data:
        if i.key() == "pseudo":
            k = i.val()
    return k

def ply_get_status(cube, player):
    """
    Permet en définissant la cible (Joueur un ou joueur deux) de récupérer son status (en attente, en jeu...).
    :param cube: Nom de l'instance ["cubone"]
    :param player: Cible le joueur ["ply_one"]
    :return: Retourne le status
    """

    k = "null"
    data = db.child(cube).child("players").child(player).get().each()
    for i in data:
        if i.key() == "status":
            k = i.val()
    return k

#Fonction de récupération des actions

def ply_get_actions(cube, ply):
    """
    Récupère l'action du joueur ciblé.
    :param cube: Nom de l'instance ["cubone"]
    :param ply: Cible le joueur ["ply_one"]
    :return: Retourne la valeur de l'action
    """

    k = "null"
    data = db.child(cube).child("actions").get().each()
    for i in data:
        if i.key() == ply:
            k = i.val()
    return k

#
#
#Injection dans la base de donnée
#
#

def inject_status(cube, player, nstatus):
    """
    Permet d'injecter le status (Joueur un ou joueur deux) dans Firebase.
    :param cube: Nom de l'instance ["cubone"]
    :param player: Cible le joueur ["ply_one"]
    :param nstatus: Status à définir ["wait"]
    :return: Retourne l'identifiant unique
    """

    log = db.child(cube).child("players").child(player).update({"status": nstatus})
    return log

def inject_id(cube, spone):
    """
    Permet d'injecter l'identifiant dans Firebase. Si le joueur est premier à s'injecter, il prendra la postion de "ply_one" sinon il prendra "ply_two".
    :param cube: Nom de l'instance ["cubone"]
    :param spone: Valeur récupérer avec la fonction {getstatus_pone}
    :return: Retourne un debug.
    """

    id = uuid.uuid1()
    if spone == "no":
        log = db.child(cube).child("config").update({"pone_defined": "yes"})
        log_t = db.child(cube).child("players").child("ply_one").update({"id": str(id.hex)})
        return log, log_t
    if spone == "yes":
        log_t = db.child(cube).child("players").child("ply_two").update({"id": str(id.hex)})
        return log_t
    return "[ERROR] Impossible de connaitre si la place du joueur un est occupé"

def inject_pseudo(cube, ply, pseudo):
    """
    Permet d'injecter le pseudo du joueur dans Firebase.
    :param cube: Nom de l'instance ["cubone"]
    :param ply: Cible le joueur ["ply_one"]
    :param pseudo: Définis le pseudo ["Arthur"]  
    """
    
    log = db.child(cube).child("players").child(ply).update({"pseudo": str(pseudo)})
    return log

def inject_action(cube, ply, action):
    """
    Permet d'injecter une action sur le joueur ciblé.
    :param cube:
    :param ply:
    :param pseudo:
    """

    log = db.child(cube).child("actions").update({ply: str(action)})
    return log