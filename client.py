def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
        except OSError:
            break
         
def send(event=None):
    msg = my_msg.get()
    my_msg.set("")  
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()
        
def closing(event=None):
    my_msg.set("{quit}")
    send()
    
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
