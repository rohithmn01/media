import socket
import os
import threading
"""
CMD@MSG
"""
def handle_clinet(conn, address):
    print(f"new connection : {address}")
    conn.send("OK@welcome to the server".encode("utf-8"))
    while True:
        data = conn.recv(1024).decode("utf-8")

        if data == "HELP":
            send_data = "LIST : list all files from server \n"
            send_data += "UPLOAD <path> : upload a file to server \n"
            send_data += "DELETE <filename> : Delete a file from the server \n"
            send_data += "LOGOUT : Disconnect from the server \n"
            send_data += "HELP : List all the commands \n"

            conn.send(send_data.encode("utf-8"))
        

def main():
    print("Server is starting..!")
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 3339))
    s.listen(10)
    print(f"server is listening on {socket.gethostname()}")

    while True:
        conn, address = s.accept()
        thread = threading.Thread(target=handle_clinet, args=(conn, address))
        thread.start()
        print("##################")
        print(f"Active connections: {threading.active_count() - 1}")







if __name__ == "__main__":
    main()