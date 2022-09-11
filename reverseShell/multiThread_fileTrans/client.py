import socket
import os

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 3339))

    while True:
        data = s.recv(1024).decode("utf-8")
        cmd, msg = data.split("@")
        if cmd == "OK":
            print(f"{msg}")

        data = input("> ")
        data = data.split(" ")
        cmd = data[0]
        if cmd == "HELP":
            s.send(cmd.encode("utf-8"))

if __name__ == "__main__":
    main()