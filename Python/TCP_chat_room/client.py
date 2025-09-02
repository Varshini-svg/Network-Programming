import socket
import threading

# Ask user for a nickname
nickname = input("Choose a nickname: ")

# Create TCP client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Function to continuously receive messages from the server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred! Disconnecting...")
            client.close()
            break

# Function to continuously send messages to the server
def write():
    while True:
        message = f'{nickname}: {input("")}'
        try:
            client.send(message.encode('ascii'))
        except:
            print("Connection lost. Exiting...")
            client.close()
            break

# Run both receive and write functions on separate threads
receive_thread = threading.Thread(target=receive, daemon=True)
receive_thread.start()

write_thread = threading.Thread(target=write, daemon=True)
write_thread.start()
