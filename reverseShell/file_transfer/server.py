import socket

s = socket.socket()
s.bind((socket.gethostname(), 3336))
s.listen(10)

while True:
    conn, address = s.accept()
    path = conn.recv(1024).decode("utf-8").strip()
    print(f"file path: {path}")
    f = open(path, 'rb')
    sendData = f.read(1024)
    while sendData:
        conn.send(sendData)
        sendData = f.read(1024)
    conn.close()