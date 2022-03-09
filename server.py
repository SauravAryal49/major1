from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from text_encryption import main as text_encrypt_main
from text_decryption import main as text_decrypt_main
from image_decryption import main as img_decrypt_main
from decryption import find_key



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
        welcome_message = "Greetings! Now type your name and press enter!"
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
        msg = client.recv(BUFSIZ).decode("utf8")
        msg = msg.rstrip()
        print(msg)
        encrypted_message, key, code = find_key(msg)

        if code == "0100":
            # img_decrypt_main(encrypted_message, key)
            broadcast(bytes(name, "utf-8"))
            broadcast(bytes(msg, "utf-8"))

        elif code == "0000":
            message = text_decrypt_main(msg)

            if message != "{quit}":  #bytes("{quit}", "utf8"):
                full_msg = name1 + ":" + message
                text_encrypt_main(full_msg)
                pass_msg = text_csv()
                broadcast(bytes(pass_msg, "utf-8"))

            else:
                # text_encrypt_main("{quit}")
                # pass_msg = text_csv()
                # client.send(bytes(pass_msg, "utf8"))
                client.close()
                del clients[client]
                quiting_msg = name1 + " has left the chat"
                text_encrypt_main(quiting_msg)
                quit_msg = text_csv()
                broadcast(bytes(quit_msg, "utf8"))
                break

        elif code[:2] == "11":
            send_mssg = name1 + " has send a file"
            text_encrypt_main(send_mssg)
            send_mssg1 = text_csv()
            broadcast(bytes(msg, "utf8"))
            broadcast(bytes(send_mssg1, "utf8"))



def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        # sock.send(bytes(prefix1, "utf8"), msg)
        sock.send(msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 10000000
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
