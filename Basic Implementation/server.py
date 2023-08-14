import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

if s:
    print("Connection is successful")

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    
    # msg = "Welcome to the server!"
    # msg = f"{len(msg):<{HEADERSIZE}}" + msg   
    
    msg = {1:"Hello", 2:"World"}
    msg = pickle.dumps(msg)
    
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg 
    
    clientsocket.send(msg)
    
    
    
