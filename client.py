from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import filedialog

from image_encryption import main as img_encrypt_main
from text_encryption import main as text_encrypt_main
from text_decryption import main as text_decrypt_main
from image_decryption import main as img_decrypt_main
from PIL import ImageTk,Image
from decryption import find_key


def text_csv(name):
    file_name = open(name, 'r')
    encrypted_data = file_name.read()
    encrypted = ''
    for i in range(0, len(encrypted_data)):
        if not encrypted_data[i] == ',':
            encrypted += encrypted_data[i]

    return encrypted


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            print(type(msg))

            separated_data, key, code = find_key(msg)

            if code == "0000":
                message = text_decrypt_main(msg)
                msg_list.insert(tkinter.END, message)

            if code == "0100":
                print("you are successful")
                # img_data = img_decrypt_main()


        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    text_encrypt_main(msg)
    my_msg.set("")  # Clears input field.

    sending_data = text_csv('text_data.csv',)
    client_socket.send(bytes(sending_data,"utf-8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def send_image(imageName):
    img_encrypt_main(imageName)
    img_data = text_csv("img_data.csv")
    client_socket.send(bytes(img_data,"utf-8"))


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


def fileAction():
    filename = filedialog.askopenfilename()
    print('Selected:',filename)
    send()


def imageAction():
    imagename = filedialog.askopenfilename(filetypes=(("Image File","*.jpg"),("Image File","*.png")))
    send_image(imagename)
    # img = Image.open(imagename)



top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.


msg_list = tkinter.Listbox(messages_frame, height=25, width=70, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

# message field
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()

# file select
file_select = tkinter.Button(top,text="Select File To Send",command=fileAction)
file_select.pack()

#image select
image_select = tkinter.Button(top,text="Select Image to Send", command = imageAction )
image_select.pack()

# send button
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()



top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = input('Enter host: ')

PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 10000
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.