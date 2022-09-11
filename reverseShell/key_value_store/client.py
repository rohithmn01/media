import socket

s=socket.socket()
s.connect((socket.gethostname(), 4436))
connected = True
while connected:
    msg = input("> ")
    if msg == "quit":
        connected = False
    else:
        s.send(msg.encode("utf-8"))
        value = s.recv(1024).decode("utf-8")
        print(value)
s.close()