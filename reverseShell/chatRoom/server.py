from email import message
import socket
import threading

s=socket.socket()
s.bind((socket.gethostname(), 3339))
s.listen(10)
print("server is listening..!")

clients = []
nick_names = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()

            nickname = nick_names[index]
            nick_names.remove(nickname)
            broadcast(f"{nickname} left the chat".encode("utf-8"))
            break

def receive():
    while True:
        client, address = s.accept()
        print(f"connected with {address}")

        client.send("NICK".encode("utf-8")) #send this to client so that it has provide the nickname first
        nickname = client.recv(1024).decode("utf-8")
        nick_names.append(nickname)
        clients.append(client)

        # broadcast the newly joined client and its nick name
        print(f"nickname of the client is : {nickname}")
        broadcast(f"{nickname} joined the chat".encode("utf-8"))

        # sed the confirmation message to the client from server
        client.send("connected to the server".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()







