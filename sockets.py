import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("https://github/laisham3/dms", 80))
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 80))
serversocket.listen(5)
while True:
    (clientsocket, address) = serversocket.accept()
    ct = client_thread(clientsocket)
    ct.run()
