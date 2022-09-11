import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 3338))
    print("clinet connect to server..!")

    connected = True
    while connected:
        msg = input("> ")
        s.send(msg.encode("utf-8"))

        if msg == "quit":
            connected = False
        else:
            data = s.recv(1024).decode("utf-8")
            print(data)

if __name__ == "__main__":
    main()