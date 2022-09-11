import socket


def main():
    print("server is statrting..!")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 3338))
    s.listen(10)
    print(f"server is listening on {socket.gethostname()}....")

    while True:
        conn, address = s.accept()
        print(f"New connection: {address}")

        filename = conn.recv(1024).decode("utf-8")
        print(f"filename : {filename}")
        f = open("/Users/i346327/media/reverseShell/new_file_transfer/"+filename, 'w')
        conn.send(bytes("Filename name received","utf-8"))
        data = conn.recv(1024).decode("utf-8")
        f.write(data)
        # while data:
        #     f.write(data)
        #     data = conn.recv(1024).decode("utf-8")
        conn.send(bytes("Filename data received", "utf-8"))
        f.close()
        conn.close()



if __name__ == "__main__":
    main()