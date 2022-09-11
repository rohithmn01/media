import socket 

s = socket.socket()
s.bind((socket.gethostname(), 3336))
s.listen(10)

connection, address = s.accept()
while True:
    print(f"connected to {address}...")
    inp = connection.recv(1024).decode("utf-8").strip()
    lis = inp.split(",")
    print(lis)
    with open(lis[0], 'a+') as f:
        f.write(lis[1])

    fl = open(lis[0], 'rb')
    sendData = fl.read(1024)
    while sendData:
        connection.send(sendData)
        sendData = fl.read(1024)
connection.close()