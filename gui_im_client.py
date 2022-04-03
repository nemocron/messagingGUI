# Gabriel Liau CIS345 12Pm A8

from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread


def event_handler(event):
    """Controls the server_ip_entry input"""
    valid_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '\b', '']
    if event.char not in valid_keys:
        return "break"


def connect():
    """Connects client to server"""
    global sock, server_ip, screen_name, connect_bttn, window, chat, PORT
    if len(server_ip.get()) > 6 and len(screen_name.get()) > 1:
        try:
            addr = (server_ip.get(), PORT)
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect(addr)
            sock.send(f'{screen_name.get()}'.encode())
        except:
            sock.close()
            sock = None
        else:
            x = Thread(target=receive_message, daemon=True)
            x.start()
        chat.grid(row=3, columnspan=2, pady=5)
        frame_chat.grid()
        # listbox.grid(row=3, columnspan=2)
        listbox.pack()
        message.grid(row=4, column=0, pady=5, sticky="W")
        send.grid(row=4, pady=5, sticky="E")
        connect_bttn.config(bg="gold", text="Disconnect", command=disconnect)
    else:
        messagebox.showinfo("Error", message="Need to add a valid IP address and a screen name")


def disconnect():
    """Disconnects client from server"""
    global sock, server_ip, screen_name, connect_bttn, window, chat
    try:
        sock.send(f'{EXIT}\n'.encode())
    except:
        pass
    finally:
        sock.close()
        sock = None
    connect_bttn.config(bg="SystemButtonFace", text="Connect", command=connect)
    chat.grid_forget()
    send_messages.set("")
    server_ip.set("")
    screen_name.set("")


def receive_message():
    """Receives messages from other client connections"""
    global sock, screen_name
    while True:
        try:
            received_message = sock.recv(1024)
        except OSError:
            received_message = None
            break
        if not received_message:
            disconnect()
            break
        listbox.insert(END, received_message.decode())


def send_message():
    """Send client's message to the server"""
    global sock, send_messages
    msg = send_messages.get()
    if msg == EXIT:
        disconnect()
    elif len(msg) > 0:
        try:
            sock.send(msg.encode())
        except OSError:
            disconnect()
    send_messages.set("")


def window_closing():
    """Closes the window"""
    global sock
    window.protocol("WM_DELETE_WINDOW", window_closing)
    if sock:
        disconnect()
    window.quit()


# Create window
window = Tk()
window.title("CIS IM Client")


# Global Variables
server_ip = StringVar()
screen_name = StringVar()
send_messages = StringVar()
EXIT = '[Q]'
PORT = 49000
sock = socket(AF_INET, SOCK_STREAM)


# Window Design
server_ip_lbl = Label(window, text="Server IP")
server_ip_lbl.grid(row=0, column=0, sticky="W", padx=5)

screen_name_lbl = Label(window, text="Screen Name")
screen_name_lbl.grid(row=1, column=0, sticky="W", padx=5)

server_ip_entry = Entry(window, textvariable=server_ip, width=30)
server_ip_entry.grid(row=0, column=1, sticky="W", padx=5)
server_ip_entry.bind('<Key>', event_handler)
screen_name_entry = Entry(window, textvariable=screen_name, width=30)
screen_name_entry.grid(row=1, column=1, sticky="W", padx=5)

connect_bttn = Button(window, text="Connect", width=35, command=connect)
connect_bttn.grid(row=2, columnspan=2, pady=10)

chat = Frame(window, padx=5, width=300, height=370, bg='maroon', relief=SUNKEN, borderwidth=5)
chat.grid_propagate(0)

frame_chat = Frame(chat, bg='white')
# frame_chat.grid_propagate(0)
scrollbar = Scrollbar(frame_chat)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(frame_chat, width=43, height=20, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

message = Entry(chat, width=38, textvariable=send_messages)
send_messages.set("Type your messages here.")

send = Button(chat, text="Send", bg='gold', command=send_message)


window.mainloop()
