import socket
import json

games = json.load(open('json/games.json', 'r'))
actions = json.load(open('json/actions_cubeone.json', 'w'))
config = json.load(open('json/config.json', 'r'))

HOST = config['system'][0]['host']
PORT = config['system'][0]['port']

print("Server Starting...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.settimeout(5)
    s.listen()
    while True:
        try:
            print("Searching...")
            conn, addr = s.accept()
            print("Connexion in progress...")
            with conn:
                print('Connected by', addr)
                while True:
                    try:
                        data = conn.recv(1024).decode("utf-8")
                        if not data:
                            break
                        conn.sendall("000".encode("utf-8"))
                        print(data)
                    except socket.timeout:
                        print("Connexion Error")
                        conn.close()
        except:
            print("No Connexion")