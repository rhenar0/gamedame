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

#Fonction qui permet de retourner les données de configuration d'une partie se trouvant sur une DB Firebase

def getstatus(cube): 
    data = db.child(cube).child("config").get().each()
    return data

def getstatus_pone(cube):
    k = "null"
    data = db.child(cube).child("config").get().each()
    for i in data:
        if i.key() == "pone_defined":
            k = i.val()
    return k

#Fonction de récupération des identifiants et status joueur

def ply_get_id(cube, player):
    k = "null"
    data = db.child(cube).child("players").child(player).get().each()
    for i in data:
        if i.key() == "id":
            k = i.val()
    return k

def ply_get_pseudo(cube, player):
    k = "null"
    data = db.child(cube).child("players").child(player).get().each()
    for i in data:
        if i.key() == "pseudo":
            k = i.val()
    return k

def ply_get_status(cube, player):
    k = "null"
    data = db.child(cube).child("players").child(player).get().each()
    for i in data:
        if i.key() == "status":
            k = i.val()
    return k

#Injection dans la base de donnée

def inject_status(cube, player, nstatus):
    log = db.child(cube).child("players").child(player).update({"status": nstatus})
    return log

def inject_id(cube, spone):
    id = uuid.uuid1()
    if spone == "no":
        log = db.child(cube).child("config").update({"pone_defined": "yes"})
        log_t = db.child(cube).child("players").child("ply_one").update({"id": str(id.hex)})
        return log, log_t
    elif spone == "yes":
        log_t = db.child(cube).child("players").child("ply_two").update({"id": str(id.hex)})
        return log_t
    else:
        return "[ERROR] Impossible de connaitre si la place du joueur un est occupé"

print(inject_id("cubone", getstatus_pone("cubone")))