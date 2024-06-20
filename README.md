# MessagingGUI

Welcome to the `MessagingGUI` repository! This project contains two Python scripts that together create a simple chat server and client with a graphical user interface (GUI) using the Tkinter library. 

## Table of Contents

- [Introduction](#introduction)
- [Files Description](#files-description)


## Introduction

The `MessagingGUI` project includes:
1. **chat_server.py**: A server-side script that manages client connections and message broadcasting.
2. **gui_im_client.py**: A client-side script that provides a GUI for users to connect to the server and chat with each other.

## Files Description

- **chat_server.py**: This script sets up a chat server that listens for incoming client connections on a specified IP and port. It manages multiple client connections using threads, allowing clients to send messages to each other. The server broadcasts messages to all connected clients and handles user join/leave notifications.

- **gui_im_client.py**: This script provides a graphical user interface (GUI) for clients to connect to the chat server. Users can enter the server IP and their screen name to join the chat. The GUI allows users to send and receive messages, with messages displayed in a chat window. The client can also disconnect from the server gracefully.
