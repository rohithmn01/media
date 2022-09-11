from fileinput import filename
import socket
from tqdm import tqdm
import os

def main():
    s = socket.socket()
    s.bind((socket.gethostname(), 3339))
    s.listen(10)


    conn, address = s.accept()
    data = conn.recv(1024).decode("utf-8")
    print(data)

    item = data.split("_")
    filename = item[0]
    filesize = int(item[1])

    print("filename and filesize recieved")
    conn.send("filename and filesize recieved".encode("utf-8"))


    bar = tqdm(range(filesize), f"receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

    with open(f"recv_{filename}", 'w') as f:
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break
            f.write(data)
            bar.update(len(data))
    conn.close()
    s.close()


if __name__ == "__main__":
    main()




