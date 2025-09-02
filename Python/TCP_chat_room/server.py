import threading
import socket

host = '127.0.0.1'
port = 55555

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# Send a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle individual client
def handle(client):
    while True:
        try:
            # Receive messages from client
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove client on disconnect/error
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode('ascii'))
            nicknames.remove(nickname)
            break

# Accept multiple clients
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Ask client for nickname
        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat!".encode('ascii'))
        client.send("Connected to the server!".encode('ascii'))

        # Start handling thread
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
