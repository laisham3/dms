class Chat():
  def accept_connections():
    client, client_address = SERVER.accept()
    print("other has connected." % client_address)
    client.send(bytes("Welcome to dms!"+
                        "Start by typing your name and pressing enter!"))
    addresses[client] = client_address
  