import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3336))
s.listen(10)

clinetsocket, address = s.accept()
while True:
    #clinetsocket, address = s.accept()
    print(f"connection from address {address} is established.!")
    #clinetsocket.send(bytes("Welcome to the Server.!!", "utf-8"))
    #clinetsocket.send(bytes("pinggggggg", "utf-8"))
    msg = clinetsocket.recv(1024)
    if not msg:
        break
    print(msg.decode("utf-8").strip())
    if msg.decode("utf-8").strip() == "ping":
        clinetsocket.send(bytes("pong \n","utf-8"))
    elif msg.decode("utf-8").strip() == "quit":
        clinetsocket.close()
    else:
        clinetsocket.send(msg)
    # if msg.decode("utf-8") == "ping":
    #     clinetsocket.send(bytes("pong", "utf-8"))

clinetsocket.close()
