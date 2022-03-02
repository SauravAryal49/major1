from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from text_encryption import main as text_encrypt_main
from text_decryption import main as text_decrypt_main


def text_csv():
    file_name = open('text_data.csv', 'r')
    encrypted_data = file_name.read()
    encrypted = ''
    for i in range(0, len(encrypted_data)):
        if not encrypted_data[i] == ',':
            encrypted += encrypted_data[i]

    return encrypted


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        welcome_message = "Greetings from the cave! Now type your name and press enter!"
        text_encrypt_main(welcome_message)
        welcome_data = text_csv()
        client.send(bytes(welcome_data, "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    name1 = text_decrypt_main(name)
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name1
    text_encrypt_main(welcome)
    welcome1 = text_csv()
    client.send(bytes(welcome1, "utf8"))
    msg = "%s has joined the chat!" % name1
    text_encrypt_main(msg)
    msg1 = text_csv()
    broadcast(bytes(msg1, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        message = text_decrypt_main(msg)
        if message != "{quit}":  #bytes("{quit}", "utf8"):

            full_msg = name1 + ":" + message
            text_encrypt_main(full_msg)
            pass_msg = text_csv()
            broadcast(bytes(pass_msg, "utf-8"))
            # broadcast(msg, name)
            # broadcast(msg)
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""


    for sock in clients:
        # sock.send(bytes(prefix1, "utf8"), msg)
        sock.send(msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 10000
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()