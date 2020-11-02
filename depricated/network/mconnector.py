import mysql.connector

def connect():
    mydb = mysql.connector.connect(
        host="cloud.imercy.fr",
        user="gamedame",
        password="damedame",
        database="gamedame",
        port=3316,
        auth_plugin='mysql_native_password'
    )
    return mydb

hello = connect()
cursor = hello.cursor()

def join_game(connector, cu, id, name):
    query = ("INSERT INTO cubeone (sessionid, player_id, player_name) VALUES (%(sessionid)s, %(player_id)s, %(player_name)s)")
    data = (1, id, name)
    cu.execute(query, data)
    connector.commit()
    return cu

def get_info(cu):
    query = ("SELECT sessionid, player_name, player_id FROM cubeone")
    cu.execute(query)
    return cu

for (sessionid, player_name, player_id) in get_info(cursor):
  print("{}, {} was hired on ".format(
    sessionid, player_name))

join_game(hello, cursor, 12, 'Rhenar')

