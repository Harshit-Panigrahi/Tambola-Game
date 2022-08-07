import socket
from threading import Thread

IP_ADDR="127.0.0.1"
PORT=5000
CLIENTS={}

def acceptConn():
  while True:
    """ """
    conn, addr = SERVER.accept()
    player_name = conn.recv(1024).decode("utf-8")
    print(f"{player_name} has connected")

    CLIENTS[player_name] = {
      "player_num": (len(CLIENTS.keys())+1),
      "name": player_name,
      "socket": conn,
      "address": addr,
      "turn": False
    }

print("\n")
print("\t"*5, end="~~*** Tambola Game ***~~\n")

SERVER=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((IP_ADDR, PORT))
SERVER.listen(10)

print("Starting the server...")
acceptConn()