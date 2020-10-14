import socket
import json

config_n = json.load(open('config/network.json'))
config_g = json.load(open('config/game.json'))

HOST = config_n['system'][0]['host']
PORT = config_n['system'][0]['port']

#NET#

def NET_initialize_client(self):
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sc.bind((HOST, PORT))
    except:
        print("Connexion Error")
    get_server = sc.recv(4096)
    return get_server

def NET_send_action(self, con, data, nb):
    con.send("action/"+ nb + "/" + data)
    return True

def NET_recv(self, con):
    get_action = con.recv(4096)
    return get_action

def NET_joinsession(self, con, id, pseudo):
    con.send("join/" + id + "/" + pseudo)
    get_nb = con.recv(4096)
    return get_nb

#JSON#

def JSON_param_session(self, data):
    d = data.split("/")
    config_g["session_id"] = d[1]
    config_g["player_id"] = d[2]
    try:
        with open('config/game.json', 'w') as outfile:
            json.dumps(config_g, outfile)
    except:
        return False
    return True

