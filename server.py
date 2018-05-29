def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcomd to dms! Type your name and press enter!"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
