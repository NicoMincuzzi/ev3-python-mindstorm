import socket
import threading
from time import sleep, time


class ServerSocket():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        def __init__(self):
            self.sock.bind(('192.168.1.175', 8070 ))
            self.sock.listen(10)
                
        def handler(self, c,a):
            while True:
                data = c.recv(1024)
                print(data)
                c.send(data)
                if not data:
                    break

        def run(self):
            while True:
                c,a = self.sock.accept()
                print(c)
                print(a)
                cThread = threading.Thread(target=self.handler, args=(c,a))
                cThread.start()