import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.hostname = socket.gethostname()
        self.server = "192.168.1.17"
        self.port = 5558
        self.addr = (self.server,self.port)
        self.player = self.connect()

    def getPlayerID(self):
        return self.player
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(4068*2).decode()
        except:
            pass

    def send(self,data):
        try:
            self.client.send(str.encode(data))  
            return pickle.loads(self.client.recv(4068*2))
        except socket.error as e:
            pass
