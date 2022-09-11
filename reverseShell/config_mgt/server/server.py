import socket

s = socket.socket()
s.bind((socket.gethostname(), 3337))
s.listen(10)

while True:
    conn, address = s.accept()
    f = open("/Users/i346327/media/reverseShell/config_mgt/server/file1.json", 'rb')
    sendData = f.read(1024)

    while sendData:
        conn.send(sendData)
        sendData = f.read(1024)
    f.close()
    conn.close()