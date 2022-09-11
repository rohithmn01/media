import socket
import threading

nickname = input("choose a nick name: ")
s=socket.socket()
s.connect((socket.gethostname(), 3339))

def receive():
    while True:
        try:
            msg = s.recv(1024).decode("utf-8")
            if msg == "NICK":
                s.send(nickname.encode("utf-8"))
            else:
                print(msg)
        except:
            print("error occured")
            s.close()
            break

def write():
    while True:
        msg = f'{nickname} > {input("")}'
        s.send(msg.encode("utf-8"))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

