import socket
from tqdm import tqdm
import os

filename = "large.txt"
filesize = os.path.getsize(filename)

def main():
    print("hi")
    s = socket.socket()
    s.connect((socket.gethostname(), 3339))

    data = f"{filename}_{filesize}"
    print(data)
    s.send(data.encode("utf-8"))
    msg = s.recv(1024).decode("utf-8")
    print(f"server msg: {msg}")

    bar = tqdm(range(filesize), f"sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, 'r') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            s.send(data.encode("utf-8"))
            bar.update(len(data))
    s.close()


if __name__ == "__main__":
    main()