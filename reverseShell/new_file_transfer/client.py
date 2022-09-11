import socket


def main():
    print("server is statrting..!")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 3338))

    f = open("/Users/i346327/media/reverseShell/new_file_transfer/data/newFile.txt","r")
    data = f.read()
    s.send("newFile.txt".encode("utf-8"))
    print(s.recv(1024).decode("utf-8"))
    
    s.send(data.encode("utf-8"))
    print(s.recv(1024).decode("utf-8"))
    f.close()
    s.close()


if __name__ == "__main__":
    main()