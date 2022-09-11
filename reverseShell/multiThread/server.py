###Multiple clients can connect to the server at the same time
import socket
import threading
import wikipedia

def handle_client(conn, address):
    print(f"New connection established: {address}")

    connected = True
    while connected:
        msg = conn.recv(1024).decode("utf-8")
        if msg == "quit":
            connected = False
        else:
            print(f"[{address}]: {msg}")
            #msg = wikipedia.summary(msg, sentences = 1)
            conn.send(msg.encode("utf-8"))
    conn.close()


def main():
    print("Server is statrting...!")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 3338))
    s.listen(10) #listen for the clinets
    print(f"sever is listening on {socket.gethostname()}...!")

    while True:
        conn, address = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, address))
        thread.start()
        print("###############")
        print(f"[active connections]: {threading.active_count() - 1}")

if __name__ == "__main__":
    main()

